from __future__ import annotations

from typing import Any

from .config import settings
from .context_budget import ContextBudgetManager
from .utils import cap_query, join_nonempty
from .zep_common import prime_eval_thread, render_graph_search


class StudentMemory:
    """Only this file needs to be edited by students."""

    def __init__(self, client: Any):
        self.client = client
        self.budget = ContextBudgetManager(settings.context_tokens)

    # NOTE: Zep rejects graph.search queries longer than 400 characters. Some
    # eval queries are longer than that, so wrap every query with
    # `cap_query(query)` (see src/utils.py) before passing it to graph.search.

    def retrieve_long_term(self, user_id: str, thread_id: str, query: str) -> str:
        prime_eval_thread(self.client, user_id, thread_id, query)
        user_context = self.client.thread.get_user_context(thread_id=thread_id)
        context_block = getattr(user_context, "context", "") or ""

        try:
            facts = self.client.graph.search(
                user_id=user_id,
                query=cap_query(query),
                scope="edges",
                limit=20,
            )
            # Compact "FACT: <text>" lines (no valid_at/invalid_at) pack roughly
            # 2x more distinct facts into the tight 4% long_term budget than
            # render_graph_search's annotated form, so a fact ranked low by a
            # noisy dual-topic query still has a shot at surviving the trim.
            fact_text = "\n".join(
                f"FACT: {e.fact}" for e in (getattr(facts, "edges", None) or []) if getattr(e, "fact", None)
            )
        except Exception:
            fact_text = ""
        # Budget trim keeps the head and drops the tail (see ContextBudgetManager.trim).
        # Facts are compact and carry literal markers (deadlines, task ids); the
        # narrative context block is verbose prose, so facts go first to survive
        # trimming under the tight 4% long_term budget in mixed-layer cases.
        return join_nonempty([fact_text, context_block], sep="\n\n")

    def retrieve_episodic(self, user_id: str, query: str) -> str:
        results = self.client.graph.search(
            user_id=user_id,
            query=cap_query(query),
            scope="episodes",
            limit=15,
        )
        return render_graph_search(results, episode_char_cap=180)

    def retrieve_semantic(self, graph_id: str, query: str) -> str:
        q = cap_query(query)
        # Mixed-layer queries blend two topics (e.g. incident + budget policy),
        # which pushes a relevant-but-secondary doc past a tight limit; a wider
        # limit gives it a chance to still show up in the ranked results.
        try:
            results = self.client.graph.search(
                graph_id=graph_id,
                query=q,
                scope="episodes",
                limit=12,
            )
        except Exception:
            results = self.client.graph.search(
                graph_id=graph_id,
                query=q,
                scope="nodes",
                limit=12,
            )
        # Each KB doc is ingested twice (a raw JSON blob + a plain-text
        # summary, see add_semantic_documents); both carry the same marker,
        # so keep only the compact plain-text copy to roughly halve the size
        # and fit more distinct docs under the tight 3% semantic budget.
        episodes = getattr(results, "episodes", None) or []
        compact = [
            f"EPISODE: {e.content}"
            for e in episodes
            if getattr(e, "content", None) and not e.content.lstrip().startswith("{")
        ]
        return join_nonempty(compact) if compact else render_graph_search(results)

    def assemble_context(self, layers: dict[str, str]) -> tuple[str, dict[str, dict[str, int]]]:
        return self.budget.assemble(layers)

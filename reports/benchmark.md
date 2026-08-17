# Lab 17 Benchmark Report

- Implementation: `student`
- Kind: `practice`
- Cases: **11**
- Passed: **11/11**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **898.0 ms**
- Average token reduction vs full source context: **19.1%**

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| E01 | short_term | PASS | 0.1 | 133 | 0.0% |  |
| E06 | semantic | PASS | 635.5 | 53 | 88.4% |  |
| E09 | long_term | PASS | 1469.2 | 704 | 0.0% |  |
| E10 | short_term | PASS | 0.6 | 195 | 0.0% |  |
| E02 | long_term | PASS | 2047.5 | 1083 | 0.0% |  |
| E03 | long_term | PASS | 1728.5 | 1086 | 0.0% |  |
| E04 | episodic | PASS | 302.0 | 570 | 0.0% |  |
| E05 | episodic | PASS | 284.9 | 564 | 0.0% |  |
| E07 | mixed | PASS | 1726.9 | 390 | 31.0% |  |
| E11 | semantic | PASS | 273.0 | 52 | 90.8% |  |
| E08 | long_term | PASS | 1410.0 | 1072 | 0.0% |  |

## Evidence excerpts

### E01 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### E06 - semantic

`EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.`

### E09 - long_term

`FACT: Lan Tran's project is LOTUS-88. FACT: Lan Tran does not use Python in the backend example. FACT: Lan Tran prioritizes Java. FACT: Lan Tran prioritizes Spring Boot. FACT: Java is related to Spring Boot.  <USER_SUMMARY> Lan's project is LOTUS-88. They prioritize Java and Spring Boot for backend development and do not use Python. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend examples.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   `

### E10 - short_term

`<SESSION_SUMMARY> user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. | assistant: Acknowledged review constraint. | user: Filler turn 1 about UI spacing. | assistant: Filler answer 1. | user: Filler turn 2 about naming. | assistant: Filler answer 2. | user: Filler turn 3 about logging. | assistant: Filler answer 3. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. - assistant: Acknowledged review constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler turn 4 about tests. assistant: Filler answer 4. user: Filler turn 5 about docs. assistant: Filler answe`

### E02 - long_term

`FACT: Minh Nguyen likes Python. FACT: Minh Nguyen prefers to use Python for personal demos for project ORCHID-27. FACT: Minh Nguyen does not like Java. FACT: Minh Nguyen is learning async/await. FACT: Minh Nguyen is learning about coroutine. FACT: Minh Nguyen tried to increase the timeout. FACT: Minh Nguyen has a task to complete the benchmark report. FACT: Minh Nguyen is debugging async HTTP. FACT: The personal demo ORCHID-27 prefers Python. FACT: The personal demo ORCHID-27 avoids Java. FACT: Da hieu has a personal demo called ORCHID-27. FACT: Minh Nguyen's personal project is ORCHID-27. FACT: When explaining code, Minh Nguyen prefers short examples. FACT: Minh Nguyen sometimes confuses co`

### E03 - long_term

`FACT: Minh Nguyen is learning about coroutine. FACT: Minh Nguyen tried to increase the timeout. FACT: Minh Nguyen is learning async/await. FACT: Minh Nguyen sometimes confuses coroutine with Task. FACT: Minh Nguyen is debugging async HTTP. FACT: Minh Nguyen sometimes confuses coroutine with Task. FACT: Minh Nguyen rules out timeout threshold as the main issue. FACT: Minh Nguyen failed to debug async HTTP even after increasing the timeout to 60s. FACT: Minh Nguyen suggests reusing aiohttp ClientSession. FACT: Minh Nguyen identifies connection churn as the main issue. FACT: Minh Nguyen likes Python. FACT: Minh Nguyen has a task to complete the benchmark report. FACT: Minh Nguyen's personal pro`

### E04 - episodic

`EPISODE: Minh sap viet script ca nhan de tai hien su co latency, muon code dung ngon ngu minh thich khi lam mot minh, dong thoi bam sat playbook incident cua lab chu dung vo tang timeout. G EPISODE: Minh con mot open-loop phai nop truoc deadline, dong thoi muon ghi chu retry payment dung so lan toi da theo policy. Nac lai ma task/deadline con dang do, va gioi han retry chinh t EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Chuan bi demo ca nhan: ten/ma project rieng cua Minh la gi, va lan async HTTP truoc minh reuse client nhu the nao (kem ma su co)? Khong can policy domain chung, chi memory cua Minh EPISOD`

### E05 - episodic

`EPISODE: Minh sap viet script ca nhan de tai hien su co latency, muon code dung ngon ngu minh thich khi lam mot minh, dong thoi bam sat playbook incident cua lab chu dung vo tang timeout. G EPISODE: Minh con mot open-loop phai nop truoc deadline, dong thoi muon ghi chu retry payment dung so lan toi da theo policy. Nac lai ma task/deadline con dang do, va gioi han retry chinh t EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Chuan bi demo ca nhan: ten/ma project rieng cua Minh la gi, va lan async HTTP truoc minh reuse client nhu the nao (kem ma su co)? Khong can policy domain chung, chi memory cua Minh E`

### E07 - mixed

`<LONG_TERM> FACT: When explaining code, Minh Nguyen prefers short examples. FACT: Minh Nguyen likes Python. FACT: Minh Nguyen prefers to use Python for personal demos for project ORCHID-27. FACT: Minh Nguyen does not like Java. FACT: Minh Nguyen is learning about coroutine. FACT: Minh Nguyen is learning async/await. FACT: Minh Nguyen tried to increase the timeout. FACT: The personal demo ORCHID-27 prefers Python. FACT: Minh Nguyen is debugging async HTTP. FACT: Minh Nguyen suggests reusing aiohttp ClientSession. FACT: Minh Nguyen's personal project is ORCHID-27. FACT: Minh Nguyen sometimes confuses coroutine with Task. FACT: Minh Nguyen failed to debug async HTTP even after increasing the ti`

### E11 - semantic

`EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.`

### E08 - long_term

`FACT: The project BLUEBIRD-42 requires TypeScript for the backend. FACT: The project BLUEBIRD-42 requires NestJS for the backend. FACT: Python is prohibited for the backend of the BLUEBIRD-42 project. FACT: Minh Nguyen is debugging async HTTP. FACT: Minh Nguyen is learning async/await. FACT: The ORCHID-27 uses Python. FACT: Minh Nguyen prefers to use Python for personal demos for project ORCHID-27. FACT: aiohttp ClientSession has concurrency set to 20. FACT: Minh Nguyen is learning about coroutine. FACT: Minh Nguyen suggests reusing aiohttp ClientSession. FACT: Minh Nguyen failed to debug async HTTP even after increasing the timeout to 60s. FACT: The assistant is checking concurrency. FACT: `

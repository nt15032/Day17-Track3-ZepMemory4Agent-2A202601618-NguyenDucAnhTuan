# Lab 17 Benchmark Report

- Implementation: `student`
- Kind: `practice`
- Cases: **11**
- Passed: **11/11**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **858.9 ms**
- Average token reduction vs full source context: **19.1%**

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| E01 | short_term | PASS | 0.1 | 133 | 0.0% |  |
| E06 | semantic | PASS | 413.8 | 53 | 88.4% |  |
| E09 | long_term | PASS | 1894.6 | 737 | 0.0% |  |
| E10 | short_term | PASS | 0.4 | 195 | 0.0% |  |
| E02 | long_term | PASS | 1687.9 | 1110 | 0.0% |  |
| E03 | long_term | PASS | 1638.9 | 1104 | 0.0% |  |
| E04 | episodic | PASS | 291.5 | 247 | 0.0% |  |
| E05 | episodic | PASS | 302.1 | 266 | 0.0% |  |
| E07 | mixed | PASS | 1720.3 | 390 | 31.0% |  |
| E11 | semantic | PASS | 258.6 | 52 | 90.8% |  |
| E08 | long_term | PASS | 1239.8 | 1085 | 0.0% |  |

## Evidence excerpts

### E01 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### E06 - semantic

`EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.`

### E09 - long_term

`FACT: LOTUS-88 uses Java + Spring Boot for backend examples. FACT: Lan Tran's project is LOTUS-88. FACT: Lan Tran does not use Python in the backend example. FACT: 'Da hieu' is identified as LOTUS-88. FACT: Lan Tran prefers Spring Boot. FACT: Lan Tran prefers Java. FACT: The Lab Assistant identifies 'Da hieu' as the subject.  <USER_SUMMARY> Lan Tran's project is LOTUS-88. They prioritize Java and Spring Boot for backend development and do not use Python in this context. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + `

### E10 - short_term

`<SESSION_SUMMARY> user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. | assistant: Acknowledged review constraint. | user: Filler turn 1 about UI spacing. | assistant: Filler answer 1. | user: Filler turn 2 about naming. | assistant: Filler answer 2. | user: Filler turn 3 about logging. | assistant: Filler answer 3. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. - assistant: Acknowledged review constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler turn 4 about tests. assistant: Filler answer 4. user: Filler turn 5 about docs. assistant: Filler answe`

### E02 - long_term

`FACT: Minh Nguyen does not like Java. FACT: Minh Nguyen likes Python. FACT: Minh Nguyen is learning async/await. FACT: Minh Nguyen has a preference for Python for the personal demo ORCHID-27. FACT: Minh Nguyen's personal project is ORCHID-27. FACT: Minh Nguyen is currently debugging async HTTP. FACT: When explaining code, Minh Nguyen prefers the assistant to use short examples. FACT: Minh Nguyen has a to-do item to complete the benchmark report. FACT: Lab Assistant demoed the ORCHID-27 personal demo. FACT: Minh Nguyen sometimes confuses coroutine with Task. FACT: Minh Nguyen recommends reusing the aiohttp ClientSession. FACT: Minh Nguyen set the timeout to 60s while debugging, but the proces`

### E03 - long_term

`FACT: Minh Nguyen is learning async/await. FACT: Minh Nguyen sometimes confuses coroutine with Task. FACT: Minh Nguyen set the timeout to 60s while debugging, but the process still failed. FACT: Minh Nguyen is currently debugging async HTTP. FACT: Minh Nguyen identified connection churn as the main issue. FACT: Minh Nguyen has a to-do item to complete the benchmark report. FACT: Minh Nguyen recommends reusing the aiohttp ClientSession. FACT: Minh Nguyen requested that the topic of async/await be explained using a timeline if it comes up again. FACT: Minh Nguyen likes Python. FACT: Minh Nguyen's personal project is ORCHID-27. FACT: Minh Nguyen does not like Java. FACT: Minh Nguyen is updating`

### E04 - episodic

`EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + con`

### E05 - episodic

`EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: `

### E07 - mixed

`<LONG_TERM> FACT: When explaining code, Minh Nguyen prefers the assistant to use short examples. FACT: Minh Nguyen has a preference for Python for the personal demo ORCHID-27. FACT: Minh Nguyen likes Python. FACT: Minh Nguyen does not like Java. FACT: Minh Nguyen is learning async/await. FACT: Minh Nguyen recommends reusing the aiohttp ClientSession. FACT: Minh Nguyen is currently debugging async HTTP. FACT: Minh Nguyen's personal project is ORCHID-27. FACT: Minh Nguyen set the timeout to 60s while debugging, but the process still failed. FACT: Minh Nguyen sometimes confuses coroutine with Task. FACT: Minh Nguyen requested that the topic of async/await be explained using a timeline if it com`

### E11 - semantic

`EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.`

### E08 - long_term

`FACT: Minh Nguyen is updating that for project BLUEBIRD-42, the backend must use NestJS. FACT: Minh Nguyen is updating that for project BLUEBIRD-42, the backend must use TypeScript. FACT: The BLUEBIRD-42 uses NestJS. FACT: The BLUEBIRD-42 uses TypeScript. FACT: Minh Nguyen is updating that for project BLUEBIRD-42, the backend must use TypeScript with NestJS. FACT: Minh Nguyen is updating that for project BLUEBIRD-42, Python is not allowed for the backend. FACT: Minh Nguyen is learning async/await. FACT: Minh Nguyen is currently debugging async HTTP. FACT: Minh Nguyen recommends reusing the aiohttp ClientSession. FACT: aiohttp ClientSession has concurrency set to 20. FACT: Minh Nguyen has a p`

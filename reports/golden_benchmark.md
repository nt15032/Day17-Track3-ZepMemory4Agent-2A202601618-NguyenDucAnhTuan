# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **20/20**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **1759.1 ms**
- Average token reduction vs full source context: **15.3%**
- Golden bonus: **10/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.2 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.0 | 133 | 0.0% |  |
| G06 | long_term | PASS | 1964.6 | 670 | 0.0% |  |
| G09 | semantic | PASS | 1144.4 | 148 | 67.8% |  |
| G10 | semantic | PASS | 231.5 | 95 | 79.3% |  |
| G14 | mixed | PASS | 2964.0 | 431 | 0.0% |  |
| G03 | long_term | PASS | 2534.7 | 1082 | 0.0% |  |
| G04 | long_term | PASS | 3821.6 | 1084 | 0.0% |  |
| G07 | episodic | PASS | 257.2 | 564 | 0.0% |  |
| G08 | episodic | PASS | 319.3 | 578 | 0.0% |  |
| G11 | mixed | PASS | 2034.5 | 439 | 22.3% |  |
| G13 | mixed | PASS | 623.4 | 406 | 28.1% |  |
| G15 | mixed | PASS | 2543.9 | 736 | 0.0% |  |
| G16 | mixed | PASS | 1872.9 | 484 | 14.3% |  |
| G17 | mixed | PASS | 3343.8 | 484 | 14.3% |  |
| G18 | mixed | PASS | 704.9 | 359 | 36.5% |  |
| G19 | mixed | PASS | 4571.2 | 581 | 0.0% |  |
| G05 | long_term | PASS | 1524.8 | 1090 | 0.0% |  |
| G12 | mixed | PASS | 2367.0 | 387 | 38.8% |  |
| G20 | mixed | PASS | 2358.1 | 609 | 3.6% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G06 - long_term

`FACT: Lan Tran does not use Python in the backend example. FACT: Lan Tran prioritizes Java. FACT: Lan Tran prioritizes Spring Boot. FACT: Lan Tran's project is LOTUS-88. FACT: Java is related to Spring Boot.  <USER_SUMMARY> Lan's project is LOTUS-88. They prioritize Java and Spring Boot for backend development and do not use Python. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 10:28:54     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Evaluation User" }: Minh la Lan, phap ly hoi gat truoc khi bat memory tren san pham. Viet hop d`

### G09 - semantic

`EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3.`

### G10 - semantic

`EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3.`

### G14 - mixed

`<LONG_TERM> FACT: Lan Tran does not use Python in the backend example. FACT: Lan Tran's project is LOTUS-88. FACT: Lan Tran prioritizes Java. FACT: Lan Tran prioritizes Spring Boot. FACT: Java is related to Spring Boot.  <USER_SUMMARY> Lan's project is LOTUS-88. They prioritize Java and Spring Boot for backend development and do not use Python. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 09:43:51     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Evaluation User" }: Lan uu tien stack backend nao cho LOTUS-88?   - Created At: 202`

### G03 - long_term

`FACT: Minh Nguyen prefers to use Python for personal demos for project ORCHID-27. FACT: When explaining code, Minh Nguyen prefers short examples. FACT: Minh Nguyen likes Python. FACT: Minh Nguyen does not like Java. FACT: Minh Nguyen is learning about coroutine. FACT: Minh Nguyen is learning async/await. FACT: The personal demo ORCHID-27 prefers Python. FACT: Minh Nguyen tried to increase the timeout. FACT: Minh Nguyen is debugging async HTTP. FACT: Minh Nguyen rules out timeout threshold as the main issue. FACT: Minh Nguyen has a task to complete the benchmark report. FACT: Minh Nguyen sometimes confuses coroutine with Task. FACT: Da hieu has a personal demo called ORCHID-27. FACT: Minh Ngu`

### G04 - long_term

`FACT: Minh Nguyen has a task to complete the benchmark report. FACT: Minh Nguyen sometimes confuses coroutine with Task. FACT: Minh Nguyen is learning about coroutine. FACT: Minh Nguyen sometimes confuses coroutine with Task. FACT: Minh Nguyen is learning async/await. FACT: Minh Nguyen tried to increase the timeout. FACT: Minh Nguyen is debugging async HTTP. FACT: Minh Nguyen rules out timeout threshold as the main issue. FACT: Minh Nguyen's personal project is ORCHID-27. FACT: Timeline is prioritized when explaining Task. FACT: Minh Nguyen does not like Java. FACT: Minh Nguyen likes Python. FACT: Minh Nguyen suggests reusing aiohttp ClientSession. FACT: The Lab Assistant prioritizes timelin`

### G07 - episodic

`EPISODE: Minh con mot open-loop phai nop truoc deadline, dong thoi muon ghi chu retry payment dung so lan toi da theo policy. Nac lai ma task/deadline con dang do, va gioi han retry chinh t EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nha`

### G08 - episodic

`EPISODE: Minh con mot open-loop phai nop truoc deadline, dong thoi muon ghi chu retry payment dung so lan toi da theo policy. Nac lai ma task/deadline con dang do, va gioi han retry chinh t EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurr`

### G11 - mixed

`<LONG_TERM> FACT: Minh Nguyen tried to increase the timeout. FACT: Minh Nguyen rules out timeout threshold as the main issue. FACT: Minh Nguyen failed to debug async HTTP even after increasing the timeout to 60s. FACT: Minh Nguyen is learning about coroutine. FACT: When explaining code, Minh Nguyen prefers short examples. FACT: Minh Nguyen is learning async/await. FACT: Minh Nguyen is debugging async HTTP. FACT: Minh Nguyen likes Python. FACT: Minh Nguyen sometimes confuses coroutine with Task. FACT: Minh Nguyen sometimes confuses coroutine with Task. FACT: Minh Nguyen does not like Java. FACT: Minh Nguyen has a task to complete the benchmark report. FACT: Minh Nguyen suggests reusing aiohtt`

### G13 - mixed

`<EPISODIC> EPISODE: Minh con mot open-loop phai nop truoc deadline, dong thoi muon ghi chu retry payment dung so lan toi da theo policy. Nac lai ma task/deadline con dang do, va gioi han retry chinh t EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet co`

### G15 - mixed

`<LONG_TERM> FACT: Minh Nguyen is debugging async HTTP. FACT: Minh Nguyen failed to debug async HTTP even after increasing the timeout to 60s. FACT: Minh Nguyen is learning async/await. FACT: Minh Nguyen tried to increase the timeout. FACT: Minh Nguyen rules out timeout threshold as the main issue. FACT: Minh Nguyen suggests reusing aiohttp ClientSession. FACT: Minh Nguyen is learning about coroutine. FACT: Minh Nguyen likes Python. FACT: Minh Nguyen sometimes confuses coroutine with Task. FACT: Minh Nguyen sometimes confuses coroutine with Task. FACT: Minh Nguyen does not like Java. FACT: The timeout was increased to 60s. FACT: Minh Nguyen has a task to complete the benchmark report. FACT: M`

### G16 - mixed

`<LONG_TERM> FACT: The Lab Assistant prioritizes timeline when explaining coroutine and Task. FACT: Minh Nguyen is learning about coroutine. FACT: Minh Nguyen is learning async/await. FACT: Minh Nguyen is debugging async HTTP. FACT: Minh Nguyen tried to increase the timeout. FACT: Minh Nguyen suggests reusing aiohttp ClientSession. FACT: Minh Nguyen failed to debug async HTTP even after increasing the timeout to 60s. FACT: Minh Nguyen sometimes confuses coroutine with Task. FACT: Minh Nguyen sometimes confuses coroutine with Task. FACT: Da hieu has a personal demo called ORCHID-27. FACT: Minh Nguyen likes Python. FACT: Minh Nguyen rules out timeout threshold as the main issue. FACT: Minh Nguy`

### G17 - mixed

`<LONG_TERM> FACT: Minh Nguyen is learning about coroutine. FACT: Minh Nguyen sometimes confuses coroutine with Task. FACT: Minh Nguyen sometimes confuses coroutine with Task. FACT: Minh Nguyen is debugging async HTTP. FACT: Minh Nguyen suggests reusing aiohttp ClientSession. FACT: Timeline is prioritized when explaining coroutine. FACT: Minh Nguyen is learning async/await. FACT: Minh Nguyen likes Python. FACT: The Lab Assistant prioritizes timeline when explaining coroutine and Task. FACT: Minh Nguyen failed to debug async HTTP even after increasing the timeout to 60s. FACT: Minh Nguyen tried to increase the timeout. FACT: Minh Nguyen does not like Java. FACT: Minh Nguyen rules out timeout t`

### G18 - mixed

`<EPISODIC> EPISODE: Minh sap viet script ca nhan de tai hien su co latency, muon code dung ngon ngu minh thich khi lam mot minh, dong thoi bam sat playbook incident cua lab chu dung vo tang timeout. G EPISODE: Minh con mot open-loop phai nop truoc deadline, dong thoi muon ghi chu retry payment dung so lan toi da theo policy. Nac lai ma task/deadline con dang do, va gioi han retry chinh t EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. EPISODE: Toi se uu tien timeline khi giai thich coroutine va Task. EPISODE: TODO: hoan thanh bench`

### G19 - mixed

`<LONG_TERM> FACT: Minh Nguyen is debugging async HTTP. FACT: Minh Nguyen suggests reusing aiohttp ClientSession. FACT: Minh Nguyen failed to debug async HTTP even after increasing the timeout to 60s. FACT: Minh Nguyen is learning async/await. FACT: Minh Nguyen prefers to use Python for personal demos for project ORCHID-27. FACT: Minh Nguyen's personal project is ORCHID-27. FACT: Minh Nguyen sometimes confuses coroutine with Task. FACT: Minh Nguyen likes Python. FACT: Minh Nguyen does not like Java. FACT: Minh Nguyen is learning about coroutine. FACT: Minh Nguyen sometimes confuses coroutine with Task. FACT: The assistant is checking the client lifecycle. FACT: Minh Nguyen tried to increase t`

### G05 - long_term

`FACT: Minh Nguyen likes Python. FACT: Minh Nguyen prefers to use Python for personal demos for project ORCHID-27. FACT: Python is prohibited for the backend of the BLUEBIRD-42 project. FACT: The project BLUEBIRD-42 requires TypeScript for the backend. FACT: Minh Nguyen is debugging async HTTP. FACT: Minh Nguyen does not like Java. FACT: Minh Nguyen's personal project is ORCHID-27. FACT: Minh Nguyen is learning async/await. FACT: Minh Nguyen is learning about coroutine. FACT: The project BLUEBIRD-42 requires NestJS for the backend. FACT: Minh Nguyen suggests reusing aiohttp ClientSession. FACT: The ORCHID-27 uses Python. FACT: Minh Nguyen sometimes confuses coroutine with Task. FACT: The pers`

### G12 - mixed

`<LONG_TERM> FACT: The project BLUEBIRD-42 requires TypeScript for the backend. FACT: The project BLUEBIRD-42 requires NestJS for the backend. FACT: Python is prohibited for the backend of the BLUEBIRD-42 project. FACT: Minh Nguyen does not like Java. FACT: Minh Nguyen is learning about coroutine. FACT: Minh Nguyen prefers to use Python for personal demos for project ORCHID-27. FACT: Minh Nguyen's personal project is ORCHID-27. FACT: Minh Nguyen suggests reusing aiohttp ClientSession. FACT: Minh Nguyen is debugging async HTTP. FACT: Minh Nguyen tried to increase the timeout. FACT: Minh Nguyen is learning async/await. FACT: The Lab Assistant prioritizes timeline when explaining coroutine and T`

### G20 - mixed

`<SHORT_TERM> <SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Filler about dashboard widgets. | assistant: Filler. | user: Filler about CSS variables. | assistant: Filler. | user: Filler about copy review. | assistant: Filler. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler about empty charts. assistant: Filler. user: Filler about telemetry. assistant: Filler. user: Filler about a11y labels. assistant: Filler. </RECENT_TURNS> </SHORT_TERM>`

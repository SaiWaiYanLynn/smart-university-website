# Feasibility and consistency review, 14 October 2026

Question: can the chosen stack carry out every scenario that the Figma prototype shows? The stack is LangChain, LangGraph, FastAPI, a PostgreSQL database, Chatwoot, Keycloak and OpenRouter. This note also lists the places where the documents disagree.

Some facts come from the web and some are my inference. Each inference is marked. Every marked item needs a short test (a spike) before the team promises it.

## 1. Verdict

1. Every scenario is possible in principle. Nothing needs a new kind of technology.
2. Three items are real risks: the free model quota, rich cards on LINE and Telegram, and the database choice.
3. Five items are gaps in the design, not in the stack. They are the ER diagram, the applicant accounts, the privacy of the instructor brief, the embedding model and the account linking.

## 2. Decision needed first: NeonDB or PostgreSQL in Docker

CLAUDE.md says PostgreSQL 16 with pgvector in Docker Compose, started with one command. The latest request names NeonDB. These two do not match.

1. Neon is hosted PostgreSQL. It supports pgvector.
2. The free plan has 0.5 GB of storage and 100 compute hours for each project. The database stops after 5 minutes without use and wakes in about a second.
3. Neon offers a pooled endpoint, and this endpoint uses transaction mode. Session features break there. The LangGraph PostgreSQL saver likely needs the direct endpoint. This is an inference. A spike must check it.
4. Chatwoot needs its own PostgreSQL with pgvector. It cannot share the Neon free project without risk to the 0.5 GB limit.
5. Docker Compose keeps the "one command" promise in the scope. Neon breaks it, because the examiners need a Neon account and a network link.

Recommendation: keep PostgreSQL in Docker Compose for the demo and the tests. Name Neon as the production option. Wai Yan Lynn decides.

## 3. Blockers and risks

### B1. The free model quota is far too small

1. OpenRouter free models allow about 20 requests a minute and 50 requests a day. A one-time purchase of 10 dollars of credit lifts the day limit to 1,000.
2. The limits belong to the account. A second key on the same account adds nothing. One key for each member on four separate accounts is legitimate and gives about 200 requests a day.
3. One student message costs several model calls. The supervisor routes, an agent selects a tool, and the agent writes the answer. A turn takes 3 calls and a multi-agent turn takes 7 or more.
4. The evaluation set has 150 messages. That needs about 450 to 600 calls. On the free plan this takes 3 to 12 days.
5. The A2.2 sample frame shows 182, 171 and 140 requests a day for each key. These numbers are impossible under the free cap. Change them to values below 50, or change the story to a paid plan.
6. Recommendation: buy the one-time credit on one account for the evaluation. Cache every evaluated answer so a re-run costs nothing.
7. Free models can be withdrawn without notice, and their tool calling is unconfirmed. Test two or three models with the real tool schemas before the model choice.

### B2. Rich cards on LINE and Telegram

1. The LINE and Telegram frames show slot cards, a summary card, a citation card and a status timeline.
2. Chatwoot documents cards, buttons and forms for the web widget only. I found no proof of these on its LINE and Telegram channels. This needs a spike.
3. LINE shows cards through Flex messages. Telegram shows buttons through inline keyboards. Both need the app to call the channel API directly.
4. Option A: the app sends the rich message straight to LINE or Telegram and copies the text into Chatwoot through its API. Staff still see the chat.
5. Option B: the app uses Chatwoot as it is and the LINE frames become text with quick replies. The frames then need a redesign.
6. Recommendation: run the spike in week 1 of Project I. The frames stay as they are until the result is known.

### B3. Two web chats

1. The prototype has a custom React chat page with history and an Agent Trace panel. The scope also lists the Chatwoot web widget.
2. Pick one path. The simplest path is a custom chat that talks to the app, with a Chatwoot API inbox that holds a copy. Staff then see every chat and the handoff works.
3. This design is my inference. The spike in B2 can check it at the same time.

### B4. LINE push quota

1. Reply messages are free. Push messages count against a monthly free quota. The exact number for Thailand was not verified.
2. J12 sends the first message. This is a push. Plan for a small number of reminders in the demo and say so in the proposal.
3. Telegram can send to a user only after that user starts the bot.

### B5. Heavy self-hosted Chatwoot

Chatwoot runs a Rails app, a worker, Redis and PostgreSQL. Expect 2 to 4 GB of memory. Check that every team laptop runs it next to the app, Keycloak and the database.

### B6. Staff sign in twice

Staff use Keycloak for the console and Chatwoot has its own users. The open source edition of Chatwoot likely has no OIDC single sign-on. This is an inference and needs a check. The fix is a short note in the proposal.

## 4. Scenario by scenario

1. J1, a policy answer with a citation. Possible. Retrieval over pgvector returns the chunk and its page. The citation card shows that chunk. Feedback saves to a table.
2. J2, refusal and human handoff. Possible. Chatwoot agent bots keep a chat pending until a human takes it. When a human owns the chat, the app must stop replying.
3. J3, own records and refusal. Possible. The tool layer reads the subject from the token. The refusal comes from code, not from the model.
4. J4 and J6, booking and two students for one slot. Possible. A unique constraint or a row lock gives one winner. This is the best scenario to test.
5. J5, a request with a timeline. Possible. A state machine with four states and an audit row for each change.
6. J7, catalogue search. Possible. Use PostgreSQL full text search with a trigram index on about 50 seeded books.
7. J7.5 and J7.6, loan renewal. Possible. The rules run in code. The model only reads the intent and asks for a yes.
8. J8, payment slip. Possible. The app downloads the image from the channel, saves it in private storage and checks the role on every read. LINE needs a token to fetch the image. The model never sees the image, so vision support does not matter.
9. J9, assistant busy. Possible. The adapter catches the 429 error and queues the message.
10. J10, memory across days. Possible. Save facts and a summary in a table keyed by student ID. LangGraph also has a long term store. The student must link LINE to the account first, or the app cannot find the student.
11. J11, one message and three agents. Possible but slow. The supervisor package hands off one agent at a time. Parallel work needs a custom graph. Expect 15 to 30 seconds on a free model.
12. J12, the assistant writes first. Possible. A scheduler container reads bookings and sends a fixed text. No model call is needed. See B4 for the quota.
13. R1, agent checks. Possible. The checks must be plain code. A model must not decide a deadline or a hold.
14. R2, instructor brief. Possible with read only records. See section 5, item 3.
15. A1, upload and unanswered questions. Possible. The ingestion worker parses, splits and embeds the file. "Asked 14 times" needs a grouping step, so store the question embedding and group by similarity.
16. A2, accounts and system health. Possible. The adapter counts its own 429 errors. Usage per key comes from the provider or from the adapter log.
17. Agent Trace panel. Possible. LangGraph streams each step. The app turns those events into trace rows.

## 4b. Records on LINE and Telegram

J13 and J14 let a student ask for the balance, the timetable, grades, loans and the request state in a chat.

1. This is possible. The Records agent reads these tables through read only tools. The linked student ID selects the rows.
2. The answers are plain text. They need no card, so they work through Chatwoot on both channels.
3. The LINE rich menu and the Telegram inline buttons need the channel API. Chatwoot does not set them. This is the same risk as B2. The spike in section 7 covers it.
4. Every read writes an audit row. This is a privacy rule, because a grade is personal data.
5. Each answer costs 3 model calls on the free tier. A student who asks six questions uses 18 of the 50 daily requests of one account.
6. A command such as /grades can skip the model. The app can answer it with fixed code. This saves quota and makes the answer exact. The frames show the model path, which is the harder case.

## 4c. Text only through Chatwoot

Wai Yan Lynn asked about a text only design that reaches the supervisor through the Chatwoot API. This design works, with limits.

1. Flow: the student writes on LINE or Telegram. Chatwoot receives the message and calls the backend by webhook. The supervisor answers and the backend posts the reply through the Chatwoot API.
2. Photos arrive as attachments in the same webhook. J8 and J20 use this path.
3. The LINE rich menu needs no channel API at run time. A tap sends a normal text message. The University sets the menu once in the LINE console.
4. Telegram commands need no channel API either. BotFather lists them, and a command arrives as text.
5. Quick reply chips, inline buttons and cards need the channel API. J13 and J14 show chips, so they need that path. J15 to J20 use text only.
6. I have not tested Chatwoot end to end. The week 1 spike must send a text and a photo through both channels.

## 4d. Agent only scenarios, J15 to J20

1. J15, a what-if sum. A tool sums the exact grade points. The model must not do the arithmetic.
2. J16, a plan. It needs the load limit from a cited rule, the credits from records and a sum. The handoff to the instructor writes to the brief.
3. J17, a standing instruction. The Request agent saves a watch. The state machine raises an event and the watch sends the message. This needs an event table and a worker.
4. J18, a condition. The Booking agent reads the timetable first, offers slots and keeps the offer in the chat state. The reply "1" only works with that state.
5. J19, a failed tool. The graph keeps the open question and retries on a timer. This is a LangGraph checkpoint plus a scheduler.
6. J20, a rule with a date and a file. A tool counts the working days. The photo goes to private storage and staff. The model never reads it.
7. The risk is quota. J16 and J20 cost 5 to 8 model calls each on the free tier. Count them in the evaluation plan.

## 4e. Role scenarios 2

These scenarios show the consoles that the agents feed. Staff chat is now in scope, see section 4f.

1. R3, a summary and a draft. The Knowledge agent writes both at the moment of escalation. This costs one extra model call. A person edits and sends the draft.
2. R4, slip checks. The amount and the name need a text reader for the image. Use a fixed tool for this, not the language model, so the privacy rule holds. The duplicate check compares a hash of the file with earlier files.
3. R5, queue order. A scoring rule that uses the deadline, the checks and the waiting time can run in code. The model only writes the reason text.
4. R6, advisee signals. A nightly worker reads the records and applies rules such as a fall of 0.5 in the average or no sign-in for 14 days. The invitation is the Booking agent writing to the student.
5. R7, plan review. The same plan tool as J16 runs again after each change of the records, so the plan updates itself.
6. A3, conflicts. The ingestion worker compares the passages that answers cite. A similarity search finds the pairs and a rule compares the numbers.
7. A4, blocked calls. The checker already exists in the design. This page reads its audit rows.
8. The risk is privacy for R6. An instructor sees the records of the advisees only. Add this rule to the role checks and to the test plan.

## 4f. Chat for staff, instructors and administrators

Wai Yan Lynn decided on 15 October 2026 that staff and teachers use the assistant in chat. J21 to J23 show it.

1. The design stays the same. One supervisor and four agents serve every role. The role comes from the token and selects a tool set. No new agent is needed.
2. The security rule matters more now. The tool layer must filter rows by role: advisees for an instructor, passed conversations for staff and system data for an administrator. Write a test for each role and for each limit.
3. Every write asks for a yes and writes an audit record with the staff ID. This is the same rule as for students.
4. Staff accounts link to LINE and Telegram like student accounts. The staff console already uses Keycloak, so the role claim exists.
5. The scope grows. Four students and ten weeks are tight. The professor already warned about this. Build the student chat first and the role chat second. J21 is the smallest part, because it only reads.
6. The evaluation sets grow. Add 20 role questions to the 50 and add role messages to the 100 routing messages. This costs more model calls on the free tier.
7. The answers about people need care. An instructor must not read the chats of students. The frames show this limit in J21.2 and J22.6.

## 5. Gaps in the design

1. The ER diagram lacks these tables: courses, class sessions, grades, notifications, feedback, the advisor link and contact messages. It also lacks site content such as news and events. Add them before the proposal.
2. Applicants fill in the Apply wizard and have no account. The decision says an administrator creates every account. Add an APPLICATION table and a public endpoint without login, or remove the wizard from the portal scope.
3. The instructor brief summarizes the private chat of a student. The frame shows no consent. Add a consent step in the frame and the proposal, or limit the brief to topic labels.
4. The embedding model is not chosen. Thai text needs a multilingual model. Free hosted embeddings are unconfirmed. A small model in the app container is the safe option.
5. LINE and Telegram account linking has to be built. The profile frames show it, and the scope does not list it.
6. The tool layer needs a rule that blocks any text in a message from changing the subject. Add a test for it.

## 6. Documents that disagree

1. The two submitted PDFs still say Ollama and a local model. CLAUDE.md lists the corrections.
2. The performance targets in NFR-01 (4 seconds to a first token and 15 seconds to a full reply) predate OpenRouter. Reset them after the model test.
3. The use case diagram does not exist yet. Build it in draw.io from the written spec.
4. The design note lists the loan rules as decided. The team has not approved them yet.

## 7. Spikes for week 1 of Project I

1. Send a Flex message and a Telegram button through Chatwoot and through the direct API. Record which one works.
2. Call three free models with the Booking tool schema. Record the tool call success rate.
3. Run the LangGraph saver against the direct database endpoint and against a pooled endpoint.
4. Time a three agent turn on the free plan.
5. Fetch a LINE image and a Telegram image and save both to private storage.

# Smart University Website: Chat Journey Scripts

For the Figma prototype. Every frame below is one Figma frame. The text is final. Lay it out, do not rewrite it.

Student persona used throughout: **Wai Yan Lynn, 67111411, 3rd year ICT.**

The university name is Thales University, a placeholder that the team can change later. Dates follow the 2026 calendar. All journeys happen on Wednesday 14 October 2026. Portal frames show Thursday 15 October 2026, in the morning. The request is ready on Friday 16 October 2026. The booking happens at 11:34. The escalation happens at 14:22. The transcript request happens at 14:31. The staff takeover happens at 14:37.

Conventions:
- **U:** student message bubble, right aligned
- **A:** agent message bubble, left aligned
- **S:** system note, centred, muted, small
- **H:** human staff bubble, left aligned, with avatar, name and role
- `[Button]` is a chip or button component inside the bubble

---

## J1. Policy question answered with a citation (4 frames)

**F1.1**
U: What documents do I need from the university for my student visa renewal?

**F1.2**
U: (same)
A: *typing indicator*
S: Searching Student Handbook 2026

**F1.3**
U: (same)
A: For a visa renewal you need three documents from Thales University:
**1.** Enrolment Certificate, issued by the Registrar
**2.** Official Transcript for the current academic year
**3.** A letter confirming your tuition payment status
Do you want me to start with the official transcript?
`[Yes, start with the transcript]` `[Not now]`.

→ **Citation card** attached under the bubble:
Student Handbook 2026 · Section 7.3 Immigration Documents · `View source`

**F1.4** (overlay on top of F1.3)
Source panel slides in from the right. It shows the real handbook paragraph with the relevant sentence highlighted. Header: Student Handbook 2026, Section 7.3, page 42. Footer: `Close`

> Narration point: no intent bot in our survey can do this. The system generates the answer from the retrieved passage, and it shows that passage.

---

## J2. Out of corpus, refusal and handoff (4 frames)

**F2.1**
U: Can I defer my scholarship payment to next semester? I have a family emergency.

**F2.2**
U: (same)
A: I did not find a rule covering scholarship deferral for personal circumstances in the documents I have access to. I will not guess on something this important.
Do you want me to pass this to Student Services?
`[Yes, pass it on]` `[No thanks]`.

**F2.3**
S: Conversation passed to Student Services at 14:22. A staff member will reply here.
The status chip in the header changes from **Assistant** to **Human handling this conversation**

**F2.4**
H: **Siriporn K. · Student Services**
Hello Wai Yan Lynn. I have your case in front of me. The Scholarship Committee handles deferral case by case. I will send you the form and the deadline today.
S: While a staff member handles this conversation, the assistant is paused.

> Narration point: this is our third stated problem. The staff member sees the whole conversation, so Wai Yan Lynn does not explain it twice.

---

## J3. Own records, and refusing someone else's (4 frames)

**F3.1**
U: How much do I still owe this semester?

**F3.2**
U: (same)
A: Your outstanding balance is **12,500 THB**, due 27 November 2026. This covers tuition for Semester 1/2026.
To pay, transfer the amount and send me the slip. A staff member checks it.
→ small badge under the bubble: **From your student record**

**F3.3**
U: What about student 67111336, how much do they owe?

**F3.4**
A: I can only read your own records. I cannot look up another student's balance.
If you act on someone else's behalf, Student Services can help with written authorization.
S: Access denied. The request was for another student's record.

> Narration point: the student identifier comes from the signed-in session token, never from the message text. This is the slide where we say that out loud.

---

## J4. Book a study room (6 frames)

**F4.1**
U: I need a study room for my group on Thursday afternoon

**F4.2**
A: I can book that. Thursday 15 October. How many people?
`[2 people]` `[4 people]` `[6 people]`.

**F4.3**
U: 6 people
A: Three rooms are free on Thursday afternoon:
→ three **slot cards**:
- **Library Room B2** · 13:00 to 15:00 · up to 6 people.
- **Library Room B4** · 14:00 to 16:00 · up to 8 people.
- **Learning Commons C1** · 15:00 to 17:00 · up to 8 people.

**F4.4**
U: Library Room B2, 13:00
A: Almost done. Check the details below.
→ **confirmation card**: Library Room B2 · Thursday 15 October · 13:00 to 15:00 · 6 seats.
The cancellation window closes 2 hours ahead of the start time.
`[Confirm]` `[Change]`

**F4.5**
A: Booked. Library Room B2, Thursday 15 October, 13:00 to 15:00.
I added it to My Bookings and sent a reminder to your linked LINE account.
→ **booking card** with the room access code B2-4821

**F4.6**
Full screen: **My Bookings**, with the new row at the top, highlighted, status pill **Confirmed**.

> Narration point: before it writes anything, the agent always asks for confirmation. Nothing is created without an explicit yes.

---

## J5. Submit and track a document request (5 frames)

**F5.1**
U: I need an official transcript for a job application

**F5.2**
A: I can submit that for you. Two things: how many copies, and do you want to collect it or have it posted?
`[1 copy]` `[2 copies]` `[3 or more]` · `[Collect]` `[Post]`

**F5.3**
U: 2 copies, collect
A: Almost done. Check the details below.
→ **summary card**: Official Transcript · 2 copies · Collect at the Registrar · Fee 200 THB, payable on collection.
`[Confirm]` `[Change]`

**F5.4**
A: Submitted. Your reference is **REQ-2026-0481**.
When the state changes, I will message you here.
→ **status timeline** component:
● Submitted, 14 Oct 14:31 · ○ Under review · ○ Ready · ○ Collected.

**F5.5** (same conversation, later, with a day divider)
S: 16 October
A: Your transcript **REQ-2026-0481** is **Ready for collection** at the Registrar, counter 3. Collect it by 23 October.
→ timeline advanced: ● Submitted · ● Under review · ● Ready, today 09:12 · ○ Collected.

> Narration point: only 3 of the 17 universities we surveyed show a student the state of a request. None of the 12 Thai ones do.

---

## J6. Two students, one slot (3 frames)

**F6.1**
Split frame, two phones side by side. Wai Yan Lynn on the left, a second student on the right. Both see the same slot list from F4.3, and both have **Library Room B2 · 13:00 to 15:00** on screen.

**F6.2**
Left: A: Booked. Library Room B2, Thursday 15 October, 13:00 to 15:00.
Right: A: Library Room B2 at 13:00 was taken a moment ago. Here are the closest alternatives:
→ two replacement slot cards

**F6.3** (annotation frame, not a user interface screen)
Diagram overlay showing what happens underneath. Four steps: open a transaction, lock the slot row, read the slot again, then commit or roll back. One student commits and one rolls back. Caption: a double booking is impossible, because the read and the write happen inside the same transaction.

> Even if F6.1 and F6.2 are cut, keep F6.3. It is the frame that earns technical marks.

---

## Channel frames (6)

**LINE, 3 frames.** The J4 booking conversation inside LINE phone chrome. Reuse the text of F4.1, F4.3 and F4.5 exactly. The point: same assistant, same conversation, no app to install.

**Telegram, 3 frames.** The J5 notification arriving. Frame 1: the "Ready for collection" message arriving as a push notification on a lock screen. Frame 2: the conversation open in Telegram, showing it in context. Frame 3: the student replies "thanks" and the agent gives the collection window.

---

## Staff console (4 frames)

**SC1, Queue.** Table of open items: type, student, subject, state, age, assignee. Filter chips along the top: All · Requests · Bookings · Escalated. One row has a red bar, the escalated conversation from J2. The snapshot is 14 October at 14:34.

**SC2, Conversation takeover.** The J2 conversation open on the staff side, with the full history visible and a banner: You are handling this conversation. The assistant is paused. `[Release back to assistant]`

**SC3, Request state change.** REQ-2026-0481 open, current state Under review, with a state selector and a confirmation step. Note under the button: the student gets a message on their originating channel.

**SC4, Audit log.** Table of actor, action, target and timestamp. The agent's booking write and the staff member's state change appear as separate rows.

---

## J7. Find a book in the library catalogue (4 frames)

**F7.1**
U: Do we have a book on database systems? Where can I find it?

**F7.2**
U: (same)
S: Searching the library catalogue

**F7.3**
U: (same)
A: Yes. The Library has 3 books on database systems. 2 are free to borrow now.
→ two **book cards** with title, author, call number, shelf and an availability pill.
→ small badge: **From the library catalogue**
`[Show the third book]` `[Open the catalogue]`

**F7.4**
U: Show the third book
A: Database Design for Mere Mortals is checked out. It is due back on 22 October. I cannot reserve books yet, but I can book a study room for you.
→ one **book card** with the pill **Checked out**.
`[Book a study room]` `[Open the catalogue]`

> Narration point: the answer comes from a database query on the catalogue table. The assistant states what it cannot do and offers the next step it can do.

---

## J8. Pay tuition with a slip (4 frames)

**F8.1**
U: I paid my tuition. Here is the slip.
→ the **slip image** as a picture bubble: 12,500.00 THB, 14 Oct 2026, 16:05.

**F8.2**
A: Thank you. I received your slip for 12,500 THB. A staff member checks it before your balance changes. When it is done, you get a message here.
→ **status timeline**: ● Slip received, 14 Oct 2026, 16:06 · ○ Under review · ○ Confirmed · ○ Balance updated.

**F8.3**
S: 15 October
A: Student Services confirmed your payment of 12,500 THB. Your balance is now 0 THB.
→ **receipt card**: Amount 12,500 THB · Paid on 14 October 2026 · Checked by Siriporn K. · Balance 0 THB · Receipt number RCP-2026-0813.

**F8.4** (alternative: the slip is not clear)
S: 15 October
A: The amount on your slip is not clear. Please send a new photo or a screenshot from your banking app.
→ the **slip image** with the details blurred.
`[Send a new slip]` `[Talk to Student Services]`

> Narration point: the assistant never decides on money. It passes the slip to a person, and the balance changes only after a staff member confirms it.

---

## Portal and public pages (not chat)

The public site has 13 pages and a mega menu. The student portal adds Academics (Timetable, Grades, Courses), Fees, Library and Notifications. The frames follow the page names in the Figma file.

## Staff console, added on 13 October (9 frames)

**SC1b, Queue with a payment slip.** The queue on 15 October at 09:30. The first row is the payment from Wai Yan Lynn. A warning toast says that a slip waits for a check.

**SC5, Requests.** All requests with their state. **SC6, Bookings.** All bookings. **SC7, Payments.** Every slip with its state: waiting, confirmed or rejected.

**SC8, Slip review.** The slip image, the payment details and four checks. Actions: `[Confirm payment]` `[Ask for a new slip]`.

**SC9, Confirm payment.** A dialog: Wai Yan Lynn gets a receipt and the balance changes to 0 THB. **SC10, Ask for a new slip.** A dialog for the unclear slip. **SC11, Payments after confirmation.** The row is Confirmed and a toast shows the receipt number.

**SC12, Conversation with a payment slip.** The student conversation on the staff side. A banner says that the assistant created a payment check, with the action `[Open payment check]`.

---

## States and errors, added on 13 and 14 October

**J9.1, the assistant is busy.** The free tier reached its limit. The assistant says it is busy and offers `[Try again]` and `[Ask Student Services]`. The first button goes back to the answer. The second hands the chat to a person.

Other state frames: login with a wrong password, search results with the assistant offer, a 404 page and a library search with no result. More frames: empty notifications, the Apply steps 2 to 4 and an application submitted page. The last frames show a contact message sent, a renewed loan, all notifications read, two Timetable weeks and a cookie notice on Home.

## J10, the assistant remembers across days (LINE, 19 and 20 October)

**F10.1** Monday 19 October, 17:40. S: Can I still withdraw from ICT440?

**F10.2** A: Yes. You can withdraw from a course until the end of week 8, which is 30 October 2026. The transcript then shows a W grade. → **citation card**: Student Handbook 2026, section 5.4. S: I need to think about it first. A: No problem. I will remember this chat, so you can come back to it. A note beside the phone says what the memory holds: topic, rule, deadline and the student ID.

**F10.3** Tuesday 20 October, 08:50. Same chat. S: Can I do that one from yesterday?

**F10.4** A: Yesterday you asked about withdrawing from ICT440 Project Studio. The deadline is 30 October 2026, so you can still do it. Shall I start the withdrawal request? `[Yes, start the request]` `[Not now]` A note says that the topic came from memory, found by student ID.

**F10.5** S: Yes, start the request. A: Done. The deadline has not passed and no hold is on your account. Student Services reviews the request next. → **summary card**: REQ-2026-0489, course withdrawal, ICT440 Project Studio, Handbook 5.4, submitted Tuesday 20 October at 08:52.

**F10.6** The portal shows REQ-2026-0489 with the channel LINE and the note that it started from the chat of 19 October.

> Narration point: the memory belongs to the student, not to the channel. LangGraph keeps it in PostgreSQL under the student ID. Chatwoot holds one contact for LINE, Telegram and web.

## Role scenarios, added on 14 October (12 frames)

**R1, Student Services staff.** R1.1 shows requests with an agent checks column. R1.2 is the brief for REQ-2026-0489 with three passed checks and the source chat. R1.3 shows the approved request and the message sent to the student.

**R2, instructor Dr. Kanda.** R2.1 lists advisees with the appointments that the assistant booked. R2.2 is the advising brief for Wai Yan Lynn, taken from the chat. R2.3 is the meeting notes page.

**A1, administrator Anan P., closing a knowledge gap.** A1.1 lists questions without an answer, and the top one was asked 14 times. A1.2 lists the documents with an Upload button. A1.3 shows the new file read, split and indexed, with a citation check on three questions. A1.4 shows the gap closed.

**A2, administrator.** A2.1 lists accounts and says that there is no self-registration. A2.2 shows system status with sample values for model keys, rate limit hits and the evaluation score.

> Narration point: these consoles show how the agents save staff time. Staff can also ask the assistant in chat, see J21 to J23.

## J11, one message and three agents (web, Wednesday 14 October, 10:05)

**F11.1** S: I want to plan my graduation. How many credits do I still need, and can I see Dr. Kanda about it? The typing indicator shows. A trace panel says that the supervisor split the message into three tasks.

**F11.2** A: You have 66 of 132 credits, so you need 66 more. The rule is 132 credits and a grade point average of 2.00 or higher. Dr. Kanda is your advisor. These times are free: → **citation card** Student Handbook 2026, section 6.2 → two **slot cards** for Dr. Kanda. The trace lists the Records, Knowledge and Booking steps.

**F11.3** S selects Wednesday 21 October, 10:00. A: Booked. I will send Dr. Kanda a short brief from this chat before the meeting. → **summary card**: booking ADV-2026-0147. My bookings already lists this appointment.

## J12, the assistant writes first (LINE, Tuesday 20 October, 10:00)

**F12.1** A: Your appointment with Dr. Kanda is tomorrow, Wednesday 21 October, at 10:00. I sent Dr. Kanda a short brief from our chats. Do you want to add anything? `[Add a topic]` `[Reschedule]` `[No, thanks]`

**F12.2** S: Add a topic. A: Which topic do you want to add? `[Course withdrawal, ICT440]` `[Study plan]` `[Something else]` This is the clarification turn. The assistant changes nothing before the student answers.

**F12.3** S: Course withdrawal, ICT440. A: Added. Dr. Kanda sees it in the brief, with your request REQ-2026-0489 and our chat of 19 October. A timed link then opens the instructor brief (R2.2).

> Narration point: the assistant starts the conversation when a timer finds an appointment in 24 hours. The same Agent Trace panel shows the agents and tools behind every answer.

## J7 extension, renewing a loan in chat (library, 14 October)

**F7.5** S: Please renew Clean Architecture. A: Clean Architecture is due on 22 October. It is not overdue and you have used 0 of 2 renewals. I can renew it for 14 days, to 5 November 2026. Shall I do it? `[Yes, renew it]` `[No, thanks]` The trace names the Supervisor, Records and Request agents.

**F7.6** S: Yes, renew it. A: Done. Clean Architecture is now due on 5 November 2026. You have 1 renewal left. A timed link then opens the Library account page with the new due date.

> Narration point: the Records agent only reads the loan. The Request agent writes the new due date after the student says yes, and the Audit step logs it.

## J13, ask everything on LINE (Thursday 15 October, 08:04)

**F13.1** A: Hello Wai Yan Lynn. Ask me about your balance, timetable, grades, loans or requests. You can also tap a button below. → **rich menu** with six buttons: Balance, Timetable, Grades, Loans, Requests and Bookings.

**F13.2** S: How much do I still owe? A: You owe 12,500 THB for tuition of Semester 1/2026, due 27 November 2026. Your slip of 14 October waits for a staff check. Then I message you.

**F13.3** S: What do I have today? A: Today, Thursday 15 October: 09:00 to 12:00, ICT430 Mobile Applications, Lab 2. 13:00 to 15:00, Library Room B2, access code B2-4821. Nothing else is planned.

**F13.4** S: What was my grade in Database Systems? A: ICT310 Database Systems, Semester 2/2025: B. Your grade point average is 3.43. You have 66 of 132 credits.

**F13.5** S: Which books are due? And where is my transcript? A: Clean Architecture is due on 22 October. Computer Networks is due on 29 October. Your transcript request REQ-2026-0481 is under review. Then I message you.

**F13.6** S: Please pay my tuition for me. A: I cannot move money. Send me a photo of your bank slip. A staff member checks it and you get a message.

> Narration point: the student never opens the website. Every answer comes from the Records agent, which only reads. The linked student ID decides whose records are read, and the message text never does.

## J14, ask everything on Telegram (Thursday 15 October, 12:18 to 12:24)

**F14.1** A: Hello Wai Yan Lynn. Type / to see what I can do, or ask in your own words. → command list: /balance, /timetable, /grades, /loans and /status.

**F14.2** S: /timetable tomorrow. A: Tomorrow, Friday 16 October: 09:00 to 11:00, ICT450 Technical English, Room 3-204. No booking is planned. `[Show my grades]` `[Back to the commands]`

**F14.3** S: /grades. A: Pick a semester. For an older one, type /grades 2/2024. `[Semester 2/2025]`

**F14.4** S: Semester 2/2025. A: Semester 2/2025, average 3.50, then the five grades of the semester.

**F14.5** S: /status. A: REQ-2026-0481, official transcript, 2 copies. State: under review. Submitted on 14 October 2026 at 14:31. Then I message you after each change.

**F14.6** S: /balance. A: Balance of Semester 1/2026: 12,500 THB, due on 27 November 2026. Your slip of 14 October waits for a staff check.

**F14.7** S: /loans. A: Clean Architecture, due on 22 October 2026. Computer Networks, due on 29 October 2026. You can renew each book twice.

> Narration point: a command is a shortcut. The supervisor reads it like any other message, so the same agents and rules serve every channel.

## J15 to J20, things that only an agent can do

These six scenarios use plain text only. A student can run them through Chatwoot with no button and no card. A fixed question and answer bot cannot handle any of them, because each one needs a record, a rule, a calculation or a later action.

**J15, what-if grade planning (Telegram, Thursday 15 October, 12:31).** S: Can I still reach 3.50 this semester? A: Your grade point average is 3.43 over 66 credits. This semester has 15 credits. You need an average of 3.80 in them, for example three A and two B+. Then you finish with 81 credits and 3.50. S: What if I get B+ in every course? A: Then your average becomes 3.44. With A in every course it becomes 3.54.

**J16, graduation plan (LINE, Thursday 15 October, 12:40).** S: Can I finish in Semester 2/2027? A: Yes, if you pass every course and keep an average of at least 2.00. A plan follows with 21, 15 and 15 credits in the next three semesters. The load limit is Handbook section 5.4. S: Send this plan to Dr. Kanda. A: Done. Dr. Kanda sees the plan in the brief for the appointment on Wednesday 21 October at 10:00.

**J17, standing instruction (LINE, Thursday 15 October, 09:50, then Friday 16 October, 09:12).** S: Tell me when my transcript is ready. A: Done. I watch REQ-2026-0481. On Friday the state changes to Ready and the assistant writes first with the collection details.

**J18, booking with a condition (Telegram, Thursday 15 October, 12:50).** S: I need a room for 6 on Friday after my class. A: The assistant reads the class that ends at 11:00 and offers two rooms. S: 1. A: Booked, reference BK-2026-0153.

**J19, a tool fails and recovers (LINE, Friday 16 October, 08:30 and 08:41).** S: What were my grades last semester? A: The grade service does not answer now. The assistant saves the question and tries again every 5 minutes. At 08:41 it sends the answer without a new question.

**J20, make-up exam request (LINE, Tuesday 20 and Wednesday 21 October).** S: I was sick on Monday and missed the ICT411 midterm. A: The assistant cites Handbook section 8.2, counts 3 working days to Thursday 22 October and offers a request. The student sends a photo of the certificate. The assistant opens REQ-2026-0490 and passes the photo to staff. On Wednesday the Registrar approves and the assistant writes the exam date.

> Narration point: each scenario needs a tool, a state or a rule that a prebuilt answer list does not have. The Agent Trace panel names the agents and the tools in every frame.

## Role scenarios 2, agent features for staff, instructor and administrator

Each console shows work that the agents and the background workers did, and a person decides every action. Staff, instructors and administrators can also ask for the same work in chat, see J21 to J23.

**R3, a handoff with a summary and a draft (staff, 14 October).** The escalated conversation of Wai Yan Lynn opens with a summary: what the student asked, what the assistant searched, what the records say and why a person is needed. A draft reply from Scholarship Rules waits in the composer. One button sends it and opens SC2.

**R4, a slip with a flagged check (staff, 15 October).** The assistant ran four checks on the slip of Napat R. The last one found that the reference was used before on another slip. The banner says that a person decides. The assistant never confirms a payment.

**R5, a queue sorted by the assistant (staff, 20 October).** The queue shows a priority and a reason for each row: a deadline, a student who waits, a fee hold, a routine item and a request that nobody collected.

**R6, advisees who need attention (instructor, 20 October).** The assistant read the records of the four advisees and flags three. The detail page for Napat R. shows the evidence and one step: ask the assistant to invite the student. The assistant then writes to the student on LINE and offers two free times.

**R7, a study plan to approve (instructor, 21 October).** The plan from J16 arrives with checks: the load per semester, the total of 132 credits, the average and the open courses. The assistant updated the plan on 20 October after the withdrawal of ICT440. One click approves it and the student gets a message.

**A3, sources that disagree (administrator, 20 October).** The assistant compared the passages it cited. It found that Library Policy v2 says 2 renewals and Student Handbook 2026 says 3. The page shows both passages. The administrator picks the right one and Student Services gets a task.

**A4, blocked attempts (administrator, 20 October).** A list shows every tool call that the checker stopped. A replay of one call shows the steps: the Records agent proposed a call for another student, and the checker stopped it before it ran.

> Narration point: the consoles stay simple, because the student side agents prepare the work. A person still decides.

## J21 to J23, the assistant for instructors, staff and administrators

Wai Yan Lynn decided on 15 October 2026 that staff and teachers use the assistant in chat too. These frames use plain text only. The same bot serves them. The linked account tells the role, and the role sets the tools and the rows that a tool can read.

**J21, an instructor (LINE, Tuesday 20 and Wednesday 21 October).** S: What classes do I have tomorrow? A: Tomorrow, Wednesday 21 October, there are the meeting at 10:00 and ICT411 Cloud Computing at 13:00 in Room 5-102. S: Prepare me for the meeting with Wai Yan Lynn. A: A short brief with the average, the credits, the approved withdrawal and the study plan. S: Move my meeting with Mali on Thursday to Friday afternoon. A: The assistant offers 15:00 or 16:00 and asks which. S: 15:00. A: Moved, and Mali S. is told on LINE. On Wednesday the instructor asks who needs a make-up exam in ICT411.

**J22, a staff member (Telegram, Tuesday 20 October, 09:11 to 09:30).** S: How many items wait for me and which is the oldest? A: 5 items. The oldest is REQ-2026-0487, blocked by a fee hold. S: Approve REQ-2026-0489. A: The assistant asks for a yes, then approves and tells the student. S: Remind everyone whose request is ready for more than 3 days. A: One student, a draft message and a question. S: Show me everything Wai Yan Lynn asked the assistant this week. A: The assistant shows only conversations that were passed to Student Services.

**J23, an administrator (LINE, Tuesday 20 October, 10:15 to 10:46).** S: Why were answers slow on Monday evening? A: 14 rate limit events on key 2, 9 delayed answers and no failure. S: Add this file, Examination Rules 2026. A: 96 sections indexed. One of the 4 open questions now has a cited answer. S: Create accounts for the 12 students in the file. A: 11 are valid and row 7 repeats an ID. After a yes the assistant creates 11 accounts.

> Narration point: the role comes from the account. The tools and the rows follow the role, and every write waits for a yes.

## J24, the instructor asks about attendance (LINE, Tuesday 20 and Wednesday 21 October)

**F24.1** S: Who missed ICT411 last Wednesday? A: Wednesday 14 October: 42 enrolled, 38 present, 1 late and 3 absent. The absent students are Kittipong A., Arthit S. and Chai W.

**F24.2** S: Is anyone close to the absence limit? A: Arthit S. has 3 absences in 9 classes. Handbook section 6.5 asks for a warning at 3 absences. Chai W. has 2. The assistant asks for a yes before it sends Arthit S. a message and tells Student Services.

**F24.3** S: Yes. A: Sent to Arthit S. on LINE. Student Services can see the warning, and the audit log holds it.

**F24.4** S (Wednesday 21 October): Did Wai Yan Lynn sit the midterm? A: No. She was absent on Monday 19 October. Her make-up exam, REQ-2026-0490, is approved for Monday 26 October at 13:00 in Room 5-102.

> Narration point: the instructor reads attendance of the own course only. A tool counts the absences, and the Handbook gives the limit.

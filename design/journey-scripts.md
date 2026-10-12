# Smart University Website: Chat Journey Scripts

For the Figma prototype. Every frame below is one Figma frame. The text is final. Lay it out, do not rewrite it.

Student persona used throughout: **Nadia Rahman, 67111402, 3rd year ICT.**

Once the team decides the university name, replace "the University" everywhere with one find-and-replace.

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
A: For a visa renewal you need three documents from the University:
**1.** Enrolment Certificate, issued by the Registrar
**2.** Official Transcript for the current academic year
**3.** A letter confirming your tuition payment status
Do you want me to request all three together?
`[Yes, request all three]` `[Not now]`.

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
Hello Nadia. I have your case in front of me. The Scholarship Committee handles deferral case by case. I will send you the form and the deadline today.
S: While a staff member handles this conversation, the assistant is paused.

> Narration point: this is our third stated problem. The staff member sees the whole conversation, so Nadia does not explain it twice.

---

## J3. Own records, and refusing someone else's (4 frames)

**F3.1**
U: How much do I still owe this semester?

**F3.2**
U: (same)
A: Your outstanding balance is **12,500 THB**, due 28 November 2026. This covers tuition for Semester 1/2026.
Do you want the payment reference?
→ small badge under the bubble: **From your student record**

**F3.3**
U: What about student 67111336, how much does he owe?

**F3.4**
A: I can only read your own records. I cannot look up another student's balance.
If you act on someone else's behalf, Student Services can help with written authorisation.
S: Access denied. The request was for another student's record.

> Narration point: the student identifier comes from the signed-in session token, never from the message text. This is the slide where we say that out loud.

---

## J4. Book a study room (6 frames)

**F4.1**
U: I need a study room for my group on Thursday afternoon

**F4.2**
A: I can book that. Thursday 16 October. How many people?
`[2 to 4]` `[5 to 8]` `[9 or more]`.

**F4.3**
U: 5 to 8
A: Three rooms are free on Thursday afternoon:
→ three **slot cards**:
- **Library Room B2** · 13:00 to 15:00 · up to 6 people.
- **Library Room B4** · 14:00 to 16:00 · up to 8 people.
- **Learning Commons C1** · 15:00 to 17:00 · up to 8 people.

**F4.4**
U: Room B2 at 1
A: Please confirm this booking:
→ **confirmation card**: Library Room B2 · Thursday 16 October · 13:00 to 15:00 · 6 seats.
The cancellation window closes 2 hours ahead of the start time.
`[Confirm]` `[Change]`

**F4.5**
A: Booked. Library Room B2, Thursday 16 October, 13:00 to 15:00.
I added it to My Bookings and sent a reminder to your linked LINE account.
→ **booking card** with a placeholder access code

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
A: Please confirm this request:
→ **summary card**: Official Transcript · 2 copies · Collect at the Registrar · Fee 200 THB, payable on collection.
`[Confirm]` `[Change]`

**F5.4**
A: Submitted. Your reference is **REQ-2026-0481**.
When the state changes, I will message you here.
→ **status timeline** component:
● Submitted, today 14:31 · ○ Under review · ○ Ready · ○ Collected.

**F5.5** (same conversation, later, with a day divider)
S: 17 October
A: Your transcript **REQ-2026-0481** is **Ready for collection** at the Registrar, counter 3. Collect it by 24 October.
→ timeline advanced: ● Submitted · ● Under review · ● Ready, today 09:12 · ○ Collected.

> Narration point: only 3 of the 17 universities we surveyed show a student the state of a request. None of the 12 Thai ones do.

---

## J6. Two students, one slot (3 frames)

**F6.1**
Split frame, two phones side by side. Nadia on the left, a second student on the right. Both see the same slot list from F4.3, and both have **Library Room B2 · 13:00 to 15:00** on screen.

**F6.2**
Left: A: Booked. Library Room B2, Thursday 16 October, 13:00 to 15:00.
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

**SC1, Queue.** Table of open items: type, student, subject, state, age, assignee. Filter chips along the top: All · Requests · Bookings · Escalated. One row flagged red, the escalated conversation from J2.

**SC2, Conversation takeover.** The J2 conversation open on the staff side, with the full history visible and a banner: You are handling this conversation. The assistant is paused. `[Release back to assistant]`

**SC3, Request state change.** REQ-2026-0481 open, current state Under review, with a state selector and a confirmation step. Note under the button: the student gets a message on their originating channel.

**SC4, Audit log.** Table of actor, action, target and timestamp. The agent's booking write and the staff member's state change appear as separate rows.

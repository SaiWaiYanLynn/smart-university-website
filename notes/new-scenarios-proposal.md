# Proposal: role scenarios, J10 and responsive pages

Date: 13 October 2026. Wai Yan Lynn approved the whole list on 14 October 2026. J10 moved to 19 and 20 October so it does not clash with the portal frames of 15 October. All scenarios are built.

The project scope says a staff-side conversational agent is out of scope. So each role scenario shows a console that the student-side agents feed. The benefit is time saved for the person, not a second chatbot.

## J10. The agent remembers across days (student)

Monday 19 October, 17:40, LINE. The student asks about the rule for a late course withdrawal. The agent cites the rule and says the deadline is 30 October.

Tuesday 20 October, 08:50, LINE. The student writes "can I still do that one from yesterday?" The agent names the topic and checks the date. It cites the rule again and offers to start the request. The student agrees and the agent opens REQ-2026-0489.

Frames: 4 on LINE, plus one frame in the portal that shows the new request with its source chat.

Benefit: the student never repeats the story. The chat history and the saved facts are keyed by student ID.

## R1. Registrar staff: a request arrives ready to approve

The agent checked the rules before the request reached the queue. The staff member opens REQ-2026-0489 and sees a brief: who asked, which rule applies, the checks the agent ran (deadline met, no hold on the account) and the source chat.

Frames: queue with a "checked by agent" column, request brief, one-click approve with a note.

Benefit: staff stop re-reading the chat and the handbook. The brief shows the time saved on a sample request.

## R2. Instructor: an advising brief before the appointment

Dr. Kanda has an advisor appointment with Wai Yan Lynn that the agent booked. The instructor console shows the brief: the topic from the chat, credits earned, current term load and open requests. Records are read only.

Frames: instructor home with advisee list and next appointments, advising brief, notes after the meeting.

Benefit: the first five minutes of the meeting are not spent asking for background.

## A1. Administrator: add a handbook and see the gaps

The administrator uploads Student Handbook 2026 (PDF). The page shows ingestion status: pages read, sections indexed and any failed pages. A second tab lists questions that the agent failed to answer with a citation. The administrator sees "late withdrawal fee" asked 14 times and uploads the missing policy.

Frames: documents page, ingestion result, unanswered questions, document uploaded and gap closed.

Benefit: the assistant improves with documents, not with code. This shows the retrieval story to the examiners.

## A2. Administrator: accounts and system health

Accounts: the administrator creates a student account and assigns a role (no self-registration, as decided). System health: the model key pool with usage per key, the number of rate-limit events and the 50-question evaluation score against the 80 percent target.

Frames: accounts page, system status page.

Benefit: it answers the question "what happens when the free tier runs out" in one frame.

## Responsive pages (decision D1)

Sizes: mobile 390 px and tablet 768 px. Pages: Home, Programs, Apply step 1, Dashboard, Assistant chat (J1.3) and My requests. This makes 12 frames. The compact Top Nav and a mobile menu are new.

## Total

About 20 new frames, plus 12 responsive frames. Wai Yan Lynn removes any scenario before the build.

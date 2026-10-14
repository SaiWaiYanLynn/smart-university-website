# Scope change: library search, payment slip and agent features

Date: 14 October 2026. Wai Yan Lynn decided that library catalogue search and the payment slip check are in scope for Project I. This note holds the text and rows that the Project Proposal, the feasibility report and the test plan need. The diagrams in `design/diagrams/` are already updated.

## 1. New requirements

Library catalogue search (Records agent, read only)

1. FR-L1. The student searches the catalogue by title, author, ISBN or subject in a chat or in the portal.
2. FR-L2. The answer shows availability, call number and shelf location from the database.
3. FR-L3. The search tool only reads. The loan list is read only too.
4. FR-L4. The student renews a loan in a chat or in the portal. The Request agent applies the renewal rules, asks for a yes and writes the new due date.
5. FR-L5. Borrowing, returning and holds are not part of Project I.

Payment slip check (Request agent, a person decides)

1. FR-P1. The student sends a slip image on web, LINE or Telegram.
2. FR-P2. The assistant stores the image and creates a payment check in the state waiting.
3. FR-P3. Staff see the check in a Payments tab and in the chat.
4. FR-P4. A staff member approves or rejects the slip. A rejection needs a reason.
5. FR-P5. The student gets a message on every linked channel after the decision.
6. FR-P6. The balance changes only after a staff member approves. The agent never decides on a payment.
7. FR-P7. Every step writes an audit record.

Features that the prototype shows and that the documents must also name

1. FR-M1. Memory across days and channels, keyed by the student ID.
2. FR-R1. A reminder that the assistant sends first, such as one 24 hours before an appointment.
3. FR-B1. A short brief for the instructor before an advising appointment.
4. FR-D1. An administrator uploads a document and sees the ingestion result.
5. FR-D2. An administrator reads the questions that the assistant failed to answer with a citation.
6. FR-A1. A page that shows the model keys, the rate limit hits and the evaluation score.

## 2. Privacy rule for slips

A slip shows a name, a bank and an account number. The proposal states these rules.

1. Only the student who sent the slip and staff with the Student Services role can open it.
2. The image sits in private storage. No public link exists. The API checks the role on every read.
3. The proposal suggests keeping an image for 90 days after the decision. The team sets the number.
4. The model never sees the image. A person reads it, so no image goes to OpenRouter.

## 3. Test plan rows

1. Catalogue: 10 questions in the 50-question set. The cases are a title search, an author search, a book with no copy and a book that does not exist.
2. Slip: 5 cases. A good slip, an unclear slip, a wrong amount, a slip from another student's chat and a file that is not an image.
3. The 100 routing messages include 10 catalogue questions and 5 messages with an image.
4. Memory: 3 cases. The same topic on the next day, the same topic on another channel and a request to forget a topic.
5. Reminder: 2 cases. A reminder at 24 hours and no reminder for a cancelled booking.

## 4. Risks to add

1. A slip can be forged. A person compares amount, account and time. The agent never approves a slip.
2. A slip holds personal data. The privacy rule in section 2 limits who sees it and for how long.
3. Seed data is small. A catalogue of about 50 books is enough for the demo. Real data comes from the adopting university.
4. Memory can keep a wrong fact. The student can ask the assistant to forget a topic.

## 5. Feasibility report v2

Add one paragraph to the scope section. Library search needs one read tool and a table of seeded books. The slip check needs an image upload, private storage and a staff tab. Both reuse the request state machine and the audit writer, so the build cost is small. The evidence table needs no new row.

## 6. Loans: decided

Wai Yan Lynn chose renewal in scope on 14 October 2026. Borrowing, returning and holds stay out. The renewal is a write, so the Request agent owns it and the Records agent stays read only.

1. Rules to seed in the library policy: a maximum of two renewals, a renewal of 14 days and no renewal for an overdue book.
2. Tests: 4 cases. A renewal that works, a book at the renewal limit, an overdue book and a loan that belongs to another student.
3. The 100 routing messages include 5 renewal messages.

## 7. Documents to update

1. Project Proposal, 17 sections: requirements, test plan, risks and the privacy rule.
2. Feasibility report v2: the scope paragraph. The PDF source was lost, so rebuild it only if the report is submitted again.
3. Diagrams: done on 14 October 2026. Rebuild the use case diagram in draw.io from `design/diagrams/diagrams-source.md`.

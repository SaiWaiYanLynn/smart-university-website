# Guest access and more diagrams, 15 October 2026

Wai Yan Lynn asked that guests read the curriculum and the course information. A guest is a visitor with no account. This note records the decisions, what the prototype now has and the diagrams that were added.

## 1. Decisions

1. Course pages are one set for everyone. A guest sees the Public nav. A signed-in student sees the Portal nav on the same page.
2. A guest never uses the assistant. The public pages have no call to chat. They point to Contact admissions instead.
3. The site is English only for now. The Thai and English switch is not built.
4. The visit page is not needed. The Contact page already holds the address, the opening hours and the directions.

## 2. What a guest can do

1. Read Home, Programs, Program detail, the curriculum, two course pages, Faculties, People and About.
2. Read Admissions, Fees and scholarships, Rules and policies, the Student Handbook, the Academic calendar, News and Contact.
3. Apply online, check the application status, send a contact message and search the site.
4. Search the Library catalogue. A guest sees the title and the shelf. The free copies need a login.

## 3. What the prototype has now

1. Program detail has a Curriculum tab with 42 courses, their prerequisite and their type. The tabs Curriculum, Admission and Fees open pages.
2. The rows ICT310 and ICT463 open a course page. The portal Courses page opens the same ICT463 page with the Portal nav.
3. The Fees and scholarships page holds the tuition table, three scholarship cards and four payment steps.
4. The application status page takes a reference and an email. The result page shows four steps.
5. Rules and policies lists four documents. The Student Handbook opens online.
6. The People page shows eight instructors and researchers.
7. Admissions, About and Faculties link to the new pages. The Application submitted page links to the status page.
8. Every guest call to chat is now Contact admissions. This covers Programs, Program detail, Apply, the mega menu, Search results and the mobile and tablet copies.

## 4. Rules for guest access

1. A guest never reads a student record, a booking, a request or a slip.
2. Every public form writes to its own table. These are the application, the contact message and the status request.
3. A public page needs no token. The REST API limits the rate of public endpoints to stop abuse.

## 5. Changes in the data model

1. The ER diagram has PROGRAM, FACULTY, PROGRAM_COURSE and STAFF_PROFILE tables.
2. COURSE has a description and a prerequisite text. DOCUMENT has a public flag. APPLICATION points to a program.

## 6. Diagrams added

The team now has 12 diagram files in `design/diagrams/`. The source of each is in `diagrams-source.md`.

1. Architecture, ER and supervisor routing. These three were updated.
2. One sequence diagram of a chat message from LINE to the reply, and one of two students and one slot.
3. Four state diagrams: request, payment check, conversation owner and reservation.
4. A deployment diagram and an access map by role.
5. A use case diagram as a draw.io file, with an SVG and a PNG.

# Scenario review, 15 October 2026

Scope: every chat scenario, J1 to J24, on LINE and Telegram. The role consoles R1 to R7, A1 to A4 and SC1 to SC12 are in scope too. So are the portal pages that the scenarios touch. Wai Yan Lynn asked for a review of correctness, consistency and quality.

## 1. How the review ran

1. A script read all text of every scenario frame. I read the text and compared names, dates, numbers and numbering.
2. A script checked every weekday against its date, and every REQ, BK, ADV, PAY and CONV number for reuse.
3. Three audits ran over all 296 frames: icons that overlap other icons or text, text that a parent frame clips, and linked items under 24 px.
4. I looked at screenshots of the frames that I changed or added. I did not open every frame of the older journeys again.

## 2. Mistakes found and fixed

1. The wrong password frame had two icons on top of each other, the eye and the error mark. I added the eye without opening that frame. The eye now sits left of the error mark, and all three Login frames are checked.
2. J1 offered to request all three documents, but the button led to the transcript flow of J5. The offer now says to start with the official transcript.
3. J3.4 repeated the first answer with a different last sentence than J3.2. Both now use the same text.
4. J6 booked Library Room B2 at 13:00 for Wai Yan Lynn, the same slot as J4. The example now uses two other students, Library Room B4 at 14:00 and the time 12:05.
5. The withdrawal deadline of 30 October was called the end of week 8. With the semester start of 17 August, 30 October is the end of week 11. The text now says week 11.
6. Handbook section 5.4 held the withdrawal deadline in J10 and the load limit in J16. The load limit is now section 5.2.
7. J11 said the Booking agent found three slots, and the card showed two. The trace says two.
8. Advisor slot cards showed a door icon. They now show a user icon.
9. R1.3 said the request was reviewed at 09:05 and approved at 09:12. The queue of R1.1 showed it as submitted at 09:10. The times are now 09:11 and 09:13, and J22 uses the same times.
10. A2.2 showed 182, 171 and 140 requests a day for each key. The free tier allows 50 a day. The values are now 46, 49 and 38.
11. J23.2 said 4 open questions, but A1.3 had already closed one. A1.3 now has the upload at 09:40, and J23.2 says 3 open questions and 2 that still need a document.
12. R2.3 planned Semester 2 as ICT411 and one elective. The plan of J16 has six courses and 21 credits. R2.3 now says so.
13. The slip of Napat R. in R4.1 was sent at 08:58, but the payments queue at 09:30 did not list it. The slip is now from 09:48.
14. J22.4 and R5.1 said ready for 5 days. The request was ready on 16 October, so the text says 4 days.
15. The blocked attempt CONV-2026-0089 had a time after CONV-2026-0097. It now has the time 13:05 of 14 October.
16. J24 had Mali S., a year 2 student, late for ICT411, which is a year 3 and 4 course. Pim T. is late instead.
17. Phone status bars showed 9:41 in many frames. They now show the time of the story.
18. J7.5 and J13 to J24 are consistent with the data in `notes/mock-data-spec.md`.

## 3. Checks that passed

1. No weekday disagrees with its date in any text.
2. Each REQ, BK, ADV and PAY number names one item. The CONV numbers rise with time.
3. No linked item is under 24 px. No text is clipped by a parent frame.
4. One exception is by design. The page content behind the cookie notice and the mega menu is cut at the screen edge.
5. No link is broken and no timed link forms a loop. The prototype has 296 frames and 3,184 links.

## 4. Open points for the team

1. The password shown state uses the same eye icon. A crossed eye icon is not in the library.
2. J6 stays a candidate to cut. It is now consistent with the other journeys.
3. The staff and role frames use invented names and numbers. They are listed in `notes/mock-data-spec.md`.
4. The slip checks in SC8 and R4 need a fixed text reading tool, because the model must not read the image.

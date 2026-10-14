# Figma review: 13 October 2026

This is a harsh review of both Figma files. Claude made no changes in this step. Wai Yan Lynn will add requests, then the fixes follow in one batch.

Scope: all 53 prototype frames at full size, the library foundations and a sample of component pages. Two measured tests ran on the prototype. One tested text contrast on 1,467 text nodes. The other traced every prototype link.

## 1. What passed

1. Every text node in the app frames meets WCAG AA. Only the LINE and Telegram chrome fails, because it copies the brand colors.
2. No unbound fill, stroke, padding, spacing or radius exists outside the phone chrome. The chrome uses raw brand colors on purpose.
3. Every frame has an outgoing link. Every frame without an incoming link is a flow start or a dark preview.
4. All 290 links use one action type (go to frame) and one transition (dissolve, 200 ms). The 14 timed links use 1 to 2.5 seconds.
5. Dark mode renders correctly in all 7 dark frames. No frame has a lost contrast or an unbound color.
6. The icon board shows all 59 icons with correct names and consistent stroke weight.

## 2. Data and story defects (high)

These break the story in front of an examiner. Fix them first.

1. The prototype has two different "today" dates. The journeys happen on Monday 12 October (14:22, 14:31, 14:52). The portal frames say Wednesday 14 October.
2. The Queue ages do not match the audit log. The queue shows 12 min, 1 h, 3 h, 5 h and 1 d. The audit log shows one afternoon, and the booking happened after the request.
3. The request channel contradicts itself. Request detail and SC3 say "Web assistant". The Telegram frames show the update arriving on Telegram. The Profile says Telegram is not linked.
4. In J4.3 the student picks "5 to 8" people. J4.4 then books "6 seats" with no reason. J4.4 also shows the student bubble "Room B2 at 1", which cuts the time.
5. J4.6 shows the chip counts All 4, Upcoming 3, Past 1. The table has 3 rows. The counts must read 3, 2 and 1.
6. Telegram 1 says "is ready". Telegram 2 and J5.5 say "is Ready" with a capital R in the middle of a sentence.
7. The Home card shows "2 November 2026" for the registration news. The Announcements page shows the publish date, 12 October. The two lists use two date meanings.
8. The spelling mixes British and American forms. "Enrolment" and "authorisation" appear next to "organizations". Pick one form and apply it to every frame.
9. SC2 still shows the Escalated pill after the staff member took over. The staff reply also sits on the left, like an incoming message.

## 3. Layout defects (high and medium)

1. Programs: the first card is 146 px tall and the other five are 122 px. The row gap is uneven. Give all six cards one height.
2. J6.3: the step cards are 131, 131, 113 and 147 px tall in row 1, and 131, 131, 113 and 165 px in row 2. The arrows do not line up. Give all cards one height and one baseline.
3. SC1: the Escalated pill is invisible on the pink row, in Light and in Dark. The pill needs its own contrast against the row.
4. J1.2: the typing bubble sits above the "Searching Student Handbook 2026" status line. The typing indicator must be the last item.
5. J1.3 and J1.4: the numbered list, the intro and the question run together inside one bubble. Add paragraph spacing.
6. About 40 percent of each chat frame and about 450 px of the Landing frame are empty. This reads as unfinished.
7. J6.1 and J6.2: the phones show a large empty area under the last message. Reduce the phone height or add the earlier messages.

## 4. UX gaps (medium)

1. J2.3 and J2.4: the composer still says "Ask about rules, records, bookings or requests". While a human handles the case, it must say "Write to Student Services".
2. J3.2 asks "Do you want the payment reference?" with no reply chips. J3.3 has no next step. Every other question has chips.
3. J5.2 asks two questions with two unlabeled chip rows. Ask one question at a time, or label each row.
4. J5.3 uses a clock icon beside "Nothing is submitted until you confirm". The meaning is a notice, so use the info icon.
5. J4.4 repeats the same sentence twice. The bubble says "Please confirm this booking" and the card title says "Confirm this booking".
6. My bookings explains how to cancel but has no Cancel or Change action. Table rows have no arrow that shows they open.
7. Programs cards do not look clickable, but the subtitle tells the student to choose a program.
8. Announcements put the date inside the body text and show no category. The filter chips have nothing to match.
9. Login repeats the Log in button in the top bar. It has no error frame and no show-password control.
10. The Select buttons in the phone frames are 32 px tall. Touch targets on a phone need 44 px.
11. The Staff Console has no Requests list and no Bookings list. This was already known.

## 5. Prototype wiring (medium)

1. The file has 15 flow starting points, not 12. The three dark copies repeat the names Public site, Student portal and Staff console. Rename them with the word Dark.
2. The file has 290 links, not 257. The project notes carry the old count.
3. The source panel in J1.4 and the confirm modal in SC3 are full frames. Present mode swaps the whole frame. An overlay action looks more real.
4. Nobody played the click-through in Present mode. Claude cannot run Present mode. Wai Yan Lynn must do this step.

## 6. Library defects (medium and low)

1. The Patterns page is empty. Delete it or fill it. The Cover does not list it.
2. The Foundations color pages show 35 of 37 Semantic tokens. The tokens destructive-hover and scrim are missing.
3. No page shows the 79 Primitive colors. The ramps are only visible in the variables panel.
4. The Typography page shows 7 of 11 text styles. The styles label/12, label/14, label/16 and overline/12 are missing.
5. The Phone Frame page has no Light and Dark review frames. Every other component page has them.
6. The Input Error variant shows the helper text in red. An error variant needs an error message.
7. The phone chrome placeholders ("Aa", "Message") and the white text on LINE green score 2.3 to 2.6 to 1. This copies the real apps. The note belongs in the Changelog.

## 7. Invented content for Wai Yan Lynn to review

The list in `notes/session-handoff.md`, section 6, still applies. The new finding is that the room "6 seats" and the fee text need one source of truth.

## 8. Suggested fix order

1. Pick one master timeline and one channel story. Apply them to every frame (section 2, items 1 to 3).
2. Fix the counts, the copy and the spelling (section 2, items 4 to 8).
3. Fix the layout defects (section 3).
4. Add the missing states and actions (section 4).
5. Fix the wiring names and the library documentation (sections 5 and 6).
6. Run the test scripts again, take new screenshots and update CLAUDE.md section 15.

## 9. Status after the fixes of 13 October 2026

Fixed and seen in a screenshot:

1. All data and story defects in section 2, except the staff reply side in SC2. The master timeline is in `notes/session-handoff.md`.
2. The layout defects 1 to 5 in section 3. The Programs cards, the J6.3 steps, the Escalated row, the typing order and the bubble paragraphs.
3. The UX gaps 1 to 5 and 9 in section 4. The composer text, the answer copy, the chip labels, the info icon, the repeated sentence and the duplicate Log in button.
4. The wiring in section 5. The file has 19 flow starting points with unique names and 1,146 links. No link is broken.
5. The library defects 1 to 6 in section 6.

Still open:

1. Present mode has not been played. Claude cannot do this step.
2. My bookings has no Cancel or Change action. Table rows have no arrow.
3. Login has no error frame and no show-password control.
4. The Select buttons in the phone frames are 32 px tall.
5. The source panel in J1.4 and the confirm modals are full frames, not overlays.
6. The staff reply in SC2 still sits on the left.
7. Chat frames still show empty space below the last message.
8. The Dark mode previews have no incoming links. They are static previews.

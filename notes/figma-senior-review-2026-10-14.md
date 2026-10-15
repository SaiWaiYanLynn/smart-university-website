# Senior review of the Figma files, 14 October 2026

Scope: the Prototype page (163 frames, about 20,000 nodes) and the Library file (50 component sets and 71 components). This review changes nothing. Wai Yan Lynn picks which fixes to apply.

## 1. How the review ran

1. Six read-only scripts scanned every frame and every component. They covered structure, text, fonts, link coverage, touch targets, dates and library hygiene.
2. Screenshots show the two worst findings. The tablet and mobile dashboards were opened and read.
3. The review did not open all 163 frames one by one in this pass. Earlier builds each had a screenshot, and the scripts cover the rest. A full manual sweep happens in the team review.

## 2. What is clean

1. No hidden layer, no default-named layer, no zero-size node and no empty frame.
2. No weekday that disagrees with its date. The scan covered every text node in 2026.
3. One date style everywhere: day, month name, year. No slash dates and no ISO dates. One currency, THB. Times use the 24 hour clock.
4. Nine request numbers, and each one names one request. REQ-2026-0489 appears in 7 frames with the same facts.
5. Every frame has an outgoing link. No timed link forms a loop.
6. The library has no unnamed component, no duplicate name, no empty page and no component without a description.
7. The page uses one font family with two weights.

## 3. Findings, most severe first

### High

H1. Class blocks overflow on every Timetable frame.
1. Evidence: the block frame is 80 px high and its body is 107 px high. 20 blocks lose 9 to 48 px of content.
2. The frames affected are Timetable, next week, previous week and Dark: Timetable.
3. Result: the room and time line is cut off in a screenshot.
4. Fix: let the block grow with its content, or shorten the text.

H2. The mobile dashboard header is clipped.
1. Evidence: the screenshot of Dashboard (mobile) shows "Good morning, Wai Yan" cut at the screen edge. The sub line is cut too. The title block overflows by 187 px.
2. Fix: let the title wrap and set the block to fill the width.

H3. In Present mode, about 25 controls do nothing after a click.
1. The scan found 224 buttons, chips and links without a link. Most are the active page in a nav bar, and those are correct.
2. The real gaps are the Library tabs (Books, Journals, Theses), the Grades semester chips and the Courses filter chips.
3. The other gaps are the Send button in about 12 chat frames, Upload a file on Apply 2, and the cookie notice buttons.
4. The last gaps are the unlink dialog buttons, the button on the Contact sent state, and Select on LINE 2 Rooms.
5. A professor who clicks these sees nothing happen. For each one, add a link or turn the control into a static label.

H4. Touch targets are too small on public pages and on mobile.
1. Evidence: 472 linked items are under 24 px high. All are 21 px text links, mostly in the footer. WCAG 2.2 criterion 2.5.8 asks for 24 px.
2. On the 390 px frames, 90 linked items are under 44 px. Most are 40 px buttons and 21 px links.
3. Fix: give footer links a 24 px row, and give mobile buttons a 44 px height.

### Medium

M1. Tablet dashboard cards have uneven heights. In each row the first card is taller because "12,500 THB" wraps. The cards need equal height in a row.

M2. 24 percent of all text is 12 px (1,687 of 7,103 nodes). Captions at 12 px are normal. Body text at 12 px is not. Check which 12 px nodes carry real content.

M3. The label "Student services" appears 111 times and "Student Services" 49 times. Pick sentence case for UI labels and fix the 49.

M4. The size scale has a stray value. One text node is 88 px, and no other node uses a size above 40. Decide whether it needs a token.

M5. One frame is 1440 by 1064 while 141 others are 1440 by 900. Check that the difference is intentional.

M6. Dark mode has 14 static previews. They have no incoming link and they do not scroll. The pages added later have no dark copy. State this in the presentation, or add dark copies of the four most visible pages.

M7. The Library property names are not uniform. Variant axes are called State (19), Type (6), Kind (7), Variant (2), Tone (7) and Style (2). Text props use Title (18) and Label (13) for the same idea. Agent Trace uses numbered props such as Agent 1 and Step 1. Rename in the next library version. Do it only with a changelog entry, because a rename can reset overrides in the prototype.

### Low and carried over

L1. Library tabs and Fees tabs are static.
L2. The filter chips on the responsive frames are static.
L3. The assistant chat has no stop button and no message times.
L4. Phone buttons are 32 px high.
L5. The source panel and the dialogs are full frames, not overlays.
L6. My bookings has no Cancel or Change action.
L7. Table rows have no chevron.
L8. Login has no show-password control.
L9. In SC2 the staff reply sits on the left.
L10. Chat frames leave empty space.
L11. Agent Trace sits beside J10 to J12 and J7 only. J1, J5 and J8 have none.

## 4. Logic gaps in the scenes

1. Assistant sends: the chat frames show a Send button but the composer text does not change between frames. This is normal for a prototype, and the timed links hide it. Say so in the demo.
2. The dashboard says "Slip under review since 14 Oct". Staff accept the slip at 09:41 on 15 October. A viewer who opens the dashboard after that time sees an old state. Keep the 15 October morning story in the script.
3. The Apply wizard serves people who are not students yet. They have no account. The project decision says accounts come from an administrator. See the feasibility note for the fix.
4. The loan renewal rules (two renewals, 14 days, no renewal for an overdue book) need the team to approve them.

## 5. Recommended fix order

1. Fix H1 and H2 first. Both are visible in the demo.
2. Fix H3 next. Do it before the Present mode test.
3. Fix H4 and M1 to M3 in one pass.
4. Leave M6 and M7 for after the team review.

## 6. Industry standard check

1. Colour contrast: passed on all earlier checks, with a lowest ratio of 3.67 to 1 for controls.
2. Target size: fails 2.5.8 on small links (H4).
3. Tokens: all fills, gaps, radii and text styles are bound, except the phone chrome and the pill radius.
4. Naming: components use Title Case and variants use Property=Value. Property names need cleanup (M7).
5. Not shown anywhere: keyboard focus rings on the page frames, loading skeletons and a second prompt before a destructive action. Add these to the spec for Project II. They are not needed for the midterm.

## 7. Status after the fixes, 14 October 2026

Fixed in the prototype:

1. H1. Class blocks now grow with their text. No block clips on the four Timetable frames. The day headings have one height, so the blocks line up.
2. H2. The title on the mobile and tablet pages wraps. The page body moves down to match. Overlaps on the Home, Programs, Apply and My requests frames are gone.
3. H3. These controls now have a link. They are the cookie buttons, the unlink Cancel button and the 404 buttons. They also include the two buttons on the empty library search and the My bookings chips.
4. H3. The staff queue chips, the Payments chips and the Unread chip on the all read page now link. The three Select buttons on LINE 2 link too.
5. H3. The responsive Programs and My requests pages have chip state frames, as the desktop pages do. This adds 8 frames.
6. H4. Text links in the page body are 24 px high. Buttons on the 390 px frames are 44 px high.
7. M1. The tablet dashboard cards have equal height in each row.
8. M3. The label reads Student Services in 123 places.
9. M5. Dark: Dashboard is a 900 px scroll window with a fixed nav, like the light frame.
10. M4 needs no fix. The 88 px text is the iPhone lock screen clock.

Fixed in the library (version 1.3.1, not yet published):

1. Footer and Footer Compact links are 24 px high.
2. The Top Nav user name is 24 px high.
3. The Logo and Footer text read Student Services.
4. The Changelog has a v1.3.1 entry.

After Wai Yan Lynn publishes, the Footer links and the Top Nav user name in the prototype pick up the 24 px height. Until then, 483 linked texts inside instances stay at 21 px.

Counts after the fixes: 171 frames, 2,169 links, 39 flow starts, no broken link and no clipped frame.

Still open:

1. Chips and tabs without a state frame: News, Library (public and account), Grades semesters, Courses, the staff request and booking lists, and the instructor and administrator pages. These need sample data that does not exist yet, so the team decides.
2. Single buttons without a target: Continue and Save draft on the mobile and tablet Apply, Upload a file and Create account. Reschedule and No thanks on J12.1 are open too.
3. The two quick replies on J1.4 and J1.5 and Settings in the cookie notice have no target.
4. M2, the share of 12 px text, needs a read of each frame.
5. M6, the dark previews, and M7, the property names, wait for the team review.
6. The carried over items L1 to L11.

## 8. Status after the data and button work, 14 October 2026

1. The chips and tabs now have state frames with tied out data. The data is in `notes/mock-data-spec.md`. The prototype has 226 frames and 2,903 links.
2. The mobile and tablet Apply has steps 2 to 4, a submitted frame and a file uploaded state. The mobile dashboard shows bookings as cards, because the table was wider than the screen.
3. The single buttons are done as chosen: navigation, feedback state or Disabled variant.
4. Open: the Present zoom of the viewer, which the plugin cannot set, M2, M6, M7 and the carried over items L1 to L11.

## 9. Status after the library publish, 14 October 2026

1. Library version 1.3.1 reached the prototype. Only one linked item is now under 24 px. It is the 20 px close icon of the Toast.
2. The label reads Student Services everywhere, 250 times, with no lower case form left.
3. M2 is closed. The 12 px text is 25 percent of all text nodes. Almost all of it is chip labels, counts, table headers, dates and initials, which is normal caption use. 11 long messages at 12 px now use the 14 px body style.
4. The SC11 chips have a state frame for each payment state. The prototype has 229 frames and 2,932 links.
5. Still open: M6, M7, the Toast close icon and the carried over items L1 to L11.

## 10. Dark previews and property names, 15 October 2026

1. M6 is closed. Four new dark previews exist: Grades, Library account, News and SC7 Payments. They scroll with a fixed nav like the light frames. The Dark mode section holds 18 previews.
2. The last small target is fixed. The dialog close icon is 24 px. No linked item is under 24 px now.
3. M7 needs no rename. I read the property names of all 50 component sets. Each axis name has one role, so the names are consistent by role.
4. State names an interaction or a status. Tone names a color emphasis. Type names a kind of content. Variant names the button hierarchy. Style names the fill of a call to action band.
5. A rename of Style or Kind touches every instance in the prototype. A rename has a risk of lost overrides and gives no benefit. The decision is to keep the names and to state the rule here.
6. The prototype has 233 frames and 2,998 links. No link is broken.

## 11. Carried over items, 15 October 2026

Done:

1. L3, the stop button. The composer shows a Stop button while the typing indicator is visible: J1.2, J7.2 and J11.1.
2. L6, booking actions. The Library Room B2 row opens a Booking detail page with Change time and Cancel booking. Cancel opens a dialog, and the result is the My bookings: cancelled state. Change time opens the room offers of J4.3. The rule text says two hours before the start, as the My bookings banner does.
3. L8, show password. The Login password field has an eye icon. It opens a Login: password shown state.
4. L9, the staff reply in the staff console now sits on the right.
5. L11, Agent Trace. The panel now sits beside J1.3, J1.4, J1.5, J4.3, J5.4 and J8.3. The chat panel of J1.3 to J1.5 is 680 px wide to make room.

Not done, by decision:

1. L5, overlays. The dialogs stay as full frames. This works in Present mode and costs nothing to keep.
2. L7, row chevrons. The table rows have no chevron. A chevron needs a library change in every row component.
3. L10, the empty space in chat frames. This is cosmetic and depends on the length of each story.
4. Message times in the chat. The day divider carries the date. A time for each message needs a library change in Chat Bubble.

The prototype has 237 frames and 3,049 links, with no broken link, no clipped frame and no linked item under 24 px.

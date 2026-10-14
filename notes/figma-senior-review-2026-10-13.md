# Senior review of the Figma work: 13 October 2026

This review is written as a senior designer with ten years of practice reads the files. It is strict on purpose. Every finding has a number, so the fixes can point back to it.

Scope: the library file (52 sets and components, 381 component variables) and the prototype file (94 frames, 1,146 links). Evidence comes from screenshots and from read-only scripts that ran on all frames.

## 1. Verdict

The foundation is strong. Every color, text style, gap and padding is bound to a token. Text contrast passed on 3,776 text nodes. Each frame has at most one lime element. The timeline is consistent and no link is broken.

The work is not yet at a standard that a senior reviewer signs off. Four reasons:

1. It shows only the happy path. No error, empty or loading state exists.
2. Every frame is 1440 px wide. A student portal that never shows a phone layout is a gap.
3. About 40 percent of the buttons have no link.
4. The system repeats hand-built patterns. The same stat block exists 43 times as loose layers, not as a component.

## 2. Critical findings

C1. Dead controls. 27 of 67 buttons have no link. Examples: Continue and Save draft on Apply, and Send message on Contact. More examples: Previous week on Timetable, Renew on Library account and Close on the J1.4 source panel. In Present mode a click does nothing, and the audience sees it.

C2. No responsive layouts. All 94 frames are 1440 px wide. The public site and the portal will run on phones. LINE and Telegram frames show chat on a phone, but not the web pages.

C3. No failure states. The project names the free-tier rate limit as its main technical risk (R1), yet no frame shows "the assistant is busy". Also missing: login failure, search with no results, a 404 page, an empty notification list and a failed upload.

C4. The payment process is not usable without the transfer details. The Fees page says "transfer the amount to the University account". It shows no account name, no account number and no payment reference. A student cannot pay from this frame.

C5. Content that contradicts itself.
1. The Faculties page counts 3, 1, 2 and 3 programs, and one program is counted twice. The Programs page lists 9.
2. The Academic calendar shows the Semester 1 tab, but three of the six items belong to Semester 2.
3. Student 67111336 in J3 is the ID of a real team member. Use an invented ID.

## 3. Major findings

M1. Design system debt. These patterns exist as loose layers and not as components: Stat (43 copies), Icon Tile (39), Check item (16), Bullet item (13), Key-value row (8) and about 30 hand-built cards. A change to one of them needs dozens of edits. This is the opposite of the "systematic" goal.

M2. The component token layer is probably too heavy. 381 Component variables mostly alias one Semantic variable one to one. This doubles the work for every change and gives no theming benefit. A senior reviewer keeps a component token only for a component that differs from the semantic rule.

M3. Foundations are incomplete. Missing: motion (duration and easing), breakpoints, icon sizes, minimum target size, elevation scale beyond two shadows and layout grids. The spacing scale lacks 2, 20, 40 and 80. During the build, scripts had to round those values.

M4. Small text. 12 px text is about one quarter of all text nodes (1,031 of 3,940). Table headers and captions can use 12 px. Book locations, stat notes and form helper text carry real information and need 14 px.

M5. Touch targets. The bell icon is 20 by 20 px. WCAG 2.2 sets 24 px as the minimum and 44 px as the comfortable size. Page buttons and the phone buttons are 32 px tall.

M6. Prototype mechanics.
1. 30 frames are taller than the screen and the top bar does not stay in place.
2. The mega menu opens on hover but has no way back except the scrim.
3. The source panel and the dialogs are full frames, not overlays.
4. Chips and tabs never change state, because no interactive variant exists.

M7. Search goes to the wrong place. The Search button opens Programs. A search needs a results page that groups programs, news and rules, and offers the assistant.

M8. The assistant interface lacks features that a grounded AI answer needs.
1. No way to mark an answer as helpful or wrong.
2. No conversation history and no "new conversation".
3. No message time.
4. No "stop" control while the assistant works.

M9. The staff console is shallow.
1. The reject dialog has no reason field.
2. Tables have no search, no sort indicator and no bulk action.
3. The audit log cannot filter by date or actor.
4. The architecture has four roles. Only one role has views.

M10. The public site misses common parts. No Apply button in the header. No Privacy and Accessibility links. No language switch, although the system supports English and Thai. No cookie notice.

M11. Date formats. The text uses six formats. Examples: 15 October 2026, 15 Oct 2026, Thu 15 Oct 2026, Thursday 15 October, 15 Oct and 15 October. A style rule is missing.

M12. Naming. "Student services" appears 45 times and "Student Services" 32 times. The department name must use one form.

M13. Type roles. The style heading/40 is used for page titles and for big numbers. The style heading/32 is used for section titles and for portal page titles. Money columns do not use tabular figures, so digits do not align.

## 4. Minor findings

N1. Frame heights vary. 50 frames use 900 px but 17 frames have other heights between 558 and 1,000 px with no rule.

N2. Chat frames leave about 40 percent of the panel empty below the last message.

N3. No frame shows a keyboard focus state in a real screen. The components have a Focus variant, but no frame uses it.

N4. The public hero has no image or illustration. Without pictures the site reads as a document. Real photography is out of reach, so a branded illustration system is the alternative.

N5. The Dark mode previews cover 14 frames. The staff pages and several public pages have no dark copy.

N6. Layer names repeat, for example "row" and "Status Pill" against "status".

N7. The design system page lists components but gives no usage rules.

N8. No dev handoff notes. There are no annotations for behavior, no Code Connect mapping and no spec of the states per component.

N9. The Figma files use no branches. A review of this size is safer on a branch.

N10. CLAUDE.md is over 400 lines and mixes decisions with build lessons. A new member needs a short README first.

## 5. What is good

1. 100 percent token binding outside the phone chrome and the pill shape.
2. Contrast passes on all 3,776 checked text nodes, in Light and Dark.
3. One lime element per frame on all 94 frames.
4. A single master timeline and one channel story across 94 frames.
5. The link graph has no broken link and no frame without an outgoing link.
6. Every review frame shows Light and Dark, and every component has a description.

## 6. Decisions that belong to Wai Yan Lynn

D1. Responsive layouts: mobile 390 px and tablet 768 px for the public site, the portal and the chat. Large work.
D2. Thai interface: show the Thai language for the key frames. The project says English and Thai in the system, and the mockups are English only.
D3. Conversation history and "new conversation" in the chat page. This changes the page layout.
D4. Views for other roles: instructor, Registrar and administrator.
D5. Interactive components: chips, tabs and accordions that change state in Present mode. This needs variant links inside the library.
D6. Scrolling prototype: frames with a fixed 900 px height and a top bar that stays. This loses the full-page view on the canvas.
D7. Trim the component token layer to the tokens that differ from the Semantic layer.
D8. A branded illustration system for hero and card art.

## 7. Fix plan

The fixes follow in `notes/session-handoff.md`, section 10. Each fix names the finding number. Items in section 6 wait for a reply.

## 8. Status on 14 October 2026

Fixed and checked in screenshots or by script:

1. C1 dead controls. About 45 buttons now link. The Apply wizard, Contact, Library renew, Notifications, Timetable weeks, Profile unlink, J1.3 feedback, cookie notice, Login error, Search results, J9.1 and J4 buttons work. The composer Send buttons stay static. The Library tabs, Grades tabs and the staff chips stay static.
2. C2 responsive layouts. Mobile 390 px and tablet 768 px frames exist for Home, Programs, Apply, Dashboard, My requests and the assistant answer. A menu frame exists for the public site and the portal.
3. C3, C4 and C5 were fixed on 13 October.
4. M1 design system debt. 101 loose layers became Stat, Icon Tile, List Item and Key Value Row instances. Three key-value layers on the Research page remain loose.
5. M3 foundations. Motion, Size and the spacing steps 40, 80 and 96 exist. Breakpoints are the two frame sizes.
6. M6 prototype mechanics. Every page frame is a scrolling window of 900 px with a fixed top bar. Filter chips switch state on My bookings, My requests and Programs. The Admissions FAQ opens and closes. The source panel and the dialogs are still full frames.
7. M7 search. The Search button opens a results page.
8. D4 views for other roles. Instructor, registrar staff and administrator scenarios exist (R1, R2, A1 and A2).
9. D8 illustrations. Eight scenes exist in the library. They sit in the 404 page, two empty states and every Program Card.

Open:

1. M8 conversation history, New conversation, message time and a stop control (decision D3 is yes, still to build).
2. M2 trim of the Component tokens (decision D7, skipped on purpose).
3. N5 dark previews for the new pages. The dark previews do not scroll.
4. M5 the phone buttons are 32 px tall.
5. Library and Fees tabs, and the filter chips on the responsive frames, are static.
6. Wai Yan Lynn has not played Present mode.

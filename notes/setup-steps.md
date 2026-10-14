# Setup steps: git, Figma file, tokens, grey components

Status on 13 October 2026: only part 1 is still open. Claude finished parts 2 to 4 in a different structure. Read `notes/session-handoff.md` for the current state.

Do the parts in order. Part 3 and part 4 do not need the color choice.

## Part 1. Start git (5 minutes)

1. Open Terminal.
2. Go to the project folder: `cd "/Users/razn1htux/Desktop/Smart University Website - Group S"`
3. Start the repository: `git init -b main`
4. Create a file named `.gitignore` that contains one line: `.DS_Store`
5. Add all files: `git add .`
6. Save the first commit: `git commit -m "Add project context, research, diagrams and midterm plan"`
7. Run `git log --oneline`. Make sure that one commit appears.
8. Run `git status`. Make sure that the message says the working tree is clean.

From now on, commit at the end of each work day. Write the message in plain words, for example "Add design tokens".

## Part 2. Create the Figma file (10 minutes)

1. Open Figma and switch to the team Krirk UIUX. Do not use your personal team, because it gives a View seat only.
2. Open the folder with id 668778480.
3. Click New design file.
4. Rename the file to `Thales University Prototype`.
5. Create one file only. Prototype links cannot cross files.
6. Add one page for each frame group. Use the names Cover and Design System first.
7. Add the pages Public and Auth, then Student Portal.
8. Add one page for each journey: J1 Policy, J2 Handoff, J3 Records, J4 Booking, J5 Request and J6 Conflict.
9. Add the last two pages: Channels and Staff Console.
10. On the Cover page, add a frame with the text "Thales University" and the line "Student services".

## Part 3. Add the tokens that need no color (30 minutes)

A variable is a named value that you reuse. All steps are on the Design System page.

1. Open the Local variables panel.
2. Create a collection named `Spacing`. Add number variables with the values 4, 8, 12, 16, 24, 32, 48 and 64.
3. Create a collection named `Radius`. Add `sm` = 4, `base` = 8 and `lg` = 12.
4. If Inter is missing, install it. It is free on Google Fonts.
5. Create text styles in Inter with these sizes: 12, 14, 16, 20, 24, 32 and 40.
6. Set the line height to 150 percent for the body sizes (12, 14 and 16).
7. Set the line height to 120 percent for the heading sizes (20 and above).
8. Create two effect styles for shadows. Name them `shadow-sm` and `shadow-md`. Do not add a third.
9. Name each style by its job, for example `body/14` and `heading/24`.

## Part 4. Build the four main components in grey (2 to 3 hours)

Use grey only for now. When you choose the color, you change the fills and every component updates. Use auto layout for every component.

1. Chat bubble. Make three variants: user, agent and system. Use the radius `base` and the spacing 12 and 16.
2. Citation card. Add a title line (rule name and section), a one-line quote, and a thin bar on the left side.
3. Slot chip. Make three variants: default, hover and selected. The text is a time, for example "Tue 11:00".
4. Status timeline. Make four steps: Submitted, In review, Ready and Done. Make three variants: past, current and future.
5. For each component, create a component set and name each variant by its state.
6. Put all four on the Design System page under a heading named "Core components".

## Part 5. Report back

When parts 1 to 4 are done, send the Figma link and the color number you chose. Then the tokens for color get locked and the rest of the components follow.

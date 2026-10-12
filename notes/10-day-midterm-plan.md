# Project I Midterm — 10-Day Plan (Figma Prototype, Slides, Proposal)

## Context

Group S presents the IT Project I midterm in 10 days (D1 = 10 Oct 2026). The professor confirmed on LINE that **no code is required** for the midterm: "Only prototype to explain the entire project workflow... Clickable design, figures, full architecture flow, it could be anything, but the workflow must present what you will develop and how."

He did **not** answer whether the 7-deliverable slide (working prototype, version control, testing results) is the midterm bar or the end-of-Project-I bar. Treat it as end of Project I. The code is deferred, not cancelled.

The deliverable is therefore three things: a high-fidelity clickable Figma prototype, the 17-section Project Proposal document, and a 40-minute presentation. The thing being graded is whether the workflow is legible, not whether the pixels are pretty — but we are going high fidelity anyway, so the screens must still earn it.

Project: **Smart University Website**, an agentic student services portal. Narrowed scope from the submitted feasibility v2: one student supervisor routing to four agents (Knowledge, Records, Booking, Request), Booking covering advisor appointments and study rooms only.

## Confirmed decisions

| Decision | Choice |
|---|---|
| Fidelity | High-fidelity polished |
| Design foundation | Build from scratch, following Radix + shadcn conventions |
| Chat journeys | All six |
| Language in UI | English only |
| Figma owner | Sai, alone |
| Slides + documentation | Sai |
| Diagrams | Other three, Mermaid from Sai → refined in draw.io |
| Flow diagram | Supervisor routing and tool selection (one only) |
| Code during these 10 days | None |
| Daily capacity | 5+ hours |

**Open item, needed on D1:** the fictional university name. Everything (wordmark, frames, slides, proposal) depends on it. Pick it before touching the design system.

## Load check

~46 frames + design system + slides + 17-section proposal, one person, 10 days at 5h = ~50 hours. It fits with no slack. The cut list below exists so that falling behind on D6 is a decision, not a panic.

---

## Design system spec

Build these yourself; follow the structure, do not copy a kit.

**Colour.** One brand hue → a 12-step Radix-style scale. One neutral grey scale. Semantic tokens only in components: `background`, `surface`, `border`, `foreground`, `muted-foreground`, `primary`, `primary-foreground`, `success`, `warning`, `destructive`. Every text pairing must pass WCAG AA.

**Spacing.** 8pt grid. Scale: 4, 8, 12, 16, 24, 32, 48, 64.

**Radius.** `sm` 4, `base` 8, `lg` 12. One decision, applied everywhere.

**Type.** Inter (free). Scale 12 / 14 / 16 / 20 / 24 / 32 / 40. Body line-height 1.5, headings 1.2.

**Elevation.** Two shadows only. Resist a third.

**Components to build (D2).** Button (primary / secondary / ghost × default / hover / disabled), input, select, card, status pill, top nav, side nav, table row, **chat bubble (user / agent / system)**, **citation card**, **slot chip**, **status timeline**, avatar, toast, modal, and phone frames for LINE and Telegram.

The four in bold are the distinctive ones. They carry the whole prototype — build them properly.

## Frame inventory (~46)

| Group | Frames | Contents |
|---|---|---|
| Public + auth | 5 | Home, programs, announcements, login, post-login landing |
| Student portal | 5 | Dashboard, my requests, request detail with status timeline, my bookings, profile with linked channels |
| J1 Policy question + citation | 4 | Ask → thinking → answer with citation card → source expanded |
| J2 Out-of-corpus refusal + handoff | 4 | Ask → refuse → offer human → staff joins |
| J3 Own records + cross-student refusal | 4 | Ask own balance → answer → ask another student → refused |
| J4 Book a study room | 6 | Ask → slots offered → pick → confirm → confirmed → appears in My Bookings |
| J5 Submit + track a request | 5 | Request transcript → fields collected → submitted → status later → ready |
| J6 Booking conflict | 3 | Two users pick the same slot → one confirmed, one told it is gone |
| Channel frames | 6 | LINE ×3 (same booking conversation), Telegram ×3 (status notification arriving) |
| Staff console | 4 | Queue, conversation takeover, request state change, audit log |

## Diagrams (other three, Mermaid → draw.io)

1. **Architecture diagram** — counted separately by the professor (slide 39, step 1).
2. **Use case diagram** — actors student, staff, advisor, administrator.
3. **ER diagram** — core tables: user, student_record, resource, slot, reservation, request, request_event, conversation, message, audit_log.
4. **Supervisor routing and tool selection flow** — classify → route to one of four agents → select tool → validate arguments → retry once → escalate on second failure.

Sai supplies the Mermaid source for all four on D1 so the other three are never blocked.

---

## Day by day

**D1 (today).** Name the university. Pick the brand hue. Create the Figma file with one page per frame group. Write the six journey scripts as exact message-by-message text. Send the four Mermaid diagrams to the diagram team. Begin colour, type and spacing tokens.

**D2.** Design system day. All components above, with variants and states. Nothing else. If this slips, every later frame drifts.

**D3.** Public site (5) + portal dashboard. Start the daily documentation block (see below).

**D4.** Portal remaining: my requests, request detail with timeline, my bookings, profile.

**D5.** Journeys 1, 2 and 3 — 12 frames. These are fast once the chat bubble and citation card exist.

**D6.** Journeys 4 and 6 — 9 frames. Booking plus the conflict.

**D7.** Journey 5 (5) + channel frames (6).

**D8.** Staff console (4). Wire the entire prototype with prototype links. Full click-through hunting for dead ends.

**D9.** Slides built from the frames. Documentation finished. Rehearsal 1 with a timer.

**D10.** Polish only. Rehearsal 2. Export a PDF of all frames and a screen recording of the click-through as a backup.

**Documentation block.** 45–60 minutes every day from D3. Sections 1–9 and 15–17 of the proposal already exist in the submitted feasibility v2 and the research report and only need assembly. Genuinely new: 10 architecture, 11 system models, 12 stack rationale, 13 methodology, 14 timeline. Do not leave this to D9.

## Cut list (drop from the top if behind)

1. J6 booking conflict — explain it verbally over the J4 frames instead
2. Profile / linked channels frame
3. Telegram frames — keep LINE only
4. Staff console audit log frame
5. Public site down to 2 frames (home, login)
6. J3 records + access refusal

Do not cut: the design system, J1, J4, J5, the architecture diagram, or the rehearsals.

## Presentation (40 minutes)

| Minutes | Segment | Owner |
|---|---|---|
| 4 | Problem, led by the 17-university survey | Diagram/doc member |
| 4 | Objectives, requirements, scope | Member |
| 8 | Architecture and the three models | Member |
| 12 | **Figma click-through of the six journeys** | Sai |
| 5 | How we will build it, stack rationale, methodology | Member |
| 3 | Project II continuation plan | Sai |
| 4 | Questions | All |

The click-through replaces what would have been a live demo. Narrate the workflow, not the visuals: at each step say what the system is doing underneath, because that is the professor's stated criterion.

## Verification

- Click-through runs start to finish with **zero dead ends**, tested by someone who did not build it.
- Every one of the six journeys is reachable from the portal dashboard.
- Rehearsal 2 finishes **under 36 minutes** so questions fit.
- Backup PDF export and screen recording both exist on D10.
- Proposal contains all 17 sections, and sections 10–14 describe what the prototype actually shows.
- Every claim in the presentation traces to either a frame, a diagram, or a number from the research report.

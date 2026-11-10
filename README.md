# Smart University Website

Thales University is a React frontend built with Vite and Tailwind CSS. The frontend implements the public university website, student portal, staff console, assistant chat, room booking, payment slip, transcript request, library, and record-access demo flows.

The project is a coursework project for IT Project I and II (BC362916 and BC362914) at Krirk University. The university in the documentation is fictional and is called Thales University.

## What the system does

- Answers from university rules and cites the source section.
- Completes requests through assistant workflows.
- Supports student and staff portal experiences.
- Provides public pages, student services, and staff review screens.
- Uses role-based demo routing in the frontend.

The full research and design documentation is in [`docs/`](./docs/), and the prototype journey content is in [`design/journey-scripts.md`](./design/journey-scripts.md).
All frontend code is inside [`frontend/`](./frontend/). The project documentation and design references are in [`design/`](./design/) and [`docs/`](./docs/).

## Start the frontend

From the repository root:

```bash
cd frontend
npm install
npm run dev
```

Open the URL shown by Vite, usually <http://localhost:5173>.

If dependencies have already been installed:

```bash
cd frontend
npm run dev
```

Stop the development server with `Ctrl + C`.

## Build and preview

```bash
cd frontend
npm run build
npm run preview
```

## How to use the website

The public website opens first. Its header includes:

- **Programmes** — programme information page
- **Admissions** — application information page
- **About** — university information page
- **Sign in** — opens the role-based login page
- **Student portal** — opens the login page when no account is signed in

### Demo login accounts

This is currently frontend-only demo authentication. No real password is required.

1. Click **Sign in** on any public page.
2. Enter an email address.
3. Click **Sign in**.

Student example:

```text
student@thales.edu
```

Any valid email address that does not contain a staff keyword opens the **Student portal**.

Staff examples:

```text
staff@thales.edu
admin@thales.edu
registrar@thales.edu
finance@thales.edu
```

Emails containing `staff`, `admin`, `registrar`, or `finance` open the **Staff console**.

### Student portal

The student portal includes:
- Overview dashboard
- Assistant chat
- Payment slip submission
- Transcript request
- Study room booking
- Library catalogue and loan renewal
- Own-record access protection

### Staff console

The staff console includes:
- Queue
- Requests
- Payments
- Audit log

## Architecture and planned backend

The planned backend stack is Python 3.12, FastAPI, LangChain, LangGraph, PostgreSQL with pgvector, Keycloak, Chatwoot, and Docker Compose. The frontend currently uses local React state for demonstration; backend and Keycloak integration are future work.

## Useful files

- [`frontend/src/App.jsx`](./frontend/src/App.jsx) — React pages, navigation, demo state, and workflows
- [`frontend/src/styles.css`](./frontend/src/styles.css) — Tailwind theme colors and global styles
- [`frontend/package.json`](./frontend/package.json) — frontend scripts and dependencies
- [`design/diagrams/`](./design/diagrams/) — architecture and system diagrams
- [`docs/`](./docs/) — project reports and documentation
- [`design/journey-scripts.md`](./design/journey-scripts.md) — prototype journey content

The login routing is only a frontend demonstration. Production authentication should be connected to Keycloak and the backend described in the project documentation.

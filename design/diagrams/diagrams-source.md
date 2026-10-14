# Smart University Website: Diagram Source

For the three members building diagrams. Workflow for each one:

1. Paste the code block into `mermaid.live`.
2. Export as SVG.
3. Open the SVG in draw.io and restyle it to match the prototype palette.
4. Export a PNG at 2x for the slides.

Diagram 2 has no Mermaid code, because Mermaid does not support use case diagrams. Build that one directly in draw.io with the UML shape library.

---

## 1. Architecture diagram

```mermaid
flowchart TB
  subgraph Users["People"]
    STU["Student"]
    STF["Staff, instructors<br/>and administrators"]
  end

  subgraph Frontend["React application, Vite"]
    PUB["Public site"]
    POR["Student portal"]
    CON["Staff console<br/>queue, payments,<br/>documents, accounts"]
  end

  CWT["Chatwoot<br/>web widget, LINE, Telegram,<br/>human handoff, image attachments"]

  subgraph API["FastAPI application"]
    REST["REST API layer<br/>verifies the access token"]
    SUP["Student supervisor<br/>LangGraph router"]
    MEM["Memory<br/>checkpointer and store,<br/>keyed by student ID"]
    SCH["Scheduler<br/>reminders and timers"]
    subgraph AG["Specialist agents"]
      K["Knowledge"]
      R["Records<br/>catalogue search and loan list"]
      B["Booking"]
      Q["Request<br/>payment checks and loan renewals"]
    end
    VAL["Tool argument validator"]
    TOOL["Tool layer<br/>subject comes from the token"]
    AUD["Audit writer"]
    ING["Ingestion worker<br/>reads uploaded documents"]
    LLM["Model adapter<br/>key pool, falls back<br/>on rate limit"]
  end

  PG[("PostgreSQL<br/>with pgvector")]
  FS[("File storage<br/>payment slip images,<br/>private volume")]
  KC["Keycloak<br/>OIDC identity"]
  OR["OpenRouter<br/>hosted model API<br/>free tier, one key per member"]

  STU --> PUB
  STU --> POR
  STU --> CWT
  STF --> CON
  STF --> CWT

  POR --> REST
  CON --> REST
  CWT -- webhook --> REST

  REST --> SUP
  REST -. verify token .-> KC
  REST --> ING

  SUP --> MEM
  MEM --> PG
  SCH --> B

  SUP --> K
  SUP --> R
  SUP --> B
  SUP --> Q

  K --> VAL
  R --> VAL
  B --> VAL
  Q --> VAL

  VAL --> TOOL
  TOOL --> PG
  TOOL --> FS
  TOOL --> AUD
  AUD --> PG
  ING --> PG

  SUP --> LLM
  K --> LLM
  LLM -. inference .-> OR
```

Three boxes sit outside the FastAPI application: Keycloak, OpenRouter and PostgreSQL. Chatwoot is outside it too. That boundary is what the professor means by showing what is inside the system and what is outside.

The model adapter is worth a sentence of its own. The team holds one OpenRouter free-tier key per member, and the adapter moves to the next key when one hits its rate limit. Changing to a paid provider later means changing settings in that one module.

Note the two paths into the application. The portal and the staff console call the REST API directly. Chat messages arrive through Chatwoot by webhook. Both paths land on the same API layer, and that layer verifies the token.

---

## 2. Use case diagram (draw.io only)

Mermaid has no use case diagram, so build this one by hand. Draw one system boundary box titled **Smart University Website**. Put the four actors outside it.

**Actor: Student.**
- Ask a policy question.
- View own academic record.
- Search the library catalogue.
- Renew a library loan.
- Book a bookable resource.
- Cancel or reschedule own booking.
- Submit a service request.
- Track a service request.
- Send a payment slip.
- Continue a conversation on another day or channel.
- Receive a reminder from the assistant.
- Ask for a human.

**Actor: Staff.**
- View the work queue.
- Take over a conversation.
- Change a request state.
- Check a payment slip, then confirm or reject it.
- Release a conversation back to the assistant.

**Actor: Advisor.**
- Publish availability.
- View own appointments.
- Read the advising brief before a meeting.

**Actor: Administrator.**
- Manage accounts and roles.
- Upload documents and read the ingestion result.
- Read the questions without an answer.
- Read the system status.
- Read the audit log.

Three relationships are worth drawing. "Ask a policy question" includes "Cite the source document". "Book a bookable resource" includes "Confirm before writing". "Send a payment slip" includes "Check a payment slip", and the check is always a person.

---

## 3. ER diagram

```mermaid
erDiagram
  USER ||--o| STUDENT_RECORD : has
  USER ||--o{ CONVERSATION : owns
  USER ||--o{ RESERVATION : makes
  USER ||--o{ REQUEST : submits
  USER ||--o{ AUDIT_LOG : generates
  CONVERSATION ||--o{ MESSAGE : contains
  RESOURCE ||--o{ SLOT : offers
  SLOT ||--o| RESERVATION : filled_by
  REQUEST ||--o{ REQUEST_EVENT : has_history
  USER ||--o{ REQUEST_EVENT : changes
  DOCUMENT ||--o{ DOCUMENT_CHUNK : split_into
  BOOK ||--o{ LOAN : lent_as
  USER ||--o{ LOAN : borrows
  USER ||--o{ CHARGE : owes
  CHARGE ||--o{ PAYMENT_CHECK : paid_by
  USER ||--o{ PAYMENT_CHECK : submits
  USER ||--o{ PAYMENT_CHECK : decides
  PAYMENT_CHECK ||--|| SLIP_FILE : shows
  USER ||--o{ MEMORY_FACT : remembered_for
  CONVERSATION ||--o{ MEMORY_FACT : source_of
  RESERVATION ||--o| ADVISOR_BRIEF : prepared_for
  UNANSWERED_QUESTION }o--o| DOCUMENT : closed_by

  USER {
    uuid id PK
    string keycloak_sub UK
    string full_name
    string role
    string email
  }
  STUDENT_RECORD {
    uuid id PK
    uuid user_id FK
    string student_number UK
    string programme
    int year_of_study
    string registration_status
    decimal outstanding_balance
  }
  RESOURCE {
    uuid id PK
    string name
    string resource_type
    int capacity
    string location
    int cancel_cutoff_minutes
  }
  SLOT {
    uuid id PK
    uuid resource_id FK
    timestamp starts_at
    timestamp ends_at
    boolean is_open
  }
  RESERVATION {
    uuid id PK
    uuid slot_id FK
    uuid user_id FK
    string state
    timestamp created_at
  }
  REQUEST {
    uuid id PK
    uuid user_id FK
    string reference UK
    string request_type
    string state
    jsonb payload
    timestamp created_at
  }
  REQUEST_EVENT {
    uuid id PK
    uuid request_id FK
    string from_state
    string to_state
    uuid changed_by FK
    timestamp changed_at
  }
  CONVERSATION {
    uuid id PK
    uuid user_id FK
    string channel
    string external_id
    boolean human_owned
  }
  MESSAGE {
    uuid id PK
    uuid conversation_id FK
    string author
    text body
    string routed_to_agent
    timestamp created_at
  }
  DOCUMENT {
    uuid id PK
    string title
    string section
    string source_url
    string language
    string state
  }
  DOCUMENT_CHUNK {
    uuid id PK
    uuid document_id FK
    text content
    vector embedding
  }
  AUDIT_LOG {
    uuid id PK
    uuid actor_id FK
    string action
    string target
    timestamp occurred_at
  }
  BOOK {
    uuid id PK
    string title
    string author
    string isbn UK
    string call_number
    string shelf_location
    int copies_total
    int copies_available
  }
  LOAN {
    uuid id PK
    uuid book_id FK
    uuid user_id FK
    date due_on
    int renewals
  }
  CHARGE {
    uuid id PK
    uuid user_id FK
    string description
    decimal amount
    date due_on
    string state
  }
  PAYMENT_CHECK {
    uuid id PK
    uuid charge_id FK
    uuid submitted_by FK
    uuid decided_by FK
    string state
    decimal amount_on_slip
    string reason
    timestamp submitted_at
    timestamp decided_at
  }
  SLIP_FILE {
    uuid id PK
    uuid payment_check_id FK
    string storage_path
    string mime_type
    timestamp keep_until
  }
  MEMORY_FACT {
    uuid id PK
    uuid user_id FK
    uuid conversation_id FK
    string topic
    text content
    timestamp saved_at
  }
  ADVISOR_BRIEF {
    uuid id PK
    uuid reservation_id FK
    text content
    timestamp updated_at
  }
  UNANSWERED_QUESTION {
    uuid id PK
    uuid document_id FK
    text question
    int times_asked
    string state
    timestamp last_asked_at
  }
```

Two points to make when presenting this. `SLOT` to `RESERVATION` is one to zero-or-one, and that single constraint is what makes double booking impossible. `DOCUMENT` and `DOCUMENT_CHUNK` carry the source title and section, which is how every answer can cite its rule.

---

## 4. Supervisor routing and tool selection

```mermaid
flowchart TD
  A["Message arrives on web, LINE or Telegram"] --> B["Detect the language"]
  B --> C["Resolve the subject from the session token"]
  C --> D{"Is the sender linked to a student account?"}
  D -- No --> E["Answer public questions only"]
  E --> Z["Send on the originating channel"]
  D -- Yes --> M["Load memory and recent messages by student ID"]
  TM["Timer: an appointment starts in 24 hours"] --> B1
  M --> IM{"Does the message carry an image?"}
  IM -- Yes --> SF["Store the image privately"]
  SF --> PC["Request agent creates a payment check, state waiting"]
  PC --> NS["Notify staff in the Payments tab and in the chat"]
  NS --> RS["Reply: sent to Student Services for a check"]
  RS --> Z
  NS -.-> SD["Staff confirm or reject the slip"]
  SD -.-> NT["Notify the student"]
  NT -.-> Z
  IM -- No --> F["Supervisor classifies the intent"]
  F --> G{"Which specialist agent?"}

  G -- "Low confidence" --> H["Hand the conversation to staff"]
  G -- "Policy question" --> K1["Knowledge agent retrieves passages"]
  G -- "Own record, loans or catalogue search" --> R1["Records agent"]
  G -- "Booking" --> B1["Booking agent"]
  G -- "Service request or loan renewal" --> Q1["Request agent"]

  K1 --> K2{"Any passage above the similarity threshold?"}
  K2 -- No --> UQ["Record the question as unanswered"]
  UQ --> H
  K2 -- Yes --> Y1["Attach the source document and section"]
  Y1 --> Y["Compose the reply"]

  R1 --> S{"Does the message name a different student?"}
  S -- Yes --> S2["Refuse, and record the attempt"]
  S2 --> Z
  S -- No --> T["Agent selects a tool and builds arguments"]

  B1 --> T
  Q1 --> T

  T --> MD{"Is a needed detail missing?"}
  MD -- Yes --> CQ["Ask one question and change nothing"]
  CQ --> Z
  MD -- No --> V{"Are the arguments valid?"}
  V -- "No, first failure" --> T2["Return a corrective message"]
  T2 --> T
  V -- "No, second failure" --> H
  V -- Yes --> W{"Does the tool write data?"}

  W -- No --> RD["Read, scoped to the subject in the token"]
  RD --> Y
  W -- Yes --> CF["Ask the student to confirm"]
  CF --> EX["Execute inside one transaction"]
  EX --> AUD["Write an audit record"]
  AUD --> Y

  Y --> SV["Save new facts to memory"]
  SV --> Z
  H --> Z
```

This is the diagram that answers the professor's requirement to show what we will develop and how. Four branches on it are worth saying out loud in the presentation. The subject always comes from the token, never from the message text. A message naming a different student is refused and recorded. No passage above the threshold means a refusal rather than a guess. Before every write, the agent asks for confirmation, and each write leaves an audit record.

import { useState } from "react";

const initialMessages = [
  {
    type: "user",
    text: "What documents do I need from the university for my student visa renewal?",
  },
  {
    type: "assistant",
    text: "For a visa renewal you need three documents from Thales University:",
    documents: [
      "Enrolment Certificate, issued by the Registrar",
      "Official Transcript for the current academic year",
      "A letter confirming your tuition payment status",
    ],
  },
];

const portalLinks = ["Overview", "Assistant", "My requests", "Transcript request", "My bookings", "Library", "My records"];

function App() {
  const [isPortal, setIsPortal] = useState(false);
  const [showLogin, setShowLogin] = useState(false);
  const [userRole, setUserRole] = useState(null);
  const [publicPage, setPublicPage] = useState("home");
  const [activePage, setActivePage] = useState("Assistant");
  const [messages, setMessages] = useState(initialMessages);
  const [draft, setDraft] = useState("");
  const [booking, setBooking] = useState({
    step: "people",
    people: null,
    slot: null,
  });
  const [payment, setPayment] = useState({ step: "start", fileName: null });
  const [transcript, setTranscript] = useState({
    step: "options",
    copies: null,
    delivery: null,
  });
  const [libraryQuery, setLibraryQuery] = useState("");

  function sendMessage(event) {
    event.preventDefault();
    const text = draft.trim();
    if (!text) return;

    setMessages((current) => [
      ...current,
      { type: "user", text },
      {
        type: "assistant",
        text: "I can help with that. I will search the Student Handbook and your student services information.",
      },
    ]);
    setDraft("");
  }

  return (
    <main className="min-h-screen bg-stone-50 text-charcoal">
      <Header
        isPortal={isPortal}
        onPublicPageChange={(page) => {
          setPublicPage(page);
          setIsPortal(false);
        }}
        onSignIn={() => setShowLogin(true)}
        onPortalToggle={() => {
          if (userRole) {
            setIsPortal((current) => !current);
          } else {
            setShowLogin(true);
          }
        }}
      />
      {showLogin ? (
        <LoginPage
          onCancel={() => setShowLogin(false)}
          onLogin={(role) => {
            setUserRole(role);
            setActivePage(role === "student" ? "Overview" : "Queue");
            setShowLogin(false);
            setIsPortal(true);
          }}
        />
      ) : isPortal ? (
        <PortalLayout activePage={activePage} onPageChange={setActivePage} role={userRole}>
          {activePage === "Assistant" ? (
            <Assistant
              draft={draft}
              messages={messages}
              onDraftChange={setDraft}
              onSend={sendMessage}
            />
          ) : activePage === "My bookings" ? (
            <BookingPage booking={booking} onBookingChange={setBooking} />
          ) : activePage === "My requests" ? (
            <PaymentPage payment={payment} onPaymentChange={setPayment} />
          ) : activePage === "Transcript request" ? (
            <TranscriptPage transcript={transcript} onTranscriptChange={setTranscript} />
          ) : activePage === "Overview" ? (
            <OverviewPage onPageChange={setActivePage} />
          ) : activePage === "Library" ? (
            <LibraryPage query={libraryQuery} onQueryChange={setLibraryQuery} />
          ) : activePage === "My records" ? (
            <RecordsPage />
          ) : userRole === "staff" && ["Queue", "Requests", "Payments", "Audit log"].includes(activePage) ? (
            <StaffConsole activeTab={activePage} />
          ) : (
            <PlaceholderPage page={activePage} />
          )}
        </PortalLayout>
      ) : (
        <PublicPage
          page={publicPage}
          onPageChange={setPublicPage}
          onPortalOpen={() => setShowLogin(true)}
        />
      )}
    </main>
  );
}

function Header({ isPortal, onPublicPageChange, onPortalToggle, onSignIn }) {
  return (
    <header className="border-b border-stone-200 bg-white">
      <div className="mx-auto flex max-w-[1440px] items-center justify-between px-6 py-4 lg:px-10">
        <button className="flex items-center gap-3 text-left" onClick={() => (isPortal ? onPortalToggle() : onPublicPageChange("home"))}>
          <div className="grid size-10 place-items-center rounded-xl bg-teal-900 font-bold text-lime-300">
            T
          </div>
          <div>
            <p className="font-semibold tracking-tight text-charcoal">Thales University</p>
            <p className="text-xs text-stone-500">Student services</p>
          </div>
        </button>
        <nav className="hidden items-center gap-6 text-sm md:flex">
          <button className="text-stone-600 hover:text-teal-900" onClick={() => onPublicPageChange("programmes")}>Programmes</button>
          <button className="text-stone-600 hover:text-teal-900" onClick={() => onPublicPageChange("admissions")}>Admissions</button>
          <button className="text-stone-600 hover:text-teal-900" onClick={() => onPublicPageChange("about")}>About</button>
        </nav>
        <div className="flex items-center gap-3 text-sm">
          {!isPortal && (
            <button
              className="rounded-full border border-teal-900 px-4 py-2 font-semibold text-teal-900 hover:bg-teal-50"
              onClick={onSignIn}
            >
              Sign in
            </button>
          )}
          <button
            className="rounded-full bg-teal-900 px-4 py-2 font-semibold text-white hover:bg-teal-800"
            onClick={onPortalToggle}
          >
            {isPortal ? "Public website" : "Student portal"}
          </button>
        </div>
      </div>
    </header>
  );
}

function PublicPage({ page, onPageChange, onPortalOpen }) {
  if (page !== "home") {
    return <PublicContentPage page={page} onPageChange={onPageChange} onPortalOpen={onPortalOpen} />;
  }

  return <PublicHome onPageChange={onPageChange} onPortalOpen={onPortalOpen} />;
}

function PublicHome({ onPageChange, onPortalOpen }) {
  return (
    <div>
      <section className="bg-teal-950">
        <div className="mx-auto grid max-w-[1440px] gap-12 px-6 py-20 lg:grid-cols-[1.1fr_0.9fr] lg:px-10 lg:py-28">
          <div className="max-w-2xl">
            <p className="mb-5 text-sm font-bold uppercase tracking-[0.2em] text-lime-300">
              Learn with purpose
            </p>
            <h1 className="text-4xl font-semibold leading-tight tracking-tight text-white sm:text-6xl">
              Make your next step count.
            </h1>
            <p className="mt-6 max-w-xl text-lg leading-8 text-teal-100">
              Explore a university that connects people, ideas and practical opportunities for a changing world.
            </p>
            <div className="mt-8 flex flex-wrap gap-3">
              <button className="rounded-lg bg-lime-300 px-5 py-3 font-semibold text-teal-950 hover:bg-lime-200" onClick={() => onPageChange("programmes")}>
                Explore programmes
              </button>
              <button
                className="rounded-lg border border-teal-700 px-5 py-3 font-semibold text-white hover:bg-teal-900"
                onClick={onPortalOpen}
              >
                Open student portal
              </button>
            </div>
          </div>
          <div className="rounded-2xl border border-teal-700 bg-teal-900 p-6 text-white shadow-2xl">
            <p className="text-sm font-semibold text-lime-300">Student services, in one place</p>
            <p className="mt-4 text-2xl font-semibold">Ask questions. Book resources. Track requests.</p>
            <p className="mt-4 leading-7 text-teal-100">
              The assistant helps you find the right university information and guides you through your next action.
            </p>
            <button className="mt-8 rounded-lg bg-white px-4 py-2.5 text-sm font-semibold text-teal-950 hover:bg-teal-50" onClick={onPortalOpen}>
              Try the assistant
            </button>
          </div>
        </div>
      </section>
      <section className="mx-auto grid max-w-[1440px] gap-5 px-6 py-14 sm:grid-cols-3 lg:px-10">
        {["Undergraduate study", "Graduate study", "Research and innovation"].map((item) => (
          <article className="rounded-2xl border border-stone-200 bg-white p-6" key={item}>
            <p className="text-sm font-semibold text-teal-800">Thales University</p>
            <h2 className="mt-3 text-xl font-semibold">{item}</h2>
            <p className="mt-3 text-sm leading-6 text-stone-600">Find programmes, support and opportunities designed around your goals.</p>
            <button className="mt-5 text-left text-sm font-semibold text-teal-800 hover:text-teal-950" onClick={() => onPageChange("about")}>Learn more →</button>
          </article>
        ))}
      </section>
    </div>
  );
}

function PublicContentPage({ page, onPageChange, onPortalOpen }) {
  const content = {
    programmes: {
      eyebrow: "Study at Thales University",
      title: "Programmes built for what comes next.",
      description: "Choose a course of study that combines strong foundations with practical experience and support from your university community.",
      cards: [
        ["Undergraduate study", "Build your foundation through focused courses, projects and opportunities to work with others."],
        ["Graduate study", "Deepen your expertise with flexible programmes led by active researchers and practitioners."],
        ["Research and innovation", "Turn questions into meaningful work with support from our research community."],
      ],
    },
    admissions: {
      eyebrow: "Join our community",
      title: "Your application starts here.",
      description: "Find the information you need to choose a programme, prepare your application and plan your first day at Thales University.",
      cards: [
        ["Explore requirements", "Review programme entry requirements and prepare the documents you need."],
        ["Application steps", "Create your application, submit your supporting documents and track your progress."],
        ["Ask a question", "Our student services team can help you understand the next step."],
      ],
    },
    about: {
      eyebrow: "About Thales University",
      title: "A university connected to its people.",
      description: "Thales University brings together learning, research and student services in a community that helps people make their next step count.",
      cards: [
        ["Our community", "Students, instructors and staff work together across disciplines and backgrounds."],
        ["Our approach", "We connect academic knowledge with practical experiences and real-world questions."],
        ["Student support", "From your first question to your next opportunity, support is available in one place."],
      ],
    },
  }[page];

  return (
    <div>
      <section className="bg-teal-950">
        <div className="mx-auto max-w-[1440px] px-6 py-20 lg:px-10 lg:py-24">
          <button className="text-sm font-semibold text-lime-300 hover:text-lime-200" onClick={() => onPageChange("home")}>← Back to home</button>
          <p className="mt-10 text-sm font-bold uppercase tracking-[0.2em] text-lime-300">{content.eyebrow}</p>
          <h1 className="mt-5 max-w-3xl text-4xl font-semibold leading-tight tracking-tight text-white sm:text-6xl">{content.title}</h1>
          <p className="mt-6 max-w-2xl text-lg leading-8 text-teal-100">{content.description}</p>
        </div>
      </section>
      <section className="mx-auto max-w-[1440px] px-6 py-14 lg:px-10">
        <div className="grid gap-5 md:grid-cols-3">
          {content.cards.map(([title, description]) => (
            <article className="rounded-2xl border border-stone-200 bg-white p-6" key={title}>
              <div className="grid size-10 place-items-center rounded-xl bg-lime-200 font-semibold text-teal-950">T</div>
              <h2 className="mt-5 text-xl font-semibold">{title}</h2>
              <p className="mt-3 text-sm leading-6 text-stone-600">{description}</p>
            </article>
          ))}
        </div>
        <div className="mt-10 rounded-2xl border border-teal-200 bg-teal-50 p-6 sm:flex sm:items-center sm:justify-between sm:gap-6">
          <div><p className="font-semibold text-teal-950">Need help finding your next step?</p><p className="mt-1 text-sm text-teal-800">Open the student portal to ask the assistant.</p></div>
          <button className="mt-4 rounded-lg bg-teal-900 px-4 py-2.5 text-sm font-semibold text-white hover:bg-teal-800 sm:mt-0" onClick={onPortalOpen}>Open student portal</button>
        </div>
      </section>
    </div>
  );
}

function PortalLayout({ activePage, onPageChange, role, children }) {
  const links = role === "staff"
    ? ["Queue", "Requests", "Payments", "Audit log"]
    : portalLinks;
  return (
    <div className="mx-auto grid max-w-[1440px] gap-8 px-6 py-8 lg:grid-cols-[230px_minmax(0,1fr)] lg:px-10">
      <aside>
        <p className="mb-3 text-xs font-bold uppercase tracking-wider text-stone-400">
          {role === "staff" ? "Staff console" : "Student portal"}
        </p>
        <nav className="space-y-1">
          {links.map((link) => (
            <button
              className={`block w-full rounded-lg px-3 py-2.5 text-left text-sm font-medium ${
                activePage === link ? "bg-teal-50 font-semibold text-teal-950" : "text-stone-600 hover:bg-white"
              }`}
              key={link}
              onClick={() => onPageChange(link)}
            >
              {link}
            </button>
          ))}
        </nav>
        <div className="mt-10 rounded-xl bg-teal-950 p-4 text-sm text-white">
          <p className="font-semibold">{role === "staff" ? "Staff tools" : "Need help?"}</p>
          <p className="mt-2 leading-6 text-teal-100">
            {role === "staff" ? "Review requests, payments and audit activity." : "Ask the assistant about university services."}
          </p>
        </div>
      </aside>
      <div>{children}</div>
    </div>
  );
}

function LoginPage({ onCancel, onLogin }) {
  const [email, setEmail] = useState("");
  const [error, setError] = useState("");

  function submit(event) {
    event.preventDefault();
    const value = email.trim().toLowerCase();
    if (!value || !value.includes("@")) {
      setError("Enter a valid university email address.");
      return;
    }

    const role = /staff|admin|registrar|finance/.test(value) ? "staff" : "student";
    onLogin(role);
  }

  return (
    <section className="flex min-h-[calc(100vh-73px)] items-center justify-center px-6 py-12">
      <div className="w-full max-w-md rounded-2xl border border-stone-200 bg-white p-8 shadow-sm">
        <div className="grid size-12 place-items-center rounded-xl bg-teal-900 font-bold text-lime-300">T</div>
        <p className="mt-6 text-sm font-semibold text-teal-800">Thales University</p>
        <h1 className="mt-1 text-3xl font-semibold">Sign in to continue</h1>
        <p className="mt-3 text-sm leading-6 text-stone-600">Use your university email. You will be sent to the portal for your account role.</p>
        <form className="mt-6 space-y-4" onSubmit={submit}>
          <label className="block text-sm font-medium">
            University email
            <input
              autoComplete="email"
              className="mt-2 w-full rounded-lg border border-stone-300 px-3 py-3 text-sm outline-none focus:border-teal-700 focus:ring-2 focus:ring-teal-100"
              onChange={(event) => {
                setEmail(event.target.value);
                setError("");
              }}
              placeholder="you@thales.edu"
              type="email"
              value={email}
            />
          </label>
          {error && <p className="text-sm text-red-700">{error}</p>}
          <button className="w-full rounded-lg bg-teal-900 px-4 py-3 text-sm font-semibold text-white hover:bg-teal-800" type="submit">Sign in</button>
        </form>
        <p className="mt-5 text-xs leading-5 text-stone-500">Demo routing: emails containing “staff”, “admin”, “registrar”, or “finance” open the staff portal. Other university emails open the student portal.</p>
        <button className="mt-5 text-sm font-semibold text-teal-800 hover:text-teal-950" onClick={onCancel}>← Back to public website</button>
      </div>
    </section>
  );
}

function Assistant({ draft, messages, onDraftChange, onSend }) {
  return (
    <section className="overflow-hidden rounded-2xl border border-stone-200 bg-white shadow-sm">
      <div className="flex items-center justify-between border-b border-stone-200 px-5 py-4">
        <div>
          <h1 className="font-semibold">Student assistant</h1>
          <p className="mt-1 flex items-center gap-1.5 text-xs text-stone-500">
            <span className="size-2 rounded-full bg-lime-500" />
            Assistant is available
          </p>
        </div>
        <button className="rounded-lg border border-stone-200 px-3 py-2 text-sm text-stone-600 hover:bg-stone-50">New chat</button>
      </div>
      <div className="space-y-5 bg-stone-50/70 p-5 sm:p-8">
        <div className="text-center text-xs text-stone-400">Wednesday 14 October 2026</div>
        {messages.map((message, index) => <Message key={`${message.type}-${index}`} message={message} />)}
        <div className="max-w-[90%] rounded-xl border border-lime-200 bg-lime-50 p-4 text-sm text-teal-950">
          <p className="font-medium">Would you like me to start with the official transcript?</p>
          <div className="mt-3 flex flex-wrap gap-2">
            <button className="rounded-lg bg-teal-900 px-3 py-2 text-xs font-semibold text-white hover:bg-teal-800">Yes, start with the transcript</button>
            <button className="rounded-lg border border-teal-200 bg-white px-3 py-2 text-xs font-semibold text-teal-950 hover:bg-teal-50">Not now</button>
          </div>
        </div>
      </div>
      <form className="border-t border-stone-200 p-4" onSubmit={onSend}>
        <div className="flex items-center gap-3 rounded-xl border border-stone-300 bg-white p-2 pl-4 focus-within:border-teal-700 focus-within:ring-2 focus-within:ring-teal-100">
          <input className="min-w-0 flex-1 bg-transparent text-sm outline-none placeholder:text-stone-400" onChange={(event) => onDraftChange(event.target.value)} placeholder="Ask about fees, bookings, documents..." value={draft} />
          <button className="rounded-lg bg-teal-900 px-4 py-2 text-sm font-semibold text-white hover:bg-teal-800" type="submit">Send</button>
        </div>
      </form>
    </section>
  );
}

function Message({ message }) {
  const isUser = message.type === "user";
  return (
    <div className={isUser ? "ml-auto max-w-[85%]" : "max-w-[90%]"}>
      <div className={isUser ? "rounded-xl rounded-br-sm bg-teal-900 px-4 py-3 text-sm leading-6 text-white" : "rounded-xl rounded-bl-sm border border-stone-200 bg-white px-4 py-3 text-sm leading-6 text-stone-700"}>
        <p>{message.text}</p>
        {message.documents && <ol className="mt-2 list-inside list-decimal space-y-1">{message.documents.map((document) => <li key={document}>{document}</li>)}</ol>}
      </div>
      {!isUser && <div className="mt-2 rounded-lg border-l-4 border-teal-700 bg-white px-3 py-2 text-xs text-stone-600 shadow-sm"><p className="font-semibold text-teal-950">Student Handbook 2026 · Section 7.3</p><p className="mt-1">Immigration documents · View source</p></div>}
    </div>
  );
}

function PaymentPage({ payment, onPaymentChange }) {
  const { step, fileName } = payment;

  function selectSlip(event) {
    const file = event.target.files?.[0];
    if (file) onPaymentChange({ step: "selected", fileName: file.name });
  }

  function submitSlip() {
    onPaymentChange({ ...payment, step: "received" });
  }

  function resetPayment() {
    onPaymentChange({ step: "start", fileName: null });
  }

  return (
    <section className="rounded-2xl border border-stone-200 bg-white shadow-sm">
      <div className="border-b border-stone-200 px-6 py-5">
        <p className="text-sm font-semibold text-teal-800">Student portal · My requests</p>
        <h1 className="mt-1 text-2xl font-semibold">Payment slip</h1>
        <p className="mt-2 text-sm text-stone-600">Send your tuition payment slip for staff review.</p>
      </div>
      <div className="p-6 sm:p-8">
        {step === "start" && (
          <div className="rounded-xl border-2 border-dashed border-stone-300 bg-stone-50 p-8 text-center">
            <p className="font-medium">I paid my tuition. Here is the slip.</p>
            <p className="mx-auto mt-2 max-w-md text-sm leading-6 text-stone-500">Upload a clear photo or screenshot of your payment slip. A staff member checks it before your balance changes.</p>
            <label className="mt-6 inline-flex cursor-pointer rounded-lg bg-teal-900 px-4 py-2.5 text-sm font-semibold text-white hover:bg-teal-800">
              Choose slip
              <input accept="image/*,.pdf" className="sr-only" onChange={selectSlip} type="file" />
            </label>
            <p className="mt-3 text-xs text-stone-400">PNG, JPG or PDF · Maximum 10 MB</p>
          </div>
        )}

        {step === "selected" && (
          <div>
            <p className="font-medium">Check your slip before sending it.</p>
            <div className="mt-4 flex items-center justify-between rounded-xl border border-stone-200 bg-stone-50 p-4">
              <div className="flex items-center gap-3">
                <span className="grid size-10 place-items-center rounded-lg bg-lime-200 text-lg">▧</span>
                <div>
                  <p className="text-sm font-semibold">{fileName}</p>
                  <p className="mt-1 text-xs text-stone-500">Ready to send to Student Services</p>
                </div>
              </div>
              <button className="text-sm font-semibold text-teal-800 hover:text-teal-950" onClick={resetPayment}>Remove</button>
            </div>
            <div className="mt-5 rounded-xl border border-lime-200 bg-lime-50 p-4 text-sm leading-6 text-teal-950">
              The assistant does not read the image. A staff member will check the amount and confirm your payment.
            </div>
            <button className="mt-5 rounded-lg bg-teal-900 px-4 py-2.5 text-sm font-semibold text-white hover:bg-teal-800" onClick={submitSlip}>Send slip</button>
          </div>
        )}

        {step === "received" && (
          <div>
            <div className="rounded-xl border border-lime-200 bg-lime-50 p-5">
              <div className="flex items-start gap-3">
                <span className="grid size-8 shrink-0 place-items-center rounded-full bg-lime-300 font-bold text-teal-950">✓</span>
                <div>
                  <p className="font-semibold text-teal-950">Slip received</p>
                  <p className="mt-2 text-sm leading-6 text-teal-900">Thank you. A staff member checks your slip before your balance changes. You will get a message here when it is done.</p>
                </div>
              </div>
            </div>
            <div className="mt-6">
              <p className="text-sm font-semibold">Payment status</p>
              <div className="mt-4 space-y-4">
                <StatusStep active label="Slip received" detail="14 October 2026, 16:06" />
                <StatusStep label="Under review" />
                <StatusStep label="Confirmed" />
                <StatusStep label="Balance updated" />
              </div>
            </div>
            <button className="mt-6 rounded-lg border border-stone-200 px-4 py-2.5 text-sm font-semibold text-stone-700 hover:bg-stone-50" onClick={resetPayment}>Send another slip</button>
          </div>
        )}
      </div>
    </section>
  );
}

function TranscriptPage({ transcript, onTranscriptChange }) {
  const { step, copies, delivery } = transcript;

  function chooseOption(key, value) {
    const updated = { ...transcript, [key]: value };
    onTranscriptChange({
      ...updated,
      step: updated.copies && updated.delivery ? "confirm" : "options",
    });
  }

  function submitRequest() {
    onTranscriptChange({ ...transcript, step: "submitted" });
  }

  function startAgain() {
    onTranscriptChange({ step: "options", copies: null, delivery: null });
  }

  return (
    <section className="rounded-2xl border border-stone-200 bg-white shadow-sm">
      <div className="border-b border-stone-200 px-6 py-5">
        <p className="text-sm font-semibold text-teal-800">Student portal · Transcript request</p>
        <h1 className="mt-1 text-2xl font-semibold">Request an official transcript</h1>
        <p className="mt-2 text-sm text-stone-600">Submit a transcript request and track it from this portal.</p>
      </div>
      <div className="p-6 sm:p-8">
        {step === "options" && (
          <div className="space-y-7">
            <div>
              <p className="font-medium">How many copies do you need?</p>
              <div className="mt-3 flex flex-wrap gap-3">
                {[1, 2, 3].map((value) => (
                  <ChoiceButton
                    active={copies === value}
                    label={value === 3 ? "3 or more" : `${value} copy${value > 1 ? "ies" : ""}`}
                    onClick={() => chooseOption("copies", value)}
                    key={value}
                  />
                ))}
              </div>
            </div>
            <div>
              <p className="font-medium">How would you like to receive it?</p>
              <div className="mt-3 flex flex-wrap gap-3">
                {["Collect", "Post"].map((value) => (
                  <ChoiceButton
                    active={delivery === value}
                    label={value}
                    onClick={() => chooseOption("delivery", value)}
                    key={value}
                  />
                ))}
              </div>
            </div>
            <p className="text-sm text-stone-500">Choose both options to review your request.</p>
          </div>
        )}

        {step === "confirm" && (
          <div>
            <p className="font-medium">Almost done. Check the details below.</p>
            <div className="mt-4 rounded-xl border border-lime-200 bg-lime-50 p-5">
              <p className="font-semibold text-teal-950">Official Transcript</p>
              <dl className="mt-3 space-y-2 text-sm text-teal-900">
                <div className="flex justify-between gap-4"><dt>Copies</dt><dd className="font-semibold">{copies === 3 ? "3 or more" : copies}</dd></div>
                <div className="flex justify-between gap-4"><dt>Delivery</dt><dd className="font-semibold">{delivery} {delivery === "Collect" && "at the Registrar"}</dd></div>
                <div className="flex justify-between gap-4 border-t border-lime-200 pt-2"><dt>Fee</dt><dd className="font-semibold">200 THB, payable on collection</dd></div>
              </dl>
            </div>
            <div className="mt-5 flex flex-wrap gap-3">
              <button className="rounded-lg bg-teal-900 px-4 py-2.5 text-sm font-semibold text-white hover:bg-teal-800" onClick={submitRequest}>Confirm request</button>
              <button className="rounded-lg border border-stone-200 px-4 py-2.5 text-sm font-semibold text-stone-700 hover:bg-stone-50" onClick={startAgain}>Change</button>
            </div>
          </div>
        )}

        {step === "submitted" && (
          <div>
            <div className="rounded-xl border border-lime-200 bg-lime-50 p-5">
              <p className="font-semibold text-teal-950">Transcript request submitted</p>
              <p className="mt-2 text-sm leading-6 text-teal-900">Your reference is <strong>REQ-2026-0481</strong>. When the state changes, I will message you here.</p>
            </div>
            <div className="mt-6">
              <p className="text-sm font-semibold">Request status</p>
              <div className="mt-4 space-y-4">
                <StatusStep active label="Submitted" detail="14 October 2026, 14:31" />
                <StatusStep label="Under review" />
                <StatusStep label="Ready" />
                <StatusStep label="Collected" />
              </div>
            </div>
            <button className="mt-6 rounded-lg border border-stone-200 px-4 py-2.5 text-sm font-semibold text-stone-700 hover:bg-stone-50" onClick={startAgain}>Create another request</button>
          </div>
        )}
      </div>
    </section>
  );
}

function ChoiceButton({ active, label, onClick }) {
  return (
    <button className={`rounded-lg border px-4 py-2.5 text-sm font-semibold ${active ? "border-teal-900 bg-teal-900 text-white" : "border-stone-200 text-stone-700 hover:border-teal-700 hover:bg-teal-50"}`} onClick={onClick}>
      {label}
    </button>
  );
}

function StatusStep({ active = false, label, detail }) {
  return (
    <div className="flex items-start gap-3">
      <span className={`mt-0.5 grid size-6 place-items-center rounded-full text-xs font-bold ${active ? "bg-teal-900 text-white" : "border border-stone-300 bg-white text-stone-400"}`}>
        {active ? "✓" : "·"}
      </span>
      <div>
        <p className={`text-sm ${active ? "font-semibold text-teal-950" : "text-stone-500"}`}>{label}</p>
        {detail && <p className="mt-1 text-xs text-stone-500">{detail}</p>}
      </div>
    </div>
  );
}

function PlaceholderPage({ page }) {
  return (
    <section className="rounded-2xl border border-stone-200 bg-white p-8 shadow-sm">
      <p className="text-sm font-semibold text-teal-800">Student portal</p>
      <h1 className="mt-2 text-3xl font-semibold">{page}</h1>
      <p className="mt-3 max-w-xl leading-7 text-stone-600">This page is ready for the next implementation phase. Its layout follows the shared portal shell and design system.</p>
    </section>
  );
}

function OverviewPage({ onPageChange }) {
  return (
    <div className="space-y-6">
      <div>
        <p className="text-sm font-semibold text-teal-800">Thursday 15 October 2026</p>
        <h1 className="mt-1 text-3xl font-semibold">Good morning</h1>
        <p className="mt-2 text-stone-600">Here is your student services overview.</p>
      </div>
      <div className="grid gap-4 sm:grid-cols-3">
        <SummaryCard label="Outstanding balance" value="12,500 THB" detail="Due 27 November 2026" />
        <SummaryCard label="Open requests" value="1" detail="REQ-2026-0481 under review" />
        <SummaryCard label="Upcoming booking" value="1" detail="Library Room B2 · Thursday" />
      </div>
      <div className="grid gap-6 lg:grid-cols-2">
        <div className="rounded-2xl border border-stone-200 bg-white p-6">
          <p className="font-semibold">Quick actions</p>
          <div className="mt-4 grid gap-3 sm:grid-cols-2">
            <QuickAction label="Ask the assistant" onClick={() => onPageChange("Assistant")} />
            <QuickAction label="Book a study room" onClick={() => onPageChange("My bookings")} />
            <QuickAction label="Request transcript" onClick={() => onPageChange("Transcript request")} />
            <QuickAction label="Search library" onClick={() => onPageChange("Library")} />
          </div>
        </div>
        <div className="rounded-2xl border border-stone-200 bg-white p-6">
          <p className="font-semibold">Recent activity</p>
          <div className="mt-4 space-y-4">
            <Activity label="Transcript request submitted" detail="REQ-2026-0481 · 14 October, 14:31" />
            <Activity label="Payment slip received" detail="12,500 THB · 14 October, 16:06" />
            <Activity label="Study room booked" detail="Library Room B2 · 15 October, 13:00" />
          </div>
        </div>
      </div>
    </div>
  );
}

function SummaryCard({ label, value, detail }) {
  return (
    <div className="rounded-2xl border border-stone-200 bg-white p-5">
      <p className="text-sm text-stone-500">{label}</p>
      <p className="mt-3 text-2xl font-semibold text-teal-950">{value}</p>
      <p className="mt-2 text-xs text-stone-500">{detail}</p>
    </div>
  );
}

function QuickAction({ label, onClick }) {
  return <button className="rounded-lg border border-stone-200 px-3 py-3 text-left text-sm font-semibold text-teal-900 hover:border-teal-700 hover:bg-teal-50" onClick={onClick}>{label} →</button>;
}

function Activity({ label, detail }) {
  return <div className="border-l-2 border-lime-400 pl-4"><p className="text-sm font-medium">{label}</p><p className="mt-1 text-xs text-stone-500">{detail}</p></div>;
}

function RecordsPage() {
  const [requestedStudent, setRequestedStudent] = useState("");
  const [denied, setDenied] = useState(false);

  function checkRecord(event) {
    event.preventDefault();
    setDenied(requestedStudent.trim() !== "" && requestedStudent.trim() !== "67111411");
  }

  return (
    <section className="rounded-2xl border border-stone-200 bg-white shadow-sm">
      <div className="border-b border-stone-200 px-6 py-5">
        <p className="text-sm font-semibold text-teal-800">Student portal · My records</p>
        <h1 className="mt-1 text-2xl font-semibold">Your student records</h1>
        <p className="mt-2 text-sm text-stone-600">Records are always read from your signed-in account.</p>
      </div>
      <div className="space-y-6 p-6 sm:p-8">
        <div className="rounded-xl border border-lime-200 bg-lime-50 p-5">
          <p className="text-sm font-semibold text-teal-950">Outstanding balance</p>
          <p className="mt-2 text-3xl font-semibold text-teal-950">12,500 THB</p>
          <p className="mt-2 text-sm text-teal-900">Due 27 November 2026 · Semester 1/2026</p>
          <span className="mt-4 inline-block rounded-full bg-white px-3 py-1 text-xs font-semibold text-teal-900">From your student record</span>
        </div>
        <div className="border-t border-stone-200 pt-6">
          <p className="font-medium">Try to view another student&apos;s balance</p>
          <form className="mt-3 flex max-w-lg gap-3" onSubmit={checkRecord}>
            <input className="min-w-0 flex-1 rounded-lg border border-stone-300 px-3 py-2 text-sm outline-none focus:border-teal-700" onChange={(event) => setRequestedStudent(event.target.value)} placeholder="Student number" value={requestedStudent} />
            <button className="rounded-lg bg-teal-900 px-4 py-2 text-sm font-semibold text-white hover:bg-teal-800" type="submit">Check</button>
          </form>
          {denied && <div className="mt-4 rounded-lg border border-red-200 bg-red-50 p-4 text-sm text-red-900"><p className="font-semibold">Access denied</p><p className="mt-1">I can only read your own records. Student Services can help with written authorization.</p><p className="mt-2 text-xs">This request was logged as an access attempt for another student.</p></div>}
        </div>
      </div>
    </section>
  );
}

function LibraryPage({ query, onQueryChange }) {
  const [renewed, setRenewed] = useState(false);
  const books = [
    { title: "Database System Concepts", author: "Abraham Silberschatz", call: "QA 76.9 D3 S55", shelf: "Science 2 · Shelf 14", available: true },
    { title: "Fundamentals of Database Systems", author: "Ramez Elmasri", call: "QA 76.9 D3 E45", shelf: "Science 2 · Shelf 15", available: true },
    { title: "Database Design for Mere Mortals", author: "Michael J. Hernandez", call: "QA 76.9 D3 H47", shelf: "Science 2 · Shelf 16", available: false },
  ];
  const visibleBooks = books.filter((book) => !query.trim() || `${book.title} ${book.author}`.toLowerCase().includes(query.toLowerCase()));
  return (
    <section className="rounded-2xl border border-stone-200 bg-white shadow-sm">
      <div className="border-b border-stone-200 px-6 py-5">
        <p className="text-sm font-semibold text-teal-800">Student portal · Library</p>
        <h1 className="mt-1 text-2xl font-semibold">Library catalogue</h1>
        <p className="mt-2 text-sm text-stone-600">Search books and manage your current loan.</p>
      </div>
      <div className="p-6 sm:p-8">
        <div className="flex gap-3">
          <input className="min-w-0 flex-1 rounded-lg border border-stone-300 px-4 py-3 text-sm outline-none focus:border-teal-700" onChange={(event) => onQueryChange(event.target.value)} placeholder="Search title, author or subject" value={query} />
          <button className="rounded-lg bg-teal-900 px-4 py-3 text-sm font-semibold text-white hover:bg-teal-800">Search</button>
        </div>
        <p className="mt-6 text-sm font-semibold">{visibleBooks.length} books found <span className="font-normal text-stone-500">· From the library catalogue</span></p>
        <div className="mt-4 grid gap-3">
          {visibleBooks.map((book) => <BookCard book={book} key={book.title} onRenew={() => setRenewed(true)} renewed={renewed} />)}
          {visibleBooks.length === 0 && <p className="rounded-lg bg-stone-50 p-5 text-sm text-stone-600">No books found. Try another search.</p>}
        </div>
      </div>
    </section>
  );
}

function BookCard({ book, onRenew, renewed }) {
  return (
    <article className="rounded-xl border border-stone-200 p-5">
      <div className="flex flex-wrap items-start justify-between gap-3">
        <div><h2 className="font-semibold">{book.title}</h2><p className="mt-1 text-sm text-stone-600">{book.author}</p></div>
        <span className={`rounded-full px-3 py-1 text-xs font-semibold ${book.available ? "bg-lime-100 text-teal-900" : "bg-stone-100 text-stone-600"}`}>{book.available ? "Available" : "Checked out"}</span>
      </div>
      <div className="mt-4 grid gap-2 text-xs text-stone-500 sm:grid-cols-2"><p>Call number: <strong className="text-stone-700">{book.call}</strong></p><p>Shelf: <strong className="text-stone-700">{book.shelf}</strong></p></div>
      {!book.available && <div className="mt-4 flex flex-wrap items-center justify-between gap-3 border-t border-stone-100 pt-4"><p className="text-sm text-stone-600">Due back on 22 October 2026.</p><button className="text-sm font-semibold text-teal-800 hover:text-teal-950">Open catalogue →</button></div>}
      {book.available && renewed && <p className="mt-4 text-sm font-semibold text-teal-800">Loan renewed until 12 November 2026.</p>}
      {book.available && !renewed && <button className="mt-4 text-sm font-semibold text-teal-800 hover:text-teal-950" onClick={onRenew}>Renew loan →</button>}
    </article>
  );
}

function StaffConsole({ activeTab = "Queue" }) {
  const [tab, setTab] = useState(activeTab);
  const tabs = ["Queue", "Requests", "Payments", "Audit log"];
  return (
    <section className="rounded-2xl border border-stone-200 bg-white shadow-sm">
      <div className="border-b border-stone-200 px-6 py-5"><p className="text-sm font-semibold text-teal-800">Staff console</p><h1 className="mt-1 text-2xl font-semibold">Student services queue</h1><p className="mt-2 text-sm text-stone-600">Review conversations, requests and payment slips.</p></div>
      <div className="border-b border-stone-200 px-6 pt-4"><div className="flex flex-wrap gap-2">{tabs.map((item) => <button className={`rounded-lg px-3 py-2 text-sm font-semibold ${tab === item ? "bg-teal-900 text-white" : "text-stone-600 hover:bg-stone-50"}`} key={item} onClick={() => setTab(item)}>{item}</button>)}</div></div>
      <div className="overflow-x-auto p-6">
        {tab === "Queue" && <QueueTable />}
        {tab === "Requests" && <RequestsTable />}
        {tab === "Payments" && <PaymentsTable />}
        {tab === "Audit log" && <AuditTable />}
      </div>
    </section>
  );
}

function QueueTable() {
  return <Table headers={["Type", "Student", "Subject", "State", "Age", "Assignee"]} rows={[["Escalated", "Wai Yan Lynn", "Scholarship deferral", "Needs staff", "12 min", "Unassigned"], ["Request", "Wai Yan Lynn", "Official transcript", "Under review", "1 day", "Siriporn K."], ["Payment", "Wai Yan Lynn", "Tuition slip", "Waiting", "18 min", "Unassigned"]]} />;
}

function RequestsTable() {
  return <Table headers={["Reference", "Student", "Request", "State", "Updated"]} rows={[["REQ-2026-0481", "Wai Yan Lynn", "Official transcript", "Under review", "14 Oct 14:31"], ["REQ-2026-0477", "Nang Ying Noom Lao", "Enrolment certificate", "Ready", "14 Oct 09:12"]]} />;
}

function PaymentsTable() {
  return <Table headers={["Student", "Amount", "Slip", "State", "Received"]} rows={[["Wai Yan Lynn", "12,500 THB", "tuition-slip.jpg", "Waiting", "14 Oct 16:06"], ["Myat Hsu Hnin", "8,000 THB", "payment.png", "Confirmed", "14 Oct 11:20"]]} />;
}

function AuditTable() {
  return <Table headers={["Actor", "Action", "Target", "Timestamp"]} rows={[["Assistant", "Created reservation", "Library Room B2", "14 Oct 13:02"], ["Siriporn K.", "Changed request state", "REQ-2026-0481", "16 Oct 09:12"], ["Staff", "Confirmed payment", "RCP-2026-0813", "15 Oct 09:30"]]} />;
}

function Table({ headers, rows }) {
  return <table className="min-w-full text-left text-sm"><thead><tr className="border-b border-stone-200 text-xs uppercase tracking-wide text-stone-400">{headers.map((header) => <th className="whitespace-nowrap px-4 py-3 font-semibold" key={header}>{header}</th>)}</tr></thead><tbody>{rows.map((row) => <tr className="border-b border-stone-100 last:border-0" key={row.join("-")}>{row.map((cell, index) => <td className={`whitespace-nowrap px-4 py-4 ${index === 0 ? "font-semibold text-teal-950" : "text-stone-600"}`} key={cell}>{cell}</td>)}</tr>)}</tbody></table>;
}

const bookingSlots = [
  { room: "Library Room B2", time: "13:00 to 15:00", capacity: "up to 6 people" },
  { room: "Library Room B4", time: "14:00 to 16:00", capacity: "up to 8 people" },
  { room: "Learning Commons C1", time: "15:00 to 17:00", capacity: "up to 8 people" },
];

function BookingPage({ booking, onBookingChange }) {
  const { people, slot, step } = booking;

  function choosePeople(value) {
    onBookingChange({ step: "slots", people: value, slot: null });
  }

  function chooseSlot(value) {
    onBookingChange({ ...booking, step: "confirm", slot: value });
  }

  function confirmBooking() {
    onBookingChange({ ...booking, step: "complete" });
  }

  function startAgain() {
    onBookingChange({ step: "people", people: null, slot: null });
  }

  return (
    <section className="rounded-2xl border border-stone-200 bg-white shadow-sm">
      <div className="border-b border-stone-200 px-6 py-5">
        <p className="text-sm font-semibold text-teal-800">Student portal · My bookings</p>
        <h1 className="mt-1 text-2xl font-semibold">Book a study room</h1>
        <p className="mt-2 text-sm text-stone-600">Thursday 15 October 2026 · Afternoon availability</p>
      </div>
      <div className="space-y-6 p-6 sm:p-8">
        {step === "people" && (
          <div>
            <p className="font-medium">How many people are in your group?</p>
            <div className="mt-4 grid gap-3 sm:grid-cols-3">
              {[2, 4, 6].map((value) => (
                <button className="rounded-xl border border-stone-200 p-4 text-left hover:border-teal-700 hover:bg-teal-50" key={value} onClick={() => choosePeople(value)}>
                  <span className="block text-lg font-semibold">{value} people</span>
                  <span className="mt-1 block text-sm text-stone-500">Show available rooms</span>
                </button>
              ))}
            </div>
          </div>
        )}

        {step === "slots" && (
          <div>
            <div className="flex flex-wrap items-center justify-between gap-3">
              <p className="font-medium">Three rooms are free for {people} people:</p>
              <button className="text-sm font-semibold text-teal-800 hover:text-teal-950" onClick={startAgain}>Change group size</button>
            </div>
            <div className="mt-4 grid gap-3">
              {bookingSlots.filter((availableSlot) => people <= 6 || availableSlot.room !== "Library Room B2").map((availableSlot) => (
                <button className="flex items-center justify-between rounded-xl border border-stone-200 p-4 text-left hover:border-teal-700 hover:bg-teal-50" key={availableSlot.room} onClick={() => chooseSlot(availableSlot)}>
                  <span>
                    <span className="block font-semibold">{availableSlot.room}</span>
                    <span className="mt-1 block text-sm text-stone-500">{availableSlot.time} · {availableSlot.capacity}</span>
                  </span>
                  <span className="text-sm font-semibold text-teal-800">Select →</span>
                </button>
              ))}
            </div>
          </div>
        )}

        {step === "confirm" && slot && (
          <div>
            <p className="font-medium">Almost done. Check the details below.</p>
            <div className="mt-4 rounded-xl border border-lime-200 bg-lime-50 p-5">
              <p className="font-semibold text-teal-950">{slot.room}</p>
              <p className="mt-2 text-sm text-teal-900">Thursday 15 October 2026 · {slot.time}</p>
              <p className="mt-1 text-sm text-teal-900">{people} seats</p>
              <p className="mt-4 border-t border-lime-200 pt-3 text-xs text-teal-800">The cancellation window closes 2 hours ahead of the start time.</p>
            </div>
            <div className="mt-5 flex flex-wrap gap-3">
              <button className="rounded-lg bg-teal-900 px-4 py-2.5 text-sm font-semibold text-white hover:bg-teal-800" onClick={confirmBooking}>Confirm booking</button>
              <button className="rounded-lg border border-stone-200 px-4 py-2.5 text-sm font-semibold text-stone-700 hover:bg-stone-50" onClick={() => onBookingChange({ ...booking, step: "slots" })}>Change</button>
            </div>
          </div>
        )}

        {step === "complete" && slot && (
          <div className="rounded-xl border border-lime-200 bg-lime-50 p-5">
            <div className="flex items-start gap-3">
              <span className="grid size-8 shrink-0 place-items-center rounded-full bg-lime-300 font-bold text-teal-950">✓</span>
              <div>
                <p className="font-semibold text-teal-950">Booking confirmed</p>
                <p className="mt-2 text-sm leading-6 text-teal-900">{slot.room}, Thursday 15 October, {slot.time}.</p>
                <p className="mt-1 text-sm text-teal-900">I added it to My Bookings and sent a reminder to your linked LINE account.</p>
              </div>
            </div>
            <button className="mt-5 rounded-lg border border-teal-300 bg-white px-4 py-2.5 text-sm font-semibold text-teal-950 hover:bg-teal-50" onClick={startAgain}>Book another room</button>
          </div>
        )}
      </div>
    </section>
  );
}

export default App;

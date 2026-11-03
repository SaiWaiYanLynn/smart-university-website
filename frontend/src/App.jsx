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

function App() {
  const [messages, setMessages] = useState(initialMessages);
  const [draft, setDraft] = useState("");

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
    <main className="min-h-screen bg-slate-50 text-slate-950">
      <header className="border-b border-slate-200 bg-white">
        <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-5 lg:px-10">
          <div className="flex items-center gap-3">
            <div className="grid size-10 place-items-center rounded-xl bg-blue-900 font-bold text-white">
              T
            </div>
            <div>
              <p className="font-semibold tracking-tight">Thales University</p>
              <p className="text-xs text-slate-500">Student services</p>
            </div>
          </div>
          <div className="flex items-center gap-4 text-sm">
            <span className="hidden text-slate-500 sm:inline">Wai Yan Lynn</span>
            <button className="rounded-full bg-slate-100 px-4 py-2 font-medium hover:bg-slate-200">
              Student portal
            </button>
          </div>
        </div>
      </header>

      <div className="mx-auto grid max-w-7xl gap-8 px-6 py-8 lg:grid-cols-[240px_minmax(0,720px)_1fr] lg:px-10">
        <aside className="hidden lg:block">
          <p className="mb-3 text-xs font-semibold uppercase tracking-wider text-slate-400">
            Workspace
          </p>
          <nav className="space-y-1 text-sm">
            <a className="block rounded-lg bg-blue-50 px-3 py-2 font-semibold text-blue-900" href="#">
              Assistant
            </a>
            <a className="block rounded-lg px-3 py-2 text-slate-600 hover:bg-white" href="#">
              My requests
            </a>
            <a className="block rounded-lg px-3 py-2 text-slate-600 hover:bg-white" href="#">
              My bookings
            </a>
            <a className="block rounded-lg px-3 py-2 text-slate-600 hover:bg-white" href="#">
              Library
            </a>
          </nav>
        </aside>

        <section className="overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm">
          <div className="flex items-center justify-between border-b border-slate-200 px-5 py-4">
            <div>
              <h1 className="font-semibold">Student assistant</h1>
              <p className="mt-1 flex items-center gap-1.5 text-xs text-slate-500">
                <span className="size-2 rounded-full bg-emerald-500" />
                Assistant is available
              </p>
            </div>
            <button className="rounded-lg border border-slate-200 px-3 py-2 text-sm text-slate-600 hover:bg-slate-50">
              New chat
            </button>
          </div>

          <div className="space-y-5 bg-slate-50/70 p-5 sm:p-8">
            <div className="text-center text-xs text-slate-400">Wednesday 14 October 2026</div>
            {messages.map((message, index) => (
              <Message key={`${message.type}-${index}`} message={message} />
            ))}
            <div className="max-w-[90%] rounded-xl border border-blue-100 bg-blue-50 p-4 text-sm text-blue-950">
              <p className="font-medium">Would you like me to start with the official transcript?</p>
              <div className="mt-3 flex flex-wrap gap-2">
                <button className="rounded-lg bg-blue-800 px-3 py-2 text-xs font-semibold text-white hover:bg-blue-900">
                  Yes, start with the transcript
                </button>
                <button className="rounded-lg border border-blue-200 bg-white px-3 py-2 text-xs font-semibold text-blue-900 hover:bg-blue-100">
                  Not now
                </button>
              </div>
            </div>
          </div>

          <form className="border-t border-slate-200 p-4" onSubmit={sendMessage}>
            <div className="flex items-center gap-3 rounded-xl border border-slate-300 bg-white p-2 pl-4 focus-within:border-blue-700 focus-within:ring-2 focus-within:ring-blue-100">
              <input
                className="min-w-0 flex-1 bg-transparent text-sm outline-none placeholder:text-slate-400"
                onChange={(event) => setDraft(event.target.value)}
                placeholder="Ask about fees, bookings, documents..."
                value={draft}
              />
              <button className="rounded-lg bg-blue-800 px-4 py-2 text-sm font-semibold text-white hover:bg-blue-900" type="submit">
                Send
              </button>
            </div>
          </form>
        </section>

        <aside className="hidden xl:block">
          <div className="rounded-2xl border border-slate-200 bg-white p-5">
            <p className="text-xs font-semibold uppercase tracking-wider text-slate-400">Your profile</p>
            <p className="mt-4 font-medium">Wai Yan Lynn</p>
            <p className="mt-1 text-sm text-slate-500">67111411 · 3rd year ICT</p>
            <div className="my-5 border-t border-slate-100" />
            <p className="text-sm font-medium">Need something else?</p>
            <p className="mt-1 text-sm leading-6 text-slate-500">
              Ask about your records, room bookings, library books, or requests.
            </p>
          </div>
        </aside>
      </div>
    </main>
  );
}

function Message({ message }) {
  const isUser = message.type === "user";
  return (
    <div className={isUser ? "ml-auto max-w-[85%]" : "max-w-[90%]"}>
      <div
        className={
          isUser
            ? "rounded-xl rounded-br-sm bg-blue-800 px-4 py-3 text-sm leading-6 text-white"
            : "rounded-xl rounded-bl-sm border border-slate-200 bg-white px-4 py-3 text-sm leading-6 text-slate-700"
        }
      >
        <p>{message.text}</p>
        {message.documents && (
          <ol className="mt-2 list-inside list-decimal space-y-1">
            {message.documents.map((document) => (
              <li key={document}>{document}</li>
            ))}
          </ol>
        )}
      </div>
      {!isUser && (
        <div className="mt-2 rounded-lg border-l-4 border-blue-700 bg-white px-3 py-2 text-xs text-slate-600 shadow-sm">
          <p className="font-semibold text-blue-900">Student Handbook 2026 · Section 7.3</p>
          <p className="mt-1">Immigration documents · View source</p>
        </div>
      )}
    </div>
  );
}

export default App;

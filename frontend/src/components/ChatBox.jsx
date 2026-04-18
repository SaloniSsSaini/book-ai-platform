import { useState } from "react";

export default function ChatBox() {
  const [q, setQ] = useState("");
  const [messages, setMessages] = useState([]);

  const ask = async () => {
    if (!q) return;

    try {
      const res = await fetch(`/api/ask/?q=${q}`);
      const data = await res.json();

      setMessages(prev => [
        ...prev,
        {
          q,
          a: data.answer,
          sources: data.sources || []
        }
      ]);

      setQ("");
    } catch (err) {
      console.error("Error:", err);
    }
  };

  return (
    <div className="mb-6">
      <h2 className="text-xl font-semibold mb-2">💬 Ask Questions</h2>

      <input
        value={q}
        onChange={(e) => setQ(e.target.value)}
        className="border p-2 w-full rounded"
        placeholder="Ask about books..."
      />

      <button
        onClick={ask}
        className="bg-blue-500 text-white px-4 py-2 mt-2 rounded"
      >
        Ask
      </button>

      {messages.map((m, i) => (
        <div key={i} className="mt-4 p-3 bg-gray-100 dark:bg-gray-700 rounded">
          <p><b>Q:</b> {m.q}</p>
          <p><b>A:</b> {m.a}</p>

          {m.sources.length > 0 && (
            <div className="text-sm text-gray-500 mt-2">
              {m.sources.map((s, idx) => (
                <div key={idx}>📌 {s}</div>
              ))}
            </div>
          )}
        </div>
      ))}
    </div>
  );
}
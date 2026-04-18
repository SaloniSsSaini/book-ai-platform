import { useEffect, useState } from "react";

export default function BookList() {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    fetch("/api/books/")
      .then(res => res.json())
      .then(setBooks)
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2 className="text-xl font-semibold mb-3">📚 Books</h2>

      <div className="grid grid-cols-2 gap-4">
        {books.map((b) => (
          <div
            key={b.id}
            className="bg-white dark:bg-gray-800 p-4 rounded shadow"
          >
            <h3 className="font-bold">{b.title}</h3>
            <p className="text-sm text-gray-500">{b.author}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
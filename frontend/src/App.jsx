import ChatBox from "./components/ChatBox";
import BookList from "./components/BookList";
import DarkToggle from "./components/DarkToggle";
import { ThemeProvider } from "./context/ThemeContext";

export default function App() {
  return (
    <ThemeProvider>
      <div className="flex h-screen dark:bg-gray-900 dark:text-white">

        <div className="w-64 bg-white dark:bg-gray-800 p-4">
          <h1 className="text-xl font-bold">📚 Book AI</h1>
        </div>

        <div className="flex-1 p-4">
          <div className="flex justify-end mb-3">
            <DarkToggle />
          </div>

          <ChatBox />
          <BookList />
        </div>
      </div>
    </ThemeProvider>
  );
}
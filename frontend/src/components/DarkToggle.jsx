import { useTheme } from "../context/ThemeContext";

export default function DarkToggle() {
  const { dark, setDark } = useTheme();

  return (
    <button
      onClick={() => setDark(!dark)}
      className="px-3 py-1 rounded bg-gray-200 dark:bg-gray-700"
    >
      {dark ? "🌙 Dark" : "☀️ Light"}
    </button>
  );
}
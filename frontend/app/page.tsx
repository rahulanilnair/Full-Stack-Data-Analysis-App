import RevenueTrends from "./chartdetail";

export default function Home() {
  return (
    <div className="min-h-screen p-8 bg-gray-50">
      {/* Title Bar */}
      <header className="w-full bg-blue-600 text-white p-4 text-center text-2xl font-bold">
        Business Intelligence Dashboard
      </header>

      {/* Chart */}
      <div className="mt-8 max-w-4xl mx-auto">
        <RevenueTrends />
      </div>
    </div>
  );
}
import { RevenueTrends, HRAnalysis, Supply_Chain_Analytics, Security_Analytics } from "./chartdetail";
import {Security_Correlation} from './heatmap';
export default function Home() {
  return (
    <div className="min-h-screen bg-cover bg-center bg-no-repeat"
  style={{ backgroundImage: "url('/wp5135746.webp')" }}>
      <header className="w-full bg-gray-800 text-white px-6 py-4 flex items-center shadow-md">
      <img src="/wayne.jpg" alt="Wayne Logo" className="h-12 w-12 object-contain mr-4" />
      <h1 className="text-3xl font-semibold" style={{ fontFamily: 'Georgia, serif' }}>
        Wayne Enterprises – Intelligence and Insight Dashboard
      </h1>
    </header>
       <main className="p-8 max-w-7xl mx-auto">
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 auto-rows-auto">
          <div className="bg-white p-4 rounded-2xl shadow-sm">
            <RevenueTrends />
          </div>
          <div className="bg-white p-3 rounded-2xl shadow-sm">
            <HRAnalysis />
          </div>
          <div className="bg-white rounded-2xl shadow-md">
            <Supply_Chain_Analytics />
          </div>
          <div className="bg-white p-6 rounded-2xl shadow-md col-span-full lg:col-span-3">
          <h2 className="text-2xl font-semibold text-gray-800 mb-4">📰 Community Engagement Reduces Crime and Increases Deployment</h2>
          <p className="text-gray-700 text-base leading-relaxed">
            In a revealing analysis of district-wise security metrics from 2023 and 2024, a strong 
            <span className="font-medium text-blue-700"> inverse relationship </span>
            was observed between <span className="font-semibold">Community Engagement Events</span>, 
            <span className="font-semibold"> Security Incidents</span> and <span className="font-semibold">Wayne Tech Deployment</span>. Districts that hosted more community engagement events reported less incident and more deployment of employees,
            the following year.
          </p>
          <p className="text-gray-700 text-base leading-relaxed mt-3">
            Particularly, neighborhoods with increased <span className="font-semibold">Wayne Tech Deployments</span> alongside 
            engagement initiatives showed the sharpest decline in average monthly incidents. This might have led to increased satisfaction and productivity among employees.
            The heatmap below illustrates these relationships, where darker blue cells indicate 
            stronger negative correlations.
          </p>
          <ul className="list-disc pl-6 mt-3 text-gray-700">
            <li><span className="font-medium">−0.94</span> between <em>Community Engagement Events (2024)</em> and <em>Security Incidents (2024)</em></li>
            <li><span className="font-medium">−0.96</span> between <em>Wayne Tech Deployments (2023)</em> and <em>Security Incidents (2024)</em></li>
            <li><span className="font-medium">1.00</span> between <em>Wayne Tech Deployments (2023)</em> and <em>Community Engagement Events (2024)</em></li>
          </ul>
          <p className="text-gray-700 text-base leading-relaxed mt-3">
            These findings emphasize the power of <span className="font-medium text-green-700">community-driven safety efforts</span> when 
            combined with strategic technological deployments. The below bar graphs provide a much more intuitive idea about the changes in incidents,
            engagement events and deployments over the past year.
          </p>
          <div className="bg-white p-6 rounded-2xl shadow-md col-span-full lg:col-span-3 overflow-auto">
            <Security_Correlation />
          </div>
        </div>
           <div className="bg-white p-4 rounded-2xl shadow-md col-span-full lg:col-span-3">
            <Security_Analytics />
          </div>
        </div>
      </main>
    </div>
  );
}
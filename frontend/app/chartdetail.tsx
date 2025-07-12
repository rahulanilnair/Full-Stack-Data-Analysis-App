'use client'
import { useEffect, useState } from 'react';
import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);
export function RevenueTrends() {
    const [financialData,setFinancialData]=useState(null)
    useEffect(()=>{
        fetch('http://127.0.0.1:8000/financial_data_analysis', { cache: 'no-store' })
      .then(res => res.json())
      .then(data => setFinancialData(data));
    },[]);
    if (!financialData) return <div>Loading...</div>;
    const options = {
    responsive: true,
    plugins: {
      legend: { position: 'top' },
      title: { display: true, text: 'Yearly Revenue Trends' },
    },
    maintainAspectRatio: false,
  };

  return (
    <div className="w-full h-[400px]"> 
      <Bar options={options} data={financialData} />
    </div>
  );
}

export function HRAnalysis() {
    const [hr_data,sethrdata]=useState(null)
    useEffect(()=>{
        fetch('http://127.0.0.1:8000/hr_analytics', { cache: 'no-store' })
      .then(res => res.json())
      .then(data => sethrdata(data));
    },[]);
    if (!hr_data) return <div>Loading...</div>;
    const options = {
    responsive: true,
    plugins: {
      legend: { position: 'top' },
      title: { display: true, text: 'Performance Rating and Satisfaction Scores per Level' },
    },
    maintainAspectRatio: false,
  };

  return (
    <div className="w-full h-[400px]"> 
      <Bar options={options} data={hr_data} />
    </div>
  );
}

export function Supply_Chain_Analytics() {
    const [supply_data,setsupplydata]=useState(null)
    useEffect(()=>{
        fetch('http://127.0.0.1:8000/supply_chain', { cache: 'no-store' })
      .then(res => res.json())
      .then(data => setsupplydata(data));
    },[]);
    if (!supply_data) return <div>Loading...</div>;
   const optionsProd = {
    responsive: true,
    plugins: {
      legend: { position: 'top' },
      title: { display: true, text: 'Production Volume per Product Line' },
    },
  };
  const optionsQual = {
    responsive: true,
    plugins: {
      legend: { position: 'top' },
      title: { display: true, text: 'Quality Score per Product Line' },
    },
  };

  return (
    <>
      <div className="w-full">
        <Bar options={optionsProd} data={supply_data.production} />
      </div>
      <div className="w-full">
        <Bar options={optionsQual} data={supply_data.quality} />
      </div>
    </>
  );
}

export function Security_Analytics() {
    const [security_data,setsecuritydata]=useState(null)
    useEffect(()=>{
        fetch('http://127.0.0.1:8000/security_data', { cache: 'no-store' })
      .then(res => res.json())
      .then(data => setsecuritydata(data));
    },[]);
    if (!security_data) return <div>Loading...</div>;
   const optionsIncidents = {
    responsive: true,
    plugins: {
      legend: { position: 'top' },
      title: { display: true, text: 'Security Incidents per District' },
    },
  };
  const optionsDep = {
    responsive: true,
    plugins: {
      legend: { position: 'top' },
      title: { display: true, text: 'Wayne Tech Deployments per District' },
    },
  };
  const optionsCEE = {
    responsive: true,
    plugins: {
      legend: { position: 'top' },
      title: { display: true, text: 'Community Engagement Events per District' },
    },
  };

  return (
    <>
      <div className="bg-white p-4 rounded-2xl shadow-sm">
        <Bar options={optionsIncidents} data={security_data.security_incidents} />
      </div>
      <div className="bg-white p-4 rounded-2xl shadow-sm">
        <Bar options={optionsDep} data={security_data.deployment} />
      </div>
      <div className="bg-white p-4 rounded-2xl shadow-sm">
        <Bar options={optionsCEE} data={security_data.community_events} />
      </div>
    </>
  );
}

export function Security_Correlation() {
    const [security_corr,setsecuritycorr]=useState(null)
    useEffect(()=>{
        fetch('http://127.0.0.1:8000/security_data_correlation', { cache: 'no-store' })
      .then(res => res.json())
      .then(data => setsecuritycorr(data));
    },[]);
    if (!security_corr) return <div>Loading...</div>;
    const labels = Object.keys(security_corr);
    const z = labels.map(row => labels.map(col => security_corr[row][col]));

    return (
        <Plot
        data={[
            {
            z: z,
            x: labels,
            y: labels,
            type: "heatmap",
            colorscale: "RdBu",
            zmin: -1,
            zmax: 1,
            showscale: true,
            },
        ]}
        layout={{
            title: "Correlation Heatmap: Security Metrics (2023 & 2024)",
            xaxis: { title: "Metric" },
            yaxis: { title: "Metric" },
            height: 500,
            width: 600,
        }}
        />
    );
}

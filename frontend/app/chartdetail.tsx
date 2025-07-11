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
export default function RevenueTrends() {
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
  };

  return <Bar options={options} data={financialData} />;
}
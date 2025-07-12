'use client'
import { useEffect, useState } from 'react';
import dynamic from 'next/dynamic';

const Plot = dynamic(() => import('react-plotly.js'), { ssr: false });

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
            xaxis: { title: "Metric", tickangle: -45, automargin: true },
            yaxis: { title: "Metric", automargin: true },
            margin: { l: 100, r: 50, b: 100, t: 60 },
            autosize: true,
        }}
        useResizeHandler={true}
        style={{ width: "100%", height: "100%" }}
        />
    );
}
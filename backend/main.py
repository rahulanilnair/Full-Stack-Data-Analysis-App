from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import pandas as pd
import numpy as np
import json
import uvicorn

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def root():
    return {'message':'Wayne Data Analysis App Running'}

@app.get('/financial_data_analysis')
async def get_financial_data_analysis():
    try:
        financial_data_df=pd.read_csv('C:/Users/rahul/Downloads/Full-Stack-Data-Analysis-App/backend/data/wayne_financial_data.csv')
        financial_data_df=financial_data_df.fillna(0)
        revenue_trends=financial_data_df.groupby(['Division','Year']).Revenue_M.sum().reset_index()
        revenue_trends=revenue_trends.pivot(index='Division',columns='Year',values='Revenue_M')
        labels=list(revenue_trends.columns)
        colors = [
            'rgba(54, 162, 235, 0.5)',
            'rgba(255, 206, 86, 0.5)',
            'rgba(75, 192, 192, 0.5)',
            'rgba(255, 99, 132, 0.5)',
            'rgba(153, 102, 255, 0.5)'
        ]
        datasets=[]
        for i,division in enumerate(revenue_trends.index):
            datasets.append({
                'label':division,
                'data':revenue_trends.loc[division].tolist(),
                'backgroundColor':colors[i%len(colors)]
            })
        chart_data={
            'labels':labels,
            'datasets':datasets
        }
        return chart_data
        
    except Exception as e:
         raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

    
@app.get('/rd_analysis')
async def get_rd_portfolio_analysis():
    try:
        rdportfolio_data_df=pd.read_csv('C:/Users/rahul/Downloads/Full-Stack-Data-Analysis-App/backend/data/wayne_rd_portfolio.csv')
        rdportfolio_data_df=rdportfolio_data_df.fillna(0)
        rd_json=rdportfolio_data_df.to_json(orient='records')
        return JSONResponse(content=json.loads(rd_json))
    except Exception as e:
         raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")
    
@app.get('/hr_analytics')
async def get_hr_analysis():
    try:
        hr_df=pd.read_csv('C:/Users/rahul/Downloads/Full-Stack-Data-Analysis-App/backend/data/wayne_hr_analytics.csv')
        hr_df=hr_df.fillna(0)
        hr_df_2023 = hr_df[hr_df['Date'].str.contains('2023')]
        hr_df_2024 = hr_df[hr_df['Date'].str.contains('2024')]
        performance_2023=hr_df_2023.groupby(['Department', 'Employee_Level'])['Performance_Rating'].mean().reset_index()
        performance_2024=hr_df_2024.groupby(['Department', 'Employee_Level'])['Performance_Rating'].mean().reset_index()
        ss_2023=hr_df_2023.groupby(['Department', 'Employee_Level'])['Employee_Satisfaction_Score'].mean().reset_index()
        ss_2024=hr_df_2024.groupby(['Department', 'Employee_Level'])['Employee_Satisfaction_Score'].mean().reset_index()
        merged = performance_2023.merge(
        performance_2024, on=['Department', 'Employee_Level'], suffixes=('_2023', '_2024')
    ).merge(
        ss_2023, on=['Department', 'Employee_Level']
    ).merge(
        ss_2024, on=['Department', 'Employee_Level'], suffixes=('_ss_2023', '_ss_2024')
    )
        merged = merged.rename(columns={
            'Performance_Rating_2023': 'Performance_Rating_2023',
            'Performance_Rating_2024': 'Performance_Rating_2024',
            'Employee_Satisfaction_Score_ss_2023': 'Employee_Satisfaction_Score_2023',
            'Employee_Satisfaction_Score_ss_2024': 'Employee_Satisfaction_Score_2024'
        })
        labels = merged.apply(lambda row: f"{row['Department']} - {row['Employee_Level']}", axis=1).tolist()
        colors = [
            'rgba(54, 162, 235, 0.5)',
            'rgba(255, 206, 86, 0.5)',
            'rgba(75, 192, 192, 0.5)',
            'rgba(255, 99, 132, 0.5)'
        ]

        datasets = [
            {
                'label': 'Performance Rating 2023',
                'data': merged['Performance_Rating_2023'].tolist(),
                'backgroundColor': colors[0]
            },
            {
                'label': 'Performance Rating 2024',
                'data': merged['Performance_Rating_2024'].tolist(),
                'backgroundColor': colors[1]
            },
            {
                'label': 'Satisfaction Score 2023',
                'data': merged['Employee_Satisfaction_Score_2023'].tolist(),
                'backgroundColor': colors[2]
            },
            {
                'label': 'Satisfaction Score 2024',
                'data': merged['Employee_Satisfaction_Score_2024'].tolist(),
                'backgroundColor': colors[3]
            }
        ]
        chart_data={
                'labels':labels,
                'datasets':datasets
        }
        return chart_data
    except Exception as e:
         raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")
    
@app.get('/security_data')
async def get_security_analysis():
    try:
        security_df=pd.read_csv('C:/Users/rahul/Downloads/Full-Stack-Data-Analysis-App/backend/data/wayne_security_data.csv')
        security_df=security_df.fillna(0)
        security_df_2023 = security_df[security_df['Date'].str.contains('2023')]
        security_df_2024 = security_df[security_df['Date'].str.contains('2024')]
        incidents_2023=security_df_2023.groupby(['District'])['Security_Incidents'].mean().reset_index()
        incidents_2024=security_df_2024.groupby(['District'])['Security_Incidents'].mean().reset_index()
        ss_2023=security_df_2023.groupby(['District'])['Wayne_Tech_Deployments'].mean().reset_index()
        ss_2024=security_df_2024.groupby(['District'])['Wayne_Tech_Deployments'].mean().reset_index()
        ce_2023=security_df_2023.groupby(['District'])['Community_Engagement_Events'].mean().reset_index()
        ce_2024=security_df_2024.groupby(['District'])['Community_Engagement_Events'].mean().reset_index()
        merged = incidents_2023.merge(
        incidents_2024, on=['District'], suffixes=('_2023', '_2024')
        ).merge(
        ss_2023, on=['District']
        ).merge(
        ss_2024, on=['District'], suffixes=('_ss_2023', '_ss_2024')
        ).merge(ce_2023, on=['District']
        ).merge(
        ce_2024, on=['District'], suffixes=('_ss_2023', '_ss_2024')
        )
        merged = merged.rename(columns={
            'Security_Incidents_2023': 'Security_Incidents_2023',
            'Security_Incidents_2024': 'Security_Incidents_2024',
            'Wayne_Tech_Deployments_ss_2023': 'Wayne_Tech_Deployments_2023',
            'Wayne_Tech_Deployments_ss_2024': 'Wayne_Tech_Deployments_2024',
            'Community_Engagement_Events_ss_2023':'Community_Engagement_Events_2023',
            'Community_Engagement_Events_ss_2024':'Community_Engagement_Events_2024'
        })
        labels = merged.apply(lambda row: f"{row['District']}", axis=1).tolist()
        colors = [
            'rgba(54, 162, 235, 0.5)',
            'rgba(255, 206, 86, 0.5)',
            'rgba(75, 192, 192, 0.5)',
            'rgba(255, 99, 132, 0.5)',
            'rgba(153, 102, 255, 0.5)',   
            'rgba(255, 159, 64, 0.5)'
        ]

        datasets1 = [
                    {
                        'label': 'Security Incidents 2023',
                        'data': merged['Security_Incidents_2023'].tolist(),
                        'backgroundColor': colors[0]
                    },
                    {
                        'label': 'Security Incidents 2024',
                        'data': merged['Security_Incidents_2024'].tolist(),
                        'backgroundColor': colors[1]
                    }]
        datasets2=[
            {
                'label': 'Wayne_Tech_Deployments 2023',
                'data': merged['Wayne_Tech_Deployments_2023'].tolist(),
                'backgroundColor': colors[2]
            },
            {
                'label': 'Wayne_Tech_Deployments 2024',
                'data': merged['Wayne_Tech_Deployments_2024'].tolist(),
                'backgroundColor': colors[3]
            }
        ]
        datasets3=[
            {
                'label': 'Community Engagement Events 2023',
                'data': merged['Community_Engagement_Events_2023'].tolist(),
                'backgroundColor': colors[2]
            },
            {
                'label': 'Community Engagement Events 2024',
                'data': merged['Community_Engagement_Events_2024'].tolist(),
                'backgroundColor': colors[3]
            }
        ]
        chart_data1={
                'labels':labels,
                'datasets':datasets1
        }
        chart_data2={
            'labels':labels,
            'datasets':datasets2
        }
        chart_data3={
                'labels':labels,
                'datasets':datasets3
        }
        return {'security_incidents': chart_data1, 'deployment': chart_data2,'community_events':chart_data3}
    except Exception as e:
         raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")
    
@app.get('/security_data_correlation')
async def get_security_analysis():
    try:
        security_df=pd.read_csv('C:/Users/rahul/Downloads/Full-Stack-Data-Analysis-App/backend/data/wayne_security_data.csv')
        security_df=security_df.fillna(0)
        security_df_2023 = security_df[security_df['Date'].str.contains('2023')]
        security_df_2024 = security_df[security_df['Date'].str.contains('2024')]
        incidents_2023=security_df_2023.groupby(['District'])['Security_Incidents'].mean().reset_index()
        incidents_2024=security_df_2024.groupby(['District'])['Security_Incidents'].mean().reset_index()
        ss_2023=security_df_2023.groupby(['District'])['Wayne_Tech_Deployments'].mean().reset_index()
        ss_2024=security_df_2024.groupby(['District'])['Wayne_Tech_Deployments'].mean().reset_index()
        ce_2023=security_df_2023.groupby(['District'])['Community_Engagement_Events'].mean().reset_index()
        ce_2024=security_df_2024.groupby(['District'])['Community_Engagement_Events'].mean().reset_index()
        merged = incidents_2023.merge(incidents_2024, on='District', suffixes=('_Incidents_2023', '_Incidents_2024')) \
            .merge(ss_2023, on='District') \
            .merge(ss_2024, on='District', suffixes=('_WTD_2023', '_WTD_2024')) \
            .merge(ce_2023, on='District') \
            .merge(ce_2024, on='District', suffixes=('_CEE_2023', '_CEE_2024'))
        merged = merged.rename(columns={
            'Security_Incidents_2023': 'Security_Incidents_2023',
            'Security_Incidents_2024': 'Security_Incidents_2024',
            'Wayne_Tech_Deployments_ss_2023': 'Wayne_Tech_Deployments_2023',
            'Wayne_Tech_Deployments_ss_2024': 'Wayne_Tech_Deployments_2024',
            'Community_Engagement_Events_ss_2023':'Community_Engagement_Events_2023',
            'Community_Engagement_Events_ss_2024':'Community_Engagement_Events_2024'
        })
        numerical = merged.drop(columns=['District'])
        corr = numerical.corr().round(2)
        return corr.to_dict()
    except Exception as e:
         raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")
    
@app.get('/supply_chain')
async def get_supply_chain_analysis():
    try:
        supply_chain_df=pd.read_csv('C:/Users/rahul/Downloads/Full-Stack-Data-Analysis-App/backend/data/wayne_supply_chain.csv')
        supply_chain_df=supply_chain_df.fillna(0)
        supply_chain_df_2023 = supply_chain_df[supply_chain_df['Date'].str.contains('2023')]
        supply_chain_df_2024 = supply_chain_df[supply_chain_df['Date'].str.contains('2024')]
        productivity_2023=supply_chain_df_2023.groupby(['Product_Line'])['Monthly_Production_Volume'].mean().reset_index()
        productivity_2024=supply_chain_df_2024.groupby(['Product_Line'])['Monthly_Production_Volume'].mean().reset_index()
        ss_2023=supply_chain_df_2023.groupby(['Product_Line'])['Quality_Score_Pct'].mean().reset_index()
        ss_2024=supply_chain_df_2024.groupby(['Product_Line'])['Quality_Score_Pct'].mean().reset_index()
        merged = productivity_2023.merge(
        productivity_2024, on=['Product_Line'], suffixes=('_2023', '_2024')
        ).merge(
        ss_2023, on=['Product_Line']
        ).merge(
        ss_2024, on=['Product_Line'], suffixes=('_ss_2023', '_ss_2024')
        )
        merged = merged.rename(columns={
            'Monthly_Production_Volume_2023': 'Monthly_Production_Volume_2023',
            'Monthly_Production_Volume_2024': 'Monthly_Production_Volume_2024',
            'Quality_Score_Pct_ss_2023': 'Quality_Score_Pct_2023',
            'Quality_Score_Pct_ss_2024': 'Quality_Score_Pct_2024'
        })
        labels = merged.apply(lambda row: f"{row['Product_Line']}", axis=1).tolist()
        colors = [
            'rgba(54, 162, 235, 0.5)',
            'rgba(255, 206, 86, 0.5)',
            'rgba(75, 192, 192, 0.5)',
            'rgba(255, 99, 132, 0.5)'
        ]

        datasets1 = [
            {
                'label': 'Production Volume 2023',
                'data': merged['Monthly_Production_Volume_2023'].tolist(),
                'backgroundColor': colors[0]
            },
            {
                'label': 'Production Volume 2024',
                'data': merged['Monthly_Production_Volume_2024'].tolist(),
                'backgroundColor': colors[1]
            }]
        datasets2=[
            {
                'label': 'Quality_Score 2023',
                'data': merged['Quality_Score_Pct_2023'].tolist(),
                'backgroundColor': colors[2]
            },
            {
                'label': 'Quality_Score 2024',
                'data': merged['Quality_Score_Pct_2024'].tolist(),
                'backgroundColor': colors[3]
            }
        ]
        chart_data1={
                'labels':labels,
                'datasets':datasets1
        }
        chart_data2={
            'labels':labels,
            'datasets':datasets2
        }
        return {'production': chart_data1, 'quality': chart_data2}
    except Exception as e:
         raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

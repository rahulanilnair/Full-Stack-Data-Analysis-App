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
        labels=list(performance_2023.columns)
        colors = [
            'rgba(54, 162, 235, 0.5)',
            'rgba(255, 206, 86, 0.5)',
            'rgba(75, 192, 192, 0.5)',
            'rgba(255, 99, 132, 0.5)',
            'rgba(153, 102, 255, 0.5)'
        ]
        l_list=[performance_2023,performance_2024,ss_2023,ss_2024]
        datasets=[]
        for i in l_list:
            for j,department in enumerate(i.index):
                datasets.append({
                    'label':department,
                    'data':j.loc[department].tolist(),
                    'backgroundColor':colors[j%len(colors)]
                })
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
        security_json=security_df.to_json(orient='records')
        return JSONResponse(content=json.loads(security_json))
    except Exception as e:
         raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")
    
@app.get('/supply_chain')
async def get_supply_chain_analysis():
    try:
        supply_chain_df=pd.read_csv('C:/Users/rahul/Downloads/Full-Stack-Data-Analysis-App/backend/data/wayne_supply_chain.csv')
        supply_chain_df=supply_chain_df.fillna(0)
        supply_chain_json=supply_chain_df.to_json(orient='records')
        return JSONResponse(content=json.loads(supply_chain_json))
    except Exception as e:
         raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

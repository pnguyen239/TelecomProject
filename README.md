# TelecomProject
Saskatchewan Telecom Market Analysis and Performance Dashboard
**Overview**
This project delivers a comprehensive Power BI dashboard for analyzing the telecommunications market in Saskatchewan, Canada. It integrates plan pricing, customer usage data, market share, and 5G adoption trends to provide actionable insights for stakeholders. The dashboard supports real-time business metrics, forecasting, and strategic decision-making to optimize plan offerings and network investments.

**Features**
Interactive Power BI dashboard visualizing KPIs including ARPU, market share, 5G and 5G+ adoption rates, and plan utilization.
Dynamic charts showing plan price vs. data allowance, monthly usage trends, and customer segmentation by provider.
Advanced data modeling with SQL and DAX calculations to aggregate, cleanse, and analyze multi-source data.
Integration of external market benchmarks from CRTC, IBISWorld, and SaskTel for data validation.
User-friendly slicers for filtering by providers, plan types, customer segments, and date ranges.
Key insights on premium plan growth potential and seasonal data consumption patterns.

**Getting Started
**Prerequisites
Power BI Desktop (latest version recommended)
SQL Server or equivalent RDBMS for querying and data preparation
Access to telecom customer and plan usage dataset (synthetic or real)

**Installation and Setup
**
Clone this repository:

bash
git clone https://github.com/yourusername/Sask-Telecom-Market-Analysis.git
Open the solution files in Power BI Desktop.
Connect to the data sources or import provided dataset CSVs.
Review and configure data model relationships as needed.
Refresh the dataset to load updated information.

**Data Sources
**
Synthetic data encompasses customer usage, plan subscriptions, and provider info.

External benchmarking data from reputable sources, including:
CRTC Canadian Telecommunications Market Report
IBISWorld Industry Reports
SaskTel Annual and Quarterly Reports

**Project Structure
**
/data - Contains cleaned data extracts and query scripts.

/reports - Power BI .pbix files and report templates.

/docs - Supporting documentation and source references.

/sql - SQL scripts used for data extraction and modeling.

**Technologies Used
**
Power BI Desktop for visualization and dashboard creation.
SQL (Oracle 19c, MS SQL Server) for data querying and transformation.
DAX for calculation of KPIs and dynamic metrics.
Microsoft Excel and Power Query for data preparation.

**Key Learnings and Outcomes
**
Successfully integrated fragmented telecom usage and plan data for comprehensive market analysis.
Built metrics revealing a 23% growth opportunity in premium plans via ARPU and adoption modeling.
Delivered decision-support tools enabling more precise forecasting and network investment planning.
Gained experience validating synthetic data against external market sources for accuracy.

**Future Enhancements
**
Incorporate predictive analytics and machine learning for churn risk and customer segmentation.
Expand geographic scope to include neighboring provinces or national telecom data.
Enhance real-time data integration with APIs from telecom providers.
Develop mobile-friendly reports for on-the-go access by executives.

# Eco395m-Army-Ants
## Goal of the Analysis
The goal of this project is to provide an overview of data science related jobs in Texas, California, and New York. Data science is a fascinating, thriving, and well-paid field. Data scientists are needed in practically every domain: business, finance, science, health, and the public sector. According to our career placement report, many alumni choose to work in data related filed. Therefore, this project intends to provide some information for econ students to help prepared themselves and find satisfying jobs.
## Methodology
This program mainly uses quantitive method to analysis the data science job market. The raw data comes from the Indeed website, and then it uses data crawling to get job descriptions of data science from indeed. After cleaning and reorganizing these raw data by pandas, six columns including job id, job title, company name, location, salary, and job rating are generated, and then plots and figures are created to visualize the relationships between the salary and location, the salary and industries, and etc. by matplotlib.
## Limitations
This project has three limitations: ambiguous classification, limited period, and opaque soft skill identification. For the job title classification, this project only selects specific jobs by filtering key words such as 'data scientist' and 'data analyst'. However, data related jobs may have various names but having the similar job descriptions, and this hiring information be ignored, which leads to incomplete data collection. Secondly, Indeed only preserves the data in the past 30 days, so this project is unable to make a time series analysis like the growth rate of the data science related jobs, or to make predictions for the future data science job market by using historic data. Besides, the soft skill identification sometimes could be hard. For example, some jobs require 'good communication skills', 'leadership', and so on. These skills are difficult to measure to some extent.
## Extensions
To make the further project be perfect, our team may set a program from now to catch the job information from Indeed every 30 days to prepare for predicting the trend of data science job market. Moreover, according to the exist conclusion, this project intends to provide some useful advice for those economic students who has the willingness to seek data related career. 

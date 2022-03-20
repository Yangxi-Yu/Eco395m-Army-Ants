# Eco395m-Army-Ants
## Group Members
* Yangxi Yu
* Xiaohan Sun
* Shuyan Yue
* Zonghao li
* Chen Tang
* Liming Pang
## Data Source 
The raw data comes from the Indeed website. 
  LINK:
## Goal of the Analysis
The goal of this project is to provide an overview of data science related jobs in Texas, California, and New York. Data science is a fascinating, thriving, and well-paid field. Data scientists are needed in practically every domain: business, finance, science, health, and the public sector. According to our career placement report, many alumni choose to work in data related filed. Therefore, this project intends to provide some information for econ students to help prepared themselves and find satisfying jobs.
## Methodology
This program mainly uses quantitative method to analysis the data science job market. 
* It uses data crawling to get job descriptions of data science from indeed.
* It uses Pandas to clean and reorganize raw data, and then generates a csv with six columns including job id, job title, company name, location, salary, and job rating.
* It uses matplotlib to create plots and figures to visualize the relationships between the data related jobs and skills, locations, companies, industries, and salary.
## Findings

## Limitations
### Data 
This project has four limitations in data resource: limited data quantity, ambiguous classification, limited period, and opaque soft skill identification.
* This project has about 5000 pieces of data in the job list, and only has about 300 pieces of data in the job description. The reason for limited data quantity is that when crawling the data from indeed, too frequent visit will be blocked by the website, so a sleeper is set but increases the time to get data. 
* For the job title classification, this project only selects specific jobs by filtering key words such as 'data scientist' and 'data analyst'. However, data related jobs may have various names but having the similar job descriptions, and this hiring information be ignored, which leads to incomplete data collection. 
* Indeed only preserves the data in the past 30 days, so this project is unable to make a time series analysis like the growth rate of the data science related jobs, or to make predictions for the future data science job market by using historic data. 
* The soft skill identification sometimes could be hard. For example, some jobs require 'good communication skills', 'leadership', and so on. These skills are difficult to measure to some extent.

### Analysis
* When analysing the salary, this project may not consider factors such as local ecnomy, house prices, and taxes. 
* Most posted job vacancies in Indeed are targetd on experienced job seekers, which may be not friendyly to fresh graduates. 

## Extensions
To make the further project be perfect, our team may set a program from now to catch the job information from Indeed every 30 days to prepare for predicting the trend of data science job market. Besides, Moreover, according to the exist conclusion, this project intends to provide some useful advice for those economic students who has the willingness to seek data related career. 

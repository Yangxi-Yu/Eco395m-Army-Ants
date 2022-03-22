# Eco395m-Army-Ants
## Team Army Ants Midterm Project for Python, Data, and Databases
## Group Members
* Yangxi Yu
* Xiaohan Sun
* Shuyan Yue
* Zonghao li
* Chen Tang
* Liming Pang
## Data Source 
The raw data comes from the [Indeed](https://www.indeed.com) website. 
## Goal of the Analysis
The goal of this project is to provide an overview of data science-related jobs in Texas, California, and New York. Data science is a fascinating, thriving, and well-paid field. Data scientists are needed in practically every domain: business, finance, science, health, and the public sector. According to our career placement report, many alumni choose to work in data-related filed. Therefore, this project intends to provide some information for econ students to help prepare themselves and find satisfying jobs.
## Methodology
This program mainly uses the quantitative method to analyze the data science job market.
![Methodology](https://github.com/Yangxi-Yu/Eco395m-Army-Ants/blob/main/figure/Methodology.png)
* It uses data crawling to get job descriptions of data science from indeed.
* It uses Pandas to clean and reorganize raw data and then generates a CSV with six columns including job id, job title, company name, location, salary, and job rating.
* It uses matplotlib to create plots and figures to visualize the relationships between the data related jobs and skills, locations, companies, industries, and salaries.
### 1. Skill & Job

![pie chart](https://github.com/Yangxi-Yu/Eco395m-Army-Ants/blob/main/figure/figure1.png)

![Skill1](https://github.com/Yangxi-Yu/Eco395m-Army-Ants/blob/main/figure/figure1-1.png)

* For data analysts, Excel, SQL are the most required skills, following by Power BI and Tableau. <br />

![Skill2](https://github.com/Yangxi-Yu/Eco395m-Army-Ants/blob/main/figure/figure1-2.png)

* For data engineers, SQL, Cloud are the most required skills, following by Python, AWS and Azure. <br />

![Skill3](https://github.com/Yangxi-Yu/Eco395m-Army-Ants/blob/main/figure/figure1-3.png)

* For data scientists, Python, Cloud are the most required skills, following by Statistics, ML and SQL.

### 2. Location & Job Vacancies
![The Number of Jobs of Each Category in Three States](https://github.com/Yangxi-Yu/Eco395m-Army-Ants/blob/e8e00ded4b6da2bbe58f23e733481bae1539f5dd/figure/figure2.png)

* Overall, California has the highest number of Data jobs posted. Among the three states, Data Analyst has the highest number of jobs posted, with 800 or more, and Data Engineer has the lowest number of jobs.
Specifically, in California, the number of Data Analyst and Data Scientist jobs posted is about the same, at 800 or more.
* New York State has the highest number of Data Analyst jobs, with a large gap between the number of Data Engineer and Data Scientist jobs.The number of Data Engineer jobs posted in the three states is the lowest, at about 200.
* Texas also posted the largest number of Data Analysts, with a large gap with the number of Data Engineer and Data Scientist.
### 3. Company & Job Vacancies
|company_name|job_id|
|------------|------|
|JPMorgan Chase Bank, N.A.|76|
|Visa|56|
|Deloitte|54|
|Amazon.com Services LLC|52|
|Citi|40|
|Google|33|
|KPMG|32|
|IBM|26|
|PRICE WATERHOUSE COOPERS|23|
|WELLS FARGO BANK|22|
|Verizon|22|
|General Motors|21|
|Accenture|21|
|Apple|21|
|Change Healthcare|21|
|Facebook App|21|
|EY|19|
|Capgemini|19|
|SiriusXM|18|
|Walmart|18|

* The table shows the top 20 companies that posted data jobs in California, New York State, and Texas in the last 30 days. Among them, JPMorgan Chase Bank (76), Visa (56), Deloitte (54) are at the top.

![Numbers of Jobs in Each Category Posted by the Top Five Companies](https://github.com/Yangxi-Yu/Eco395m-Army-Ants/blob/e8e00ded4b6da2bbe58f23e733481bae1539f5dd/figure/figure3.png)
* This diagram shows the top 5 companies in terms of the number of job postings for the positions Data Analyst, Data Engineer, and Datra Scientist.
* At JPMorgan Chase Bank and Citi, the job title with the highest demand is Data Analyst.
* At Visa, the job title with the highest demand is Data Engineer.
* At Deloitte, the number of Data Analyst and Data Engineer job postings is similar, ranging from 20-25.
* At Amazon.com Services LLC, the most in-demand position is Data Scientist.

### 4. Industry & Job Vacancies
![Numbers of Jobs in Each Category Posted by the Top Five Industries](https://github.com/Yangxi-Yu/Eco395m-Army-Ants/blob/e8e00ded4b6da2bbe58f23e733481bae1539f5dd/figure/figure4.png)
* This section focuses on the distribution of job numbers in three titles among different industries and the top five industries.
* The total number of jobs in information technology is far ahead of jobs in other industries. Apart from the information industry, health care is eager for employing many jobs for data analysts. 
* There are relatively many jobs for data scientists in financial services, healthcare, and information technology. It makes sense since data scientists may be responsible for evaluating different models and abstracting their commercial values and providing suggestions, which are important for health and financial analyses and model selection among information technology.
### 5. Salary & Job
![Salaries Among Three Categories in Three Locations](https://github.com/Yangxi-Yu/Eco395m-Army-Ants/blob/ae18d189fcc3231153a84e0ea696dfc482399727/figure/figure5-1.png)
* In any of the three job categories, salaries of data engineers and data scientists are significantly higher than data analysts. From the general perspective, workers in California and New York earns more than those in Texas.

![Salaries in Three Locations Between Three Job Categories](https://github.com/Yangxi-Yu/Eco395m-Army-Ants/blob/ae18d189fcc3231153a84e0ea696dfc482399727/figure/figure5-2.png)

* The box plots show the distribution of salaries of different job categories in different states, especially they can show the discrete values.
* Although the average salary of data analysts is lower than the other two, there are several working opportunities to earn quite high, about 250000.
* The average salary of data engineers is high and there are also several workers earning very high, so earnings of data engineers are very high, which may mean that this job needs relatively high ability.
* The distribution of salary of data scientists is relatively narrower than the other two, which may mean this job type provides steady work.


## Limitations
### Data 
This project has four limitations in data resource: limited data quantity, ambiguous classification, limited period, and opaque soft skill identification.
* This project has about 5000 pieces of data in the job list and only has about 300 pieces of data in the job description. The reason for limited data quantity is that when crawling the data from the indeed, too frequent visits will be blocked by the website, so a sleeper is set but increases the time to get data. 
* For the job title classification, this project only selects specific jobs by filtering keywords such as 'data scientist' and 'data analyst'. However, data-related jobs may have various names but have similar job descriptions, and this hiring information is ignored, which leads to incomplete data collection. 
* Indeed only preserves the data in the past 30 days, so this project is unable to make a time series analysis like the growth rate of the data science-related jobs, or to make predictions for the future data science job market by using historic data. 
* Soft skill identification sometimes could be hard. For example, some jobs require 'good communication skills', 'leadership', and so on. These skills are difficult to measure to some extent.

### Analysis
* When analyzing the salary, this project may not consider factors such as the local economy, house prices, and taxes. 
* Most posted job vacancies in Indeed are targeted at experienced job seekers, which may be not friendly to fresh graduates.

## Extensions
* To make the further project perfect, our team may set a program from now to catch the job information from Indeed every 30 days to prepare for predicting the trend of data science job market. 
* Factors that can influence the salaries among differenct regions such as tax, house price may be considered in the future analysis. 
* According to the exist conclusion, this project intends to provide some useful advice for those economic students who has the willingness to seek data related career. 

## Instructions
### 0. Installation
Run `pip install -r requirements.txt`
### 1. Data Scraping
*Please note that the data scraping process may take a lot of time, so, it’s better to skip this section and start reproduce process from section 2 – Data Cleaning.*
#### Output:`data/merged_searched_job_html.csv`
#### Step 1. Get Searched Job List HTML
Run `python3 code/get_searched_job_html.py` and enter position, location, date range, sort to scrape the job list html in the [indeed](https://www.indeed.com/jobs?q=data%20analyst&l=Austin) website. In this project, here are all the files that need to be generated in this step:

|Generate Files|Parameters Entered|
|--------------|------------------|
|Data Analyst_Texas_30.csv|Data Analyst, Texas, 30, date|
|Data Analyst_California_30.csv|Data Analyst, California, 30, date|
|Data Analyst_New York State_30.csv|Data Analyst, New York State, 30, date|
|Data Engineer_Texas_30.csv|Data Engineer, Texas, 30, date|
|Data Engineer_California_30.csv|Data Engineer, California, 30, date|
|Data Engineer_New York State_30.csv|Data Engineer, New York State, 30, date |
|Data Scientist_Texas_30.csv|Data Scientist, Texas, 30, date|
|Data Scientist_California_30.csv|Data Scientist, California, 30, date|
|Data Scientist_New York State_30.csv|Data Scientist, New York State, 30, date|

Run ```python3 code/merge_html_csv.py```, which merges csv files in step 1 and add `Title` and `Location `columns. The output file is `data/merged_searched_job_html.csv`.

*Note: Since the generated file is larger than 100M which cannot be uploaded in GitHub, please run the python script and generate it locally*
#### Step 2. Randomly select 100 jobs in each job titles (Data Analyst, Data Engineer, Data Scientist) and get their job description HTML
Run `python3 code/get_job_des.py` and enter a job title (Data Analyst/ Data Scientist/ Data Engineer) to get the selected 300 job descriptions. Here are all the files that need to be generated:
|Generate Files|Parameters Entered|
|--------------|------------------|
|data/job_des_html_Data Analyst.csv|Data Analyst|
|data/ job_des_html_Data Engineer.cs|Data Engineer|
|data/job_des_html_Data Scientist.csv|Data Scientist|

### 2. Data Cleaning: clean HTML files that generated in section 1-1 to get basic information for each job
#### Output:[job_basic_info.csv](https://github.com/Yangxi-Yu/Eco395m-Army-Ants/blob/main/data/job_basic_info.csv)
Run `python3 html_dataframe.py` to generate [job_basic_info.csv](https://github.com/Yangxi-Yu/Eco395m-Army-Ants/blob/main/data/job_basic_info.csv) with information of job_id, salary, ratings, company, specific location and specific title.
|Generate Files|Parameters Entered|
|--------------|------------------|
|[data/job_basic_info.csv](https://github.com/Yangxi-Yu/Eco395m-Army-Ants/blob/main/data/job_basic_info.csv)|data/merged_searched_job_html.csv|

### 3. Data Cleaning: clean HTML files that generated in section 1-2 to get detailed information for each job
#### Output:[job_desc_info.csv](https://github.com/Yangxi-Yu/Eco395m-Army-Ants/blob/422eb57683d040c95dd25c1106d54b4e39b9e998/data/job_desc_info.csv)
#### Step 1. Get industry information based on the files that generated in section 1-2
Run `python3 code/get_industry.py` and enter a job title (Data Analyst/ Data Scientist/ Data Engineer) to fetch industry information for all the jobs in section 1-2. Here are the output files:
|Generate Files|Parameters Entered|
|--------------|------------------|
|data/job_industry_Data Analyst.csv|Data Analyst|
|data/ job_industry_Data Engineer.csv|Data Engineer|
|data/ job_industry_Data Scientist.csv|Data Scientist|

#### Step 2. Get skill keywords counts based on the files that generated in section 1-2
Run `python3 code/get_skills_list.py` and enter a job title (Data Analyst/ Data Scientist/ Data Engineer) to get skill keywords counts in the job description for all the jobs in section 1-2. Here are the output files:
|Generate Files|Parameters Entered|
|--------------|------------------|
|data/job_skills_counts_Data Analyst.csv|Data Analyst|
|data/job_skills_counts_Data Engineer.csv|Data Engineer|
|data/job_skills_counts_Data Scientist.csv|Data Scientist|

#### Step 3. Merged all the files generated from section 3-1 and 3-2
Run `python3 merge_job_desc_info.py` which helps merge all 6 files in section 3-1 and 3-2. The output file is [data/job_desc_info.csv](https://github.com/Yangxi-Yu/Eco395m-Army-Ants/blob/422eb57683d040c95dd25c1106d54b4e39b9e998/data/job_desc_info.csv).


### 4. Analyze and visualize cleaned data
Run `python3 analysis_plot.ipynb` and we can get totally 7 plots for 5 sections. The detailed instructions for each figure are below.

Figure 1: 
Use pandas, matplot and wordcloud for this section.
1. Create a dataframe showing number of skills among three job titles.
(1) Create a dataframe by setting Title as an index.
(2) Modify it and create a new dataframe containing the rows of skills and the columns of job types.
2. Draw three pie plots showing the top 10 skills for each of the three job titles.
(1) Make pie plot of top 10 skills for data analysts: 
(i) Select the 'Data Analyst' column and create a new dataframe.
(ii) Sort skill numbers and select the top 10 skills.
(iii) Draw a pie plot for that modified dataframe.
(2) Make pie plot of top 10 skills for data engineers:
(i) Select the 'Data Engineers' column and create a new dataframe.
(ii) Sort skill numbers and select the top 10 skills.
(iii) Draw a pie plot for that modified dataframe.
(3) Make pie plot of top 10 skills for data scientists:
(i) Select the 'Data Scientist' column and create a new dataframe. 
(ii) Sort skill numbers and select the top 10 skills.
(iii) Draw a pie plot for that modified dataframe.
3. Display these 3 plots in one row.

Figure 1-1 instruction:
Draw three wordcloud plots showing the frequency of skills for each job titles.
(1) Create a new dataframe showing the number of all skills and sort them, by using dataframe of data analyst before.
(2) Create a wordcloud plot for that dataframe.

The instructions for Figure 1-2 and 1-3 are very similar to these two steps above.

Figure 3-1:
Use pandas for this section.
Count the top 20 companies in terms of number of jobs posted.

Figure 3-2:
Use pandas and matplot for this section.
(a) Select the top 5 companies among the top 20 companies in terms of number of jobs posted as dataframe company_top5.
(b) Count the jobs for each category and company combination as dataframe company_top5_2.
(c) Merge two dataframes: company_top5 left joins company_top5_2 on company_name, choosing three categories.
(d) Make the barplot of the number of jobs in each category posted by the top five companies, horizontalling the bar plot.
(e) Name the plot, x axis and y axis.
(f) Reorder the y axis. In other words, the company with the most job posted should appear first.

Figure 4:
Use pandas and matplot for this section.
(a) Count the top 5 industries in terms of number of jobs posted as dataframe industry_top5.
(b) Count the jobs for each category and industry combination as dataframe industry_top5_2.
(c) Merge two dataframes: industry_top5 left joins industry_top5_2 on industry, choosing three categories.
(d) Make the barplot of the number of jobs in each category posted by the top five industries, horizontalling the bar plot.
(e) Name the plot, x axis and y axis.
(f) Reorder the y axis. In other words, the industry with the most job posted should appear first.

Figure 5-1:
Use pandas, matplot for this section.
(a) Use the modified dataframe to group data by location and job title, and make the salary as mean values, then make a bar plot.
(b) Name the plot, x axis and y axis.

Figure 5-2:
Use pandas, matplot and sns for this section.
(a) Similarly, group data by location, set x axis as job title and y axis as salary, and then make a box plot.
(b) Nmae the plot, x axis and y axis.

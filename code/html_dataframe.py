import pandas as pd
from bs4 import BeautifulSoup
import re
import numpy as np
import os 

OUTPUT_DIR = "data"
input_file = os.path.join(OUTPUT_DIR,"merged_searched_job_html.csv")
output_path = os.path.join(OUTPUT_DIR,"job_basic_info.csv")


def job_rating(card):
    try:
        job_rating=card.find('span','ratingsDisplay').a.text
    except AttributeError:
        job_rating=''
    return job_rating

def job_salary(card):
    try:
        job_salary=card.find(class_='salary-snippet-container').text
    except AttributeError:
        job_salary=''
    if job_salary=='':
        try:
            job_salary=card.find(class_='metadata estimated-salary-container').text
        except AttributeError:
            job_salary=''
    return job_salary

def clean_salary(df_basic):
    resultlist=[]
    mean_list=[]
    for i in df_basic['salary']:
        # print(i)
        # x=i.replace(".", "")
        x=re.sub(",", "", i)
        result=re.findall('[0-9.]+',x)
        time_measure=re.findall('[A-Za-z]+',x)
        result=[float(r) for r in result]
        if 'K' in time_measure:
            result=[1000*r for r in result]
        else:
            result=result
        if 'year' in time_measure:
            result=result
            mean=np.mean(result)
        elif 'month' in x:
            result=[12*i for i in result]
            mean=np.mean(result)         
        else:
            result=[]
            mean=''
        resultlist.append(result)
        mean_list.append(mean)    
    df_basic['salary_scale']=resultlist
    df_basic['salary_mean']=mean_list
    return df_basic

#Set the structual of dataframe
def df_basic(raw):
    df = pd.read_csv(raw)
    df_basic = pd.DataFrame(columns=("job_title","company_name","location_in_detail",'salary','rating','title','location'))
    for index,row in df.iterrows():
        soup=BeautifulSoup(row[1],'html.parser')
        script = soup.find("script", text=lambda text: text and "var jobKeysWithInfo" in text).text
        cards=soup.find_all('div','job_seen_beacon')
        result=[[card.h2.text,card.find("div",'heading6').contents[0].text,card.find('div','companyLocation').text,
                job_salary(card),job_rating(card)] for card in cards]
        """Add salary """
        [result[i].append(row[2]) for i in range(len(result))]
        """Add location """
        [result[i].append(row[3]) for i in range(len(result))]
        for r in range(len(result)):
            df_basic=df_basic.append(pd.Series(result[r], index = ["job_title","company_name","location_in_detail",'salary','rating','title','location']), ignore_index=True)
        """return into dataframe with order"""
        df_basic=df_basic[["job_title","company_name","location_in_detail",'salary','rating','title','location']]
        '''clean salary '''
        df_basic=clean_salary(df_basic)
        '''output result.csv'''
        df_basic.to_csv(output_path,index=False, encoding='utf-8')
    return df_basic

if __name__ == "__main__":
    df=df_basic(input_file)
import pandas as pd
from bs4 import BeautifulSoup
import re
import requests
import numpy as np
import time
import os

def get_cmp_name():
    '''Return a dataframe that list all jid and company name'''
    input_file = os.path.join("data", "job_des_html.csv")
    df_job_des_html = pd.read_csv(input_file)
    jid_cmp_dic = {}
    for row in range(len(df_job_des_html) - 1):
        html = BeautifulSoup(df_job_des_html['HTML'][row],'html.parser') # need to check whether it can run. in test file it is html = df_test['HTML'][row]
        jid = df_job_des_html['jid'][row]
        cmp_names = html.find_all("div", "icl-u-lg-mr--sm icl-u-xs-mr--xs")
        for cmp_name in cmp_names:
            if cmp_name.text != "":
                jid_cmp_dic[jid] =  cmp_name.text
    
    jid_cmp_df = pd.DataFrame(list(jid_cmp_dic.items()))
    jid_cmp_df.columns = ['jid', 'Company_name']
    
    return jid_cmp_df


def sleeper(min_sleep_sec, max_sleep_sec):
    '''Give a random sleep time between min_sleep_sec and max_sleep_sec.'''
    time_splits = np.linspace(min_sleep_sec, max_sleep_sec, num=60)
    alarm = np.random.choice(time_splits)
    rounding = np.random.choice(list(range(2,6)))
    
    return time.sleep(round(alarm, rounding))


def get_com_industry(jid_cmp_df):
    '''Return a dataframe that list all company name and industry'''
    industry = {}
    for row in range(len(jid_cmp_df) - 1):
        company = jid_cmp_df['Company_name'][row]
        
        com_url = 'https://www.indeed.com/cmp/' + company
        cmp_response=requests.get(cmp_url)
        cmp_html=BeautifulSoup(cmp_response.text,'html.parser')
        cmp_industry = cmp_html.find("li", attrs={"data-testid": "companyInfo-industry"})
        if cmp_industry != None:
            industry_name = cmp_industry.text
            industry[company] = industry_name[8: ]
        else:
            industry[company] = ""
        
        sleeper(10.6666, 105.999)
        
    cmp_industry_df = pd.DataFrame(list(industry.items()))
    cmp_industry_df.columns = ['Company_name', 'Industry']
    
    return cmp_industry_df



if __name__ == "__main__":

    jid_cmp_df = get_cmp_name()
    cmp_industry_df = get_com_industry(jid_cmp_df)

    output_file = pd.merge(jid_cmp_df, cmp_industry_df, how = 'outer', on = 'Company_name')
    output_path = os.path.join("data", "jid_cmp_industry.csv")
    output_file.to_csv(output_path, index = False)  

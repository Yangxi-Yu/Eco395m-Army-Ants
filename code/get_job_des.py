import pandas as pd
from bs4 import BeautifulSoup
import re
import requests
import numpy as np
import time
import os

def merge_all_files():
    ''' Merge all output files from get_searched_job_html.py, return a dataframe and save it as csv'''
    df_merge = pd.DataFrame(columns=['Page', 'HTML', 'Title', 'Location'])


    file_list = ['Data Analyst_California_30.csv',
                 'Data Analyst_New York State_30.csv',
                 'Data Analyst_Texas_30.csv',
                 'Data Scientist_California_30.csv',
                 'Data Scientist_New York State_30.csv',
                 'Data Scientist_Texas_30.csv',
                 'Data Engineer_California_30.csv',
                 'Data Engineer_New York State_30.csv',
                 'Data Engineer_Texas_30.csv']

  
    for file in file_list:
        file_path = os.path.join("data", file)
        df_file = pd.read_csv(file_path)
        df_file['Title'] = file.split('_')[0]
        df_file['Location'] = file.split('_')[1]
        df_merge = pd.concat([df_merge, df_file])


    df_merge.reset_index()
    
    return df_merge.reset_index()

def get_jid_list(df_merge):
    '''Get and return a dataframe contains jid, location, job title from merged_searched_job_html'''
    find_jid = re.compile(r'(jobKeysWithInfo\[([a-zA-z0-9]{16})\])')
    jid_lo_dic = {}
    jid_title_dic = {}
    
    for row in range(len(df_merge) - 1):
        html = BeautifulSoup(df_merge['HTML'][row],'html.parser')
        script = html.find("script", text=lambda text: text and "var jobKeysWithInfo" in text).text
        for line in script.split('\n'):
            if line.startswith('jobKeysWithInfo'):
                if find_jid.search(line.replace("'", "")):
                    jid = find_jid.search(line.replace("'", "")).group(2)
                    
                    jid_lo_dic[jid] = df_merge['Location'][row]
                    jid_title_dic[jid] = df_merge['Title'][row]
                    
    jid_lo_df = pd.DataFrame(list(jid_lo_dic.items()))
    jid_lo_df.columns = ['jid', 'Location']
    
    jid_title_df = pd.DataFrame(list(jid_title_dic.items()))
    jid_title_df.columns = ['jid', 'Title']
    
    jid_lo_title_df = pd.merge(jid_lo_df, jid_title_df, how = 'inner', on = 'jid')
    

    return jid_lo_title_df



def select_300_job_postings():
    '''Return a dataframe that randomly select 100 job postings in 3 different job(DA,DS,DE).'''

    df_da = jid_lo_title_df.loc[jid_lo_title_df['Title'] == 'Data Analyst'].sample(n = 100)
    df_ds = jid_lo_title_df.loc[jid_lo_title_df['Title'] == 'Data Scientist'].sample(n = 100)
    df_de = jid_lo_title_df.loc[jid_lo_title_df['Title'] == 'Data Engineer'].sample(n = 100)
    df_merge_select_300 = pd.concat([df_da, df_ds,df_de])

    return df_merge_select_300.reset_index()



def sleeper(min_sleep_sec, max_sleep_sec): # 10.166, 300.233
    '''Give a random sleep time between min_sleep_sec and max_sleep_sec.'''
    time_splits = np.linspace(min_sleep_sec, max_sleep_sec, num=60)
    alarm = np.random.choice(time_splits)
    rounding = np.random.choice(list(range(2,6)))
    
    return time.sleep(round(alarm, rounding))




def get_job_des_html(df_merge_select_300):
    '''Get every job description from the jid_list, and save it into a csv file.'''
    job_des_html = {}
    for jid in list(df_merge_select_300['jid']):
        job_des_url = 'https://www.indeed.com/viewjob?jk=' + jid
        job_des_response=requests.get(job_des_url)
        job_des_html=BeautifulSoup(job_des_response.text,'html.parser')
        job_des_html[jid] = job_des_html
        
        sleeper(10.9866, 20.99999)
        
    df_job_des_html = pd.DataFrame(list(job_des_html.items()))
    df_job_des_html.columns = ['jid', 'HTML']

    output_path = os.path.join("data", "job_des_html.csv")
    df_job_des_html.to_csv(output_path, index = False)





if __name__ == "__main__":
    df_merge = merge_all_files()
    jid_lo_title_df = get_jid_list(df_merge)    
    df_merge_select_300 = select_300_job_postings()
    df_job_des_html = get_job_des_html(df_merge_select_300)
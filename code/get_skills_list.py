import pandas as pd
from bs4 import BeautifulSoup
import re
import os

JOB_TITLE = input("Please enter a job title (Data Analyst/ Data Scientist/ Data Engineer): ")
INPUT_FILE = "job_des_html_" + JOB_TITLE + ".csv"
OUTPUT_FILE = "job_skills_counts_" + JOB_TITLE + ".csv"
INPUT_PATH = os.path.join("data", INPUT_FILE)
OUTPUT_PATH = os.path.join("data", OUTPUT_FILE)
skill_list = [
    'math',
    'statistics',
    'communication',
    'presentation',
    'collaboration',
    'Python',
    'R',
    'SQL',
    'Java',
    'Stata',
    'Tableau',
    'curiosity',
    'spark',
    'excel',
    'word',
    'powerpoint',
    'BI',
    'ETL',
    'aws',
    'snowflake',
    'writing',
    'reading',
    'cloud',
    'matlab',
    'AI',
    'ML',
    'c',
    'linux',
    'pytorch',
    'NLP',
    'pandas',
    'matplotlib',
    'Hive']

def get_lowercase_skill_list(skill_list):

    cleaned_skill_list = []
    for skill in skill_list:
        cleaned_skill_list.append(skill.lower())
        
    return cleaned_skill_list




def get_job_des_scripts(INPUT_PATH):

    df_job_des_html = pd.read_csv(INPUT_PATH)
    jid_scripts_dict = {}
    
    for row in range(len(df_job_des_html)):
        html = BeautifulSoup(df_job_des_html['HTML'][row],'html.parser')
        script = html.find_all(id = 'jobDescriptionText')
        jid = df_job_des_html['jid'][row]
        jid_scripts_dict[jid] = script

    jid_scripts_df = pd.DataFrame(list(jid_scripts_dict.items()))
    jid_scripts_df.columns = ['jid', 'scripts']

    
    return jid_scripts_df



def job_des_lines(jid_scripts_df):
    '''Generate a datadrame that contains jid and corresponding cleaned jobe description.'''
    job_des_lines_dic = {}

    for row in range(len(jid_scripts_df)):
        script = jid_scripts_df['scripts'][row] 

        cleaned_script_lines = []
        for line in str(script).split('\n'):
            line_pre = re.sub('<', ' ', line)
            line_post = re.sub('>', ' ', line_pre)
            clean_line = re.sub('[^A-Za-z\s]', '', line_post)
            
            cleaned_script_lines.append(clean_line.lower().strip())
        
        
        job_des_lines_dic[jid_scripts_df['jid'][row]] = cleaned_script_lines
    
    job_des_lines_df = pd.DataFrame(list(job_des_lines_dic.items()))
    job_des_lines_df.columns = ['jid', 'cleaned_description']
    

    return job_des_lines_df


def count_job_des_skills(cleaned_skill_list, job_des_lines_df):
    
    
    df = pd.DataFrame(columns = cleaned_skill_list + ['jid'])
    

    for row in range(len(job_des_lines_df)):
  
        cleaned_skill_dict = dict.fromkeys(cleaned_skill_list, 0)


        for line in job_des_lines_df['cleaned_description'][row]:
            for word in line.split():
                if word in cleaned_skill_dict:
                    cleaned_skill_dict[word] = cleaned_skill_dict[word] + 1

        cleaned_skill_df = pd.DataFrame(list(cleaned_skill_dict.items()))
        transpose_cleaned_skill_df = cleaned_skill_df.transpose()
        transpose_cleaned_skill_df.columns = transpose_cleaned_skill_df.iloc[0]
        transpose_cleaned_skill_df = transpose_cleaned_skill_df[1:]
        transpose_cleaned_skill_df['jid'] = job_des_lines_df['jid'][row]

        df = pd.concat([transpose_cleaned_skill_df, df], ignore_index=True, sort=False)
    
    df.to_csv(OUTPUT_PATH, index = False)
    



if __name__ == "__main__":
    cleaned_skill_list = get_lowercase_skill_list(skill_list)
    jid_scripts_df = get_job_des_scripts(INPUT_PATH)
    job_des_lines_df = job_des_lines(jid_scripts_df)
    count_job_des_skills(cleaned_skill_list, job_des_lines_df)
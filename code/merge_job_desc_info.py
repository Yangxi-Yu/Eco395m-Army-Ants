import pandas as pd
import os

JOB_INDUSTRY_FILE_LIST = [
    'job_industry_Data Analyst.csv',
    'job_industry_Data Scientist.csv',
    'job_industry_Data Engineer.csv'
]

JOB_SKILL_FILE_LIST = [
    'job_skills_counts_Data Analyst.csv',
    'job_skills_counts_Data Scientist.csv',
    'job_skills_counts_Data Engineer.csv'
]

OUT_PATH = os.path.join('data', 'job_desc_info.csv')

def get_job_industry_merged_df(JOB_INDUSTRY_FILE_LIST):
    ''' Merge all files from JOB_INDUSTRY_FILE_LIST and generate a new cloumn lists job title, return a dataframe'''
    job_industry_df = pd.DataFrame()

    for file in JOB_INDUSTRY_FILE_LIST:
        file_path = os.path.join('data', file)
        df_file = pd.read_csv(file_path)
        df_file['Title'] = file.split('_')[2].split('.')[0]
        
        job_industry_df = pd.concat([job_industry_df, df_file])

    return job_industry_df


def get_job_skill_merged_df(JOB_SKILL_FILE_LIST):
    ''' Merge all files from JOB_SKILL_FILE_LIST, return a dataframe'''
    job_skill_df = pd.DataFrame()

    for file in JOB_SKILL_FILE_LIST:
        file_path = os.path.join('data', file)
        df_file = pd.read_csv(file_path)

        job_skill_df = pd.concat([job_skill_df, df_file])

    return job_skill_df




if __name__ == '__main__':
    job_industry_df = get_job_industry_merged_df(JOB_INDUSTRY_FILE_LIST)
    job_skill_df = get_job_skill_merged_df(JOB_SKILL_FILE_LIST)
    merged_file = pd.merge(job_industry_df, job_skill_df, how = 'inner', on = 'jid')
    merged_file.to_csv(OUT_PATH, index = False)
import os
import pandas as pd

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
        file_path = os.path.join('data', file)
        df_file = pd.read_csv(file_path)
        df_file['Title'] = file.split('_')[0]
        df_file['Location'] = file.split('_')[1]
        df_merge = pd.concat([df_merge, df_file])


    df_merge.reset_index()

    output_path = os.path.join('data', 'merged_searched_job_html.csv')
    df_merge.to_csv(output_path, index = False)
    
    return df_merge.reset_index()



if __name__ == '__main__':
    merge_all_files()
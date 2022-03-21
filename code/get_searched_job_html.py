import csv
import requests
from bs4 import BeautifulSoup 
import numpy as np 
import time 
import os

OUTPUT_DIR = 'data'


def get_jid_url(position, location, fromage, sort):
    '''Generate a url from position, location, date and sort.'''

    template='https://www.indeed.com/jobs?q={}&l={}&fromage={}&sort={}'
    url=template.format(position, location, fromage, sort)
    
    return url


def sleeper(min_sleep_sec, max_sleep_sec):
    '''Give a random sleep time between min_sleep_sec and max_sleep_sec.'''

    time_splits = np.linspace(min_sleep_sec, max_sleep_sec, num=60)
    alarm = np.random.choice(time_splits)
    rounding = np.random.choice(list(range(2,6)))
    
    return time.sleep(round(alarm, rounding))

def get_searched_job_html():
    '''Find all results that match the 4 search conditions and save the HTML as in a csv file.'''

    position = input('Please enter a position: ')
    location = input('Please enter a location: ')
    fromage = input('Please enter a date range (0 - 30): ')
    sort = input('Please choose date/relevance: ')
    
    page_html_dict = {}
    page_number = 1
    url = get_jid_url(position, location, fromage, sort)
    
    while True:
        response=requests.get(url)
        html=BeautifulSoup(response.text,'html.parser')
        
        page_html_dict[page_number] = html
        print('Page ' + str(page_number) + ' completed')
        
        try:
            url='https://www.indeed.com'+html.find('a',{'aria-label':'Next'}).get('href')
            page_number += 1
            sleeper(10.166, 180.233)
            
        except AttributeError: 
            break
    
    page_html_list = list(page_html_dict.items())
    output_file_name = str(position) + '_' + str(location) + '_' + str(fromage) + '.csv'
    output_file_path = os.path.join(OUTPUT_DIR, output_file_name)
    
    with open(output_file_path, 'w+') as out_file:
        csv_writer = csv.writer(out_file)
        header = ['Page', 'HTML']
        csv_writer.writerow(header)
        csv_writer.writerows(page_html_list)

if __name__ == '__main__':

    get_searched_job_html()
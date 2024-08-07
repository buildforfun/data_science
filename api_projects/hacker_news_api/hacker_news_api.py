import requests
import json 

from operator import itemgetter

'''
Hacker news - a place for people to share info on programming
'''


def api_call(url):
    '''
    Make an API call

    url - url of 
    '''

    r = requests.get(url)
    print("Status code: "+str(r.status_code))

    # Explore the structure of the data
    response_dict = r.json()
    readable_file = 'hn_data.json'
    with open(readable_file, 'w') as f:
        json.dump(response_dict, f, indent=4)


def api_topstories(url):
    '''
    API Top stories
    '''
    r = requests.get(url)
    submission_ids = r.json()
    submission_dicts = []
    for submission_id in submission_ids[:30]:
        # Make a separate API call for each submission
        url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
        r = requests.get(url)
        response_dict = r.json()

        # Build a dictionary for each article
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f'http://news.ycombinator.com/item?id={submission_id}',
            'comments': response_dict
        }
        submission_dicts.append(submission_dict)

    for submission_dict in submission_dicts:
        print('Title: '+ str(submission_dict['title']))
        print('Link: '+ submission_dict['hn_link'])
        print('---')
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'

api_call(url)

url_top_stories = 'https://hacker-news.firebaseio.com/v0/topstories.json'

api_topstories(url_top_stories)
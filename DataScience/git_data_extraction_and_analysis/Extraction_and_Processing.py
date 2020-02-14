# Just try to understand................................but not fully complete

import json
import requests
from pandas.io.json import json_normalize
import pandas as pd
import numpy as np 
import config

import re
import ast
from datetime import datetime
pd.set_option('display.max_columns', 20)
pd.set_option('display.width',1000)
pd.set_option('display.max_colwidth', -1)




# successfully imported modules
print("successfully imported modules")



# this function takes owner and repository name as paremeters
# and returns a list of commits of the owner
# url = api + '/repos/{}/{}/branches?page={}&per_page=100'.format(owner, repo, page_number)

def commits_of_owner(repo, owner, api):
	commits = []
	next = True
	i = 1
	while next == True:
		url = api + '/repos/{}/{}/branches?page={}&per_page=100'.format(owner, repo, i)

		commit_page = gh_session.get(url = url)
		commit_page_list = [dict(item, **{'repo_name':'{}'.format(repo)}) for item in commit_page.json()]
		commit_page_list = [dict(item, **{'owner':'{}'.format(owner)}) for item in commit_page_list]
		
		commits = commits + commit_page_list

		if 'Link' in commit_page.headers:
			if 'rel="next"' not in commit_page.headers['Link']:
				next = False
		i = i + 1
	return commits



# Pandas Dataframe

def commits_dataframe(repo, owner, api):
	commits_list = commits_of_owner(repo, owner, api)
	return pd.json_normalize(commits_list)




# db406386def3f2301226e85a1e5dc5932d00f047

github_api = "https://api.github.com"
gh_session = requests.Session()
# gh_session.auth = (config.GITHUB_USERNAME, config.GITHUB_TOKEN)


# GET /repos/:owner/:repo/commits
# So we can write it as...

# url = github_api + '/repos/apache/spark/commits'
# commits = gh_session.get(url = url)
# commits_json = commits.json()

# print(commits_json)


commits = commits_dataframe('spark', 'apache', github_api)
# print(commits)


commits.info()
# print(commits.info())


# commits['date'] = pd.to_datetime(commits['commit.committer.date'])
# commits['date'] = pd.to_datetime(commits['date'], utc = True)
# commits['commit_date'] = commits['date'].dt.date
# commits['commit_year'] = commits['date'].dt.year 
# commits['commit_hour'] = commits['date'].dt.hour 


commits.head()
# print(commits.head())


print(commits.head())




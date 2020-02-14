
def Commits_Search(repo, owner, api):
	    commits = []
	    next = True
	    i = 1
	    while next == True:
	        url = api + '/repos/{}/{}/commits?page={}&per_page=100'.format(owner, repo, i)
	        commit_pg = gh_session.get(url = url)
	        print(i)

	        commit_pg_list = [dict(item, **{'repo_name':'{}'.format(repo)}) for item in commit_pg.json()]    
        	commit_pg_list = [dict(item, **{'owner':'{}'.format(owner)}) for item in commit_pg_list]


	        commits = commits + commit_pg_list
	        if 'Link' in commit_pg.headers:
	            if 'rel="next"' not in commit_pg.headers['Link']:
	                next = False

	        i = i + 1
	        if i==10:
	        	break
	    return commits


def Commit_Dataframe(repo, owner, api):
    commits_list = Commits_Search(repo, owner, api)
    return pd.json_normalize(commits_list)


try:
	import json
	import requests
	from pandas.io.json import json_normalize
	import pandas as pd
	# by this two line we can see all data of the output table as table size is so much big
	# pd.set_option('display.max_columns', 500)
	# pd.set_option('display.width', 1000)
	import numpy as np
	from datetime import datetime
	import config

except Exception as e:
	print("Some Modules are missing {}".format(e))

else:
	print("Successfully started")

	github_api = "https://api.github.com"
	gh_session = requests.Session()
	

	print("Commit suru hoye gache?")

	commits = Commit_Dataframe('RailwayGuide', 'Sowmik23', github_api)
	print(commits)

	print("successfully we got output")

	# Save data into .csv file
	commits.to_csv('data/sowmik_commits.csv')
	print("\nSuccessfully write the output into csv file")


finally:
	print("\n\nSuccessfully end the program")



# Same to determine the data of branches, pulls, issues just change the url :) and draw plot if you want
# returns all the repository name and links


def branches_of_repo(repo, owner, api):
    # url = "https://github.com/tishat-ahasan?tab=repositories"
    url = api + '{}?tab={}'.format(owner,repo)

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    li = soup.findAll('div', class_='d-inline-block mb-1')
    base_url = "https://github.com/"
    no = []
    Repo = []
    url = []

    for x,i in enumerate(li):
        for a in i.findAll('a'):
            newUrl = base_url + a["href"]
        no.append(x)
        Repo.append(i.text.strip())
        url.append(newUrl)
        # print(x, i.text.strip(), newUrl)
    temp = list(zip(no, Repo, url ))
    df = pd.DataFrame(data=temp, columns=["No", "Repositories", "Url"])

    return df






'''
# repo description query
def repo_description(repo, owner, api):
    # url = "https://github.com/tishat-ahasan?tab=repositories"
    url = api + '{}?tab={}'.format(owner,repo)

    page = requests.get(url)

    # soup returns the whole html content
    soup = BeautifulSoup(page.text, 'html.parser')
    # print(soup)


    # li = soup.findAll('div', class_='col-9 d-inline-block text-gray mb-2 pr-4')
    li = soup.findAll('div', class_='col-10 col-lg-9 d-inline-block')
    base_url = "https://github.com/"

    no = []
    name = []
    des = []
    dat = []
    language = []
    url = []

    # tree = html.fromstring(page.content)
    # tree.xpath('//div[@title="buyer-name"]/text()')

    

    des_box = soup.findAll('div', class_ = 'col-9 d-inline-block text-gray mb-2 pr-4')
    language_box = soup.findAll('div',  )

    for x,i in enumerate(li):
        for a in 
            name.append(i.h3.a.text)
            no.append(x)
            des.append(i.text.strip())
            url.append(newUrl)
        # print(x, i.text.strip(), newUrl)
    temp = list(zip(no, des, url ))
    df = pd.DataFrame(data=temp, columns=["No", "Description", "Url"])

    return df
'''


try:
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd 
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)
    import json
    import requests
    from pandas.io.json import json_normalize
    # by this two line we can see all data of the output table as table size is so much big
    # pd.set_option('display.max_columns', 500)
    # pd.set_option('display.width', 1000)
    import numpy as np
    from datetime import datetime
    import config


except Exception as e:
    print("Some Modules are missing {}".format(e))


else:
    print("Program started successfully ")
    # github_api = "https://api.github.com"
    github_api = "https://github.com/"
    gh_session = requests.Session()
    # gh_session.auth = (config.GITHUB_USERNAME, config.GITHUB_TOKEN)

    
    # print(df)
    # print(df.to_html)  #to save it just add .to_excel/.to_json etc.

    # repos = branches_of_repo('repositories', 'tishat-ahasan', github_api)
    # print(repos)

    description = branches_of_repo('repositories', 'tishat-ahasan', github_api)
    print(description)

    # repos.to_csv('data/repositories.csv')  #it saves the repos data into repositories.cse file
    print("\nSuccessfully write into the csv file")




finally:
    print("\n\nSuccessfully end the program")



# Analysis data
'''
    repos = pd.read_csv('data/repositories.csv', parse_dates=True)


    repos['date'] =  pd.to_datetime(commits['commit.committer.date'])

    commits['commit_date'] = commits['date'].dt.date
    commits['commit_hour'] = commits['date'].dt.hour
    commits['commit_month'] = commits['date'].dt.month
    commits['commit_year'] = commits['date'].dt.year

'''









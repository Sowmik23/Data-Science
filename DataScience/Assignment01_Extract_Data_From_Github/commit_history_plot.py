
try:
	import pandas as pd
	import plotly
	import chart_studio.plotly as py
	import plotly.graph_objs as plot_graph
	from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

except Exception as e:
	print("Some Modules are missing {}".format(e))

else:
	print("Successfully import modules")
	commits = pd.read_csv('data/Sowmik23_RailwayGuide.csv', parse_dates=True)

	#print the commits table data
	# commits.info()  

	commits['date'] =  pd.to_datetime(commits['commit.committer.date'])

	commits['commit_date'] = commits['date'].dt.date
	commits['commit_hour'] = commits['date'].dt.hour
	commits['commit_month'] = commits['date'].dt.month
	commits['commit_year'] = commits['date'].dt.year


	# fix the columns
	commits = commits[['sha', 'author.login', 'commit_date', 'commit_hour', 'commit_month', 'commit_year']]

	# print the table
	# commits.info()

	# head() returns top n column
	commits.head()
	# print(commits.head())

	commits_in_hour = commits.groupby('commit_hour')[['sha']].count()
	#rename the column name
	commits_in_hour = commits_in_hour.rename(columns = {'sha': 'commit_count'})   
	# print(commits_in_hour)


# figure of commits in an hour
	fig = plot_graph.Figure([plot_graph.Bar(
	    x=commits_in_hour.index, 
	    y=commits_in_hour.commit_count, 
	    text=commits_in_hour.commit_count, 
	    textposition='auto')])
	fig.update_layout(
	    title = 'Commits in Hour in RailwayGuide by Sowmik23', 
	    xaxis_title = 'Hour', 
	    yaxis_title = 'Commits Count', 
	    xaxis_tickmode = 'linear')
	fig.show()



	commits.head()
	commits_in_month = commits.groupby('commit_month')[['sha']].count()
	#rename the column name
	commits_in_month= commits_in_month.rename(columns = {'sha': 'commit_count'})   
	# print(commits_in_month)

# figure of commits in a month
	fig = plot_graph.Figure([plot_graph.Bar(
	    x=commits_in_month.index, 
	    y=commits_in_month.commit_count, 
	    text=commits_in_month.commit_count, 
	    textposition='auto')])
	fig.update_layout(
	    title = 'Commits in Month in RailwayGuide by Sowmik23', 
	    xaxis_title = 'Month', 
	    yaxis_title = 'Commits Count', 
	    xaxis_tickmode = 'linear')
	fig.show()


	commits.head()
	commits_in_year = commits.groupby('commit_year')[['sha']].count()
	#rename the column name
	commits_in_year= commits_in_year.rename(columns = {'sha': 'commit_count'})   
	# print(commits_in_month)

# figure of commits in a year
	fig = plot_graph.Figure([plot_graph.Bar(
	    x=commits_in_year.index, 
	    y=commits_in_year.commit_count, 
	    text=commits_in_year.commit_count, 
	    textposition='auto')])
	fig.update_layout(
	    title = 'Commits in Year in RailwayGuide by Sowmik23', 
	    xaxis_title = 'Year', 
	    yaxis_title = 'Commits Count', 
	    xaxis_tickmode = 'linear')
	fig.show()



finally:
	print("\n\nSuccessfully end the program")
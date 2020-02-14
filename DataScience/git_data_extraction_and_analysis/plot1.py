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

	x_position = [2,4,5,6,7,8,9,9,7,6,5,4,3,2,4,5,67,8,8,6,5,3,2,4,6,7]
	y_position = [5,5,4,3,5,7,8,9,0,9,8,6,5,46,7,8,9,0,9,8,6,5,6,7,8,55]




	fig = plot_graph.Figure([plot_graph.Bar(
	    x=x_position,
	    y=y_position,
	    text=y_position, 
	    textposition='auto')])
	fig.update_layout(
	    title = 'Test Plot by Sowmik Sarker', 
	    xaxis_title = 'x postion value', 
	    yaxis_title = 'y postion value', 
	    xaxis_tickmode = 'linear')
	fig.show()



finally:
	print("\n\nSuccessfully end the program")
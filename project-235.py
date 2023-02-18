import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px


dataset = pd.read_csv('projectC234_EPL.csv')
football_club=dataset['Club'].value_counts().head(20)
print("Top 20 Clubs Are:",football_club)
fig=go.Figure(data=[go.Pie(labels=football_club.index,values=football_club.values,hole=0.5)])
fig.show()


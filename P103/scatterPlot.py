import pandas as pd 
import plotly.express as px

df=pd.read_csv("cases.csv")

figure=px.scatter(df, x="Date", y="Cases", color="Country", title="Cases")
figure.show()

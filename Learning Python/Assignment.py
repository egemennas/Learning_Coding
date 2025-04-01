import yfinance as yf
import pandas as pd
import requests as rq
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

#Question 1: Use yfinance to Extract Stock Data
#Reset the index, save, and display the first five rows of the tesla_data dataframe using the head function. Upload a screenshot of the results and code from the beginning of Question 1 to the results below.

Tesla = yf.Ticker("TSLA")
tesla_data = Tesla.history(period="max")
tesla_data.reset_index(inplace= True)
tesla_data.head()

#Question 2: Use Webscraping to Extract Tesla Revenue Data
#Display the last five rows of the tesla_revenue dataframe using the tail function. Upload a screenshot of the results.

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data = rq.get(url).text
soup = BeautifulSoup(html_data,"html.parser")
table = soup.find_all("tbody")[1]
tesla_revenue = {"Date":[],"Revenues":[]}
for row in table.find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text
    tesla_revenue["Date"].append(date)
    tesla_revenue["Revenues"].append(revenue)
tesla_revenue = pd.DataFrame(tesla_revenue,columns=["Date","Revenues"])
tesla_revenue["Revenues"] = tesla_revenue["Revenues"].str.replace(",","").str.replace("$","")
tesla_revenue = tesla_revenue[tesla_revenue['Revenues']!= ""]
tesla_revenue.tail()

#Question 3: Use yfinance to Extract Stock Data
#Reset the index, save, and display the first five rows of the gme_data dataframe using the head function. Upload a screenshot of the results and code from the beginning of Question 1 to the results below.

GameStop = yf.Ticker("1GME")
gme_data = Tesla.history(period="max")
gme_data.reset_index(inplace= True)
gme_data.head()

#Question 4: Use Webscraping to Extract GME Revenue Data
#Display the last five rows of the gme_revenue dataframe using the tail function. Upload a screenshot of the results.

url_gme = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data_gme = rq.get(url_gme).text
soup_gme = BeautifulSoup(html_data_gme,"html.parser")
table_gme = soup_gme.find_all("tbody")[1]
gme_revenue = {"Date":[],"Revenues":[]}
for row_gme in table_gme.find_all("tr"):
    col_gme = row_gme.find_all("td")
    date_gme = col_gme[0].text
    revenue_gme = col_gme[1].text
    gme_revenue["Date"].append(date_gme)
    gme_revenue["Revenues"].append(revenue_gme)
gme_revenue = pd.DataFrame(gme_revenue,columns=["Date","Revenues"])
gme_revenue["Revenues"] = gme_revenue["Revenues"].str.replace(",","").str.replace("$","")
gme_revenue = gme_revenue[gme_revenue['Revenues']!= ""]
gme_revenue.tail()

#Question 5: Plot Tesla Stock Graph
#Use the make_graph function to graph the Tesla Stock Data, also provide a title for the graph.

def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2,cols=1,shared_xaxes=True,subplot_titles=("Historical Share Price", "Historical Revenue"),vertical_spacing=.1)
    stock_data_specific = stock_data[stock_data["Date"]<="2021-06-14"]
    revenue_data_specific = revenue_data[revenue_data["Date"]<="2021-04-30"]
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific["Date"], infer_datetime_format=True), y=stock_data_specific["Close"].astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific["Date"], infer_datetime_format=True), y=revenue_data_specific["Revenues"].astype("float"), name="Revenues"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenues ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,)
    fig.show()
make_graph(tesla_data,tesla_revenue,"Tesla")

#Question 6: Plot GameStop Stock Graph
#Use the make_graph function to graph the GameStop Stock Data, also provide a title for the graph.

make_graph(gme_data,gme_revenue,"GameStop")
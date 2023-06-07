import streamlit as st
import pandas as pd
import numpy as np
#import plotly as px
#import plotly.figure_factory as ff
#from bokeh.plotting import figure
#import matplotlib.pyplot as plt

st.header(':blue[Police Incident Reports from 2018 to 2020 in San Francisco] :police_car: :us:')
st.markdown("_The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution._")
df=pd.read_csv("https://github.com/amyrhuerta/Amairany_a01702927/blob/c010d2d44ddb43506255da1551f75b20e8453543/Police.csv")
st.dataframe(df)

mapa=pd.DataFrame()
mapa['Year']=df["Incident Year"]
mapa['Day']=df["Incident Day of Week"]
mapa['Neighborhoods']=df["Analysis Neighborhoods"]
mapa['Incident Category']=df["Incident Category"]
mapa['Incident Subcategory']=df["Incident Subcategory"]
mapa['Resolution']=df["Resolution"]
mapa['lat']=df["Latitude"]
mapa['lon']=df["Longitude"]

mapa=mapa.dropna()
st.map(mapa.astype(int))

st.write(f'Total Records: {len(df)}')

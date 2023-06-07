import streamlit as st
import pandas as pd
import numpy as np
#import plotly as px
#import plotly.figure_factory as ff
#from bokeh.plotting import figure
#import matplotlib.pyplot as plt

st.header(':blue[Police Incident Reports from 2018 to 2020 in San Francisco] :police_car: :us:')
df=pd.read_csv("Police.csv")

st.markdown("_The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution._")

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

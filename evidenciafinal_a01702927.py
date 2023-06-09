import streamlit as st
import pandas as pd
import numpy as np
import plotly as px
import plotly.figure_factory as ff
from bokeh.plotting import figure
import matplotlib.pyplot as plt

st.header(':green[Police Incident Reports from 2018 to 2020 in] **:black[San Francisco]** :police_car: :us:')
st.markdown("_The data shown below belongs to incident reports in the city of San Francisco, from the year 2018 to 2020, with details from each case such as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution._")
df=pd.read_csv("Police.csv")

mapa=pd.DataFrame()
mapa['Date']=df['Incident Date']
mapa['Day']=df['Incident Day of Week']
mapa['Police District'] = df['Police District']
mapa['Neighborhoods']=df['Analysis Neighborhood']
mapa['Incident Category']=df['Incident Category']
mapa['Incident Subcategory']=df['Incident Subcategory']
mapa['Resolution']=df['Resolution']
mapa['lat']=df['Latitude']
mapa['lon']=df['Longitude']
mapa=mapa.dropna()

subset_data2 = mapa
police_district_input = st.sidebar.multiselect(
'Police District',
mapa.groupby('Police District').count().reset_index()['Police District'].tolist())
if len(police_district_input) > 0:
    subset_data2 = mapa[mapa['Police District'].isin(police_district_input)]

subset_data1 = subset_data2
neighborhood_input = st.sidebar.multiselect(
'Neighborhoods',
subset_data2.groupby('Neighborhoods').count().reset_index()['Neighborhoods'].tolist())
if len(neighborhood_input) > 0:
    subset_data1 = subset_data2[subset_data2['Neighborhoods'].isin(neighborhood_input)]

subset_data = subset_data1
incident_input = st.sidebar.multiselect(
'Incident Category',
subset_data1.groupby('Incident Category').count().reset_index()['Incident Category'].tolist())
if len(incident_input) > 0:
    subset_data = subset_data1[subset_data1['Incident Category'].isin(incident_input)]
            
subset_data
st.caption(f'Total Records: {len(df)}')

st.markdown("_It is important to mention that any police district can answer to any incident, the neighborhood in which it happened is not related to the police district._")
st.divider()

st.markdown("Cirme locations in San Francisco:")
st.map(subset_data)
st.divider()
st.markdown("Crimes ocurred per day of the week:")
st.line_chart(subset_data["Day"].value_counts())
st.divider()
st.markdown("Type of crimes committed:")
st.bar_chart(subset_data["Incident Subcategory"].value_counts())
st.caption('En la gráfica anterior podemos observar el total de los diferentes tipos de crimenes en San Francisco.')
st.divider()

agree=st.button("Click to see Incident Subcategories")
if agree:
  st.markdown("Subtype of crimes commited")
  st.bar_chart(subset_data["Incident Subcategory"].value_counts())

st.markdown("Resolution status")
fig1, ax1=plt.subplots()
labels=subset_data["Resolution"].unique()
ax1.pie(subset_data["Resolution"].value_counts(), labels=labels, autopct="%1.1f%%", startangle=20)
st.pyplot(fig1)

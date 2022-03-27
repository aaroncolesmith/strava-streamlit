# Using GitHub Copilot to help built a quick Streamlit data app

import streamlit as st
import pandas as pd
import plotly_express as px
from datetime import datetime


def main():
    df = pd.read_csv('https://raw.githubusercontent.com/aaroncolesmith/portland_crime_map/main/data.csv')
    df['DATE'] = pd.to_datetime(df['DATE'],utc=True)

    # Convert date from UTC to PST
    df['DATE'] = df['DATE'].dt.tz_convert('US/Pacific')
    df['HOUR'] = df['DATE'].dt.floor('h')
    df['DAY'] = df['DATE'].dt.floor('d')

    st.title('Portland Crime Map')
    st.markdown('This app is a Streamlit dashboard that shows the number of crimes in Portland, Oregon.')

    st.markdown('Updated as of: ' + str(df['DATE'].max().strftime('%Y-%m-%d %H:%M')))

    st.subheader('Crime Counts by Type')
    st.write(df.groupby('CRIME').size().sort_values(ascending=False).head(10))


    # Scatter plot of crime counts by hour
    df['HOUR']=df['DATE'].dt.floor('h')
    fig = px.scatter(df.groupby('HOUR').size().to_frame('COUNT').reset_index(), x='HOUR', y='COUNT')
    st.plotly_chart(fig)


    # Stacked bar chart over by by crime type
    fig = px.bar(df.groupby(['HOUR','CRIME']).size().to_frame('COUNT').reset_index(), x='HOUR', y='COUNT', color='CRIME')
    st.plotly_chart(fig)

    # start_time = st.slider('Start Date', 
    #     df['DATE'].min().to_pydatetime(),
    #     format="MM/DD/YY - hh:mm")

    # d=df.loc[df.DATE >= start_time].groupby(['LATITUDE','LONGITUDE']).agg({'CRIME': lambda x: ', '.join(x),
    #                                        'ID': 'size'}).reset_index()

    d=df.groupby(['LATITUDE','LONGITUDE','ADDRESS']).agg({'CRIME': lambda x: ', '.join(x),
                                            'ID': 'size',
                                            'DATE':'max'}).reset_index()

    d.columns = ['LATITUDE','LONGITUDE','ADDRESS','CRIME','COUNT','LAST_DATE']
    d['LATITUDE'] = pd.to_numeric(d['LATITUDE'])
    d['LONGITUDE'] = pd.to_numeric(d['LONGITUDE'])
    d['CRIME'] = d['CRIME'].str.wrap(50)
    d['CRIME'] = d['CRIME'].apply(lambda x: x.replace('\n', '<br>'))
    d['COUNT_SCALED'] = d['COUNT']*3

    d['LAT_LON'] = d['LATITUDE'].astype('str') + ', ' +  d['LONGITUDE'].astype('str')

    # if the crime desciption is greater than 500 characters, cut it off at 500 characters
    d['CRIME'] = d['CRIME'].apply(lambda x: x[:500] + '...' if len(x) > 500 else x)

    st.subheader('Crime Map')
    fig = px.density_mapbox(d, 
                        lat='LATITUDE', 
                        lon='LONGITUDE', 
                        z='COUNT',
                        radius=50,
                        center=dict(lat=pd.to_numeric(d['LATITUDE'],errors='coerce').mean(), lon=pd.to_numeric(d['LONGITUDE'],errors='coerce').mean()), 
                        zoom=10,
                        opacity=.75, 
                        height=800,
                        hover_data=['CRIME','LAST_DATE'],
                        mapbox_style="stamen-terrain")
    st.plotly_chart(fig)

    fig = px.scatter_mapbox(d, 
                            lat='LATITUDE', 
                            lon='LONGITUDE', 
                            hover_name='CRIME',
                            hover_data=['ADDRESS','COUNT','LAST_DATE'],
                            size='COUNT_SCALED',
                            color_discrete_sequence=["fuchsia"],
                            opacity=.6,
                            size_max=50, 
                            center=dict(lat=pd.to_numeric(d['LATITUDE'],errors='coerce').mean(), lon=pd.to_numeric(d['LONGITUDE'],errors='coerce').mean()),
                            zoom=10, 
                            height=800)
    fig.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig)

    d=df.groupby(['LATITUDE','LONGITUDE','ADDRESS','DAY']).agg({'CRIME': lambda x: ', '.join(x),
                                            'ID': 'size',
                                            'DATE':'max'}).reset_index()
    d.columns = ['LATITUDE','LONGITUDE','ADDRESS','DAY','CRIME','COUNT','LAST_DATE']
    d['LATITUDE'] = pd.to_numeric(d['LATITUDE'])
    d['LONGITUDE'] = pd.to_numeric(d['LONGITUDE'])
    d['CRIME'] = d['CRIME'].str.wrap(50)
    d['CRIME'] = d['CRIME'].apply(lambda x: x.replace('\n', '<br>'))
    d['LAT_LON'] = d['LATITUDE'].astype('str') + ', ' +  d['LONGITUDE'].astype('str')

    # if the crime desciption is greater than 500 characters, cut it off at 500 characters
    d['CRIME'] = d['CRIME'].apply(lambda x: x[:500] + '...' if len(x) > 500 else x)
    d['DAY']=d['DAY'].dt.tz_localize(None).dt.to_pydatetime()
    d['COUNT_SCALED'] = d['COUNT']*5

    d=d.sort_values('DAY',ascending=True).reset_index(drop=True)

    fig = px.density_mapbox(d, 
                            lat='LATITUDE', 
                            lon='LONGITUDE', 
                            hover_name='CRIME',
                            hover_data=['ADDRESS','LAST_DATE','COUNT'],
                            animation_frame=d['DAY'].astype('str'),
                            zoom=10, 
                            center=dict(lat=pd.to_numeric(d['LATITUDE'],errors='coerce').mean(), lon=pd.to_numeric(d['LONGITUDE'],errors='coerce').mean()),
                            height=800)
    fig.update_layout(mapbox_style="stamen-terrain")
    st.plotly_chart(fig)
    
    fig = px.scatter_mapbox(d, 
                            lat='LATITUDE', 
                            lon='LONGITUDE', 
                            hover_name='CRIME',
                            hover_data=['ADDRESS','LAST_DATE','COUNT'],
                            size='COUNT_SCALED',
                            animation_group='LAT_LON',
                            animation_frame=d['DAY'].astype('str'),
                            color_discrete_sequence=["fuchsia"],
                            opacity=.6,
                            center=dict(lat=pd.to_numeric(d['LATITUDE'],errors='coerce').mean(), lon=pd.to_numeric(d['LONGITUDE'],errors='coerce').mean()),
                            size_max=100, 
                            zoom=10, 
                            height=800)
    fig.update_layout(mapbox_style="stamen-terrain")
    st.plotly_chart(fig)




    st.write(df.tail(5))




if __name__ == "__main__":
    #execute
    main()










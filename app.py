# Using GitHub Copilot to help built a quick Streamlit data app

import streamlit as st
import pandas as pd
import plotly_express as px


def main():
    df = pd.read_csv('https://raw.githubusercontent.com/aaroncolesmith/portland_crime_map/main/data.csv')
    df['DATE'] = pd.to_datetime(df['DATE'],utc=True)


    st.write(df.tail(5))

    st.title('Portland Crime Map')
    st.markdown('This app is a Streamlit dashboard that shows the number of crimes in Portland, Oregon.')

    st.markdown('Updated as of: ' + str(df['DATE'].max()))

    st.subheader('Crime Counts by Type')
    st.write(df.groupby('CRIME').size().sort_values(ascending=False).head(10))


    # Scatter plot of crime counts by hour
    # d = df.groupby([pd.Grouper(key='DATE', freq='H')]).size().to_frame('COUNT').reset_index()
    df['HOUR']=df['DATE'].dt.floor('h')
    fig = px.scatter(df.groupby('HOUR').size().to_frame('COUNT').reset_index(), x='HOUR', y='COUNT')
    st.plotly_chart(fig)

    start_time = st.slider('Start Date', df['DATE'].min(), format="MM/DD/YY - hh:mm")
    d=df.loc[df.DATE >= start_time].groupby(['LATITUDE','LONGITUDE']).agg({'CRIME': lambda x: ', '.join(x),
                                           'ID': 'size'}).reset_index()
    d.columns = ['LATITUDE','LONGITUDE','CRIME','COUNT']
    d['CRIME'] = d['CRIME'].str.wrap(50)
    d['CRIME'] = d['CRIME'].apply(lambda x: x.replace('\n', '<br>'))

    d['LAT_LON'] = d['LATITUDE'].astype('str') + ', ' +  d['LONGITUDE'].astype('str')

    # if the crime desciption is greater than 500 characters, cut it off at 500 characters
    d['CRIME'] = d['CRIME'].apply(lambda x: x[:500] + '...' if len(x) > 500 else x)

    fig = px.density_mapbox(d, 
                        lat='LATITUDE', 
                        lon='LONGITUDE', 
                        z='COUNT',
                        radius=50,
                        center=dict(lat=pd.to_numeric(d['LATITUDE'],errors='coerce').mean(), lon=pd.to_numeric(d['LONGITUDE'],errors='coerce').mean()), 
                        zoom=10,
                        opacity=.75, 
                        hover_data=['CRIME'],
                        mapbox_style="stamen-terrain")
    st.plotly_chart(fig)


if __name__ == "__main__":
    #execute
    main()










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

    st.markdown('Updated as of: ' + df['DATE'].max())

    st.subheader('Crime Counts by Type')
    st.write(df.groupby('CRIME').size().sort_values(ascending=False).head(10))


    # Scatter plot of crime counts by hour
    # d = df.groupby([pd.Grouper(key='DATE', freq='H')]).size().to_frame('COUNT').reset_index()
    df['HOUR']=df['DATE'].dt.floor('h')
    fig = px.scatter(df.groupby('HOUR').size().to_frame('COUNT'), x='HOUR', y='COUNT', log_x=True, log_y=True)
    st.plotly_chart(fig)
    
#data.groupby([pd.Grouper(key='DATE', freq='1D')]).size()

if __name__ == "__main__":
    #execute
    main()










# Using GitHub Copilot to help built a quick Streamlit data app

import streamlit as st
import pandas as pd


def main():
    df = pd.read_csv('https://raw.githubusercontent.com/aaroncolesmith/portland_crime_map/main/data.csv')
    df['DATE'] = pd.to_datetime(df['DATE'])
    df['DATE'] = df['DATE'].dt.tz_localize('UTC').dt.tz_convert('US/Pacific')

    st.title('Portland Crime Map')
    st.markdown('This app is a Streamlit dashboard that shows the number of crimes in Portland, Oregon.')

    st.markdown('Updated as of: ' + pd.to_datetime(df['DATE']).max())

    st.subheader('Crime Counts by Type')
    st.write(df.groupby('CRIME').size().sort_values(ascending=False).head(10))

    st.subheader('Crime Counts by Month')
    st.write(df.groupby('MONTH').size().sort_values(ascending=False).head(10))

    st.subheader('Crime Counts by Day of Week')
    st.write(df.groupby('DAY_OF_WEEK').size().sort_values(ascending=False).head(10))

    st.subheader('Crime Counts by Hour')
    st.write(df.groupby('HOUR').size().sort_values(ascending=False).head(10))


if __name__ == "__main__":
    #execute
    main()










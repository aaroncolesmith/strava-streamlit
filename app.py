# Using GitHub Copilot to help built a quick Streamlit data app

import streamlit as st
import pandas as pd


def main():
    df = pd.read_csv('https://raw.githubusercontent.com/aaroncolesmith/portland_crime_map/main/data.csv')
    st.title('Portland Crime Map')
    st.markdown('This app is a Streamlit dashboard that shows the number of crimes in Portland, Oregon.')
    st.markdown('**Data Source:** [https://data.pdx.gov/api/views/v8jb-q3jb/rows.csv](https://data.pdx.gov/api/views/v8jb-q3jb/rows.csv)')
    st.markdown('**Data Description:** [https://data.pdx.gov/api/views/v8jb-q3jb/](https://data.pdx.gov/api/views/v8jb-q3jb/)')
    st.markdown('**Data License:** [https://data.pdx.gov/api/views/v8jb-q3jb/](https://data.pdx.gov/api/views/v8jb-q3jb/)')

    st.subheader('Crime Counts by Type')
    st.write(df.groupby('CRIME').size().sort_values(ascending=False).head(10))

    st.subheader('Crime Counts by Month')
    st.write(df.groupby('MONTH').size().sort_values(ascending=False).head(10))

    st.subheader('Crime Counts by Day of Week')
    st.write(df.groupby('DAY_OF_WEEK').size().sort_values(ascending=False).head(10))

    st.subheader('Crime Counts by Hour')
    st.write(df.groupby('HOUR').size().sort_values(ascending=False).head(10))

    











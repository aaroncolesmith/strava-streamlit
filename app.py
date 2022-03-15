import streamlit as st

PAGES = {
"About": 'about',
"Experience": 'experience',
"Projects": 'projects',
"Bovada": 'bovada'
}

pages = list(PAGES.keys())
query_params = st.experimental_get_query_params()
st.write(query_params)
try:
    query_option = query_params['page'][0]
except:
    st.experimental_set_query_params(page=pages[0])
    query_params = st.experimental_get_query_params()
    query_option = query_params['page'][0]
st.write(query_params)


st.sidebar.title('Navigation')
st.write(query_option)
query_option = query_option.title()
st.write(query_option)
page_selected = st.sidebar.selectbox('Pick option',
                                        pages,
                                        index=pages.index(query_option))


st.write(page_selected)
st.write(PAGES[page_selected])
p = PAGES[page_selected]

if page_selected:
    st.experimental_set_query_params(page=page_selected)


import streamlit as st



PAGES = {
"About": 'about',
"Experience": 'experience',
"Projects": 'projects',
"Bovada": 'bovada'
}

st.sidebar.title('Navigation')
st.experimental_set_query_params(option=options[1])
sel = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[sel]

st.write(page)




# # query params exist
# try:
#     options = ['cat', 'dog', 'mouse', 'bat', 'duck']

#     query_params = st.experimental_get_query_params()
#     query_option = query_params['option'][0] #throws an exception when visiting http://host:port

#     option_selected = st.sidebar.selectbox('Pick option',
#                                             options,
#                                             index=options.index(query_option))
#     if option_selected:
#         st.experimental_set_query_params(option=option_selected)

# # run when query params don't exist. e.g on first launch
# except: # catch exception and set query param to predefined value
#     options = ['cat', 'dog', 'mouse', 'bat', 'duck']
#     st.experimental_set_query_params(option=options[1]) # defaults to dog

#     query_params = st.experimental_get_query_params()
#     query_option = query_params['option'][0]

#     option_selected = st.sidebar.selectbox('Pick option',
#                                             options,
#                                             index=options.index(query_option))
#     if option_selected:
#         st.experimental_set_query_params(option=option_selected)

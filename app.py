import streamlit as st

PAGES = {
"About": 'about',
"Experience": 'experience',
"Projects": 'projects',
"Bovada": 'bovada'
}


# try:
#     options = list(PAGES.keys())
#     query_params=st.experimental_set_query_params()
#     query_option = query_params['option'][0]

#     st.sidebar.title('Navigation')
#     option_selected = st.sidebar.selectbox('Pick option',
#                                             options,
#                                             index=options.index(query_option))

    
#     # sel = st.sidebar.radio("Go to", list(PAGES.keys()))
#     if option_selected:
#         page = PAGES[option_selected]

#         st.write(page)
#         st.experimental_set_query_params(option=option_selected)

# except:

#     options = list(PAGES.keys())
#     st.write(options)
#     st.experimental_set_query_params(option=options[1])


#     query_params = st.experimental_get_query_params()
#     query_option = query_params['option'][0]

#     st.sidebar.title('Navigation')
#     option_selected = st.sidebar.selectbox('Pick option',
#                                             options,
#                                             index=options.index(query_option))

    
#     # sel = st.sidebar.radio("Go to", list(PAGES.keys()))
#     if option_selected:
#         page = PAGES[option_selected]

#         st.write(page)
#         st.experimental_set_query_params(option=option_selected)



# query params exist
# try:
#     # options = ['cat', 'dog', 'mouse', 'bat', 'duck']
#     options=list(PAGES.keys())

#     query_params = st.experimental_get_query_params()
#     query_option = query_params['page'][0] #throws an exception when visiting http://host:port

#     st.sidebar.title('Navigation')
#     option_selected = st.sidebar.selectbox('Pick option',
#                                             options,
#                                             index=options.index(query_option))
#     st.write(option_selected)
#     st.write(PAGES[option_selected])

#     if option_selected:
#         st.experimental_set_query_params(page=option_selected)
#         st.write(option_selected)

# # run when query params don't exist. e.g on first launch
# except: # catch exception and set query param to predefined value
#     # options = ['cat', 'dog', 'mouse', 'bat', 'duck']
#     options = list(PAGES.keys())
#     st.experimental_set_query_params(page=options[0]) # defaults to dog

#     query_params = st.experimental_get_query_params()
#     query_option = query_params['page'][0]

#     st.sidebar.title('Navigation')
#     option_selected = st.sidebar.selectbox('Pick option',
#                                             options,
#                                             index=options.index(query_option))

#     st.write(option_selected)
#     st.write(PAGES[option_selected])
    
#     if option_selected:
#         st.experimental_set_query_params(page=option_selected)
#         st.write(option_selected)





# options = list(PAGES.keys())
# st.experimental_set_query_params(page=options[1]) # defaults to dog

# query_params = st.experimental_get_query_params()
# query_option = query_params['page'][0]

# st.sidebar.title('Navigation')
# option_selected = st.sidebar.selectbox('Pick option',
#                                         options,
#                                         index=options.index(query_option))

# st.write(option_selected)
# st.write(PAGES[option_selected])

# if option_selected:
#     st.experimental_set_query_params(page=option_selected)
#     st.write(option_selected)


pages = list(PAGES.keys())
query_params = st.experimental_get_query_params()
try:
    query_option = query_params['page'][0]
except:
    st.experimental_set_query_params(page=pages[0])
    query_params = st.experimental_get_query_params()
    query_option = query_params['page'][0]
st.write(query_params)


st.sidebar.title('Navigation')
page_selected = st.sidebar.selectbox('Pick option',
                                        pages,
                                        index=pages.index(query_option))


st.write(page_selected)
st.write(title(PAGES[page_selected]))

if page_selected:
    st.experimental_set_query_params(page=page_selected)


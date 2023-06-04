import snscrape.modules.twitter as sntwitter
import pandas as pd
import streamlit as st
import datetime
from time import sleep

tweets_df = pd.DataFrame()
st.sidebar.write("# Twitter data scraping")

with st.sidebar.form("input"):    
    option = st.selectbox('How would you like the data to be searched?',('Keyword', 'Hashtag'))
    word = st.text_input('Please enter a '+option, '')
    start = st.date_input("Select the start date")
    end = st.date_input("Select the end date")
    tweet_c = st.slider('How many tweets to scrape', 0, 1000)
    submit_button = st.form_submit_button(label="Extract data")

if submit_button:
    # Check that text field is not empty
    if not option.strip() and not word.strip() and not start.strip() and not end.strip() and not tweet_c.strip():
        st.error("WARNING: Please fill the form")
    else:
        with st.spinner(text = "Extracting information…"):
            sleep(3)
            st.session_state["option"] = option
            st.session_state["word"] = word
            st.session_state["start"] = start
            st.session_state["end"] = end
            st.session_state["tweet_c"] = tweet_c
            st.write(st.session_state)

tweets_list = []

if "option" not in st.session_state:
    st.session_state["option"] = None
if "word" not in st.session_state:
    st.session_state["word"] = None
if "start" not in st.session_state:
    st.session_state["start"] = None
if "end" not in st.session_state:
    st.session_state["end"] = None
if "tweet_c" not in st.session_state:
    st.session_state["tweet_c"] = None

# # SCRAPE DATA USING TwitterSearchScraper
# if word:
#     try:
#         if option=='Keyword':
#             for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{word} lang:en since:{start} until:{end}').get_items()):
#                 if i>tweet_c-1:
#                     break
#                 tweets_list.append([ tweet.content, tweet.user.username, tweet.replyCount, tweet.retweetCount,tweet.likeCount ])
#             tweets_df = pd.DataFrame(tweets_list, columns=['Content', 'Username', 'ReplyCount', 'RetweetCount', 'LikeCount'])
#         else:
#             for i,tweet in enumerate(sntwitter.TwitterHashtagScraper(f'{word} lang:en since:{start} until:{end}').get_items()):
#                 if i>tweet_c-1:
#                     break            
#                 tweets_list.append([ tweet.content, tweet.user.username, tweet.replyCount, tweet.retweetCount,tweet.likeCount ])
#             tweets_df = pd.DataFrame(tweets_list, columns=['Content', 'Username', 'ReplyCount', 'RetweetCount', 'LikeCount'])
#     except Exception as e:
#         st.error(f"Too many requests, TwitterRateLimit exceeded, please try again after few hours")
#         st.stop()
# else:
#     st.warning(option,' cant be empty', icon="⚠️")


# # DOWNLOAD AS CSV
# @st.cache # IMPORTANT: Cache the conversion to prevent computation on every rerun
# def convert_df(df):    
#     return df.to_csv().encode('utf-8')

# if not tweets_df.empty:
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         csv = convert_df(tweets_df) # CSV
#         c=st.download_button(label="Download data as CSV",data=csv,file_name='Twitter_data.csv',mime='text/csv',)        
#     with col2:    # JSON
#         json_string = tweets_df.to_json(orient ='records')
#         j=st.download_button(label="Download data as JSON",file_name="Twitter_data.json",mime="application/json",data=json_string,)

#     with col3: # SHOW
#         y=st.button('Show Tweets',key=2)

# if c:
#     st.success("The Scraped Data is Downloaded as .CSV file:",icon="✅")  
# if j:
#     st.success("The Scraped Data is Downloaded as .JSON file",icon="✅")     
# if x: # DISPLAY
#     st.success("The Scraped Data is:",icon="✅")
#     st.write(tweets_df)
# if y: # DISPLAY
#     st.balloons()
#     st.success("Tweets Scraped Successfully:",icon="✅")
#     st.write(tweets_df)

    


            


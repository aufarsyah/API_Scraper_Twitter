import json
from flask import Flask, request, jsonify
import pandas as pd
import snscrape.modules.twitter as sntwitter

app = Flask(__name__)

@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('name')
    return jsonify({'data': name})

@app.route('/', methods=['POST'])
def update_record():
    data = request.get_json()
    # return jsonify(data)

    tweets_list = []
    option = data['option']
    word = data['word']
    start = data['start']
    end = data['end']
    tweet_c = data['tweet_c']

    try:
        if option=='Keyword':
            for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{word} since:{start} until:{end}').get_items()):
                if i>tweet_c-1:
                    break
                tweets_list.append([
                    tweet.url, 
                    tweet.date, 
                    tweet.rawContent, 
                    tweet.renderedContent, 
                    tweet.user.username, 
                    tweet.user.displayname, 
                    tweet.user.followersCount, 
                    tweet.user.friendsCount, 
                    tweet.user.created, 
                    tweet.user.protected, 
                    tweet.likeCount, 
                    tweet.retweetCount, 
                    tweet.quoteCount, 
                    tweet.replyCount, 
                    tweet.sourceLabel, 
                    tweet.retweetedTweet, 
                    tweet.quotedTweet, 
                    tweet.mentionedUsers])
            
            return jsonify(tweets_list)
        else:
            for i,tweet in enumerate(sntwitter.TwitterHashtagScraper(f'{word}since:{start} until:{end}').get_items()):
                if i>tweet_c-1:
                    break            
                tweets_list.append([ tweet.content, tweet.user.username, tweet.replyCount, tweet.retweetCount, tweet.likeCount ])

            return jsonify(tweets_list)
    except Exception as e:
        return e

app.run(debug=True)
import json
import tweepy as tw
import mysql.connector as mysql

db = mysql.connect( host = 'localhost', user = 'root', password = input('Enter SQL Password: '))
cursor = db.cursor()

consumer_key = 'ltGVs7SJfXPeLSsNDX1vGt7U1'
consumer_secret = 'qliNjfmDhCIVshMnCoIHvx9bPoA536ObENp7qO1yH5jEKhCezU'
access_token = '14551064-5muN697c57MqrjCix0l6wqUJ24rFWV9sKJ0OHHwMf'
access_token_secret = 'YHVBov1VI1HPcRNY2yj7u3hEdGtbftywtfDRFgSDa1N4G'


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#use r to give raw for twitter api to not mess up
# search_words = r'#NBA'
# date_since = r'2020-01-01'

api = tw.API(auth, wait_on_rate_limit=True)

tweets = api.user_timeline(id=name, count=tweetcount)

# tweets = tw.Cursor(api.search,
                       # q=search_words,
                       # lang="en",
                       # since=date_since).items(1)
for i in tweets:
    text = i._json['text']
    words_in_tweets = text.split()
    for word in words_in_tweets:
        if word.startswith('#') or word.startswith('@'):
            print (word)
            #cursor.execute("INSERT INTO capstone.favorite_artist(tweet_id, keyword, favorite_count) VALUES (i.j_son['id'], word, i._json['favorites_count'])")
            print (i._json['favorites_count'])
            # i._json['favorites_count'])
        
    print(i._json['text'])




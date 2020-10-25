import json
import csv
import tweepy
from textblob import TextBlob
import nltk
from nltk.tokenize import word_tokenize


def search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase):
    # create authentication for accessing Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # initialize Tweepy API
    api = tweepy.API(auth)

    # get the name of the spreadsheet we will write to
    fname = "data"
    string = " "
    # open the spreadsheet we will write to
    with open('%s.csv' % fname, 'w') as file:
        w = csv.writer(file)

        # write header row to spreadsheet
        w.writerow(['timestamp', 'tweet_text', 'username',
                    'all_hashtags', 'followers_count', 'location'])

        # for each tweet matching our hash tags, write relevant info to the spreadsheet
        i = 1
        for tweet in tweepy.Cursor(api.search, q=hashtag_phrase + ' -filter:retweets',
                                   lang="en", tweet_mode='extended').items(5000):
            string = string + tweet.full_text.replace('\n', ' ')
            w.writerow([tweet.created_at, tweet.full_text.replace('\n', ' ').encode('utf-8'),
                        tweet.user.screen_name.encode('utf-8'),
                        [e['text'] for e in tweet._json['entities']['hashtags']], tweet.user.followers_count, tweet.user.location])

            print(i , [tweet.created_at, tweet.full_text.replace('\n', ' ').encode('utf-8'),
                   tweet.user.screen_name.encode('utf-8'),
                   [e['text'] for e in tweet._json['entities']['hashtags']], tweet.user.followers_count, tweet.user.location])
            i = i+1

    print("Done")
    #string = word_tokenize(string)
    # print(nltk.pos_tag(string))


if __name__ == '__main__':
    consumer_key = 'B8UbvqDsG7Dpf4lfGx0uEMObl'
    consumer_secret = 'kymKFIj56unZAWXZF4j9f93Oa89371SMsLbDsJXybrgnmh0eI7'
    access_token = '1944237696-UIpFJBtKBnprVgiZsV2LCd8wtAgkoC0VmxM7qdL'
    access_token_secret = 'OKxS42AbBh8luJ9IoGLqgajzoblwyYdsqJLtGEnDaKSzJ'
    hashtag_phrase = 'geocode:27.466079,89.639010,30km'

    search_for_hashtags(consumer_key, consumer_secret,
                        access_token, access_token_secret, hashtag_phrase)

import re
import csv
import json
from datetime import datetime
from urllib2 import urlopen
from pymongo import MongoClient

STOPWORDS = set(word.strip() for word in open("data/stopwords.txt"))

def save_tweet(tweet, coll, word_to_name):
    """
    Saves a TWEET in the collection COLL if TWEET mentions contains a word
    from WORDS_TO_COMPANY (mostly the names of important companies, but can
    be expanded later to do other stuff). A tweet is defined by Topsy and
    is JSON form.
    """
    text = tweet['content'].lower()
    words = re.findall(r"(\w+)|['\-/()=:;]['\-/()=:;]+", text)
    companies = []
    for word in words:
        if word in STOPWORDS:
            continue
        potential_companies = word_to_name.get(word, None)
        if potential_companies is not None:
            companies += potential_companies
    if companies:
        shit = {
            "date" : datetime.fromtimestamp(tweet['firstpost_date']),
            "content" : tweet['content'],
            "related_to" : companies
        }
        coll.save(shit)

def query(name, num=50, start_date="20060101", end_date="20110101"):
    """
    Queries for old twitter data that matches NAME, up to NUM tweets.
    """
    start_date = datetime.strptime(start_date, "%Y%m%d").strftime("%s")
    end_date = datetime.strptime(end_date, "%Y%m%d").strftime("%s")
    url = 'http://otter.topsy.com/search.json?' + \
        'apikey=WG2JO6FTYF7Q4MV4AYLAAAAAAAB4HI2LRBIQAAAAAAAFQGYA' + \
        '&type=tweet' + \
        '&perpage=' + str(num) + \
        '&allow_lang=en' + \
        '&mintime=' + str(start_date) + \
        '&maxtime=' + str(end_date) + \
        '&q=' + name
    return json.loads(urlopen(url).read(), encoding='utf-8')['response']['list']

def find_tweets(name, coll, word_to_name):
    """
    Similar to 'query(name)', but finds a multitude of tweets and loads
    them into the database.
    """
    start_date = datetime.strptime("20130325", "%Y%m%d")
    end_date = datetime.strptime("20130401", "%Y%m%d")
    while end_date <= datetime.strptime("20130407", "%Y%m%d"):
        qs = query(name, 200, start_date.strftime("%Y%m%d"),
                   end_date.strftime("%Y%m%d"))
        for q in qs:
            save_tweet(q, coll, word_to_name)
        start_date, end_date = end_date, end_date + timedelta(days=31)

if __name__ == "__main__":
    client = MongoClient()
    db = client['tweet-stock']
    tweets = db['tweets']

    with open("data/companylist.csv") as f:
        f.readline()  # skip header
        c = csv.reader(f)
        name_to_ticker = dict()
        ticker_to_name = dict()
        word_to_name = dict()
        stopwords = ["inc","inc.","ltd","ltd.","co","co.", ""]
        for mappings in c:
            name_to_ticker[mappings[1].lower()] = mappings[0]
            ticker_to_name[mappings[0]] = mappings[1].lower()
            namewords = mappings[1].lower().split()
            for word in namewords:
                word = re.sub("[&,!.:()]", "", word)
                if word not in stopwords: 
                    if word not in word_to_name:
                        word_to_name[word] = [mappings[1].lower()]
                    else:
                        word_to_name[word] += [mappings[1].lower()]

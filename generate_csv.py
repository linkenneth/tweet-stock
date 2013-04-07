# Generates a CSV file because Jackie wants it.............
# Format is just like, you know
# "DATE","PRICE","SENTIMENT"
# and sentiment is -100 ~ 100

# Usage is sorta like, generate_csv SYM where SYM is the stock symbol of
# the stock. You know.
import csv
import re
import sys

from evaluator import Sentimentor
from pymongo import MongoClient
from datetime import datetime, timedelta

if __name__ == "__main__":

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

    sym = sys.argv[1]
    s = Sentimentor()
    client = MongoClient()
    db = client['tweet-stock']
    date = datetime.strptime("20090101", "%Y%m%d")
    end_date = datetime.strptime("20120101", "%Y%m%d")
    while date < end_date:
        sents = 0
        tweet_query = { "date" : { "$gte" : date - timedelta(days=2),
                                   "$lt" : date + timedelta(days=2) },
                        "related_to" : ticker_to_name[sym.upper()] }
        price_query = { "date" : date,
                        "sym" : sym }
        for tweet in db.tweets.find(tweet_query):
            sents += s.eval(tweet['content'])
        sents /= float(db.tweets.count())
        price = db.prices.find_one(price_query)
        if price:
            price = price['price']
            print "%s,%.2f,%.10f" % (date.strftime("%Y-%m-%d"), price, sents)
        date += timedelta(days=1)

# Generates a CSV file because Jackie wants it.............
# Format is just like, you know
# "DATE","PRICE","SENTIMENT"
# and sentiment is -100 ~ 100

# Usage is sorta like, generate_csv SYM where SYM is the stock symbol of
# the stock. You know.
import csv
from evaluator import Sentimentor
from pymongo import MongoClient
from datetime import datetime, timedelta

if __name__ == "__main__":
    sym = sys.argv[1]
    s = Sentimentor()
    client = MongoClient()
    db = client['tweet-stock']
    date = datetime.strptime("20090101", "%Y%m%d")
    end_date = datetime.strptime("20120101", "%Y%m%d")
    while date < end_date:
        sents = 0
        next_date = date + timedelta(days=1)
        for tweet in db.tweets.find({ "date" : {
                    "$gte" : date, "$lt" : next_date
                    }}):
            sents += s.eval(tweet['context'])
        sents /= (5 * db.tweets.count())
        price = db.prices.find_one({ "date" : {
                    "$gte" : date, "$lt" : next_date
                    }})
        print date, price, sents
        date += timedelta(days=1)

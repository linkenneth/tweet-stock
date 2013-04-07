import re
import csv
from pymongo import MongoClient

def save(tweet, db, words_to_company):
    """
    Saves a TWEET in the database DB if TWEET mentions contains a word from
    WORDS_TO_COMPANY (mostly the names of important companies, but can be
    expanded later to do other stuff). A tweet is defined by Topsy and is
    JSON form.
    """
    words = re.findall(r"(\w+)|['\-/()=:;]['\-/()=:;]+", tweet)

if __name__ == "__main__":
    client = MongoClient()
    tweets = client['tweets']
    with open("companylist.csv") as f:
        f.readline()  # skip header
        c = csv.reader(f)
        symbol, name = c.next() # [ 'Symbol', 'Name' ]
        companies_to_symbols = dict(csv.reader(f))

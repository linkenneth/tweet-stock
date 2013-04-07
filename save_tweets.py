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
    with open("data/companylist.csv") as f:
        f.readline()  # skip header
        c = csv.reader(f)
        nametoticker = dict()
        tickertoname = dict()
        wordtoname = dict()
        stopwords = ["inc","inc.","ltd","ltd.","co","co."]
        for mappings in c:
            nametoticker[mappings[1].lower()] = mappings[0]
            tickertoname[mappings[0]] = mappings[1].lower()
            namewords = re.split(",? ", mappings[1].lower())
            for word in namewords:
                if word not in stopwords: 
                    if word not in wordtoname:
                        wordtoname[word] = [mappings[1].lower()]
                    else:
                        wordtoname[word] += [mappings[1].lower()]

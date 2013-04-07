import re
import csv
from pymongo import MongoClient

def save(tweet, db, words):
    """
    Saves a TWEET in the database DB if TWEET mentions contains a word from
    WORDS (mostly the names of important companies, but can be expanded
    later to do other stuff).
    """
    tweet = 

if __name__ == "__main__":
    client = MongoClient()
    tweets = client['tweets']
    with open("companylist.csv") as f:
        f.readline()  # skip header
        c = csv.reader(f)
        nametoticker = dict()
        wordtoname = dict()
        for mappings in c:
            nametoticker[string.lower(mappings[1])] = mappings[0]
        for mappings in c:
            namewords = string.split(string.lower(mapping[1]))
            for word in namewords:
                if "inc" not in word: 
                    if word not in wordtoname:
                        wordtoname[word] = [string.lower(mappings[1])]
                    else:
                        wordtoname[word] += [string.lower(mappings[1])]
                        




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
        companies = dict(csv.reader(f))

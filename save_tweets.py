from pymongo import MongoClient

client = MongoClient()
tweets = client['tweets']

def save(tweet, db):
    """
    Saves a TWEET in the database DB if TWEET mentions contains a word from
    WORDS (mostly the names of important companies, but can be expanded
    later to do other stuff).
    """

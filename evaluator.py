# Evaluates sentiments !LOLOLOLOLOL
import train
import re

class Sentimentor:
    def __init__(self, sf='/home/link/code/tweet-stock/data/subjclueslen1-HLTEMNLP05.tff'):
        self.sentiments = train.train(sf)
    def eval(self, text):
        score = 0.0
        r = re.findall("\w+", text)
        for word in r:
            score += self.sentiments.get(word.lower(), 0)
        return score / len(r)

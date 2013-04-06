import nltk

SENTIMENT_FILE = '/home/link/code/tweet-stock/data/subjclueslen1-HLTEMNLP05.tff'
WEIGHTS = {
    "positive" : 1,
    "neutral" : 0,
    "negative" : -1,
    "weaksubj" : 1.0,
    "strongsubj" : 5.0
}

SENTIMENTS = {}  # make default 0?

with open(SENTIMENT_FILE) as f:
    for line in f:
        x = dict(x.split("=") for x in line.split())
        SENTIMENTS[x['word1']] = WEIGHTS[x['type']] * WEIGHTS[x['priorpolarity']]

print SENTIMENTS


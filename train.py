import nltk

def train(sf = '/home/link/code/tweet-stock/data/subjclueslen1-HLTEMNLP05.tff'):
    """
    Trains the system on SF, a sentiment file. A very simple training
    that simply reads off the sentiments from SF, actually.
    """
    weights = {
        "positive" : 1,
        "neutral" : 0.0,
        "negative" : -1.0,
        "weakneg" : -0.5,
        "both" : 0.0,  # no way to distinguish with unigrams
        "weaksubj" : 1.0,
        "strongsubj" : 5.0
        }

    sentiments = {}  # make default 0?

    with open(f) as f:
        for line in f:
            x = dict(x.split("=") for x in line.split())
            sentiments[x['word1']] = weights[x['type']] * \
                weights[x['priorpolarity']]
    
    return sentiments

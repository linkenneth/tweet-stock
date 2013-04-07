from urllib2 import urlopen, quote
import json, time
from pymongo import MongoClient

def sent_query(text):
    text = text.replace('&', "")
    text = text.encode('ascii', 'ignore')
    text = quote(text)
    url = 'https://app.viralheat.com/social/api/sentiment?' + \
        'api_key=pGspS0bjcj5klpfPOA' + \
        '&text="' + text + '"'
    return json.loads(urlopen(url).read(), encoding='utf-8')

def sentimentalize(text, coll):
    if coll.find_one({ 'content' : text}):
        return coll.find_one({ 'content' : text })['sent']
    while True:
        res = sent_query(text)
        if not res['error']:
            s = (1.0 if res['mood'] == u"'positive'" else -1.0) * \
                float(res['prob'])
            coll.save({ 'sent' : s, 'content' : text })
            return s
        time.sleep(1)

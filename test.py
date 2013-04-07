import re
import csv


with open("data/companylist.csv") as f:
        f.readline()  # skip header
        c = csv.reader(f)
        nametoticker = dict()
        wordtoname = dict()
        stopwords = ["inc","inc.","ltd","ltd.","co","co."]
        for mappings in c:
            nametoticker[mappings[1].lower()] = mappings[0]
            namewords = (mappings[1].lower()).split()
            for word in namewords:
                if word not in stopwords : 
                    if word not in wordtoname:
                        wordtoname[word] = [mappings[1].lower()]
                    else:
                        wordtoname[word] += [mappings[1].lower()]
        
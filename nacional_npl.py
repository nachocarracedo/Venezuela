import pandas as pd
import nltk
from collections import Counter

#open csv and fill nan values ""
nacional = pd.read_csv("C:\\Users\\carrai1\\Desktop\\Projects\\Venezuela\\nacional1.csv")
nacional.drop('Unnamed: 0',axis=1,inplace=True)
stemmer = nltk.SnowballStemmer('spanish')
nacional = nacional.fillna(" ")

def stemm_headlines (row):
    words = row["headlines"].split(' ')
	for i in puntuation:
		if i in words:
			
    stem_words = [stemmer.stem(word) for word in words]
    return Counter(stem_words)

def stemm_summaries (row):
    words = row["summaries"].split(' ')
    stem_words = [stemmer.stem(word) for word in words]
    return Counter(stem_words)
    
def stemm_bodies (row):
    words = row["bodies"].split(' ')
    stem_words = [stemmer.stem(word) for word in words]
    return Counter(stem_words)

def remove_puntuation(row)
    
    
nacional["stem_headlines"] = nacional[["headlines"]].apply(stemm_headlines, axis=1)
nacional["stem_summaries"] = nacional[["summaries"]].apply(stemm_summaries, axis=1)
nacional["stem_bodies"] = nacional[["bodies"]].apply(stemm_bodies, axis=1)

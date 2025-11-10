import spacy
import numpy
import pywikibot
import requests
#import wikipediaapi
from spacy.lang.en import English

#required vars for def
user_agent = 'fpsScraper; (https://francisparker.org; ctokunaga2026@francisparker.org)'
#site = pywikibot.Site("en", "wikipedia")
nlp = English()
ruler = nlp.add_pipe("attribute_ruler")
entTokens = []

def tokenEnt(textVal):
    if textVal != "exit":
        doc = nlp(textVal)
        for ent in doc.ents:
            print(ent.text)
            if not ent.text in entTokens :
                insert = []
                if len(ent) > 1:
                    for token in ent:
                        insert.append({"LOWER": token.text})
                pattern = [{"patterns": [[{"TAG": "NNP"}]], "attrs": {"POS": "PROPN"}}, {"pattern": insert, "attrs": {"LEMMA": "namedEntity"}, "index": -1}]
                #ruler.add_patterns(pattern)
                print(pattern)
                entTokens.append(ent.text)
        doc = nlp(" ".join([token.text for token in doc if not token.is_stop]))

        for token in doc:
            print(token.text)
            print(token.pos_)


        newInput = input("Search: ")
        tokenEnt(newInput)


#interface

text = input('Search (Type "exit" to leave): ')

tokenEnt(text)


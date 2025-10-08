import spacy
import numpy
import pywikibot
import requests
import wikipediaapi

#required vars for def
user_agent = 'fpsScraper; (https://francisparker.org; ctokunaga2026@francisparker.org)'
site = pywikibot.Site("en", "wikipedia")
nlp = spacy.load("en_core_web_sm")
ruler = nlp.add_pipe("entity_ruler")
entTokens = []

def tokenEnt(textVal):
    if textVal != "exit":
        doc = nlp(textVal)
        for ent in doc.ents:
            print(ent.text)
            if not ent.text in entTokens :
                pattern = []
                if len(ent) > 1:
                    for token in ent:
                        pattern.append({"LOWER": token.text})
                ruler.add_patterns({"label": "customTok", "pattern": pattern[>=0]})
                entTokens.append(ent.text)
        doc = nlp(" ".join([token.text for token in doc if not token.is_stop]))

        for token in doc:
            print(token.text)
            print(token.dep_)


        newInput = input("Search: ")
        tokenEnt(newInput)


#interface

text = input('Search (Type "exit" to leave): ')

tokenEnt(text)


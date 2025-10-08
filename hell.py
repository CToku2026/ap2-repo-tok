import spacy
import numpy
import pywikibot
import requests
import wikipediaapi

#required vars for def
user_agent = 'studentProjectBot; (https://francisparker.org; ctokunaga2026@francisparker.org)'
site = pywikibot.Site("en", "wikipedia")
nlp = spacy.load("en_core_web_sm")

def progExp(textVal):
    if textVal:
        summary = get_wikipedia_summary(textVal)
        print(f"\nSummary for '{textVal}':\n{summary}\n")
    else:
        print(f"Could not find information for '{textVal}'")

def get_wikipedia_summary(title):
    wiki_wiki = wikipediaapi.Wikipedia(user_agent, 'en')
    page_py = wiki_wiki.page(title)
    if page_py.exists():
        return page_py.summary
    return None

def tokenEnt(textVal):
    if textVal != "exit":
        doc = nlp(textVal)

        for ent in doc.ents:
            progExp(ent.text)

        doc = nlp(" ".join([ent.text for ent in doc if not ent.ent_type_]))

        for token in doc :
            if token.pos_ == "NOUN" or token.pos_ == "PROPN" :
                progExp(token.text)

        newInput = input("Search: ")
        tokenEnt(newInput)


#interface

text = input('Search (Type "exit" to leave): ')

tokenEnt(text)


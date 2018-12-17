import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from nltk.stem import WordNetLemmatizer

## leemos el dataset
import pandas as pd
filename = pd.read_csv("bullying.csv")

## 
def getTweetLabel():
    Tweet = [] ## dataset
    Clase = [] ## etiquetas Bullying/ noBullying
    for row in filename["Tweet"]:
        ## tokenizamos palabras
        words = word_tokenize(row)
        ## eliminar puntuaciones
        clean_words = [word.lower() for word in words if word not in set(string.punctuation)]
        ## eliminar stopwords
        e_wstops = set(stopwords.words('english'))
        characters_to_remove = ["''",'``',"rt","https","’","“","”","\u200b","--","n't","'s","...","//t.c" ]
        clean_words = [word for word in clean_words if word not in e_wstops]
        clean_words = [word for word in clean_words if word not in set(characters_to_remove)]
        ## lematizamos palabras
        wordnet_lemmatizer = WordNetLemmatizer()
        lemma_list = [wordnet_lemmatizer.lemmatize(word) for word in clean_words]
        ## agregamos los tweets lematizados
        Tweet.append(lemma_list)
        
        for row in filename["Text Label"]:
            Clase.append(row)
    return Tweet, Clase

Tweet, Clase = getTweetLabel()

combined = zip(Tweet, Clase)


## creamos un diccionario con nuestra bolsa de palabras
## true si la palabra existe
def bag_of_words(words):
    return dict([word,True] for word in words)
## 'palabra' : true

Res_Data = []
## diccionario por cada tweet
for roots,  lbl in combined:
    #bag_of_words(r)
    Res_Data.append((bag_of_words(roots),lbl))

import random
random.shuffle(Res_Data)
#print(Res_Data[0])

## separamos la data
train_set, test_set = Res_Data[0:746], Res_Data[746:]

import nltk
import collections
from nltk.metrics.scores import (accuracy, precision, recall, f_measure)
from nltk import metrics

refsets = collections.defaultdict(set)
testsets = collections.defaultdict(set)


classifier = nltk.NaiveBayesClassifier.train(train_set)

for i, (feats, label) in enumerate(test_set):
    #print(i, (feats, label))
    refsets[label].add(i)  ## 'bullying' : {1,5,7,...}
    observed = classifier.classify(feats)

    testsets[observed].add(i) ## agrupamos el resultado mendiante la etiqueta y agregamos el indice 
    #print(i, observed)




print('Naive Bayes con Unigramas ')
print('Precision:', nltk.classify.accuracy(classifier, test_set))


nb_classifier = nltk.NaiveBayesClassifier.train(train_set)

nbrefset = collections.defaultdict(set)
nbtestset = collections.defaultdict(set)
 

for i, (feats, label) in enumerate(test_set):
    nbrefset[label].add(i)
    observed = nb_classifier.classify(feats)
    nbtestset[observed].add(i)

print('UnigramNB Rellamada')
print('Rellamada:', recall(nbtestset['Bullying'], nbrefset['Bullying']))
print("-------------------------------------------------")
print("-------------------------------------------------")

#########################################
############## BIGRAMA #################

from  nltk import bigrams, trigrams
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures


combined =zip(Tweet, Clase)


def bad_of_words_bigrams_words(words, score_fn=BigramAssocMeasures.chi_sq, n=200):
    bigram_finder = BigramCollocationFinder.from_words(words)
    bigrams = bigram_finder.nbest(score_fn, n) ## selecciones los n mejores resultados
    return bag_of_words(bigrams)



Res_Data2 = []


## creamos bigramas, y los agrupamos con 
## ('sabe', 'vivi'): True  por cada tweet
for roots, lbl in combined:
    Res_Data2.append((bad_of_words_bigrams_words(roots), lbl))


import random
random.shuffle(Res_Data2)
print(len(Res_Data2))

train_set , test_set = Res_Data2[0:747], Res_Data2[747:]


import nltk
import collections
from nltk.metrics.scores import (accuracy, precision, recall, f_measure)
from nltk import metrics

refsets = collections.defaultdict(set)
testsets = collections.defaultdict(set)

classifier = nltk.NaiveBayesClassifier.train(train_set)


for i, (feats, label) in enumerate(test_set):
    refsets[label]. add(i)
    observed = classifier.classify(feats)
    testsets[observed].add(i)


print('Naive Bayes con Bigramas')
print('Precision:', nltk.classify.accuracy(classifier, test_set))


#classifier.show_most_informative_features(n=10)

print('BigramNB Recall')
print('Recall:', recall(testsets["Bullying"], refsets["Bullying"]))
print("-------------------------------------------------")
print("-------------------------------------------------")


#########################################
############ TRIGRAMAS ##################

from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import TrigramAssocMeasures

def bag_of_trigrams_words(words, score_fn=TrigramAssocMeasures.chi_sq, n=200):
    trigram_finder = TrigramCollocationFinder.from_words(words)  
    trigrams = trigram_finder.nbest(score_fn, n)  
    return bag_of_words(trigrams)

combined = zip(Tweet,Clase)
Res_Data3 = []

for roots, lbl in combined:
    #bag_of_trigrams_words(z)
    Res_Data3.append((bag_of_trigrams_words(roots),lbl))


import random
random.shuffle(Res_Data3)
print(len(Res_Data3))


train_set, test_set = Res_Data3[0:747], Res_Data3[747:]
import nltk
import collections
from nltk.metrics.scores import (accuracy, precision, recall, f_measure)
from nltk import metrics

refsets = collections. defaultdict(set)
testsets = collections.defaultdict(set)

classifier = nltk.NaiveBayesClassifier.train(train_set)


for i, (feats, label) in enumerate(test_set):
    refsets[label].add(i)
    observed = classifier.classify(feats)
    testsets[observed].add(i)


print('Naive Bayes con Trigramas ')
print('Precision:', nltk.classify.accuracy(classifier, test_set))

#print('bullying precision:', precision(refsets['Bullying'], testsets['Bullying']))
print('Rellamada:',recall(refsets['Bullying'], testsets['Bullying']))
print("-------------------------------------------------")
print("-------------------------------------------------")
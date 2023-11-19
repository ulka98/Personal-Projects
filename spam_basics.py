#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 19:27:33 2023

@author: ulka
"""

import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, precision_score, recall_score, accuracy_score, f1_score

ps = PorterStemmer()
corpus = []
dataset = pd.read_csv('SMSSpamCollection',sep='\t',names=["label","messages"])


for i in range(0,len(dataset)):
    review = re.sub('[^a-zA-Z]', ' ', dataset['messages'][i])
    review = review.lower()
    review = review.split()
    
    review = [ps.stem(word) for word in review if word not in stopwords.words('english')]
    review = ' '.join(review)
    corpus.append(review)
    
cv = CountVectorizer(max_features=(2500))
X = cv.fit_transform(corpus).toarray()


y = pd.get_dummies(dataset['label'])
y = y.iloc[:,1]

X_train, X_test, y_train, y_test = train_test_split(X,y,train_size=0.80,random_state=42)

spam_detector_model = MultinomialNB().fit(X_train,y_train)

y_spam_predict = spam_detector_model.predict(X_test)
                                                    
confusion_matrix = confusion_matrix(y_test, y_spam_predict)

precision_score = precision_score(y_test,y_spam_predict)
accuracy_score = accuracy_score(y_test,y_spam_predict)
recall_score = recall_score(y_test,y_spam_predict)
f1_score = f1_score(y_test,y_spam_predict)

print(f'precision_score: {precision_score},\nrecall_score: {recall_score},\nf1_score: {f1_score},\naccuracy: {accuracy_score}')
'''
Output from spyder call 'get_namespace_view':
precision_score: 0.9281045751633987,
recall_score: 0.9530201342281879,
f1_score: 0.9403973509933774,
accuracy: 0.9838565022421525
'''
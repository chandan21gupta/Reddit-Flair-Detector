import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.externals import joblib
import pickle

flairs = ["AskIndia", "Non-Political", "[R]eddiquette", "Scheduled", "Photography", "Science/Technology", "Politics", "Business/Finance", "Policy/Economy", "Sports", "Food", "AMA"]

data = pd.read_csv('cleaned_dataset_title_comment_url.csv')

#Dependent and independent variables
y = data.flair
X = data.feature_combine

#Setting training and testing dataset
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.1,random_state = 42)

#Naive Bayes
nb = Pipeline([('vect', CountVectorizer()),
               ('tfidf', TfidfTransformer()),
               ('clf', MultinomialNB()),
              ])

NB = nb.fit(X_train, y_train)
#pickle.dump(NB,open("model_NB.sav",'wb'))
y_pred = nb.predict(X_test)


print(f"NB accuracy {accuracy_score(y_pred, y_test)}")
print(classification_report(y_test, y_pred,target_names=flairs))

#SGD
sgd = Pipeline([('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42, max_iter=5, tol=None)),
               ])
SGD = sgd.fit(X_train, y_train)
#pickle.dump(SGD,open("model_SGC.sav",'wb'))
y_pred = sgd.predict(X_test)

print(f"SGD accuracy % {accuracy_score(y_pred, y_test)}")
print(classification_report(y_test, y_pred,target_names=flairs))

#Logistic Regression
logreg = Pipeline([('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', LogisticRegression(n_jobs=1, C=1e5)),
               ])
LOGREG = logreg.fit(X_train, y_train)
#pickle.dump(LOGREG,open("model_LOGREG.sav",'wb'))
y_pred = logreg.predict(X_test)

print(f"LOG accuracy % {accuracy_score(y_pred, y_test)}")
print(classification_report(y_test, y_pred,target_names=flairs))



#Random Forest
ranfor = Pipeline([('vect', CountVectorizer()),
                   ('tfidf', TfidfTransformer()),
                   ('clf', RandomForestClassifier(n_estimators = 1000, random_state = 42)),
                  ])
RM = ranfor.fit(X_train, y_train)
#pickle.dump(RM,open("model_RM.sav",'wb'))
y_pred = ranfor.predict(X_test)

print(f"RM accuracy % {accuracy_score(y_pred, y_test)}")
print(classification_report(y_test, y_pred,target_names=flairs))

#mlp
mlp = Pipeline([('vect', CountVectorizer()),
                  ('tfidf', TfidfTransformer()),
                  ('clf', MLPClassifier(hidden_layer_sizes=(30,30,30))),
                 ])
MLP = mlp.fit(X_train, y_train)
#pickle.dump(MLP,open("model_MLP.sav",'wb'))
y_pred = mlp.predict(X_test)

print(f"MLP accuracy % {accuracy_score(y_pred, y_test)}")
print(classification_report(y_test, y_pred,target_names=flairs))
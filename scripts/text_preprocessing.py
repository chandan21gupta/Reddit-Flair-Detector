import pandas as pd
import textcleaning as TP

posts = pd.read_csv('reddit-india-data-sample.csv')

posts['title'] = posts['title'].apply(TP.string_form)
posts['body'] = posts['body'].apply(TP.string_form)
posts['comment'] = posts['comment'].apply(TP.string_form)

posts['title'] = posts['title'].apply(TP.clean_text)
posts['body'] = posts['body'].apply(TP.clean_text)
posts['comment'] = posts['comment'].apply(TP.clean_text)

feature_combine = posts["title"] + posts["comment"] + posts["url"] + posts["body"]
posts = posts.assign(feature_combine = feature_combine)

posts.to_csv('sample.csv',index=False)
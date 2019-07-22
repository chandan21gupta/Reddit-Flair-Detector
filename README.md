# Reddit-Flair-Detector
A Web App based on Python's micro web framework Flask which detects the flair (category) of a post on the subreddit [india](https://www.reddit.com/r/india/) by
utilising the power of Natural Language Processing and Machine Learning.

## Working
The user enters the url of the required post. The app takes the url, extracts various features from it (comments, authors, body .etc.)
and tries to predict the flair using them by applying the finalized model.

## Files And Directories
[Data](https://github.com/chandan21gupta/Reddit-Flair-Detector/tree/master/Data) contains mongodb instance of raw data,its csv and the resulting data after cleaning and pre processing.

[Finalized_Model](https://github.com/chandan21gupta/Reddit-Flair-Detector/tree/master/Finalised_model) contains the finalizes ML algorithm and combined data feature which gave the maximum accuracy during testing and training.

Web contains the flask application deployed for heroku server.

[Scripts](https://github.com/chandan21gupta/Reddit-Flair-Detector/tree/master/scripts) contains the the files used pre deployment, that is, the code used for scraping reddit posts and training the Machine Learning ALgorithms.

[sources.txt](https://github.com/chandan21gupta/Reddit-Flair-Detector/blob/master/sources.txt) lists the sources used for the entire project.

# Process

## Pre Deployment

1. The data was collected using the praw library in Python.The codebase is located in the [Scripts](https://github.com/chandan21gupta/Reddit-Flair-Detector/tree/master/scripts) under the name reddit_webScrapper.py
For comments - top ten comments were considered along with their authors.

2. After the data collection, and going through various articles on internet about first step towards analysis of collected data, I got across [this](https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568) wonderful article which explained everything, from the data pre-processing to data analysis in Natural Language Processing. The data was cleaned using textcleaning.py [Scripts](https://github.com/chandan21gupta/Reddit-Flair-Detector/tree/master/scripts) 

3. After cleaning the data, various ML algorithms were trained with testing and training dataset in the ratio 3:7.

### Features
First standalone features were tried like comments, title, body, url .etc. However the accuracy was not upto the mark.
The average accuracy remained around 50-55%.
After that, many features were combined on the basis of their standlone accuracies. The combination of features that gave the best accuracy (60-65%) was that of title,comments,url and body, with Logistic Regression giving the best accuracy(66%).
After that, the training and tesing ratio was increased to improve the model (9:1), since the data was sparse.

## During Deployment

A flask app was made with two routes - "/" the home route, and "/action_page" for displaying the predicted flair.

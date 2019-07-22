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

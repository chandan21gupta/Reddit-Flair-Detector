'''
	This script was used to scrape reddit data using Praw library in python.
	After scraping data this script saves the data in a csv file for further processing.

'''
import pymongo
from pymongo import MongoClient
import praw
from praw.models import MoreComments
import pandas as pd

client = MongoClient('mongodb://localhost:27017/')
db = client["reddit"]
mycol = db["subreddits"]


#OAuth with reddit API.
reddit = praw.Reddit(client_id = "0hliVZBlDhlipQ",client_secret = "pjUJDMMXhYaEmyJaLkQYb_2Fccg",user_agent = "Reddit Flair Detector",username = "chandan21121998",password = "Chandan@1234")
#Subreddit of which data is to be scraped.
subreddit = reddit.subreddit('india')


#List of all the flairs. These will be the keys in classification.
flairs = ["AskIndia", "Non-Political", "[R]eddiquette", "Scheduled", "Photography", "Science/Technology", "Politics", "Business/Finance", "Policy/Economy", "Sports", "Food", "AMA"]

#List of associated data for all posts.
#topics_dict = {}
for flair in flairs:
	'''
		The posts' data is collected by searching by the flair name in the list. Top 100 posts are recorded and stored for analysis.
	'''
	relevant_subreddits = subreddit.search(f"flair_name:{flair}",limit=100)

	for submission in relevant_subreddits:
		#del topics_dict['_id'] 
		posts = {
		"title":str(submission.title),
		"score":str(submission.score),
		"id":str(submission.id),
		"url":str(submission.url),
		"comms_num":str(submission.num_comments),
		"created":str(submission.created),
		"body":str(submission.selftext),
		"author":str(submission.author),
		"flair":str(flair),	
		}


		'''
			Only top ten comments and their authors are considered. The comments are not threads but the main
			ones.
		'''
		submission.comments.replace_more(limit=None)
		comment = ''
		authors = ''
		count = 0
		for top_level_comment in submission.comments:
		 	comment = comment + ' ' + top_level_comment.body
		 	authors = authors + ' ' + str(top_level_comment.author)
		 	count+=1     
		 	if(count > 10):
		 		#print(count)
		 		break
		
		posts["comment"] = str(comment)
		posts["authors"] = str(authors)
		#print(posts)
		result = db.posts.insert_one(posts)
		

#Saving the file


import praw
import pdb
import re
import os

reddit = praw.Reddit('sleet_bot_1')

subreddit = reddit.subreddit("learnpython")


if not os.path.isfile("C:\\Users\\Dan\\PycharmProjects\\RedditBot1\\posts_replied_to.txt"):
    posts_replied_to = []

else:
    with open("posts_replied_to.txt", "r") as f:
       posts_replied_to = f.read()
       posts_replied_to = posts_replied_to.split("\n")
       posts_replied_to = list(filter(None, posts_replied_to))

#Add Testline

print('Fuck off')
#banana
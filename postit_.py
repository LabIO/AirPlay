import tweepy
import glob
import random
import os
import sys

#Personal, every user should complete.
api_key = "LaSZvuGxHxAhZeyNaEty9njLS"
api_secret = "FQX0rxy0gSEGs35X3Uan3azSNlfW3oSOcyTyeGTZBDQViLmVfc"
oauth_token = "2199387756-pHa1Dmmsjp486ZbwkFsXUtz1dMMf9OK9ZsUQ3S3" # Access Token
oauth_token_secret = "un4ovUsYXBRn9N7tOr6EPdoTdOmS8ZJcnMGjTSRaDLKBB" # Access Token Secret

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(oauth_token, oauth_token_secret)
api = tweepy.API(auth)

#Changes directory to where the script is located (easier cron scheduling, allows you to work with relative paths)
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def randomimagetwitt(folder):
   #Takes the folder where your images are as the input and twitts one random file.
   #images = glob.glob(folder + "*")
   #image_open = images[random.randint(0,len(images))-1]
    image_open = sys.argv[1] # Get first argument

    api.update_with_media(image_open, "#LabIO_AirPlay")

#Twitts
randomimagetwitt("source images folder")

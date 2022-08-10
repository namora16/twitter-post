import tweepy

def main():
    twitter_auth_keys = {
        "consumer_key"        : "your consumer_key is here",
        "consumer_secret"     : "your consumer_secret is here",
        "access_token"        : "your access_token is here",
        "access_token_secret" : "your access_token_secret is here"
    }

    auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
            )
    auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
            )
    api = tweepy.API(auth)


    # Upload image
    media = api.media_upload("../img/mymedia.png")

    link = "https://yourlink.com/blah/blah"
    # Post tweet with image
    tweet = "\n\n\nYour tweet text status\n\n\n\n✅ Post with some emoticons\n✅ or linefeed\n✅ Etc.\n\n\n\n🧡click here : " + link
    post_result = api.update_status(status=tweet, media_ids=[media.media_id])


if __name__ == "__main__":
    main()
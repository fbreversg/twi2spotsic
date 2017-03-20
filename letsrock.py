from twitter import Api
import config

def get_twitter_api():

    return Api(config.CONSUMER_KEY,
               config.CONSUMER_SECRET,
               config.ACCESS_TOKEN,
               config.ACCESS_TOKEN_SECRET)


api = get_twitter_api()

statuses = api.statuses.user_timeline(screen_name='mad_scaramouche')
# Print text
print([status['text'] for status in statuses])

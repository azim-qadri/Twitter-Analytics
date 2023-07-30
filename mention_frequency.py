import sys
from collections import Counter
import json


def get_mentions(tweet):
    entities = tweet.get('entities', {})
    mention = entities.get('user_mentions', [])
    return [tag['screen_name'] for tag in mention]


if __name__ == '__main__':
    fname = sys.argv[1]
    with open(fname, 'r') as f:
        users = Counter()
        for line in f:
            tweet = json.loads(line)
            mentions_in_tweet = get_mentions(tweet)
            users.update(mentions_in_tweet)
        for user, count in users.most_common(40):
            print("{}: {}".format(user, count))

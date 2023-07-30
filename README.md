# Twitter Analytics

This repository contains a collection of Python scripts for analyzing Twitter data and obtaining useful statistics from user timelines and hashtags.

## Requirements

To use these scripts, you'll need the following:

- Python 3.x
- Tweepy library (for Twitter API access)
- nltk library (Natural Language Toolkit) for text processing (used in term_frequency.py)

You can install the required libraries using the following command:

```
pip install tweepy nltk
```

## Twitter API Authorization (twitter_client.py)

### Description

The `twitter_client.py` script provides functions for setting up Twitter API authentication and creating a Twitter API client for further use in other scripts. The script reads the Twitter API credentials (consumer key, consumer secret, access token, and access secret) from separate files, and these files are used for token authorization.

### Instructions

1. Obtain Twitter API credentials:  
   Before running the scripts that require API access, make sure you have obtained valid Twitter API credentials. Create four separate text files (e.g., `consumer_key.txt`, `consumer_secret.txt`, `access_token.txt`, and `access_secret.txt`) containing the respective credentials.

2. Replace the filenames:  
   In `twitter_client.py`, replace the empty strings with the filenames corresponding to the respective API credentials.

3. Set up the Twitter client:  
   Import the `get_twitter_client()` function from `twitter_client.py` in your script to create a Twitter API client. The client will be used to interact with Twitter's API.

## Script 1: Get User Timeline (get_user_timeline.py)

### Description

The `get_user_timeline.py` script retrieves a specified Twitter user's timeline using the Twitter API client. It writes the fetched data to a JSON Lines file (`user_timeline_<username>.jsonl`) containing the user's tweets in JSON format, one tweet per line.

### Instructions

To use this script, run the following command in your terminal or command prompt:

```
python get_user_timeline.py <username>
```

Replace `<username>` with the Twitter screen name of the user whose timeline you want to retrieve.

## Script 2: Get Hashtag Statistics (get_hashtag_statistics.py)

### Description

The `get_hashtag_statistics.py` script analyzes a JSON Lines file (e.g., `user_timeline_<username>.jsonl`) containing tweets and calculates statistics related to hashtags. It counts the number of tweets with hashtags, the minimum and maximum number of hashtags in a tweet, and the percentage of tweets with different numbers of hashtags. The statistics are printed to the console.

### Instructions

To analyze the hashtag statistics, run the following command in your terminal or command prompt:

```
python get_hashtag_statistics.py <filename.jsonl>
```

Replace `<filename.jsonl>` with the name of the JSON Lines file containing tweets.

## Script 3: Mention Frequency (mention_frequency.py)

### Description

The `mention_frequency.py` script reads a JSON Lines file (e.g., `user_timeline_<username>.jsonl`) and calculates the frequency of user mentions in the tweets. It prints the top 40 most mentioned users and their respective mention counts.

### Instructions

To analyze the mention frequency, run the following command in your terminal or command prompt:

```
python mention_frequency.py <filename.jsonl>
```

Replace `<filename.jsonl>` with the name of the JSON Lines file containing tweets.

## Script 4: Term Frequency (term_frequency.py)

### Description

The `term_frequency.py` script reads a JSON Lines file (e.g., `user_timeline_<username>.jsonl`) and processes the text of each tweet to calculate the term frequency of words (excluding stop words and punctuations). It prints the top 40 most frequent words and their respective counts.

### Instructions

To calculate the term frequency of words in tweets, run the following command in your terminal or command prompt:

```
python term_frequency.py <filename.jsonl>
```

Replace `<filename.jsonl>` with the name of the JSON Lines file containing tweets.

## Note

Ensure you have the required JSON Lines file (e.g., `user_timeline_<username>.jsonl`) obtained from the `get_user_timeline.py` script before running the analysis scripts.

For any questions or issues, please contact [Azim](mailto:syed.azim.q@gmail).

---
_This repository is hosted on GitHub. For more details, visit the GitHub page: [twitter-analytics](https://github.com/azim-qadri/Twitter-Analytics)_

# Introduction

Given a search string, this returns a random tweet found by Twitter's search API.
See here: https://dev.twitter.com/rest/public/search for more details on searching.

## Set up

This project is in **python 3**, so when creating your virtualenv remember to specify

```
virtualenv my_dir  -p python3
cd my_dir
source bin/activate
```

After you pull this repo, install dependencies via

```
pip install -r requirements.txt
```

Next, you need to set your Twitter API credentials as  **environment variables**

```
# Obviously, replacing empty strings with your own keys
export TWITTER_CONSUMER_KEY=''
export TWITTER_CONSUMER_KEY_SECRET=''
export TWITTER_ACCESS_TOKEN=''
export TWITTER_ACCESS_TOKEN_SECRET=''
```

It might be helpful to put these in your bin/activate script.

## Running

Simply:

```
python twitter_search.py
```

You'll see the following prompt:

```
Please input any string to search on twitter: 
```

As per above, any string can be used to search.  Expected output is as such:

```
Please input any string to search on twitter: "@oprah ur caps r on, btw"
@stylesandfranta
RT @SHAQ: @oprah ur caps r on, btw
```

If no tweets found, you will simply see "No matching tweets found."

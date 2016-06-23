# tweet-automation
Just messing around with automation. I chose to use Twitter as the API was easy to connect and multiple examples exist online.

### Prerequisites
1. Download zip of repository
2. Move folder to your desktop
3. Open shell and install `tweepy` by `$ pip install tweepy` (if running into issues on later versions of OS X due to `six`, just google something along the lines of "six error install tweepy OS X version #")

### Linking to Twitter
1. Go to apps.twitter.com
2. Sign in and fill out the relevant information to create a new app (if you do not have a URL, copy and paste your current *https://apps.twitter.com/app* URL into that field)
3. Click "Keys and Access Tokens" at the top of your app profile
4. Generate an **Access Token & Secret**
5. Copy and paste the **Consumer Key/Secret** and **Access Token/Secret** into their respective fields in `autotweeterkeys.py`
6. Update `auy.txt` with your desired lines of text, where each line represents a tweet.

### Automating your Twitter
1. Open shell and change your working directory to the folder of this repository: `$ cd Desktop/tweet-automation`
2. Run the `autotweeter.py` script: `$ python autotweeter.py`

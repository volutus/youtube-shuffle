# youtube-shuffle

Flask application that accepts a YouTube playlist ID and shuffles it. I built this because YouTube's shuffle function is pretty awful and the website I was previously using for this task stopped working.

# Project Setup
To setup the project from scratch, you'll need to create a virtual environment and activate it. Note that Python IDEs like PyCharm may do these for you. 

Run the following in your console: 

`python -m venv venv`

To activate the virtual environment, do the following. Note that this is the Windows version. The syntax on other operating systems may differ a little:

`"venv/Scripts/activate"`

Lastly, you'll need to install everything in requirements. Run the following:

`pip install -r requirements.txt`

At this point, setup is complete. Before running the project, you'll need to create a directory named 'secrets' in the root of the project and put 2 files in there. I've detailed both files below:

FLASK_SECRET_KEY -- This is just a source of entropy for the Flask server, but it needs to be secret. Generate entropy however you desire. I used my password manager to generate a random 32 character string.

YOUTUBE_API_KEY -- This is your YouTube API key. [You'll need to get it from the Google developers console.](https://developers.google.com/youtube/v3/getting-started)

Once these secrets are in place, you're good to go. To run the project, do the following:

`flask run`


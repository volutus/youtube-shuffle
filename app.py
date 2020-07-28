from flask import Flask, render_template, session, redirect
from forms import RandomizerForm
from utils import youtube, file_utils
from random import shuffle

# This is the flask Secret key. It just needs to be some kind of entropy.
FLASK_SECRET_LOCATION = 'secrets/FLASK_SECRET_KEY'

# Start flask app by doing `flask run` in the terminal
# Runs at localhost:5000
app = Flask(__name__)
app.config['SECRET_KEY'] = file_utils.read_file(FLASK_SECRET_LOCATION)

# Frontend routes
@app.route('/', methods=['GET', 'POST'])
def root():
    form = RandomizerForm()
    if form.validate_on_submit():
        playlist_id = form.playlist_id.data
        session['playlist_id'] = playlist_id
        return redirect('/randomize')

    missing_id = session.pop('missing_id', False)
    return render_template('root.html', title='YouTube Randomizer: Start', form=form, missing_id=missing_id)


@app.route('/randomize')
def randomize():
    if 'playlist_id' not in session:
        session['missing_id'] = True
        return redirect('/')
    else:
        # Put these into the browser's storage to prevent duplicate lookups
        playlist_id = session['playlist_id']
        videos = youtube.fetch_videos(playlist_id)
        shuffle(videos)
        return render_template('randomize.html', title='YouTube Randomizer: Playing', videos=videos)

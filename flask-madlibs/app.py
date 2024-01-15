from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def select_story():

    return render_template('select_story.html', stories = stories.values() )



@app.route('/prompts')
def show_prompts():

    story_id = request.args['story_id']
    story = stories[story_id]

    prompts = story.prompts

    return render_template('prompts.html', prompts=prompts, story_id = story_id, title = story.title)



@app.route('/story')
def show_story():

    story_id = request.args['story_id']
    story = stories[story_id]
    text = story.generate(request.args)

    return render_template('story.html', text = text, story = story)
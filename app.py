from flask import Flask, render_template,request, abort

app = Flask(__name__)

topics = {
    "እንስሳት": "እንስሳት",
    "market": "Market Adventure",
    "holiday": "Holiday Fun",
    "ethiopia": "Ethiopian Tradition"
}
stories = {
    "እንስሳት": "Today at school, I saw a {{ adjective }} {{ noun }} who was {{ verb }} in the hallway.",
    "market": "At the market, I bought a {{ adjective }} {{ noun }} and then decided to {{ verb }} home.",
    "holiday": "During the holiday, I felt so {{ adjective }} when I saw the {{ noun }} and decided to {{ verb }} all day.",
    "ethiopia": "In Ethiopia, people celebrate with a {{ adjective }} {{ noun }} while they {{ verb }} joyfully."
}
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/topics')
def options():
    import random
    topic_list = [{"name": v, "url": f"/story/{k}"} for k, v in topics.items()]
    random.shuffle(topic_list)
    return render_template('topics.html', topics=topic_list)

@app.route('/story/<topic>', methods=['GET', 'POST'])
def story(topic):
    if topic not in topics:
        abort(404)  # if invalid topic, show 404
    title = topics[topic]
    story_template = stories[topic]
    if request.method == 'POST':
        # Get words from form
        adjective = request.form.get('adjective', '')
        noun = request.form.get('noun', '')
        verb = request.form.get('verb', '')

        # Fill the story template
        filled_story = story_template.replace("{{ adjective }}", adjective)\
                                     .replace("{{ noun }}", noun)\
                                     .replace("{{ verb }}", verb)

        return render_template(f"{topic}.html", title=title, story=filled_story,
                               adjective=adjective, noun=noun, verb=verb)

    # GET request – show empty form
    return render_template(f"{topic}.html", title=title, story=None,
                           adjective='', noun='', verb='')

if __name__ == '__main__':
    app.run(debug=True)

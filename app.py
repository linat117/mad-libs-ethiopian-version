from flask import Flask, render_template,request, abort

app = Flask(__name__)

topics = {
    "ቅዠት": "ቅዠት",
    "ምኞት": "ምኞት",
    "ያልታሰበው": "ያልታሰበው",
    "አድናቆት": "አድናቆት"
}
stories = {
    "ቅዠት": "ዛሬ በጠዋት ነው ከእንቅልፌ የተነሳሁት። ከዚያም ለባብሼ ደብተሬን ይዤ ወደ  {{ ተቋም }} ሄድኩ።በመንገዴ ላይ ትልቅ  {{ ቀለም }}  {{ እንሰሳ }}  እየሮጠ ወደኔ ሲመጣ ሳየው ደንግጬ ወደኋላ ተመልሼ መሮጥ ጀመርኩ። ከዛ ተንሽራትቼ የሆነ ጉድጓድ ውስጥ ገባሁ። ወዲያው ከእንቅልፌ ስነቃ ራሴን ከ {{ የቤት_እቃ }} ላይ ወድቄ መሬት ላይ አገኘሁት።",
    "ምኞት": "ወደፊት {{ የስራ_ዘርፍ }} መሆን እፈልጋለሁ ፣  {{ ቀለምም }} ጋውን እለብሳለው ፣ {{ ተቋምም }} ውስጥ ብዙ ሰዎችን በማከም ደስታቸውን ማየት  እፈልጋለሁ ።",
    "ያልታሰበው": "እሁድ ዕለት ከቤተሰቦቼ ጋር ወደ {{ ቦታ }} ሄድን። {{ የውሃ_አካል }} ዳር ተቀምጠንም {{ የባህር_እንሰሳ }} በላን።ከዚያም ተዝናንተን ውለን ሲመሽ ወደቤት ለመሄድ መንገድ ጀመርን።በመሃል የመኪናው {{ የመኪና_ክፍል }} ተነፈሰብን፣ ተቀያሪ ባለመኖሩም መንገድ ላይ አደርን።",
    "አድናቆት": "ዛሬ ጠዋት ወደ ስራ ልሄድ ስል ራሴን በ{{ የቤት_እቃቃ }} አየሁት። ከዚያም ሳላስበው  {{ የቤት_እቃቃ }}ኡ {{ የሰውነት_ክፍል }} አውጥቶ በጣም አምሮብሻል አለኝ። ይሄንን ስሰማ ደንግጬ ራሴን ስቼ ወድቄ  {{ ተተቋም }} ተወሰድኩ ።  በዛም ምክንያት ከስራ ቀረሁ።"
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
        abort(404)

    title = topics[topic]
    story_template = stories[topic]

    if request.method == 'POST':
        if topic == "ቅዠት":
            ተቋም = request.form.get('ተቋም', '')
            ቀለም = request.form.get('ቀለም', '')
            እንሰሳ = request.form.get('እንሰሳ', '')
            የቤት_እቃ = request.form.get('የቤት_እቃ', '')
            filled_story = story_template.replace("{{ ተቋም }}", ተቋም)\
                                         .replace("{{ ቀለም }}", ቀለም)\
                                         .replace("{{ እንሰሳ }}", እንሰሳ)\
                                         .replace("{{ የቤት_እቃ }}", የቤት_እቃ)
            return render_template(f"{topic}.html", title=title, story=filled_story)

        elif topic == "ምኞት":
            የስራ_ዘርፍ = request.form.get('የስራ_ዘርፍ', '')
            ቀለምም = request.form.get('ቀለምም', '')
            ተቋምም = request.form.get('ተቋምም', '')
            filled_story = story_template.replace("{{ የስራ_ዘርፍ }}", የስራ_ዘርፍ)\
                                         .replace("{{ ቀለምም }}", ቀለምም)\
                                         .replace("{{ ተቋምም }}", ተቋምም)
            return render_template(f"{topic}.html", title=title, story=filled_story)

        elif topic == "ያልታሰበው":
            ቦታ = request.form.get('ቦታ', '')
            የውሃ_አካል = request.form.get('የውሃ_አካል', '')
            የባህር_እንሰሳ= request.form.get('የባህር_እንሰሳ', '')
            የመኪና_ክፍል= request.form.get('የመኪና_ክፍል', '')
            filled_story = story_template.replace("{{ ቦታ }}", ቦታ)\
                                         .replace("{{ የውሃ_አካል }}", የውሃ_አካል)\
                                         .replace("{{ የባህር_እንሰሳ }}", የባህር_እንሰሳ)\
                                         .replace("{{ የመኪና_ክፍል }}", የመኪና_ክፍል)
            return render_template(f"{topic}.html", title=title, story=filled_story)

        elif topic == "አድናቆት":
            የቤት_እቃቃ = request.form.get('የቤት_እቃቃ', '')
            የሰውነት_ክፍል = request.form.get('የሰውነት_ክፍል', '')
            ተተቋም = request.form.get('ተተቋም', '')
            filled_story = story_template.replace("{{ የቤት_እቃቃ }}", የቤት_እቃቃ)\
                                         .replace("{{ የሰውነት_ክፍል }}", የሰውነት_ክፍል)\
                                         .replace("{{ ተተቋም }}", ተተቋም)
            return render_template(f"{topic}.html", title=title, story=filled_story)

    # GET Request (show empty form)
    return render_template(f"{topic}.html", title=title, story=None)

if __name__ == '__main__':
    app.run(debug=True)

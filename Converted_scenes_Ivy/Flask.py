from flask import Flask, request, render_template

app = Flask(__name__, template_folder= "templates")

global points
points = 0

@app.route("/scene3")
def scene3():
    return render_template("scene3.html")

@app.route("/scene3a", methods = ['post'])
def scene3a():
    comment = request.form['response']
    angryWords = "deserve desire want angry mad unfair upset fight !"
    submissiveWords = "okay fine ... ok right alright sure yes agree"
    angry = [word for word in comment if word in angryWords]
    submissive = [word for word in comment if word in submissiveWords]
    global points
    if len(angry) >= 1:
        points = points + 2
        sisters = "They look shocked at your outburst, but they still say with arrogance, 'We're going to a ball at the palace. And you're not invited.'"
    elif len(submissive) >= 1:
        points = points + 0
        sisters = "They nod. 'Good bye', they say. The next morning, however, as you walk by their door to prepare them breakfast, you hear them laughing. 'I'm so excited for the ball!' they exclaim. You realize that last night, they had been trying on dresses for the ball."
    else:
        points = points + 1
        sisters = "But they don't even listen to what you have to say. They laugh over your response and slam the door shut. You eavesdrop, and realize that they're trying on clothes for a ball at the palace."
    return render_template("scene3a.html",
                          answer = sisters
                          )

@app.route("/scene4")
def scene4():
    return render_template("scene4.html")

@app.route("/scene4a")
def scene4a():
    global points
    points = points + 0
    global past
    past = "You realize the fairy godmother's magic wears off then, and in your haste running back home and away from the prince, you leave behind a shoe."
    return render_template("scene4a.html")

@app.route("/scene4b")
def scene4b():
    global points
    points = points + 1
    global past
    past = "You realize your sisters are going back home at midnight, and they will be suspicious if you are not there if they call you to make them some tea after a night out. In your haste running back home and away from the prince, you leave behind a shoe."
    return render_template("scene4b.html")

@app.route("/scene4c")
def scene4c():
    global points
    points = points + 2
    global past
    past = "You realize your sisters are going back home at midnight, and they will be suspicious if you are not there if they call you to make them some tea after a night out. In your haste running back home and away from the prince, you leave behind a shoe."
    return render_template("scene4c.html"
                          )

@app.route("/scene7")
def scene7():
    new_past = past
    global points
    points = points
    return render_template("scene7.html",
                          past_variable = new_past,
                          point = points
                          )
    

if __name__ == '__main__':
    app.run()
    

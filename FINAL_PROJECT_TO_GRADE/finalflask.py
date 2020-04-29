from flask import Flask, request, render_template

app = Flask(__name__, template_folder= "templates")

@app.route("/")
def about():
    global points
    points = 0
    return render_template("about.html")

@app.route("/scene1")
def scene1():
    return render_template("scene1.html")

@app.route("/scene1_a")
def scene1_a():
    return render_template("scene1_a.html")

@app.route("/scene1_b")
def scene1_b():
    global points
    points = points + 1
    return render_template("scene1_b.html")

@app.route("/scene1_c")
def scene1_c():
    global points
    points = points + 2
    return render_template("scene1_c.html")

@app.route("/scene1_d")
def scene1_d():
    global points
    points = points + 3
    return render_template("scene1_d.html")

@app.route("/scene2")
def scene2():
    return render_template("scene2.html")

@app.route("/scene2a")
def scene2a():
    global points
    points = points + 0
    global past
    past = "The stepsisters walk away smugly, feeling satisfied that you did their bidding."
    return render_template("scene2_a.html")

@app.route("/scene2b")
def scene2b():
    global points
    points = points + 1
    global past
    past = "The stepsisters tell you that you better do it now, and walk away, annoyed."
    return render_template("scene2_b.html")

@app.route("/scene2c")
def scene2c():
    global points
    points = points + 2
    global past
    past = "The stepsisters say that you have to do it or they'll tell your stepmother, and walk away, upset."
    return render_template("scene2_c.html")

@app.route("/scene2d")
def scene2d():
    global points
    points = points + 3
    global past
    past = "The stepsisters get so angry, tell you that you won't get away with this, and stomp away, furious."
    return render_template("scene2_d.html")

@app.route("/scene3")
def scene3():
    return render_template("scene3.html")

@app.route("/scene3a", methods = ['post'])
def scene3a():
    comment = request.form['response']
    new_comment = comment.split()
    angryWords = "deserve desire want angry mad unfair upset fight !"
    submissiveWords = "okay fine ... ok right alright sure yes agree"
    angry = [word for word in new_comment if word in angryWords]
    submissive = [word for word in new_comment if word in submissiveWords]
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
    return render_template("scene4c.html")

@app.route("/scene5")
def scene5():
    return render_template("scene5.html")

@app.route("/scene5a")
def scene5a():
    return render_template("scene5a.html")

@app.route("/scene5b")
def scene5b():
    global points
    points = points + 1
    return render_template("scene5b.html")

@app.route("/scene5c")
def scene5c():
    global points
    points = points + 2
    return render_template("scene5c.html")

@app.route("/scene5d")
def scene5d():
    global points
    points = points + 3
    return render_template("scene5d.html")

@app.route("/scene6")
def scene6():
    return render_template("scene6.html")

@app.route("/scene6a")
def scene6a():
    global points
    points = points + 0
    global past
    past = "...story continues..."
    return render_template("scene6_next.html")

@app.route("/scene6b")
def scene6b():
    global points
    points = points + 1
    global past
    past = "...story continues..."
    return render_template("scene6_next1.html")

@app.route("/scene6c")
def scene6c():
    global points
    points = points + 2
    global past
    past = "...story continues..."
    return render_template("scene6_next2.html")

@app.route("/scene6d")
def scene6d():
    global points
    points = points + 3
    global past
    past = "...story continues..."
    return render_template("scene6_next3.html")

@app.route("/scene7")
def scene7():
    new_past = past
    global points
    points = points
    return render_template("scene7.html",
                          past_variable = new_past,
                          )

@app.route("/scene8")
def scene8():
    return render_template("scene8.html")

@app.route("/scene8a")
def scene8a():
    global points
    points = points + 0
    global past
    past = "The mice free you by stealing the key to the attic from your stepmother."
    return render_template("scene8_ab0.html")

@app.route("/scene8b")
def scene8b():
    global points
    points = points + 1
    global past
    past = "The mice free you by stealing the key to the attic from your stepmother."
    return render_template("scene8_ab1.html")

@app.route("/scene8c")
def scene8c():
    global points
    points = points + 2
    global past
    past = "You can go show the Duke that the slipper fits you."
    return render_template("scene8_cd0.html")

@app.route("/scene8d")
def scene8d():
    global points
    points = points + 3
    global past
    past = "You can go show the Duke that the slipper fits you."
    return render_template("scene8_cd1.html")

@app.route("/scene9")
def scene9():
    return render_template("scene9.html")

@app.route("/scene9_a")
def scene9_a():
    return render_template("scene9_a.html")

@app.route("/scene9_b")
def scene9_b():
    global points
    points = points + 1
    return render_template("scene9_b.html")

@app.route("/scene10")
def scene10():
    return render_template("scene10.html")

@app.route("/scene10_a")
def scene10_a():
    return render_template("scene10_a.html")

@app.route("/scene10_b")
def scene10_b():
    global points
    points = points + 1
    return render_template("scene10_b.html")


@app.route("/scene11")
def scene11():
    return render_template("scene11.html")

@app.route("/scene11_a")
def scene11_a():
    return render_template("scene11_a.html")

@app.route("/scene11_b")
def scene11_b():
    return render_template("scene11_b.html")

@app.route("/scene12")
def scene12():
    global points
    points = points
    if points <= 9:
        rebellion_score = "You are not very rebellious"
    elif points <= 18:
        rebellion_score = "You're somewhat rebellious"
    else:
        rebellion_score = "You are super rebellious"
    return render_template("scene12.html",
                           point = points,
                           rebellion = rebellion_score
                          )

if __name__ == '__main__':
    app.run('127.0.0.1',port=5000)

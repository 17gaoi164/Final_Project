from flask import Flask, render_template, request
import hangman_app
app = Flask(__name__)

global state
state = {
        'decision':'',
        'points': 0,
        
         }

@app.route('/')
@app.route('/main')
def main():
	return render_template('about.html')

if __name__ == '__main__':
    app.run(port=3000)

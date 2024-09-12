from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)
score = 0

def bot_choice():
    return random.randint(1,3)

@app.route('/')
def index():
    return render_template('index.html', score=score)

@app.route('/exec', methods=['POST'])
def logic():
    global score
    button = request.json['button_id']
    bot = bot_choice()
    options = ['Rock', 'Paper', 'Scissors']
    comp = options[bot -1]

    if button == 'rock-btn':
        u = 1
    elif button == 'paper-btn':
        u = 2        
    elif button == 'scissor-btn':
        u = 3

    if u == bot:
        result = "Draw"    
    elif u == bot + 1 or bot - u == 2:
        result = "Victory !"
        score += 1
    else:
        result = "Defeat :("
        score -= 1

    return jsonify(score = score, result = result, comp = comp)

if __name__ == '__main__':
    app.run()


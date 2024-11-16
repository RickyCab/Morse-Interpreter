from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
app.config['SECRET_KEY'] = "12345"
Bootstrap5(app)

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ' ': '/', '\r': ' ', '\n':' '
}

def clean_text(text):
    clean_text = ""
    for letter in text.upper():
        if letter.isalpha():
            clean_text+=letter
    return clean_text


def text_to_morse(text):
    result = ""
    for letter in text.upper():
        result += morse_code_dict[letter]
    return result


@app.route("/", methods=["GET", "POST"])
def home():

    result = request.args.get("result")
    cleaned = request.args.get("cleaned")

    if request.method == "POST":
        text = request.form["input-text"]
        cleaned = clean_text(text)
        result = text_to_morse(cleaned)
        return redirect(url_for('home', result=result, cleaned=cleaned))

    return render_template("index.html", result=result, cleaned=cleaned)










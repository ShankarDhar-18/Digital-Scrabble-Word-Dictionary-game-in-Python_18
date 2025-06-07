from flask import Flask, render_template, request
import string

app = Flask(__name__)

# Letter scores
letter_scores = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1,
    'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
    'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1,
    'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
    'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4,
    'Z': 10
}

# Valid words (you can expand this with a real dictionary later)
valid_words = {
    "HELLO", "WORLD", "PYTHON", "SKILL", "SCRABBLE", "GAME",
    "WORD", "BOARD", "KOALA", "AX", "OAK", "LOX"
}

def calculate_score(word):
    return sum(letter_scores.get(letter.upper(), 0) for letter in word)

def is_valid_word(word):
    return word.upper() in valid_words

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    letters = []

    if request.method == "POST":
        # Get 7 user-selected letters from form
        for i in range(7):
            l = request.form.get(f"letter{i}")
            if l:
                letters.append(l.upper())

        input_word = request.form.get("word", "").upper()

        if input_word:
            # Check if word is valid and uses only the given letters
            if all(input_word.count(l) <= letters.count(l) for l in input_word) and is_valid_word(input_word):
                score = calculate_score(input_word)
                message = f"✅ '{input_word}' is valid! Score: {score}"
            else:
                message = f"❌ '{input_word}' is not a valid word or doesn't match the given letters."

    return render_template("index.html", letters=letters, message=message)

if __name__ == "__main__":
    print("✅ Flask app is starting...")
    app.run(debug=True)

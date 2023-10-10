from flask import Flask, render_template, request
from translate import Translator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def translate_text():
    if request.method == "POST":
        from_lang = request.form.get("from_lang")
        to_lang = request.form.get("to_lang")
        text_to_translate = request.form.get("text_to_translate")

        if from_lang and to_lang and text_to_translate:
            translator = Translator(to_lang=to_lang, from_lang=from_lang)
            result = translator.translate(text_to_translate)
            return render_template("index.html", result=result)

    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, render_template, request
from langdetect import detect, detect_langs, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

app = Flask(__name__)

# Make predictions more reproducible
DetectorFactory.seed = 0

LANGUAGE_NAMES = {
    "en": "English",
    "bn": "Bengali",
    "hi": "Hindi",
    "fr": "French",
    "es": "Spanish",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    "ru": "Russian",
    "ja": "Japanese",
    "ko": "Korean",
    "zh-cn": "Chinese (Simplified)",
    "zh-tw": "Chinese (Traditional)",
    "ar": "Arabic",
    "ur": "Urdu",
    "ta": "Tamil",
    "te": "Telugu",
    "mr": "Marathi",
    "gu": "Gujarati",
    "pa": "Punjabi",
    "ml": "Malayalam",
    "th": "Thai",
    "vi": "Vietnamese",
    "nl": "Dutch",
    "tr": "Turkish",
    "pl": "Polish",
    "id": "Indonesian",
    "uk": "Ukrainian",
    "sv": "Swedish",
    "el": "Greek",
    "he": "Hebrew",
    "fa": "Persian",
    "ro": "Romanian",
    "hu": "Hungarian",
    "da": "Danish",
    "fi": "Finnish",
    "no": "Norwegian",
    "cs": "Czech",
    "sk": "Slovak",
    "bg": "Bulgarian",
    "hr": "Croatian",
    "sr": "Serbian",
    "sw": "Swahili",
    "ca": "Catalan",
    "et": "Estonian",
    "lt": "Lithuanian",
    "lv": "Latvian",
    "sl": "Slovenian",
    "af": "Afrikaans"
}


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None
    text = ""

    if request.method == "POST":
        text = request.form.get("text", "").strip()

        if not text:
            error = "Please enter some text to detect its language."

        elif len(text) < 3:
            error = "Please enter at least 3 characters."

        else:
            try:
                language_code = detect(text)
                predictions = detect_langs(text)

                probability = next(
                    (item.prob for item in predictions
                     if item.lang == language_code),
                    0.0
                )

                result = {
                    "language": LANGUAGE_NAMES.get(
                        language_code, language_code
                    ),
                    "code": language_code,
                    "probability": round(probability * 100, 2)
                }

            except LangDetectException:
                error = (
                    "The language could not be detected. "
                    "Try entering a longer sentence."
                )

    return render_template(
        "index.html",
        result=result,
        error=error,
        text=text
    )


if __name__ == "__main__":
    app.run(debug=True)

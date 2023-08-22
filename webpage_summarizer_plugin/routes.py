from flask import render_template, request
from webpage_summarizer_plugin import app
from bs4 import BeautifulSoup
import re
import nltk
import requests
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

nltk.download("punkt")
nltk.download("stopwords")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    result = []
    heading = ""
    error_msg = ""
    if "input_field" in request.form:
        input_value = request.form["input_field"]
        is_url_valid = check_validity(input_value)
        if is_url_valid:
            extracted_text = extract_text(input_value)
            if "summary" in request.form:
                if extracted_text:
                    summary = generate_summary(extracted_text)
                    result = summary
                    heading = "The Summary is:"
            elif "major_points" in request.form:
                if extracted_text:
                    major_points = get_major_points(extracted_text)
                    result = major_points
                    heading = "The Major Points are:"
        else:
            result = []
            heading = "WARNING!!!"
            error_msg = "Enter a valid URL"
    return render_template(
        "index.html", result=result, heading=heading, error_msg=error_msg
    )


def check_validity(url):
    regex = (
        "((http|https)://)(www.)?"
        + "[a-zA-Z0-9@:%._\\+~#?&//=]"
        + "{2,256}\\.[a-z]"
        + "{2,6}\\b([-a-zA-Z0-9@:%"
        + "._\\+~#?&//=]*)"
    )
    p = re.compile(regex)
    if re.search(p, url):
        return True
    else:
        return False


def extract_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        extracted_text = soup.get_text()
        return extracted_text
    except requests.exceptions.RequestException as e:
        print("Error fetching webpage:", e)
        return None


def get_major_points(text, num_sentences=10):
    sentences = sent_tokenize(text)
    stop_words = set(stopwords.words("english"))
    filtered_sentences = [
        " ".join(word for word in sentence.split() if word.lower() not in stop_words)
        for sentence in sentences
    ]
    words = " ".join(filtered_sentences).split()
    fdist = FreqDist(words)
    key_words = fdist.most_common(10)
    key_sentences = []
    for sentence in sentences:
        if any(word in sentence for word, _ in key_words):
            key_sentences.append(sentence)
    return key_sentences[:num_sentences]


def generate_summary(text, num_sentences=10):
    sentences = sent_tokenize(text)
    words = " ".join(sentences).split()
    fdist = FreqDist(words)
    sentence_scores = {}
    for sentence in sentences:
        for word, freq in fdist.items():
            if word in sentence:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = freq
                else:
                    sentence_scores[sentence] += freq
    sorted_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    return sorted_sentences[:num_sentences]

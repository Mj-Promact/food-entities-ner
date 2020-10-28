import os
import io
import sys
import flask
import spacy
import PyPDF2

from werkzeug.utils import secure_filename
from flask import Flask, request, render_template, redirect, url_for, flash, Response


##UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['pdf'])

app = Flask(__name__)
app.secret_key = "this is a secret key, can you believe it!!!"

def allowed_file(filename: str):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_ner(path: str):
    food_tagger = spacy.load(path)
    print(f'LOG: NER model loaded successfully...')

    return food_tagger

def parse_pdf(file: bytes):
    buffer_reader = io.BufferedReader(io.BytesIO(file))
    pdf_reader = PyPDF2.PdfFileReader(buffer_reader)

    pdf_string = ""
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        pdf_string += page.extractText()

    pdf_string = pdf_string.split("\n")

    return " ".join(pdf_string)
    

@app.route('/text_review', methods=['POST'])
def text_review():
    food_entities = []

    if request.form['review']:
        review = request.form['review']

        if review:
            print(f"LOG: Text-review received...")

        entities = food_tagger(review)

        for ent in entities.ents:
            food_entities.append(ent)

    else:
        flash('Please enter valid review')
        return redirect('/')

    return render_template('home.html', food_entities=food_entities)

@app.route('/pdf_review', methods=['POST'])
def pdf_review():
    food_entities = []

    if 'pdf' not in request.files:
        flash('Please enter valid review pdf file')
        return redirect('/')

    pdf_file = request.files['pdf']
    if pdf_file.filename == '':
        flash('No pdf file selected for uploading')
        return redirect('/')

    if pdf_file and allowed_file(pdf_file.filename):
        filename = secure_filename(pdf_file.filename)
        
        review = parse_pdf(pdf_file.read())
        if review:
            print(f'LOG: PDF-review received...')

        entities = food_tagger(review)

        for ent in entities.ents:
            food_entities.append(ent)

    else:
        flash('Allowed doc type is -> pdf')
        return redirect('/')

    return render_template('home.html', food_entities=food_entities)

@app.route('/', methods=['GET'])
def home():
    food_entities = []

    return render_template('home.html', food_entities=food_entities)


## Load model whenever application is run first time
path = "./Spacy Model"
food_tagger = load_ner(path)


if __name__ == '__main__':
    app.run()

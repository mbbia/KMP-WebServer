from flask import Flask, render_template, redirect, url_for, request
from helper import process_sequence, check_letters
from kmp_algorithm import *

app = Flask(__name__)

# loading covid sequence and process it
covid_sequence = process_sequence('sequence.fasta')

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/ff/', methods=('POST', 'GET'))
def file():
    if request.method == 'POST':
        # if the user provides a file
        if 'file' in request.files:
            # loading and processing the submitted sequence
            input_file = request.files['file']
            if input_file and input_file.filename.endswith('.txt'):
                input_sequence = input_file.read().decode('utf-8').strip().split()
                input_sequence = ''.join(input_sequence).upper()
                check = check_letters(input_sequence)
            else:
                input_sequence = 'This will throw an error'
                check = False

        # using the Knuth Morris Pratt algorithm
        if input_sequence:
            results, number = kmp_search(covid_sequence, input_sequence)
        else:
            results, number = None, None

        # returns the results in a new page
        return render_template('results.html', sequence=input_sequence, check=check, results=results, number=number)
    else:
        # returns the input file page
        return render_template('file.html')

@app.route('/hws/', methods=('POST', 'GET'))
def hand():
    if request.method == 'POST':
        # if the user write a sequece
        if 'seq' in request.form:
            # loading and processing the submitted sequence
            input_text = request.form['seq']
            input_sequence = input_text.strip().split()
            input_sequence = ''.join(input_sequence).upper()
            check = check_letters(input_sequence)

        # using the Knuth Morris Pratt algorithm
        if input_sequence:
            results, number = kmp_search(covid_sequence, input_sequence)
        else:
            results, number = None, None

        # returns the results in a new page
        return render_template('results.html', sequence=input_sequence, check=check, results=results, number=number)
    else:
        # returns the hand writing inpute page
        return render_template('hand.html')


if __name__ == '__main__':
    app.run()

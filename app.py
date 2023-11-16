from flask import Flask, render_template, request, jsonify
from getcsv2json import showdata
from fibonaci import show_fibonacci

app = Flask(__name__)


# HOME ROUTE
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hobby')
def get_hobby():
    return render_template('hobby.html')


@app.route('/education')
def get_education():
    return render_template('education.html')


@app.route('/work')
def get_work():
    return render_template('work.html')


@app.route('/contact')
def get_contact():
    return render_template('contact.html')


# OTHER ROUTE

@app.route('/showdata')
def get_data():
    return showdata()


@app.route('/getdata')
def retrieve_data():
    return render_template('dataretriever.html')


@app.route('/fibonacci/<int:n>')
def fibonacci(n):
    fibonacci_sequence = show_fibonacci(n)
    return f"{n} Deret Fibonacci adalah: {fibonacci_sequence}"


@app.route('/showform', methods=['GET', 'POST'])
def showform():
    if request.method == 'POST':
        email = request.form.get('email')
        message = request.form.get('message')
        return f'Email: {email}, Message: {message}'
    else:
        return '<a href="/">Invalid Request, Go Back To Previous Site</a>'


if __name__ == "__main__":
    app.run(debug=True)

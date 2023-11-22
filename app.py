from flask import Flask, render_template, request, jsonify
from getcsv2json import showdata
from fibonaci import show_fibonacci
from pujakerangajaib import generate_random_message

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


@app.route('/fibonacci', methods=['GET', 'POST'])
def fibonacci():
    if request.method == 'POST':
        n = int(request.form['jumlah'])
        fibonacci_sequence = show_fibonacci(n)
        return render_template('fibonacci.html', fibonacci_sequence=fibonacci_sequence)
    else:
        return render_template('fibonacci.html', fibonacci_sequence=None)


@app.route('/showform', methods=['GET', 'POST'])
def showform():
    if request.method == 'POST':
        email = request.form.get('email')
        message = request.form.get('message')
        return f'Email: {email}, Message: {message}'
    else:
        return '<a href="/">Invalid Request, Go Back To Previous Site</a>'


@app.route('/pujakerangajaib', methods=['GET', 'POST'])
def pujakerangajaib():
    if request.method == 'POST':
        message = f"Selamat datang, {request.form['name']}, anda berhasil masuk ke Puja Kerang Ajaib"
    else:
        name_param = request.args.get('name')
        name = name_param or "Spongebob"
        message = generate_random_message(name)

    message = message.title()
    return render_template('pujakerangajaib.html', message=message)


@app.route('/pujakerangajaib/req', methods=['GET', 'POST'])
def pujakerangajaibreq():
    return render_template('pujakerangajaibreq.html')


if __name__ == "__main__":
    app.run(debug=True)

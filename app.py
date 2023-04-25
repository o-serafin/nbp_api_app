from flask import Flask, render_template, request, redirect, url_for
from functions import avg_exchange_rate, major_difference, min_max_average
from utilities import get_currencies


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        currency = request.form['currency']

        if request.form['method'] == '1':
            date = request.form['date']
            return redirect(url_for('get_avg_exchange_rate', currency=currency, date=date))
        
        elif request.form['method'] == '2':
            n = request.form['number']
            return redirect(url_for('get_min_max_average', currency=currency, n=n))
        
        elif request.form['method'] == '3':
            n = request.form['number']
            return redirect(url_for('get_major_difference', currency=currency, n=n))
        
    currencies = get_currencies()
    return render_template('home.html', currencies=currencies)


@app.route('/exchanges/<currency>/<date>')
def get_avg_exchange_rate(currency, date):
    result = avg_exchange_rate(currency, date)
    return result
    

@app.route('/min-max/<currency>/<n>')
def get_min_max_average(currency, n):
    result = min_max_average(currency, n)
    return result
   

@app.route('/major-diff/<currency>/<n>')
def get_major_difference(currency, n):
    result = major_difference(currency, n)
    return result


if __name__ == '__main__':
    app.run(debug=True)

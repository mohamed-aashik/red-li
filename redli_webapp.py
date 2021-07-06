from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/track', methods=['POST'])
def track():
    if request.method == 'POST':
        url = request.form['user_url']
        resp = requests.get(url)
        redirect_ulr = resp.history
        return render_template('track.html', endurl = resp, redirect = redirect_ulr)

if __name__=='__main__':
    app.run(debug=True)

from datetime import datetime
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello():
    browserName = request.headers.get('User-Agent')
    currentDate = datetime.now().strftime("%Y-%m-%d")
    return f'Current date is: {currentDate}. \nYour browser is: {browserName}!'
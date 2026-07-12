from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index_task_1.html')

@app.route('/get_time')
def get_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({"time": current_time})

if __name__ == '__main__':
    app.run()
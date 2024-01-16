from flask import Flask, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script1')
def run_script1():
    subprocess.run(['python', 'scripts/script1.py'])
    return redirect(url_for('index'))

@app.route('/run_script2')
def run_script2():
    subprocess.run(['python', 'scripts/script2.py'])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

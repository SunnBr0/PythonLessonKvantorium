from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('./24.04.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
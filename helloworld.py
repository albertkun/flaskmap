from flask import Flask
import webbrowser
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hey world!</h1>'

if __name__ == '__main__':
    app.run(debug=True)

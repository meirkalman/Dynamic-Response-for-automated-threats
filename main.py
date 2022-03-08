from flask import Flask,redirect
app = Flask(__name__)


@app.route("/")
def test():
    return redirect('127.0.0.1:3001', code=301)


if __name__ == '__main__':
   app.run(debug = True )
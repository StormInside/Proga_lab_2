import unittest
from TestMe import TestMe
from flask import Flask, redirect
# import flask.Flask as Flask

app = Flask(__name__)

@app.route("/")
def redirect_to_test():
    return redirect("/test")

@app.route("/test")
def test_program():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMe)
    if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful():
        return "Test was succesful"
    else:
        return "Some errors ocured during the test"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
    
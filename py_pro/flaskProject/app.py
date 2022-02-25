import queue

from flask import Flask, url_for, jsonify
from flask import render_template


app = Flask(__name__)


@app.route('/')
@app.route('/hello/<name>')
def hello_world(name=None):  # put application's code here
    return render_template('hello.html', name=name)



@app.route('/login/')
def login():
    return f'login'


@app.route('/user/<username>')
def user(username):
    return f'{username}\'s profile'

#
# seed = 0
# @app.route('/image')
# def image():
#     return

with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('login'))
    print(url_for('login',next='/'))
    print(url_for('user',username='hah'))
    print(jsonify([1,2,3]))


if __name__ == '__main__':
    [].__mul__()
    {1,2,3}.add(4)
    queue.Queue()
    # app.run()
    print(jsonify([1,2,3]))

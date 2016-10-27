import flask

app = flask.Flask(__name__)


@app.route('/')
@app.route('/index')
def hello_world():
    user = {'nickname': 'Miguel'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return flask.render_template('index.html',
                                 title='alan',
                                 user=user,
                                 posts=posts)


if __name__ == '__main__':
    app.run(debug=True)

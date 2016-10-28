import flask
from flask import flash
from flask import redirect
from forms import LoginForm

app = flask.Flask(__name__)
app.config.from_object('config')


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


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/index')
    else:
        flash('Login requested for Name: ' + str(form.name.data))
        flash('passwd: ' + str(form.password.data))
        flash('remember_me: ' + str(form.remember_me.data))

    return flask.render_template('login.html', form=form, title="Sign In")

if __name__ == '__main__':
    app.run(debug=True)

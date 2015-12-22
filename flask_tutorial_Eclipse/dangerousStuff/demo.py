import flask, flask.views
import os
app = flask.Flask(__name__)
# Don't do this!
#os.listdir('.') list all in the current directory
#open('index.py').read()
#open('templates/test.html','w').write("Very Interesting")
app.secret_key = "bacon"

class View(flask.views.MethodView):
    def get(self):
        return flask.render_template('index.html')
        
    def post(self):
        result = eval(flask.request.form['expression'])
        flask.flash(result)
        return self.get()
    
app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST'])

app.debug = True
app.run()
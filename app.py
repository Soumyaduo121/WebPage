# it is the app which is capable of making app
from datetime import datetime
from distutils.log import debug
from email.policy import default
from pydoc import describe
from turtle import title
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)  #to initialize the app
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///soumyaToDo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)

class TODO(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)



def __repr__(self)->str:
    return f"{self.sno} - {self.title}"


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = TODO(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
    allTodo = TODO.query.all()
    return render_template('first.html', allTodo=allTodo)

# @app.route("/show")
# def products():
#     allTodo = TODO.query.all()
#     print(allTodo)
#     return "<p>products</p>"

@app.route("/delete/<int:sno>")
def delete(sno):
    todo = TODO.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

@app.route("/update/<int:sno>",methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = TODO.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    todo = TODO.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)


if __name__ == "__main__":
    app.run(debug=True, port=8000)  #condition of run the app
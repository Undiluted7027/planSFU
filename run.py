from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__, template_folder='app/templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)
app.app_context().push()


class progress(db.Model):
    course_id = db.Column("Course ID", db.String(10), primary_key = True)
    pre_requisite = db.Column("Pre Requisite", db.Boolean)
    section = db.Column("Section", db.String(5))
    grade = db.Column("Grade", db.String(2))

    def __init__(self, course_id, pre_requisite, section, grade) :
        self.course_id = course_id
        self.pre_requisite = pre_requisite
        self.section = section
        self.grade = grade

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "POST" :
        user = request.form["nm"]
        return redirect(url_for("survey"))
    else :
        return render_template("home.html")

@app.route("/survey")
def survey():
    return f"Survey here"


# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    db.create_all()
    app.run(debug = True)
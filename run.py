
from flask import Flask, render_template, request, redirect, url_for

 
# Flask constructor takes the name of 
# current module (__name__) as argument.
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
@app.route('/begin')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    '''Test fn for first time use'''
    return 'Hello World'

@app.route('/')
def index():
    return render_template('base.html')
 
@app.route('/survey/', methods=('GET', 'POST')) 
def survey():
    if request.method == 'POST':
        # Process the form data here
        lower_div_courses = []
        for i in range(3):
            course = request.form.get('course{}'.format(i + 1))
            status = request.form.get('status{}'.format(i + 1))
            grade = request.form.get('grade{}'.format(i + 1)) if i > 0 else None
            lower_div_courses.append({
                'course': course,
                'status': status,
                'grade': grade
            })

        print("Lower Division Courses:", lower_div_courses)
        return redirect(url_for('thank_you'))

    # Add a return statement for the 'GET' method
    return render_template('survey.html')

@app.route('/thank_you')
def thank_you():
    return "Thank you for submitting the survey!"
=======
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


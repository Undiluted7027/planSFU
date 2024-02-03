
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
    course = db.Column("Course ID", db.String(10), primary_key = True)
    section = db.Column("Section", db.String(5))
    grade = db.Column("Grade", db.String(2))

    def __init__(self, course_id, section, grade) :
        self.course_id = course_id
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

@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "POST" :
        user = request.form["nm"]
        return redirect(url_for("survey"))
    else :
        return render_template("home.html")
 
@app.route('/survey/', methods=('GET', 'POST')) 
def survey():
    if request.method == 'POST':
        # Process the form data here
        lower_div_courses = []
        for i in range(3):
            course = request.form.get('course{}'.format(i + 1))
            section = request.form.get('section{}'.format(i + 1))
            grade = request.form.get('grade{}'.format(i + 1)) if i > 0 else None
            lower_div_courses.append({
                'course': course,
                'section': section,
                'grade': grade
            })

        print("Lower Division Courses:", lower_div_courses)
        for i in lower_div_courses:
            print(i['course'])
            student_progress = progress(i.get('course'), i.get('section'), i.get('grade'))
            db.session.add(student_progress)
            db.session.commit()
        return redirect(url_for('thank_you'))

    # Add a return statement for the 'GET' method
    return render_template('survey.html')

@app.route('/thank_you')
def thank_you():
    return "Thank you for submitting the survey!"

# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    db.create_all()
    app.run(debug = True)


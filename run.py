
from flask import Flask, render_template, request, redirect, url_for

 
# Flask constructor takes the name of 
# current module (__name__) as argument.
 
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__, template_folder='app/templates')

 
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
    app.run(debug = True)


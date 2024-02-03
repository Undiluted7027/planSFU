from flask import Flask, render_template, url_for, request, redirect
 
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__, template_folder='app/templates')
 
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
    app.run(debug = True)
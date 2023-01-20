'''
Before coding, the command 'pip3 install Flask' has been run in the terminal.

To install Heroku within Gitpod:
npm install -g Heroku

To login to Heroku:
heroku login -i

To view your Heroku apps:
heroku apps

To rename a Heroku app:
heroku apps:rename NEW-NAME --app CURRENT-APP-NAME

Deployed Heroku app URL:
https://YOUR-APP-NAME.herokuapp.com

To view verbose Git remotes:
git remote -v

Creating Heroku Git remote by going to Settings and copying the Git URL link:
git remote add heroku https://git.heroku.com/YOUR-APP-NAME.git

To create a requirements.txt file:
pip3 freeze --local > requirements.txt

To create a Procfile:
echo web: python run.py > Procfile

To push code to Heroku remote:
git push -u heroku main
'''

import os
import json
# Flask Class imported, along with render_template() function.
# To find out what HTML method is used, 'request' is imported.
# To display some feedback to users, the flash() function is imported:
from flask import Flask, render_template, request, flash

# The env.py gets imported only if the system can find an env.py file:
if os.path.exists("env.py"):
    import env

# Instance of Flask class. The convention is that the variable is called 'app'.
# The first argument of the Flask class is the name of the application module.
# Since we are using a single module, we can use __name__ which is a built-in
# Python variable. Flask needs it to look for templates and static files.
app = Flask(__name__)
# The following creates the __pycache__/ directory,
# which should go in .gitignore along with env.py:
app.secret_key = os.environ.get("SECRET_KEY")


# The route decorator tells Flask what URL triggers the function that follows.
# When we try to browse to the root directory, as indicated by the "/",
# Flask triggers the index function underneath, which and returns its value.
@app.route("/")
def index():
    # Thanks to render_template(), we return the HTML index file, which
    # Flask expects to be in a directory called templates.
    # It must be at the same level as our run.py file:
    return render_template("index.html")


# The route decorator binds the function to itself.
# Hence, whenever it is called, the function is called.
# This function is also called a 'view'.
@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    # The variable page_title is used to store a page-specific value:
    return render_template("about.html", page_title="About", company=data)


# The angle brackets pass data from the URL path into our view below:
@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for object in data:
            if object["url"] == member_name:
                member = object
    # 1st 'member' is the variable name being passed through into our html file
    # 2nd 'member' is the member object we created above (on line 43)
    return render_template("member.html", member=member)


# Flask looks up these views and injects the URL for each view
# into the respective href attribute (assigned in the HTML pages).
# 'methods=["get", "post"]' is needed when we want method=post in HTML to work.
@app.route("/contact", methods=["get", "post"])
def contact():
    # This is to thank the user who submitted with a flash-message:
    flash("Thanks {}, we have received your message!".format(
        request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


# Everything coming from base.html template is normally run, too.
@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


# If __name__ is equal to "__main__",
# our app will run with the following arguments.
# Of course, __"main"__ is the name of the default module in Python.
if __name__ == "__main__":
    app.run(
        # We use the os module from the standard library to get the 'IP'
        # environment variable if it exists, but set a default value if
        # it is not found. Same for port (cast as integer).
        # Never leave debug=True in production environments:
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)

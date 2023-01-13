'''
Before coding, the command 'pip3 install Flask' has been run in the terminal.
'''

import os
# Flask Class imported, along with render_template() function:
from flask import Flask, render_template

# Instance of Flask class. The convention is that the variable is called 'app'.
# The first argument of the Flask class is the name of the application module.
# Since we are using a single module, we can use __name__ which is a built-in
# Python variable. Flask needs it to look for templates and static files.
app = Flask(__name__)


# The route decorator tells Flask what URL triggers the function that follows.
# When we try to browse to the root directory, as indicated by the "/",
# Flask triggers the index function underneath and returns "Hello, World"
@app.route("/")
def index():
    # Thanks to render_template(), instead of returning text, we return
    # the HTML index file, which Flask expects to be in a directory called
    # templates, which must be at the same level as our run.py file:
    return render_template("index.html")


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

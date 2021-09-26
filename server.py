from flask import (
    Flask,
    render_template
)

app = Flask(__name__, template_folder = "templates")

@app.route('/')
def home():
    """
    This function just responds to the browser URL
    localhost:5000/

    :return: the rendered template 'home.html'
    """
    return render_template('home.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
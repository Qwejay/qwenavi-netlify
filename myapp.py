from flask import Flask, render_template
app = Flask('web app')


@app.route('/')
def htmlHomePage():
    return render_template('home_two.html')


if __name__ == "__main__":
    app.run(debug=True)
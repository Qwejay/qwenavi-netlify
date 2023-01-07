# flask_netlify

Reference: https://testdriven.io/blog/static-site-flask-and-netlify/

Steps:

- python3 -m venv venv
- source venv/bin/activate
- pip3 install Frozen-Flask
- pip3 freeze > requirements.txt
- pip3 install -r requirements.txt
- export FLASK_APP=app.py
- pip install black --upgrade
- pip3 install black --upgrade
- flask run
- python3 freeze.py
- git add . && git commit -m "c" && git push origin main
- deactivate

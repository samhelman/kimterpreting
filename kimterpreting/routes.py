from kimterpreting import app
from flask import render_template

@app.route('/')
def home_animations():
  return render_template('home.html', animations=True)

@app.route('/home')
def home():
  return render_template('home.html', title="Home", animations=False)

@app.route('/about')
def about():
  return "About"

@app.route('/contact')
def contact():
  return "Contact"

@app.route('/faq')
def faq():
  return "FAQ"

@app.route('/terms')
def terms():
  return "Terms"
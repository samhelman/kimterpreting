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
  return render_template('about.html', title="About")

@app.route('/contact')
def contact():
  return render_template('contact.html', title="Contact")

@app.route('/faq')
def faq():
  return render_template('faq.html', title="FAQ")

@app.route('/terms')
def terms():
  return render_template('terms.html', title="Terms and Conditions")
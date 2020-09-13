 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, Length, Email

class ContactForm(FlaskForm):
  id = "message"
  name = StringField('Name', validators=[DataRequired(), Length(max=100)])
  email = StringField('Email', validators=[DataRequired(), Email()])
  subject = StringField('Subject', validators=[DataRequired(), Length(max=100)])
  message = StringField('Message', widget=TextArea(), validators=[DataRequired(), Length(max=500)])
  terms = BooleanField(validators=[DataRequired()])
  submit = SubmitField('Send Message')

class QuoteForm(FlaskForm):
  id = "quote"
  name = StringField('Name', validators=[DataRequired(), Length(max=100)])
  email = StringField('Email', validators=[DataRequired(), Email()])
  day_type = RadioField('Full/Half Day?', choices=['Full Day', 'Half Day'], default='Full Day', validators=[DataRequired()])
  location = StringField('Location', validators=[DataRequired(), Length(max=50)])
  description = StringField('Job Description', widget=TextArea(), validators=[DataRequired(), Length(max=500)])
  terms = BooleanField(validators=[DataRequired()])
  submit = SubmitField('Request Quote')
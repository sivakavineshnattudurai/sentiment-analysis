from flask import flask, render_template, request, url_for
from flask_bootstrap import Bootstrap 
from textblob import TextBlob, word
import random
import time 

app1=Flask(__name__)
Bootstrap(app1)
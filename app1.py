from flask import flask, render_template, request, url_for
from flask_bootstrap import Bootstrap 
from textblob import TextBlob, word
import random
import time 

app1=Flask(__name__)
Bootstrap(app1)

@app1.route('/') #input
def index():
    return render_template('index.html')

@app1.route('/analyse',methods=['POST']) #analyses-input
def analyse():
    start=time.time()
    if request.method=='POST':
        rawtext=request.form['rawtext']
        blob= TextBlob(rawtext)
        received_text=blob
        blob_sentiment,blob_subjectivity=blob.sentiment.polarity, blob.sentiment.subjectivity
        no_of_tokens=len(list[blob.words])
        nouns=list()
        for word, tag in blob.tags:
            if tag=='NN': #ERROR1 "=" to "=="
                nouns.append(word.lemmatize)
                len_words=len(nouns)
                rand_words=random.sample(nouns, len(nouns))
                final_word=list()
                for item in rand_words:
                    word=word(item).pluralize()  #Word
                    final_word.append(word)
                    summary= final_word
                    end=time.time()
                    final_time=end-start
        return render_template("index.html",received_text=received_text,no_of_tokens=no_of_tokens,blob_sentiment=blob_sentiment,blob_subjectivity=blob_subjectivity,summary=summary, final_time=final_time)



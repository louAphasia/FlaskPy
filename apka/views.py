from apka import app
from flask import render_template

@app.route('/')
def index():
    user={'name': 'Nadi'}
    navigation=[
        {
            'href':'o mnie',
            'caption': 'O mnie'
        },
        {
            'href':'kontakt',
            'caption':'Kontakt'
        }
    ]
    return render_template('index.html', user=user,navigation=navigation)

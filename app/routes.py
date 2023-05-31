from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')

@app.route('/name/', defaults={'name' : "Anonim"})
@app.route('/name/<name>')
def name(name=None):
    return f"Hello {name}"

@app.route('/author')
def author():
    return render_template('oAutorze.html')

@app.route('/ekstrakcja')
def ekstrakcja():
   
    
        

    return render_template('ekstrakcja_opinii.html')

@app.route('/lista_produktów')
def listaproduktow():

    return render_template('lista_produktów.html')

@app.route('/produkt')
def produkt():
    return render_template('produkt.html')
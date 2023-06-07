from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')


@app.route('/author')
def author():
    return render_template('oAutorze.html')

@app.route('/ekstrakcja')
def ekstrakcja():
   return render_template('ekstrakcja_opinii.html')

@app.route('/listaproduktow')
def listaproduktow():
    return render_template('lista_produktow.html')

@app.route('/produkt')
def produkt():
    return render_template('produkt.html')
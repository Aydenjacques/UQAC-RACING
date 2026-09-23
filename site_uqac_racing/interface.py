from flask import Flask, render_template, request, redirect, make_response,session
from functools import wraps
import uuid
import os
import ast
app = Flask(__name__)

  

   

@app.route("/")
def index():

    return redirect("/acceuil.html")

@app.route("/commanditaire.html")
def commanditaire():
    return render_template("commanditaire.html")

@app.route("/acceuil.html")
def acceuil():
    return render_template("acceuil.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/equipe.html")
def equipe():
    return render_template("equipe.html")

@app.route("/galerie.html")
def galerie():
    return render_template("galerie.html")

@app.route("/voiture.html")
def voiture():
    return render_template("voiture.html")

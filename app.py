from flask import Flask, render_template, request
import pandas as pd     #importar pandas al proyecto
import re
import matplotlib.pyplot as plt
import io           #renderizar gráficos
import base64

from datetime import datetime

app = Flask(__name__)
# Flask app.route decorador paa mapear la ruta URL / a esta función

paciente= {}
@app.route("/")
def home():
    return "Hola locos"

   

@app.route("/pagina2")
def pagina2():
   return render_template("index.html", paciente= paciente)
#>>>>---------------------------------------------------->


#>>>>---------------------------------------------------->


#>>>>---------------------------------------------------->  

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method== 'POST':
        usuario= request.form['username']
        return f'Bienvenido, {usuario}'
    return '''
    <form method= "post">
    Usuario: <input type= "text" name="username">
    <br>
    <input type= "submit" value="Enviar">
    </form> '''


#>>>>---------------------------------------------------->


#>>>>---------------------------------------------------->




#>>>--------------------------------->  Imagen con plot
@app.route('/integrarGráficos')
def integrarGraficos():

        #Cargar archivo csv
        df= pd.read_csv('data/inscritosCompetencia.csv')

        df.groupby("Nombre Participante")["Edad"].plot(kind="barh", color="orange")
        plt.title("Comparativo Practicantes por Edad")
        plt.xlabel("Edades")
        plt.ylabel("Practicantes activos")
        
        
        

        buf= io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        imagen= base64.b64encode(buf.getvalue()).decode('utf8')


#>>>---------------------------------> Imagen dinámica
        labels= ["Principiantes", "Intermedios", "Avanzados", "Destacados"]
        junior= [9, 6, 9, 2]
        mayores= [1, 2, 2, 1]
        return render_template("index1.html", labels= labels, junior= junior, mayores= mayores, imagen= imagen)



  

       


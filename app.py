from flask import Flask, render_template
#inizializza l'app Flask
app = Flask(__name__)
#rotta principale
lista_spesa=[]
@app.route('/')
def home():
    return render_template('index.html',lista=lista_spesa)
#avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/aggiungi', methods=['POST'])
def aggiungi():
#ottiene elemento dal form
    elemento = request.form['elemento']
#aggiunge alla lista
    if elemento:
        lista_spesa.append(elemento)
    return redirect(url_for('home'))
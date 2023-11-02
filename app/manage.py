from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Configuration de la base de données PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@db:5432/mydatabase'
db = SQLAlchemy(app)

# Modèle de données
class Connexion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Créez la table "Connexion" si elle n'existe pas
with app.app_context():
    db.create_all()

@app.route('/')
def hello_world():
    # Obtenir l'adresse IP du client
    client_ip = request.remote_addr
    
    # Obtenir l'heure actuelle
    current_time = datetime.utcnow()

    # Exemple d'ajout d'une nouvelle connexion à la base de données avec l'adresse IP
    new_connexion = Connexion(name=f'{client_ip}')
    db.session.add(new_connexion)
    db.session.commit()

    return 'Nouvelle connexion ajoutée à la base de données avec l\'adresse IP et l\'heure de connexion!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)


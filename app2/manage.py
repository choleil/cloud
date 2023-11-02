from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Configuration de la base de données PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@db:5432/mydatabase'
db = SQLAlchemy(app)

# Modèle de données pour les connexions
class Connexion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Créez la table "Connexion" si elle n'existe pas
with app.app_context():
    db.create_all()

@app.route('/')
def get_connexions():
    # Récupérez toutes les connexions depuis la base de données
    connexions = Connexion.query.all()
    
    if connexions:
        # Si des connexions existent, retournez-les au format JSON
        connexions_data = [{'id': connexion.id, 'name': connexion.name, 'timestamp': str(connexion.timestamp)} for connexion in connexions]
        return jsonify("Voici l'historique des connexions:",connexions_data)
        
    else:
        # Si la liste de connexions est vide, affichez un message personnalisé
        return "Il n'y a aucune connexion enregistrée pour le moment."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)


"""convertire l'app in modo da avere delle chiamate a servizi rest e restituiscono un json postman postman o su brownswer a video
2)500 404 gestione di errori e ritorna un json 
3) creazione di un docker per vedere se funziona tutto """

from datetime import datetime
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, jsonify
from flask_cors import CORS 
import json

app = Flask(__name__)
CORS(app)
#per vedere l'ip della macchina sotto linux ip addr show
# Configurazione database 
db_config = {
    "host": "127.0.0.1",  # Cambio con l'indirizzo IP della macchina
    "port": "5432",
    "dbname":"accademia",
    "user": "postgres",
    "password": "postgres"
}

def get_db_connection():
    try:
        return psycopg2.connect(**db_config, cursor_factory=RealDictCursor) #  La sintassi ** decompone il dizionario db_config in attributi chiave valore
    # cursor_factory=RealDictCursor: Specifica il tipo di cursore da utilizzare. In questo caso:
    #RealDictCursor restituisce i risultati delle query come un elenco di dizionari, dove le chiavi sono i nomi delle colonne e
    #i valori sono i dati associati. Questo formato Ã¨ molto utile per lavorare con dati strutturati, specialmente quando si usa JSON come risposta.
    except Exception as e:
        return str(e)

def carica_json(percorso: str):
    try:
        with open(percorso, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"error": f"File non trovato: {percorso}"}
    except json.JSONDecodeError:
        return {"error": f"Errore nella decodifica del file JSON: {percorso}"}
    except PermissionError:
        return {"error": f"Permesso negato per il file: {percorso}"}
    except Exception as e:
        return {"error": f"Errore generico: {str(e)}"}

def calcola_durata_in_giorni(data_inizio, data_fine):
    try:
        # Converti le stringhe di data in oggetti datetime
        data_inizio = datetime.strptime(data_inizio, '%Y-%m-%d')
        data_fine = datetime.strptime(data_fine, '%Y-%m-%d')
        # Calcola la durata in giorni
        durata = (data_fine - data_inizio).days
        return durata
    except Exception as e:
        return {"error": f"Errore nel calcolo della durata: {str(e)}"}

@app.route('/1', methods=['GET'])
def get_progetto():
    
    try:
        connection = get_db_connection()

        if (type(connection) == str):

            json_backup = carica_json('./json/progetti.json')

            for row in json_backup:
                row['durata'] = calcola_durata_in_giorni(row['inizio'], row['fine'])
            
            return jsonify(json_backup)
        
        else:
            cursor = connection.cursor()
            cursor.execute("SELECT *, (fine - inizio) AS durata_in_giorni FROM progetto")
            risultato = cursor.fetchall()
            cursor.close()
            connection.close()
            return jsonify(risultato)
    except psycopg2.Error as e:
            
        return jsonify({"error": f"Errore nel database : {str(e)}"}), 500
    

@app.route('/2', methods=['GET'])
def get_assenza():
    
    try:
        connection = get_db_connection()

        if (type(connection) == str):

            json_backup = carica_json('./json/assenze.json')

            json_persone = carica_json('./json/persone.json')


            for row in json_backup:
                
                for persona in json_persone:


                    print(f"{persona['id']}" + " " + f"{row['persona']}")

                    if persona['id'] == row['persona']:

                        row['persona'] = f"{persona['id']}) {persona['nome']} {persona['cognome']}"
        
            print(json_backup)
            return jsonify(json_backup)
        else:

            cursor = connection.cursor()
            query = "SELECT a.id as aid, p.id as pid, p.nome, p. cognome, a.tipo, a.giorno FROM assenza as a, persona as p WHERE a.persona = p.id;"
            cursor.execute(query)
            risultato = cursor.fetchall()
            cursor.close()
            connection.close()
            return jsonify(risultato)
    except psycopg2.Error as e:
            return jsonify({"error": f"Errore nel database : {str(e)}"}), 500
    

@app.route('/3', methods=['GET'])
def get_persona():
    
    try:
        connection = get_db_connection()

        if (type(connection) == str):

            json_backup = carica_json('./json/persone.json')
            
            json_assenze = carica_json('./json/assenze.json')

            for persona in json_backup:

                persona['assenze'] = 0

                for assenza in json_assenze:

                    if ( persona['id'] == assenza['persona']):

                         persona['assenze'] += 1

            
            
            return jsonify(json_backup)
        
        else:
            connection = get_db_connection()
            cursor = connection.cursor()

            query1 = "SELECT p.id, p.nome, p.cognome, p.posizione, p.stipendio, COUNT(a.persona) AS numero_assenze "
            query2 = "FROM persona AS p  LEFT JOIN assenza AS a ON p.id = a.persona "
            query3 = "GROUP BY p.id, p.nome, p.cognome, p.posizione, p.stipendio "
            query4 = "ORDER BY p.id;"
            query = query1 + query2 + query3 + query4
            cursor.execute(query)
            risultato = cursor.fetchall()
            cursor.close()
            connection.close()

        return jsonify(risultato)
    except psycopg2.Error as e:
            return jsonify({"error": f"Errore nel database : {str(e)}"}), 500
   
"""@app.route('/4/<string:table_name>', methods=['GET'])
def get_table(table_name):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        risultato = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(risultato)
    except psycopg2.Error as e:
        return jsonify({"error": f"Errore nel database : {str(e)}"}), 500"""
    

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Risorsa non trovata"}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Errore interno del server"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
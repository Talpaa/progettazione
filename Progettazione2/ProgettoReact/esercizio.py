"""convertire l'app in modo da avere delle chiamate a servizi rest e restituiscono un json postman postman o su brownswer a video
2)500 404 gestione di errori e ritorna un json 
3) creazione di un docker per vedere se funziona tutto """

import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, jsonify
from flask_cors import CORS 

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

@app.route('/1', methods=['GET'])
def get_progetto():
    
        connection = get_db_connection()
        print(connection)
        cursor = connection.cursor()
        cursor.execute("SELECT *, (fine - inizio) AS durata_in_giorni FROM progetto")
        risultato = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(risultato)
    

@app.route('/2', methods=['GET'])
def get_assenza():
    
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "SELECT a.id as aid, p.id as pid, p.nome, p. cognome, a.tipo, a.giorno FROM assenza as a, persona as p WHERE a.persona = p.id;"
        cursor.execute(query)
        risultato = cursor.fetchall()
        cursor.close()
        connection.close()
        print(risultato)
        return jsonify(risultato)
    

@app.route('/3', methods=['GET'])
def get_persona():
    
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
        #print(risultato)
        return jsonify(risultato)
   
@app.route('/4/<string:table_name>', methods=['GET'])
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
        return jsonify({"error": f"Errore nel database : {str(e)}"}), 500
    

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Risorsa non trovata"}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Errore interno del server"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
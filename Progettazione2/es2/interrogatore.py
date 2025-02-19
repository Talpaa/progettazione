import connect_db as db
from myjson import JsonDeserialize, JsonSerialize
cursor = db.connection.cursor()

cursor.execute('''select *
from persona p, attivitaprogetto ap
where p.id = ap.persona''')

rows = cursor.fetchall()

for row in rows:
    print(row)
print()
cursor.execute("Select * From attivitaprogetto")

rows = cursor.fetchall()

for row in rows:
    print(row)
print()
cursor.execute("Select * From progetto")

rows = cursor.fetchall()

for row in rows:
    print(row)

i = '0'

while (i != '4'):

    print('''Inserisci\n
          1) Per visualizzare una tabella;
          2) Per viualizzare una colonna in particolare della tabella;
          3) Per visualizzare una tabella con una condizione;
          4) EXIT.

    ''')

    i = input('\n    SCELTA: ')

    if i == '1':
        tab = input('Inserisci il nome della tabella: ')
        cursor.execute(f"Select * From {tab}")

        rows = cursor.fetchall()

        for row in rows:
            print(row)
        
        JsonSerialize(rows, f'{tab}.json')
    elif i == '2':
        tab = input('Inserisci il nome della tabella: ')
        col = input('Inserisci il nome della colonna: ')
        cursor.execute(f"Select {col} From {tab}")

        rows = cursor.fetchall()

        for row in rows:
            print(row)
    elif i == '3':
        tab = input('Inserisci il nome della tabella: ')
        cond = input('Inserisci la condizione: ')
        cursor.execute(f"Select * From {tab} where {cond}")

        rows = cursor.fetchall()

        for row in rows:
            print(row)
    elif i == '4':
        print('Arrivederci.')
    else:
        print('Scelta inesistente.')

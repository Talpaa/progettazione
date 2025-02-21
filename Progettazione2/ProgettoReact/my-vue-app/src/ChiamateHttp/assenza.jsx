import { useState, useEffect } from 'react';
import Table from 'react-bootstrap/Table';
import './stile.css'

function Assenza() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Effettua una chiamata HTTP con fetch
    fetch('http://127.0.0.1:5004/2')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Errore nella risposta del server');
        }
        return response.json(); // Converte la risposta in formato JSON
      })
      .then((data) => {
        setUsers(data);  // Imposta lo stato con i dati ricevuti
        setLoading(false); // Rimuove lo stato di caricamento
      })
      .catch((error) => {
        setError(error.message); // Gestisce gli errori
        setLoading(false);
      });
  }, []); // L'array vuoto significa che la chiamata HTTP avviene una sola volta, al primo render

  if (loading) return <p>Caricamento...</p>;
  if (error) return <p>Errore: {error}</p>;

  return (
    <div>

      <container className="title-container">
      <h2 id='title'>Elenco Assenze</h2>
      </container>

      <Table striped bordered hover>
        <thead>
          <tr>
            <th id="title-column">ID</th>
            <th id="title-column">PERSONA</th>
            <th id="title-column">TIPO</th>
            <th id="title-column">GIORNO</th>
          </tr>
        </thead>
        <tbody>
          {users.map((user) => (
            <tr key={user.id}>
              <td> {user.id}</td>
              <td>{user.persona}</td>
              <td>{user.tipo}</td>
              <td>{user.giorno}</td>
            </tr>

            /* 
            <tr key={user.aid}>
              <td> {user.aid}</td>
              <td>{user.pid}-{user.nome} {user.cognome}</td>
              <td>{user.tipo}</td>
              <td>{user.giorno}</td>
            </tr>
            */
          ))}
        </tbody>
      </Table>
    </div>
  );
};

export default Assenza;

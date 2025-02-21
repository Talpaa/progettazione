import { useState, useEffect } from 'react';
import Table from 'react-bootstrap/Table';

import './stile.css';

function Persona() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:5004/3')
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Errore ${response.status}: ${response.statusText}`);
        }
        return response.json();
      })
      .then((data) => setUsers(data))
      .catch((error) => setError(error.message))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p>Caricamento...</p>;
  if (error) return <p style={{ color: 'red' }}>Errore: {error}</p>;

  return (
    <div>
      <container className="title-container">
      <h2 id='title'>Elenco Persone</h2>
      </container>

      <Table striped bordered hover>
        <thead>
          <tr>
            <th id="title-column">ID</th>
            <th id="title-column">NOME</th>
            <th id="title-column">COGNOME</th>
            <th id="title-column">POSIZIONE</th>
            <th id="title-column">STIPENDIO</th>
            <th id="title-column">ASSENZE</th> {/* Aggiungi la colonna per le assenze */}
          </tr>
        </thead>
        <tbody>
          {users.map((user) => (
            <tr key={user.id}>
              <td>{user.id}</td>
              <td>{user.nome}</td>
              <td>{user.cognome}</td>
              <td>{user.posizione}</td>
              <td>{user.stipendio}</td>
              <td>{user.assenze}</td> {/* Aggiungi il numero di assenze */}
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
};

export default Persona;

import { useState, useEffect } from 'react';
import Table from 'react-bootstrap/Table';
import './stile.css'


function Wp() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Effettua una chiamata HTTP con fetch
    fetch('http://127.0.0.1:5004/1')
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
      <h2 id='title'>Elenco Progetti</h2>
      </container>
      
      <Table striped bordered hover>
        <thead>
          <tr>
            <th id="title-column">ID</th>
            <th id="title-column">NOME</th>
            <th id="title-column">DURATA</th>
            <th id="title-column">INIZIO</th>
            <th id="title-column">FINE</th>
            <th id="title-column">BUDGET</th>
          </tr>
        </thead>
        <tbody>
          {users.map((user) => (
            <tr key={user.id}>
              <td>{user.id}</td>
              <td>{user.nome}</td>
              <td>{user.durata} giorni</td>
              <td>{user.inizio}</td>
              <td>{user.fine}</td>
              <td>{user.budget}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
};

export default Wp;

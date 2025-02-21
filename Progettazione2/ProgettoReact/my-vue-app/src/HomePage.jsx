// HomePage.jsx
import { Link } from 'react-router-dom';
import './HomePage.css'; // Importa il file CSS per questa pagina

function HomePage() {
  return (
    <div className="home-container">
      <container className="title-container">
      <h2 id='title'>Home Page</h2>
      </container>

      <section className="home-content">
        <div className="home-card">
          <h2>Elenco<br />Progetti </h2>
          <Link to="/progetti" className="home-link">Visualizza progetti</Link>
        </div>

        <div className="home-card">
          <h2>Elenco<br />Assenze</h2>
          <Link to="/assenze" className="home-link">Visualizza Assenze</Link>
        </div>

        <div className="home-card">
          <h2>Elenco<br />Persone</h2>
          <Link to="/persone" className="home-link">Visualizza Persone</Link>
        </div>
      </section>
    </div>
  );
}

export default HomePage;

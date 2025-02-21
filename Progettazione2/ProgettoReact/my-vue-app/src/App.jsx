import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './HomePage'; // Importiamo la nuova pagina iniziale
import Persona from './ChiamateHttp/persona';
import Assenza from './ChiamateHttp/assenza';
import Progetto from './ChiamateHttp/progetto';
import './App.css';
import Header from './components/Header';

function App() {
  

  return (
    <Router>
      <Header /> {/* Usa il componente Navbar qui */}

      <main className="main-content">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/progetti" element={<Progetto />} />
          <Route path="/assenze" element={<Assenza />} />
          <Route path="/persone" element={<Persona />} />
        </Routes>
      </main>
    </Router>
  );
}

export default App;

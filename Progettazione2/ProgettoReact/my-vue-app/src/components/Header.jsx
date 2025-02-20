// Header.jsx
import { useLocation } from 'react-router-dom';

import Navbar from './Navbar';

function Header() {
  const location = useLocation();  // Ottieni la posizione corrente della pagina

  // Verifica se siamo sulla homepage
  const isHomePage = location.pathname === '/';

  // Mostra l'header solo se non siamo sulla homepage
  if (isHomePage) {
    return null;  // Non rendere nulla se siamo sulla homepage
  }

  return (
    <header className="header">
      <div className="logo">
          
      </div>
      <Navbar /> {/* Usa il componente Navbar qui */}
    </header>
  );
}

export default Header;

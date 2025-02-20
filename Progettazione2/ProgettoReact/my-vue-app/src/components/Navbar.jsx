import { Link, useLocation } from 'react-router-dom';

function Navbar() {

    const location = useLocation();
  
    const isHomePage = location.pathname === '/';
    const isWpPage = location.pathname === '/wp';
    const isAssenzaPage = location.pathname === '/assenza';
    const isPersonaPage = location.pathname === '/persona';

    return (
        // Se non siamo sulla homepage, mostriamo la navbar
        !isHomePage && (
          <nav>
            <ul className="nav-links">
              {/* Link per la Home */}
              <li><Link to="/" className="nav-item">Home</Link></li>
    
              {/* Nascondi il link 'Elenco WP' se siamo sulla pagina '/wp' */}
              {!isWpPage && <li><Link to="/wp" className="nav-item">Elenco Progetti</Link></li>}
    
              {/* Nascondi il link 'Elenco Assenze' se siamo sulla pagina '/assenza' */}
              {!isAssenzaPage && <li><Link to="/assenza" className="nav-item">Elenco Assenze</Link></li>}
    
              {/* Nascondi il link 'Elenco Persone' se siamo sulla pagina '/persona' */}
              {!isPersonaPage && <li><Link to="/persona" className="nav-item">Elenco Persone</Link></li>}
            </ul>
          </nav>
        )
      );
    }
    
export default Navbar;
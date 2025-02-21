import { Link, useLocation } from 'react-router-dom';

function Navbar() {

    const location = useLocation();
  
    const isHomePage = location.pathname === '/';
    const isWpPage = location.pathname === '/progetti';
    const isAssenzaPage = location.pathname === '/assenze';
    const isPersonaPage = location.pathname === '/persone';

    return (
        // Se non siamo sulla homepage, mostriamo la navbar
        !isHomePage && (
          <nav>
            <ul className="nav-links">
              {/* Link per la Home */}
              <li><Link to="/" className="nav-item">Home</Link></li>
    
              {/* Nascondi il link 'Elenco WP' se siamo sulla pagina '/wp' */}
              {!isWpPage && <li><Link to="/progetti" className="nav-item">Elenco Progetti</Link></li>}
    
              {/* Nascondi il link 'Elenco Assenze' se siamo sulla pagina '/assenza' */}
              {!isAssenzaPage && <li><Link to="/assenze" className="nav-item">Elenco Assenze</Link></li>}
    
              {/* Nascondi il link 'Elenco Persone' se siamo sulla pagina '/persona' */}
              {!isPersonaPage && <li><Link to="/persone" className="nav-item">Elenco Persone</Link></li>}
            </ul>
          </nav>
        )
      );
    }
    
export default Navbar;
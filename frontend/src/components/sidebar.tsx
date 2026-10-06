import { Link } from "react-router-dom";

function Sidebar() {
  return (
    <aside className="sidebar">

      <h2>Biblioteca</h2>

      <nav>

        <Link to="/dashboard">
          Dashboard
        </Link>

        <Link to="/livros">
          Livros
        </Link>

        <Link to="/usuarios">
          Usuários
        </Link>

        <Link to="/emprestimos">
          Empréstimos
        </Link>

        <Link to="/perfil">
          Perfil
        </Link>

      </nav>

    </aside>
  );
}

export default Sidebar;
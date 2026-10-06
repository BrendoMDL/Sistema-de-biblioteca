import Navbar from "../components/navbar";
import Sidebar from "../components/sidebar";

function Usuarios() {
  return (
    <div className="layout">

      <Sidebar />

      <main className="main-content">

        <Navbar />

        <h1>Usuários</h1>

        <p>
          Aqui serão exibidos os usuários cadastrados.
        </p>

      </main>

    </div>
  );
}

export default Usuarios;
import Navbar from "../components/navbar";
import Sidebar from "../components/sidebar";

function Perfil() {
  return (
    <div className="layout">

      <Sidebar />

      <main className="main-content">

        <Navbar />

        <h1>Meu Perfil</h1>

        <p>
          Informações do usuário.
        </p>

      </main>

    </div>
  );
}

export default Perfil;
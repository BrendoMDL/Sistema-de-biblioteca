import Navbar from "../components/navbar";
import Sidebar from "../components/sidebar";

function Emprestimos() {
  return (
    <div className="layout">

      <Sidebar />

      <main className="main-content">

        <Navbar />

        <h1>Empréstimos</h1>

        <p>
          Aqui serão exibidos os empréstimos dos livros.
        </p>

      </main>

    </div>
  );
}

export default Emprestimos;
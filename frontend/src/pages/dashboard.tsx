import Navbar from "../components/navbar";
import Sidebar from "../components/sidebar";

function Dashboard() {
  return (
    <div className="layout">

      <Sidebar />

      <main className="main-content">

        <Navbar />

        <section className="dashboard">

          <h1>Dashboard</h1>

          <div className="cards">

            <div className="dashboard-card">
              <h3>Livros</h3>
              <p>0</p>
            </div>

            <div className="dashboard-card">
              <h3>Usuários</h3>
              <p>0</p>
            </div>

            <div className="dashboard-card">
              <h3>Empréstimos</h3>
              <p>0</p>
            </div>

            <div className="dashboard-card">
              <h3>Atrasados</h3>
              <p>0</p>
            </div>

          </div>

        </section>

      </main>

    </div>
  );
}

export default Dashboard;
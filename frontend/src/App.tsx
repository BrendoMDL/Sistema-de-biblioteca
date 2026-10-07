import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/login";
import Dashboard from "./pages/dashboard";
import Livros from "./pages/livros";
import NovoLivro from "./pages/novolivro";
import Usuarios from "./pages/usuarios";
import Emprestimos from "./pages/emprestimos";
import Perfil from "./pages/perfil";

function App() {
  return (
    <BrowserRouter>

      <Routes>

        <Route
          path="/"
          element={<Login />}
        />

        <Route
          path="/login"
          element={<Login />}
        />

        <Route
          path="/dashboard"
          element={<Dashboard />}
        />

        <Route
          path="/livros"
          element={<Livros />}
        />

        <Route
          path="/livros/novo"
          element={<NovoLivro />}
        />

        <Route
          path="/usuarios"
          element={<Usuarios />}
        />

        <Route
          path="/emprestimos"
          element={<Emprestimos />}
        />

        <Route
          path="/perfil"
          element={<Perfil />}
        />

      </Routes>

    </BrowserRouter>
  );
}

export default App;
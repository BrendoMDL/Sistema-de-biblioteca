import { useState } from "react";
import { useNavigate } from "react-router-dom";

function Login() {

  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");

  function handleLogin(event: React.FormEvent) {

    event.preventDefault();

    console.log("Email:", email);
    console.log("Senha:", senha);

    // Temporariamente vamos entrar no dashboard.
    // Depois vamos substituir isso pela autenticação do FastAPI.
    navigate("/dashboard");
  }

  return (
    <div className="login-container">

      <div className="login-box">

        <h1>📚 Biblioteca</h1>

        <h2>Login</h2>

        <form onSubmit={handleLogin}>

          <div>
            <label>Email</label>

            <input
              type="email"
              value={email}
              onChange={(event) => setEmail(event.target.value)}
              placeholder="Digite seu email"
              required
            />
          </div>

          <div>
            <label>Senha</label>

            <input
              type="password"
              value={senha}
              onChange={(event) => setSenha(event.target.value)}
              placeholder="Digite sua senha"
              required
            />
          </div>

          <button type="submit">
            Entrar
          </button>

        </form>

      </div>

    </div>
  );
}

export default Login;
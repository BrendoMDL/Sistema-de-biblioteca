import { useState } from "react";
import { useNavigate } from "react-router-dom";

function NovoLivro() {

  const navigate = useNavigate();

  const [titulo, setTitulo] = useState("");
  const [autor, setAutor] = useState("");
  const [isbn, setIsbn] = useState("");
  const [editora, setEditora] = useState("");
  const [anoPublicacao, setAnoPublicacao] = useState("");
  const [categoria, setCategoria] = useState("");
  const [quantidade, setQuantidade] = useState(0);
  const [descricao, setDescricao] = useState("");

  function handleSubmit(event: React.FormEvent) {

    event.preventDefault();

    const livro = {
      titulo,
      autor,
      isbn,
      editora,
      ano_publicacao: Number(anoPublicacao),
      categoria,
      quantidade,
      descricao
    };

    console.log(livro);

    // Depois enviaremos para:
    // POST /livros/

    navigate("/livros");
  }

  return (
    <div className="layout">

      <main className="main-content">

        <h1>Novo Livro</h1>

        <form onSubmit={handleSubmit}>

          <div>
            <label>Título</label>

            <input
              type="text"
              value={titulo}
              onChange={(event) => setTitulo(event.target.value)}
              required
            />
          </div>

          <div>
            <label>Autor</label>

            <input
              type="text"
              value={autor}
              onChange={(event) => setAutor(event.target.value)}
              required
            />
          </div>

          <div>
            <label>ISBN</label>

            <input
              type="text"
              value={isbn}
              onChange={(event) => setIsbn(event.target.value)}
              required
            />
          </div>

          <div>
            <label>Editora</label>

            <input
              type="text"
              value={editora}
              onChange={(event) => setEditora(event.target.value)}
            />
          </div>

          <div>
            <label>Ano de publicação</label>

            <input
              type="number"
              value={anoPublicacao}
              onChange={(event) => setAnoPublicacao(event.target.value)}
            />
          </div>

          <div>
            <label>Categoria</label>

            <input
              type="text"
              value={categoria}
              onChange={(event) => setCategoria(event.target.value)}
            />
          </div>

          <div>
            <label>Quantidade</label>

            <input
              type="number"
              min="0"
              value={quantidade}
              onChange={(event) => setQuantidade(Number(event.target.value))}
            />
          </div>

          <div>
            <label>Descrição</label>

            <textarea
              value={descricao}
              onChange={(event) => setDescricao(event.target.value)}
            />
          </div>

          <button type="submit">
            Cadastrar livro
          </button>

        </form>

      </main>

    </div>
  );
}

export default NovoLivro;
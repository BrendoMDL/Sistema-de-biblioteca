import { useState } from "react";
import { useNavigate } from "react-router-dom";

import api from "../services/api";

import type { LivroCreate } from "../types/livro";


function NovoLivro() {

  // Permite navegar para outra página depois do cadastro
  const navigate = useNavigate();


  // Estados dos campos do formulário
  const [titulo, setTitulo] = useState("");
  const [autor, setAutor] = useState("");
  const [isbn, setIsbn] = useState("");
  const [editora, setEditora] = useState("");
  const [anoPublicacao, setAnoPublicacao] = useState("");
  const [categoria, setCategoria] = useState("");
  const [quantidade, setQuantidade] = useState(0);
  const [descricao, setDescricao] = useState("");


  // Controla o estado do botão enquanto a requisição está acontecendo
  const [carregando, setCarregando] = useState(false);


  // Guarda mensagem de erro
  const [erro, setErro] = useState("");


  // Função executada quando o formulário é enviado
  async function handleSubmit(
    event: React.FormEvent<HTMLFormElement>
  ) {

    // Impede o navegador de recarregar a página
    event.preventDefault();


    // Limpa mensagens de erro anteriores
    setErro("");


    // Informa que estamos enviando os dados
    setCarregando(true);


    // Monta o objeto que será enviado para o FastAPI
    const livro: LivroCreate = {
      titulo: titulo,
      autor: autor,
      isbn: isbn,
      editora: editora || undefined,
      ano_publicacao: anoPublicacao
        ? Number(anoPublicacao)
        : undefined,
      categoria: categoria || undefined,
      quantidade: quantidade,
      descricao: descricao || undefined
    };


    try {

      // Faz uma requisição POST para o FastAPI
      //
      // A URL completa será:
      // http://127.0.0.1:8000/livros/
      //
      // O objeto "livro" será enviado no corpo da requisição.
      const resposta = await api.post(
        "/livros/",
        livro
      );


      // Mostra no console a resposta recebida do backend
      console.log(
        "Livro cadastrado:",
        resposta.data
      );


      // Informa ao usuário que deu certo
      alert("Livro cadastrado com sucesso!");


      // Volta para a página de livros
      navigate("/livros");


    } catch (error: unknown) {

      console.error(
        "Erro ao cadastrar livro:",
        error
      );


      // Verifica se o FastAPI enviou uma mensagem de erro
      if (error instanceof Object && "response" in error) {

        const detalhe = (error as { response: { data: { detail: string } } }).response.data?.detail;


        if (typeof detalhe === "string") {

          setErro(detalhe);

        } else {

          setErro(
            "Não foi possível cadastrar o livro."
          );

        }

      } else {

        // Caso o backend esteja desligado,
        // ou exista algum problema de conexão.
        setErro(
          "Não foi possível conectar ao servidor."
        );

      }

    } finally {

      // Libera novamente o botão
      setCarregando(false);

    }
  }


  return (
    <div className="layout">

      <main className="main-content">

        <h1>Novo Livro</h1>


        {/* Mensagem de erro */}
        {erro && (
          <div className="erro">
            {erro}
          </div>
        )}


        <form onSubmit={handleSubmit}>


          {/* TÍTULO */}
          <div>
            <label htmlFor="titulo">
              Título
            </label>

            <input
              id="titulo"
              type="text"
              value={titulo}
              onChange={(event) =>
                setTitulo(event.target.value)
              }
              placeholder="Digite o título do livro"
              required
            />
          </div>


          {/* AUTOR */}
          <div>
            <label htmlFor="autor">
              Autor
            </label>

            <input
              id="autor"
              type="text"
              value={autor}
              onChange={(event) =>
                setAutor(event.target.value)
              }
              placeholder="Digite o nome do autor"
              required
            />
          </div>


          {/* ISBN */}
          <div>
            <label htmlFor="isbn">
              ISBN
            </label>

            <input
              id="isbn"
              type="text"
              value={isbn}
              onChange={(event) =>
                setIsbn(event.target.value)
              }
              placeholder="Digite o ISBN"
              required
            />
          </div>


          {/* EDITORA */}
          <div>
            <label htmlFor="editora">
              Editora
            </label>

            <input
              id="editora"
              type="text"
              value={editora}
              onChange={(event) =>
                setEditora(event.target.value)
              }
              placeholder="Digite a editora"
            />
          </div>


          {/* ANO DE PUBLICAÇÃO */}
          <div>
            <label htmlFor="anoPublicacao">
              Ano de publicação
            </label>

            <input
              id="anoPublicacao"
              type="number"
              value={anoPublicacao}
              onChange={(event) =>
                setAnoPublicacao(event.target.value)
              }
              placeholder="Ex: 2024"
            />
          </div>


          {/* CATEGORIA */}
          <div>
            <label htmlFor="categoria">
              Categoria
            </label>

            <input
              id="categoria"
              type="text"
              value={categoria}
              onChange={(event) =>
                setCategoria(event.target.value)
              }
              placeholder="Ex: Romance, Fantasia, Tecnologia..."
            />
          </div>


          {/* QUANTIDADE */}
          <div>
            <label htmlFor="quantidade">
              Quantidade
            </label>

            <input
              id="quantidade"
              type="number"
              min="0"
              value={quantidade}
              onChange={(event) =>
                setQuantidade(
                  Number(event.target.value)
                )
              }
              required
            />
          </div>


          {/* DESCRIÇÃO */}
          <div>
            <label htmlFor="descricao">
              Descrição
            </label>

            <textarea
              id="descricao"
              value={descricao}
              onChange={(event) =>
                setDescricao(event.target.value)
              }
              placeholder="Digite uma descrição do livro"
            />
          </div>


          {/* BOTÃO */}
          <button
            type="submit"
            disabled={carregando}
          >

            {carregando
              ? "Cadastrando..."
              : "Cadastrar livro"}

          </button>


        </form>

      </main>

    </div>
  );
}


export default NovoLivro;
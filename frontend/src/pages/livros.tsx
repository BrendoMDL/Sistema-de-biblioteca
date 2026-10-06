import { useEffect, useState } from "react";

import Navbar from "../components/navbar";
import Sidebar from "../components/sidebar";
import LivroCard from "../components/livrocard";
import Loading from "../components/loading";

import api from "../services/api";

import type { Livro } from "../types/livro";


function Livros() {

  // Guarda os livros recebidos do FastAPI
  const [livros, setLivros] = useState<Livro[]>([]);

  // Controla o estado de carregamento
  const [carregando, setCarregando] = useState(true);

  // Guarda uma possível mensagem de erro
  const [erro, setErro] = useState("");


  // Executa quando a página é carregada
  useEffect(() => {

    async function buscarLivros() {

      try {

        setCarregando(true);

        setErro("");

        // Faz uma requisição GET para:
        // http://127.0.0.1:8000/livros/
        const resposta = await api.get<Livro[]>("/livros/");

        // Guarda os livros recebidos do FastAPI
        setLivros(resposta.data);

      } catch (error) {

        console.error(
          "Erro ao buscar livros:",
          error
        );

        setErro(
          "Não foi possível carregar os livros."
        );

      } finally {

        setCarregando(false);

      }
    }

    buscarLivros();

  }, []);


  return (
    <div className="layout">

      <Sidebar />

      <main className="main-content">

        <Navbar />

        <section>

          <h1>Livros</h1>

          <p>
            Livros cadastrados na biblioteca.
          </p>


          {/* Botão para cadastrar um novo livro */}
          <button
            onClick={() => {
              window.location.href = "/livros/novo";
            }}
          >
            + Novo livro
          </button>


          {/* Estado de carregamento */}
          {carregando && (
            <Loading />
          )}


          {/* Mensagem de erro */}
          {!carregando && erro && (
            <div className="erro">
              {erro}
            </div>
          )}


          {/* Lista de livros */}
          {!carregando && !erro && (

            <div className="livros-grid">

              {livros.length === 0 ? (

                <p>
                  Nenhum livro cadastrado.
                </p>

              ) : (

                livros.map((livro) => (

                  <LivroCard
                    key={livro.id}
                    livro={livro}
                  />

                ))

              )}

            </div>

          )}

        </section>

      </main>

    </div>
  );
}

export default Livros;
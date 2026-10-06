interface Livro {
  id: number;
  titulo: string;
  autor: string;
  isbn: string;
  categoria?: string;
  quantidade: number;
}

interface LivroCardProps {
  livro: Livro;
}

function LivroCard({ livro }: LivroCardProps) {
  return (
    <div className="livro-card">

      <h3>{livro.titulo}</h3>

      <p>
        <strong>Autor:</strong> {livro.autor}
      </p>

      <p>
        <strong>ISBN:</strong> {livro.isbn}
      </p>

      <p>
        <strong>Categoria:</strong>{" "}
        {livro.categoria || "Não informada"}
      </p>

      <p>
        <strong>Disponíveis:</strong> {livro.quantidade}
      </p>

    </div>
  );
}

export default LivroCard;
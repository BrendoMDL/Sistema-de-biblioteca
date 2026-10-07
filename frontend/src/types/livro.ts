export interface Livro {
  id: number;
  titulo: string;
  autor: string;
  isbn: string;
  editora?: string;
  ano_publicacao?: number;
  categoria?: string;
  quantidade: number;
  descricao?: string;
}

export interface LivroCreate {
  titulo: string;
  autor: string;
  isbn: string;
  editora?: string;
  ano_publicacao?: number;
  categoria?: string;
  quantidade: number;
  descricao?: string;
}

export interface LivroUpdate {
  titulo?: string;
  autor?: string;
  isbn?: string;
  editora?: string;
  ano_publicacao?: number;
  categoria?: string;
  quantidade?: number;
  descricao?: string;
}
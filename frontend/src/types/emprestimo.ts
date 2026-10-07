export interface Emprestimo {
  id: number;
  usuario_id: number;
  livro_id: number;
  data_emprestimo: string;
  data_prevista_devolucao: string;
  data_devolucao?: string;
  status: string;
}

export interface EmprestimoCreate {
  usuario_id: number;
  livro_id: number;
  data_prevista_devolucao: string;
}
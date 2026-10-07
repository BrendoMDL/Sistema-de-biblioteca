export interface Usuario {
  id: number;
  nome: string;
  cpf: string;
  email: string;
  telefone?: string;
  tipo: string;
}

export interface UsuarioCreate {
  nome: string;
  cpf: string;
  email: string;
  telefone?: string;
  senha: string;
  tipo?: string;
}
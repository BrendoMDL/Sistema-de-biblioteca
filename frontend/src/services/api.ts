import axios from "axios";

// URL da API definida durante o build para producao.
// Se nao houver configuracao, utiliza o endereco local.
const api = axios.create({
  baseURL:
    import.meta.env.VITE_API_URL ||
    "http://127.0.0.1:8000",
});

export default api;
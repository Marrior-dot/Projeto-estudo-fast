import axios from 'axios'; //Biblioteca para fazer requisições HTTP

//Instância do axios baseada na URL da API
const api = axios.create({
  baseURL: "http://localhost:8000"
});

//Exporta a instância do axios, api para poder reaproveitar a URL base
export default api;
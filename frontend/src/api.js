import axios from 'axios';

const API = axios.create({
  baseURL: process.env.REACT_APP_API_BASE_URL,
});

// If you later add auth, you can intercept requests here:
// API.interceptors.request.use(config => { ... });

export default API;

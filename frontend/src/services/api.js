import axios from "axios";

export const api = axios.create({
  baseURL: import.meta.env.VITE_APP_API_BASE_URL,
  withCredentials: true,
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers["Authorization"] = `Bearer ${token}`;
  }
  return config;
});

export const login = async (credentials) => {
    const response = await api.post('/login/', credentials);
    if (response.data.access && response.data.refresh) {
        localStorage.setItem('token', response.data.access);
        localStorage.setItem('refresh', response.data.refresh);
    }
    return response.data;
};

export const refreshToken = async (refresh) => {
  try {
    const response = await api.post('/refresh/', { refresh });
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const logout = async (refresh_token) => {
    const response = await api.post("/logout/", refresh_token);
    localStorage.removeItem('token');
    localStorage.removeItem('refresh');
}

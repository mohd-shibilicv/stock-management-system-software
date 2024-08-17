import { setTokenExpired } from "@/features/slices/authSlice";
import store from "@/features/store";
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

api.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (
      error.response.status === 401 &&
      error.response.data.messages &&
      error.response.data.messages[0] &&
      error.response.data.messages[0].message === "Token is invalid or expired"
    ) {
      // Dispatch an action to show the token expiration modal
      store.dispatch(setTokenExpired(true));

      return Promise.reject(error);
    }
    return Promise.reject(error);
  }
);

export const login = async (credentials) => {
  const response = await api.post("/login/", credentials);
  if (response.data.access && response.data.refresh) {
    localStorage.setItem("token", response.data.access);
    localStorage.setItem("refresh", response.data.refresh);
  }
  return response.data;
};

export const refreshToken = async (refresh) => {
  try {
    const response = await api.post("/refresh/", { refresh });
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const logout = async () => {
  const refresh_token = localStorage.getItem('refresh');
  try {
      await api.post("/logout/", { refresh_token });
  } catch (error) {
      console.error("Logout error:", error);
  } finally {
      localStorage.removeItem('token');
      localStorage.removeItem('refresh');
  }
};

import axios from "axios";

export const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000/api/v1",
  timeout: 30000,
});

export async function uploadProductImage(file) {
  const formData = new FormData();
  formData.append("file", file);
  const response = await api.post("/scan", formData);
  return response.data;
}

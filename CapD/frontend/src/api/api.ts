import axios from "axios"

const api = axios.create({
  baseURL: "http://localhost:8000", // FastAPI 백엔드 주소
})

export default api
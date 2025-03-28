import { BrowserRouter, Routes, Route, Link } from "react-router-dom"
import NewsPage from "./pages/NewsPage"
import SearchPage from "./pages/SearchPage"

export default function App() {
  return (
    <BrowserRouter>
      <nav className="flex gap-4 p-4 border-b">
        <Link to="/">뉴스 등록</Link>
        <Link to="/search">뉴스 검색</Link>
      </nav>
      <Routes>
        <Route path="/" element={<NewsPage />} />
        <Route path="/search" element={<SearchPage />} />
      </Routes>
    </BrowserRouter>
  )
}

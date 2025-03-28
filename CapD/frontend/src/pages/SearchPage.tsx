import { useState } from "react"
import api from "../api/api"

interface SearchResult {
  id: number
  score: number
  summary: string
}

export default function SearchPage() {
  const [query, setQuery] = useState("")
  const [results, setResults] = useState<SearchResult[]>([])

  const handleSearch = async () => {
    const res = await api.get("/search", { params: { q: query } })
    setResults(res.data)
  }

  return (
    <div className="max-w-xl mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">뉴스 요약 검색</h1>
      <input className="border w-full p-2 mb-2" placeholder="검색어" value={query} onChange={(e) => setQuery(e.target.value)} />
      <button className="bg-green-500 text-white px-4 py-2 rounded" onClick={handleSearch}>검색</button>

      <ul className="mt-4 space-y-2">
        {results.map((item) => (
          <li key={item.id} className="p-3 border rounded bg-gray-50">
            <div className="text-sm text-gray-600">유사도: {item.score.toFixed(3)}</div>
            <p>{item.summary}</p>
          </li>
        ))}
      </ul>
    </div>
  )
}

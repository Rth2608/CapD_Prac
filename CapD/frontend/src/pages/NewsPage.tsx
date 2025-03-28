import { useState } from "react"
import api from "../api/api"

export default function NewsPage() {
  const [title, setTitle] = useState("")
  const [content, setContent] = useState("")
  const [summary, setSummary] = useState("")

  const handleSubmit = async () => {
    const res = await api.post("/news", { title, content })
    setSummary(res.data.summary)
  }

  return (
    <div className="max-w-xl mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">뉴스 등록</h1>
      <input className="border w-full p-2 mb-2" placeholder="제목" value={title} onChange={(e) => setTitle(e.target.value)} />
      <textarea className="border w-full p-2 mb-2 h-32" placeholder="내용" value={content} onChange={(e) => setContent(e.target.value)} />
      <button className="bg-blue-500 text-white px-4 py-2 rounded" onClick={handleSubmit}>요약 요청</button>

      {summary && (
        <div className="mt-4 bg-gray-100 p-4 rounded">
          <h2 className="font-bold">요약 결과:</h2>
          <p>{summary}</p>
        </div>
      )}
    </div>
  )
}

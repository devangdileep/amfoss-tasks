import { useState, useEffect } from 'react'
import MovieCard from '../components/MovieCard'

export default function Home({ search, onSelect, onAdd, isAdded }) {
  const [movies, setMovies] = useState([])
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const key = import.meta.env.VITE_TMDB_API_KEY
    if (!key) return

    let url = 'https://api.themoviedb.org/3/movie/popular?api_key=' + key
    if (search && search.trim() !== '') {
      url = 'https://api.themoviedb.org/3/search/movie?api_key=' + key + '&query=' + encodeURIComponent(search)
    }

    async function getMovies() {
      try {
        const res = await fetch(url)
        const data = await res.json()
        setMovies(data.results || [])
      } catch (err) {
        setError(err.message)
      } finally {
        setLoading(false)
      }
    }

    getMovies()
  }, [search])

  return (
    <div className="container page">
      <h2>{search ? 'Search Results' : 'Popular Movies'}</h2>
      {error && <div className="err-msg">{error}</div>}
      {loading && <div className="loading-msg">Loading...</div>}
      {!loading && movies.length === 0 && (
        <div className="empty-msg">No movies found.</div>
      )}
      {!loading && movies.length > 0 && (
        <div className="grid">
          {movies.map((movie) => (
            <MovieCard
              key={movie.id}
              movie={movie}
              onSelect={onSelect}
              onAdd={onAdd}
              isAdded={isAdded(movie.id)}
            />
          ))}
        </div>
      )}
    </div>
  )
}

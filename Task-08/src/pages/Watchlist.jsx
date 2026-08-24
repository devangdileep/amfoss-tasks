import { useState } from 'react'
import MovieCard from '../components/MovieCard'

export default function Watchlist({ list, user, openAuth, onSelect, onAdd, isAdded }) {
  const [tab, setTab] = useState('want')

  if (!user) {
    return (
      <div className="container page center">
        <h2>My Watchlist</h2>
        <div className="auth-prompt">
          <p>Please login to see your watchlist.</p>
          <button className="btn-main" onClick={openAuth}>
            Login
          </button>
        </div>
      </div>
    )
  }

  const movies = list.filter((m) => m.status === tab)

  return (
    <div className="container page">
      <h2 className="page-title">My Watchlist</h2>

      <div className="tabs">
        <button
          className={tab === 'want' ? 'tab active' : 'tab'}
          onClick={() => setTab('want')}
        >
          Want to Watch ({list.filter((m) => m.status === 'want').length})
        </button>
        <button
          className={tab === 'watched' ? 'tab active' : 'tab'}
          onClick={() => setTab('watched')}
        >
          Watched ({list.filter((m) => m.status === 'watched').length})
        </button>
      </div>

      {movies.length === 0 ? (
        <div className="empty-msg">No movies in this list.</div>
      ) : (
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

export default function MovieCard({ movie, onSelect, onAdd, isAdded }) {
  const img = movie.poster_path
    ? 'https://image.tmdb.org/t/p/w500' + movie.poster_path
    : 'https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=500&auto=format&fit=crop&q=60'

  return (
    <div className="movie-card" onClick={() => onSelect(movie)}>
      <div className="img-box">
        <img src={img} alt={movie.title} />
      </div>
      <div className="info">
        <div className="title">{movie.title}</div>
        <div className="meta">
          <span>{movie.release_date || ''}</span>
          <span>⭐ {movie.vote_average || '0.0'}</span>
        </div>
        <button
          className={isAdded ? 'btn-card added' : 'btn-card'}
          onClick={(e) => {
            e.stopPropagation()
            onAdd(movie)
          }}
        >
          {isAdded ? '✓ Added' : '+ Add'}
        </button>
      </div>
    </div>
  )
}

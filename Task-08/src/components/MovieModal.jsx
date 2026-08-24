export default function MovieModal({ movie, onClose, onAdd, onWatch, isAdded, isWatched }) {
  if (!movie) return null

  const img = movie.poster_path
    ? 'https://image.tmdb.org/t/p/w500' + movie.poster_path
    : 'https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=500&auto=format&fit=crop&q=60'

  return (
    <div className="modal-bg" onClick={onClose}>
      <div className="modal-box" onClick={(e) => e.stopPropagation()}>
        <button className="close-btn" onClick={onClose}>✕</button>
        <div className="modal-body">
          <img src={img} alt={movie.title} className="modal-img" />
          <div className="modal-info">
            <h2>{movie.title}</h2>
            <p className="desc">{movie.overview || 'No overview available.'}</p>
            <p>Rating: ⭐ {movie.vote_average || '0.0'}</p>
            <p>Release Date: {movie.release_date || 'Unknown'}</p>
            <div className="modal-btns">
              <button className="btn-main" onClick={() => onAdd(movie)}>
                {isAdded ? 'Remove from Watchlist' : '+ Add to Watchlist'}
              </button>
              <button
                className={isWatched ? 'btn-sub watched' : 'btn-sub'}
                onClick={() => onWatch(movie)}
              >
                {isWatched ? '✓ Watched' : 'Mark as Watched'}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

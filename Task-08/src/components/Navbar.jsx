export default function Navbar({ page, setPage, search, setSearch, count, user, openAuth, logout }) {
  return (
    <div className="navbar">
      <div className="container nav-box">
        <h1 className="logo" onClick={() => setPage('home')}>
          Ohara Archive
        </h1>

        <div className="search-box">
          <input
            type="text"
            placeholder="Search movies..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />
        </div>

        <div className="nav-btns">
          <button className={page === 'home' ? 'nav-link active' : 'nav-link'} onClick={() => setPage('home')}>
            Home
          </button>
          <button className={page === 'watchlist' ? 'nav-link active' : 'nav-link'} onClick={() => setPage('watchlist')}>
            Watchlist ({count})
          </button>

          {user ? (
            <div className="user-box">
              <span>{user.email}</span>
              <button className="logout-btn" onClick={logout}>
                Logout
              </button>
            </div>
          ) : (
            <button className="login-btn" onClick={openAuth}>
              Login
            </button>
          )}
        </div>
      </div>
    </div>
  )
}

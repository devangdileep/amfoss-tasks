import { useState, useEffect } from 'react'
import Navbar from './components/Navbar'
import MovieModal from './components/MovieModal'
import AuthModal from './components/AuthModal'
import Home from './pages/Home'
import Watchlist from './pages/Watchlist'
import { supabase } from './supabase'

import './css/global.css'
import './css/navbar.css'
import './css/movies.css'
import './css/modal.css'
import './css/watchlist.css'

export default function App() {
  const [page, setPage] = useState('home')
  const [search, setSearch] = useState('')
  const [selected, setSelected] = useState(null)
  const [showAuth, setShowAuth] = useState(false)
  const [user, setUser] = useState(null)
  const [watchlist, setWatchlist] = useState([])

  async function getWatchlist(userId) {
    if (!supabase || !userId) return
    const res = await supabase
      .from('watchlist')
      .select('*')
      .eq('user_id', userId)

    if (res.data) {
      const items = res.data.map((item) => ({
        id: Number(item.movie_id),
        title: item.title,
        poster_path: item.poster_path,
        release_date: item.release_date,
        vote_average: item.vote_average,
        overview: item.overview,
        status: item.status
      }))
      setWatchlist(items)
    }
  }

  useEffect(() => {
    if (!supabase) return

    supabase.auth.getUser().then((res) => {
      const currentUser = res.data ? res.data.user : null
      setUser(currentUser)
      if (currentUser) {
        getWatchlist(currentUser.id)
      }
    }).catch(() => {})

    const { data: authListener } = supabase.auth.onAuthStateChange((event, session) => {
      const currentUser = session ? session.user : null
      setUser(currentUser)
      if (currentUser) {
        getWatchlist(currentUser.id)
      } else {
        setWatchlist([])
      }
    })

    return () => {
      if (authListener && authListener.subscription) {
        authListener.subscription.unsubscribe()
      }
    }
  }, [])

  async function handleAdd(movie) {
    if (!user) {
      setShowAuth(true)
      return
    }

    const movieId = Number(movie.id)
    const exists = watchlist.find((item) => Number(item.id) === movieId)

    if (exists) {
      setWatchlist(watchlist.filter((item) => Number(item.id) !== movieId))
      if (supabase) {
        await supabase
          .from('watchlist')
          .delete()
          .eq('movie_id', movieId)
          .eq('user_id', user.id)
      }
    } else {
      const newItem = {
        id: movieId,
        title: movie.title,
        release_date: movie.release_date,
        vote_average: movie.vote_average,
        poster_path: movie.poster_path,
        overview: movie.overview,
        status: 'want'
      }

      setWatchlist([...watchlist, newItem])

      if (supabase) {
        await supabase.from('watchlist').upsert({
          user_id: user.id,
          movie_id: movieId,
          title: movie.title,
          poster_path: movie.poster_path,
          release_date: movie.release_date,
          vote_average: movie.vote_average,
          overview: movie.overview,
          status: 'want'
        }, { onConflict: 'user_id,movie_id' })
      }
    }
  }

  async function handleWatch(movie) {
    if (!user) {
      setShowAuth(true)
      return
    }

    const movieId = Number(movie.id)
    const exists = watchlist.find((item) => Number(item.id) === movieId)
    const newStatus = (exists && exists.status === 'watched') ? 'want' : 'watched'

    if (exists) {
      setWatchlist(watchlist.map((item) => Number(item.id) === movieId ? { ...item, status: newStatus } : item))
    } else {
      const newItem = {
        id: movieId,
        title: movie.title,
        release_date: movie.release_date,
        vote_average: movie.vote_average,
        poster_path: movie.poster_path,
        overview: movie.overview,
        status: newStatus
      }
      setWatchlist([...watchlist, newItem])
    }

    if (supabase) {
      await supabase.from('watchlist').upsert({
        user_id: user.id,
        movie_id: movieId,
        title: movie.title,
        poster_path: movie.poster_path,
        release_date: movie.release_date,
        vote_average: movie.vote_average,
        overview: movie.overview,
        status: newStatus
      }, { onConflict: 'user_id,movie_id' })
    }
  }

  async function handleLogout() {
    if (supabase) {
      await supabase.auth.signOut()
    }
    setUser(null)
    setWatchlist([])
  }

  function isAdded(id) {
    return watchlist.some((item) => Number(item.id) === Number(id))
  }

  function isWatched(id) {
    const found = watchlist.find((item) => Number(item.id) === Number(id))
    return found ? found.status === 'watched' : false
  }

  return (
    <div>
      <Navbar
        page={page}
        setPage={setPage}
        search={search}
        setSearch={setSearch}
        count={watchlist.length}
        user={user}
        openAuth={() => setShowAuth(true)}
        logout={handleLogout}
      />

      {page === 'home' ? (
        <Home
          search={search}
          onSelect={(movie) => setSelected(movie)}
          onAdd={handleAdd}
          isAdded={isAdded}
        />
      ) : (
        <Watchlist
          list={watchlist}
          user={user}
          openAuth={() => setShowAuth(true)}
          onSelect={(movie) => setSelected(movie)}
          onAdd={handleAdd}
          isAdded={isAdded}
        />
      )}

      {selected && (
        <MovieModal
          movie={selected}
          onClose={() => setSelected(null)}
          onAdd={handleAdd}
          onWatch={handleWatch}
          isAdded={isAdded(selected.id)}
          isWatched={isWatched(selected.id)}
        />
      )}

      {showAuth && (
        <AuthModal
          onClose={() => setShowAuth(false)}
          onSuccess={(currentUser) => {
            if (currentUser) getWatchlist(currentUser.id)
          }}
        />
      )}
    </div>
  )
}

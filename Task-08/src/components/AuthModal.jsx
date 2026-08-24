import { useState } from 'react'
import { supabase } from '../supabase'

export default function AuthModal({ onClose, onSuccess }) {
  const [isLogin, setIsLogin] = useState(true)
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')

  async function handleSubmit(e) {
    e.preventDefault()
    setError('')

    if (!supabase) {
      setError('Supabase is not configured')
      return
    }

    if (isLogin) {
      const res = await supabase.auth.signInWithPassword({
        email: email,
        password: password
      })
      if (res.error) {
        setError(res.error.message)
      } else {
        onSuccess(res.data.user)
        onClose()
      }
    } else {
      const res = await supabase.auth.signUp({
        email: email,
        password: password
      })
      if (res.error) {
        setError(res.error.message)
      } else {
        onSuccess(res.data.user)
        onClose()
      }
    }
  }

  return (
    <div className="modal-bg" onClick={onClose}>
      <div className="modal-box auth-box" onClick={(e) => e.stopPropagation()}>
        <button className="close-btn" onClick={onClose}>✕</button>
        <h3>{isLogin ? 'Login' : 'Register'}</h3>

        <div className="auth-tabs">
          <button
            className={isLogin ? 'tab-btn active' : 'tab-btn'}
            onClick={() => {
              setIsLogin(true)
              setError('')
            }}
          >
            Login
          </button>
          <button
            className={!isLogin ? 'tab-btn active' : 'tab-btn'}
            onClick={() => {
              setIsLogin(false)
              setError('')
            }}
          >
            Register
          </button>
        </div>

        {error && <div className="err-box">{error}</div>}

        <form onSubmit={handleSubmit} className="auth-form">
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <button type="submit" className="btn-main">
            {isLogin ? 'Login' : 'Register'}
          </button>
        </form>
      </div>
    </div>
  )
}

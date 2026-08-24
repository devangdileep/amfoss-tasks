# Ohara Archive - Movie Watchlist

A movie watchlist web app built with React, Vite, TMDB API, and Supabase.

## Implementation Brief

- **Project Structure**: Organized code into `components/` (Navbar, MovieCard, MovieModal, AuthModal), `pages/` (Home, Watchlist), and `css/` for stylesheets.
- **TMDB API**: Fetches popular movies and handles live title searches with real-time poster images and ratings.
- **Movie Modal**: Opens when a card is clicked to show movie overview, release date, and watchlist action buttons.
- **Supabase Auth**: Implemented user signup and login to manage individual user sessions.
- **Supabase Database**: Stores and syncs the user's movie watchlist in a `watchlist` table with "Want to Watch" and "Watched" status.

## What I Learned

- Managing component state and data fetching using `useState` and `useEffect`.
- Integrating external REST APIs (TMDB) with `fetch` and handling async operations.
- Setting up user authentication and database CRUD operations using Supabase.
- Structuring React applications with reusable components and clean CSS.
- Storing environment variables securely in `.env`.

## Setup

```bash
npm install
npm run dev
```

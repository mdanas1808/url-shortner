import React, { useState } from 'react';
import './App.css';

function App() {
  const [originalUrl, setOriginalUrl] = useState('');
  const [shortenedUrl, setShortenedUrl] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();

    const response = await fetch('http://localhost:5000/shorten', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ original_url: originalUrl }),
    });

    const data = await response.json();
    setShortenedUrl(data.short_url); // Get shortened URL from the response
  };

  return (
    <div className="App">
      <h1>URL Shortener</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="original_url">Original URL:</label>
        <input
          type="text"
          id="original_url"
          value={originalUrl}
          onChange={(e) => setOriginalUrl(e.target.value)}
          required
        />
        <button type="submit">Shorten URL</button>
      </form>

      {shortenedUrl && (
        <div>
          <h2>Shortened URL:</h2>
          <p>{shortenedUrl}</p>
        </div>
      )}
    </div>
  );
}

export default App;


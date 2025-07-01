import React, { useState } from 'react';
import { Routes, Route, Link } from 'react-router-dom';

function Home() {
  return <h1 className="text-2xl">Welcome to Tactic CRM</h1>;
}

export default function App() {
  const [mode, setMode] = useState('STUDIO');

  return (
    <div className="p-4">
      <header className="mb-4 flex justify-between items-center">
        <nav>
          <Link to="/" className="mr-4">Home</Link>
        </nav>
        <button onClick={() => setMode(mode === 'STUDIO' ? 'LIVE' : 'STUDIO')}>
          Switch Mode: {mode}
        </button>
      </header>
      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
    </div>
  );
}

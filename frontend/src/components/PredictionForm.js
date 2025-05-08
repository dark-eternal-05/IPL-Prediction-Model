import React, { useState } from 'react';
import API from '../api';

export default function PredictionForm({ onResult }) {
  const [teamA, setTeamA] = useState('');
  const [teamB, setTeamB] = useState('');
  const [date, setDate] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const matchId = `IPL-${Date.now()}`;
    try {
      const res = await API.post('/predict/', {
        team_a: teamA,
        team_b: teamB,
        match_id: matchId,
        date,
      });
      onResult(res.data);
    } catch (err) {
      console.error(err);
      alert('Error fetching prediction');
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: 20 }}>
      <div>
        <input
          type="text"
          placeholder="Team A"
          value={teamA}
          onChange={(e) => setTeamA(e.target.value)}
          required
        />
      </div>
      <div>
        <input
          type="text"
          placeholder="Team B"
          value={teamB}
          onChange={(e) => setTeamB(e.target.value)}
          required
        />
      </div>
      <div>
        <input
          type="datetime-local"
          value={date}
          onChange={(e) => setDate(e.target.value)}
          required
        />
      </div>
      <button type="submit">Predict</button>
    </form>
  );
}

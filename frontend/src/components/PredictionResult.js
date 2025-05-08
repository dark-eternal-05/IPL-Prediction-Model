import React from 'react';

export default function PredictionResult({ result }) {
  if (!result) return null;

  return (
    <div style={{ border: '1px solid #ccc', padding: 10, marginBottom: 20 }}>
      <h3>Predicted Winner: {result.predicted_winner}</h3>
      <p>
        Score — {result.team_a_score} : {result.team_b_score}
      </p>
      <p>
        Confidence Interval: {result.confidence_interval[0]} –{' '}
        {result.confidence_interval[1]}
      </p>
      <p>
        <strong>Explanation:</strong> {result.explanation}
      </p>
    </div>
  );
}

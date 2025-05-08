import React, { useState } from 'react';
import PredictionForm from './components/PredictionForm';
import PredictionResult from './components/PredictionResult';
import LiveUpdates from './components/LiveUpdates';
import Chatbot from './components/Chatbot';

function App() {
  const [result, setResult] = useState(null);

  return (
    <div style={{ maxWidth: 600, margin: '0 auto', padding: 20 }}>
      <h1>IPL Predictor</h1>
      <PredictionForm onResult={setResult} />
      <PredictionResult result={result} />
      <LiveUpdates />
      <Chatbot />
    </div>
  );
}

export default App;

import React, { useState } from 'react';
import API from '../api';

export default function Chatbot() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');

  const ask = async () => {
    try {
      const res = await API.post('/llm-chat/', { query });
      setResponse(res.data.response);
    } catch (err) {
      console.error(err);
      setResponse('Error contacting LLM');
    }
  };

  return (
    <div style={{ border: '1px solid #ddd', padding: 10 }}>
      <h4>Chatbot</h4>
      <textarea
        rows={3}
        style={{ width: '100%' }}
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Ask about predictions..."
      />
      <button onClick={ask}>Send</button>
      {response && (
        <pre style={{ whiteSpace: 'pre-wrap', marginTop: 10 }}>
          {response}
        </pre>
      )}
    </div>
  );
}

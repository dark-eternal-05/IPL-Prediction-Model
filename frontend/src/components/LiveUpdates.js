import React from 'react';
import useWebSocket from '../hooks/useWebSocket';

export default function LiveUpdates() {
  const update = useWebSocket(process.env.REACT_APP_WS_URL);

  if (!update) return null;

  return (
    <div style={{ border: '1px dashed #666', padding: 10, marginBottom: 20 }}>
      <h4>Live Match Update</h4>
      <pre style={{ whiteSpace: 'pre-wrap' }}>
        {JSON.stringify(update, null, 2)}
      </pre>
    </div>
  );
}

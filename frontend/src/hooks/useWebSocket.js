import { useEffect, useState } from 'react';

const useWebSocket = (url) => {
  const [message, setMessage] = useState(null);

  useEffect(() => {
    const ws = new WebSocket(url);
    ws.onmessage = (e) => {
      try {
        setMessage(JSON.parse(e.data));
      } catch {
        setMessage(e.data);
      }
    };
    return () => ws.close();
  }, [url]);

  return message;
};

export default useWebSocket;

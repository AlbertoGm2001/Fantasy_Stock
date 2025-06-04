
//Renderiza App.jsx en un div de id 'root' del archivo HTML index.html, que es lo que se muestra en el navegador. 


import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);



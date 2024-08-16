import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import TradingViews from './pages/TradingViews';
function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path="/trading_views" element={<TradingViews />} />
          <Route path="/" element={<div>Home Page</div>} />
        </Routes>
      </Router>
    </>
  );
}

export default App;

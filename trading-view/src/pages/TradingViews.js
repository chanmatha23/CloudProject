import React from 'react';
import TradingViewWidget from '../components/TradingViewWidget';

const TradingViews = ({ symbol }) => {
  return (
    <div className="min-h-screen h-screen bg-black text-white flex flex-col">
      <div className="container mx-auto py-10 flex-grow">
        <h1 className="text-3xl font-bold mb-8 text-center">Trading View Chart for {symbol.toUpperCase()}</h1>
        <div className="bg-gray-800 p-6 rounded-lg shadow-lg h-full">
          <TradingViewWidget symbol={symbol} />
        </div>
      </div>
    </div>
  );
};

export default TradingViews;

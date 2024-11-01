import React from 'react';
import { useParams } from 'react-router-dom';
import TradingViewWidget from '../components/TradingViewWidget';

const StockChartPage = () => {
  const { symbol } = useParams();

  return (
    <div className="min-h-screen bg-black text-white">
      <div className="container mx-auto py-10 px-4 sm:px-6 lg:px-8">
        <h1 className="text-2xl sm:text-3xl font-bold mb-8 text-center">Trading View Chart for {symbol.toUpperCase()}</h1>
        <div className="bg-gray-800 p-4 sm:p-6 rounded-lg shadow-lg h-96 sm:h-[500px]">
          <TradingViewWidget symbol={symbol} />
        </div>
      </div>
    </div>
  );
};

export default StockChartPage;

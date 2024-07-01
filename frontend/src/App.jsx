import React from 'react';
import Plot from 'react-plotly.js';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Backtesting Program</h1>
        <Plot
          data={[
            {
              x: [1, 2, 3, 4],
              y: [2, 6, 3, 5],
              type: 'scatter',
              mode: 'lines+markers',
              marker: { color: 'red' },
            },
          ]}
          layout={{ width: 720, height: 440, title: 'A Fancy Plot' }}
        />
      </header>
    </div>
  );
}

export default App;

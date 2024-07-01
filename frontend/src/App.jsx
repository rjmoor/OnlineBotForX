// src/App.jsx
import React, { useState } from 'react';
import Sidebar from './components/Sidebar';
import AccountInfo from './components/AccountInfo';
import AutoTrade from './components/AutoTrade';
import Backtest from './components/Backtest';
import './styles/styles.scss';

function App() {
  const [section, setSection] = useState('account');

  return (
    <div className="App">
      <Sidebar setSection={setSection} />
      <div className="main-content">
        {section === 'account' && <AccountInfo />}
        {section === 'autotrade' && <AutoTrade />}
        {section === 'backtest' && <Backtest />}
      </div>
    </div>
  );
}

export default App;

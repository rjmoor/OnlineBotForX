// src/components/Sidebar.jsx
import React from "react";

function Sidebar({ setSection }) {
	return (
		<div className="sidebar">
			<ul>
				<li onClick={() => setSection("account")}>Account Info</li>
				<li onClick={() => setSection("autotrade")}>Auto Trade</li>
				<li onClick={() => setSection("backtest")}>Backtest</li>
			</ul>
		</div>
	);
}

export default Sidebar;

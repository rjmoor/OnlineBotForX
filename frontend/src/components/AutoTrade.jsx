// src/components/AutoTrade.jsx
import React, { useState, useEffect } from "react";
import axios from "axios";

function AutoTrade() {
	const [forexPairs, setForexPairs] = useState([]);
	const [selectedPair, setSelectedPair] = useState("");
	const [tradeStatus, setTradeStatus] = useState("red");

	useEffect(() => {
		async function fetchForexPairs() {
			const response = await axios.get("/api/forex/pairs");
			setForexPairs(response.data);
		}

		fetchForexPairs();
	}, []);

	useEffect(() => {
		if (selectedPair) {
			// Logic to update trade status and fetch historical information
		}
	}, [selectedPair]);

	return (
		<div>
			<h2>Auto Trade</h2>
			<select onChange={(e) => setSelectedPair(e.target.value)} value={selectedPair}>
				<option value="">Select Forex Pair</option>
				{forexPairs.map((pair) => (
					<option key={pair} value={pair}>
						{pair}
					</option>
				))}
			</select>
			<div className="trade-status">
				<div className={`light ${tradeStatus === "red" ? "red" : ""}`}></div>
				<div className={`light ${tradeStatus === "yellow" ? "yellow" : ""}`}></div>
				<div className={`light ${tradeStatus === "green" ? "green" : ""}`}></div>
			</div>
			{/* Display grid and trading information */}
		</div>
	);
}

export default AutoTrade;

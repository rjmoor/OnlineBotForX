// src/components/Backtest.jsx
import React from "react";
import Plot from "react-plotly.js";

function Backtest() {
	return (
		<div>
			<h2>Backtest</h2>
			<div className="backtest-grid">
				<div className="parameter-names">
					<p>RSI</p>
					<p>SMA</p>
					<p>EMA</p>
					<p>MACD</p>
					<p>BB</p>
					<p>STOCH</p>
				</div>
				<div className="indicator-selects">
					<select>
						<option>On</option>
						<option>Off</option>
					</select>
					<select>
						<option>On</option>
						<option>Off</option>
					</select>
					<select>
						<option>On</option>
						<option>Off</option>
					</select>
					<select>
						<option>On</option>
						<option>Off</option>
					</select>
					<select>
						<option>On</option>
						<option>Off</option>
					</select>
					<select>
						<option>On</option>
						<option>Off</option>
					</select>
				</div>
			</div>
			<Plot
				data={[
					{
						x: [1, 2, 3, 4],
						y: [2, 6, 3, 5],
						type: "scatter",
						mode: "lines+markers",
						marker: { color: "red" },
					},
				]}
				layout={{ width: 720, height: 440, title: "Profit/Loss Graph" }}
			/>
			<table>
				<thead>
					<tr>
						<th>Parameter</th>
						<th>Value</th>
					</tr>
				</thead>
				<tbody>
					<tr>
						<td>Profit</td>
						<td>$1000</td>
					</tr>
					{/* Add more rows as needed */}
				</tbody>
			</table>
		</div>
	);
}

export default Backtest;

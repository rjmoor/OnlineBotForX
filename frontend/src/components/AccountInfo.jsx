// src/components/AccountInfo.jsx
import React, { useEffect, useState } from "react";
import axios from "axios";

function AccountInfo() {
	const [accountDetails, setAccountDetails] = useState({});

	useEffect(() => {
		async function fetchAccountDetails() {
			const response = await axios.get("/api/account/details");
			setAccountDetails(response.data);
		}

		fetchAccountDetails();
	}, []);

	return (
		<div>
			<h2>Account Information</h2>
			<pre>{JSON.stringify(accountDetails, null, 2)}</pre>
		</div>
	);
}

export default AccountInfo;

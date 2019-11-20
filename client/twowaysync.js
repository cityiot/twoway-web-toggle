function init() {
	const toggle = document.getElementById("toggle1");

	toggle.addEventListener('change', (event) => {
		if (event.target.checked) {
			console.log('checked');
			setstate('automatic');
		} else {
			console.log('not checked');
			setstate('manual');
		}
	});

	return toggle;
}


async function setViewFromData(toggle) {
	let wmode = await getstate();
	if (wmode == 'automatic') {
		console.log('Set toggle to: automatic');
		toggle.checked = true;
	} else {
		console.log('Set toggle to: not automatic');
		toggle.checked = false;
	}
}

async function getstate() {
	const response = await fetch('https://cityiot-oulu.appspot.com/optimasolutions_get1');
	const rjson = await response.json();
	//console.log(JSON.stringify(rjson));

	const wmodedata = rjson['workingMode'];
	const wmode = wmodedata['value'];
	console.log("Got mode: " + wmode);

	return wmode;
}

async function setstate(statestring) {
	//const url = 'https://cityiot-oulu.appspot.com/optimasolutions_set1'
	const url = 'http://localhost:8080/optimasolutions_set1'
	const postDataText = `wms|${statestring}`;

	try {
		const response = await fetch(url, {
			method: 'POST', // or 'PUT'
			body: postDataText,
			headers: {
				'Content-Type': 'text/plain'
			}
		});
		const text = await response.text();
		console.log('Success:', text);
	} catch (error) {
		console.error('Error:', error);
	}
}

window.addEventListener('DOMContentLoaded', (event) => {
	console.log("DOMContentLoaded");
	const toggle = init();
	setViewFromData(toggle);
});

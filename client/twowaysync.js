function init() {
	const toggle = document.getElementById("toggle1");

	toggle.addEventListener('change', (event) => {
		if (event.target.checked) {
			console.log('checked');
			//getstate();
		} else {
			console.log('not checked');
			//getstate();
		}
	});

	return toggle;
}

async function setstate(toggle) {
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
	const response = await fetch('https://cityiot-oulu.appspot.com/optimasolutions1');
	const rjson = await response.json();
	//console.log(JSON.stringify(rjson));

	const wmodedata = rjson['workingMode'];
	const wmode = wmodedata['value'];
	console.log("Got mode: " + wmode);

	return wmode;
}

window.addEventListener('DOMContentLoaded', (event) => {
	console.log("DOMContentLoaded");
	const toggle = init();
	setstate(toggle);
});

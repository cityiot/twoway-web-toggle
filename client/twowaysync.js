function init() {
    const toggle1 = document.getElementById("toggle1");
    const toggle2 = document.getElementById("toggle2");

	toggle1.addEventListener('change', (event) => {
		if (event.target.checked) {
            console.log('checked');
			setstate('wms', 'automatic');
		} else {
			console.log('not checked');
            setstate('wms', 'manual');
		}
    });

    toggle2.addEventListener('change', (event) => {
        if (event.target.checked) {
            console.log('checked');
            setstate('pss', 'on');
        } else {
            console.log('not checked');
            setstate('pss', 'off');
        }
    });

	return [toggle1, toggle2];
}

function idasCommandString(attribute, value) {
    return `${attribute}|${value}`; //`wms|${statestring}`
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

	//Ossi's two variable system to make robust. Not configed to use now to test web ui, while his notification thing is not on
	//const wmodedata = rjson['workingMode'];
	const wmodedata = rjson['workingModeSet']; //this is what IDAS sets, and it's then reflected to workingMode. new Orion with notify-only-changed might well fix the need for this.
	const wmode = wmodedata['value'];
	//console.log("Got mode: " + wmode);

	return wmode;
}

async function setstate(attribute, value) {
	const url = 'https://cityiot-oulu.appspot.com/optimasolutions_set1'
	//const url = 'http://localhost:8080/optimasolutions_set1'
    
    const postDataText = idasCommandString(attribute, value);
	console.log(`Sending IDAS state: ${postDataText}`);

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
	const toggles = init();
	//setViewFromData(toggles);

	// repeat with the interval of 2 seconds (10 now)
	//let timerId = setInterval(() => setViewFromData(toggle), 10000);

	// after 5 seconds stop
	//setTimeout(() => { clearInterval(timerId); alert('stop'); }, 5000);
});

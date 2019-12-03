function init() {
    const toggle1 = document.getElementById("toggle1");
    const toggle2 = document.getElementById("toggle2");

	toggle1.addEventListener('change', (event) => {
		if (event.target.checked) {
            console.log('checked');
			setstate1('wms', 'automatic');
		} else {
			console.log('not checked');
            setstate1('wms', 'manual');
		}
    });

    toggle2.addEventListener('change', (event) => {
        if (event.target.checked) {
            console.log('checked');
            setstate2('pss', 'on');
        } else {
            console.log('not checked');
            setstate2('pss', 'off');
        }
    });

	return [toggle1, toggle2];
}

function idasCommandString(attribute, value) {
    return `${attribute}|${value}`; //`wms|${statestring}`
}

async function setViewFromDataWithGetterToToggle(getter, attrval, toggle) {
    let val = await getter();
    if (val == attrval) {
        console.log('Set toggle to:' + attrval);
        toggle.checked = true;
    } else {
        console.log('Set toggle to: not ' + attrval);
        toggle.checked = false;
    }
}

async function setViewFromData(toggles) {
    setViewFromDataWithGetterToToggle(getstate1, 'automatic', toggles[0]);
    setViewFromDataWithGetterToToggle(getstate2, 'on', toggles[1]);
}

async function getstateOfAttr(getterurl, attribute) {
    const baseurl = 'https://cityiot-oulu.appspot.com/';
    //const baseurl = 'http://localhost:8080/';

    const response = await fetch(baseurl + getterurl); //optimasolutions_get2
    const rjson = await response.json();

    const attrdata = rjson[attribute];
    const attrval = attrdata['value'];
    return attrval;
}

async function getstate1() {
    //this is what IDAS sets, and it's then reflected to workingMode. new Orion with notify-only-changed might well fix the need for this.
    const wmode = getstateOfAttr("optimasolutions_get1", 'workingMode')
	//console.log(JSON.stringify(rjson1));
	//Ossi's two variable system to make robust. Not configed to use now to test web ui, while his notification thing is not on
	//const wmodedata = rjson['workingMode'];
	console.log("Got workingMode: " + wmode);

	return wmode;
}

async function getstate2() {
    const pss = getstateOfAttr('optimasolutions_get2', 'powerState');
    console.log("Got powerState: " + pss);

    return pss;
}


async function setstateOfAttr(setterurl, attribute, value) {
	const baseUrl = 'https://cityiot-oulu.appspot.com/'
	//const baseUrl = 'http://localhost:8080/'

    const url = baseUrl + setterurl;
    
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

async function setstate1(attribute, value) {
    const setterurl = "optimasolutions_set1";
    setstateOfAttr(setterurl, attribute, value);
}

async function setstate2(attribute, value) {
    const setterurl = "optimasolutions_set2";
    setstateOfAttr(setterurl, attribute, value);
}

window.addEventListener('DOMContentLoaded', (event) => {
	console.log("DOMContentLoaded");
	const toggles = init();
	setViewFromData(toggles);

	// repeat with the interval of 2 seconds (10 now)
	let timerId = setInterval(() => setViewFromData(toggles), 3000);

	// after 5 seconds stop
	//setTimeout(() => { clearInterval(timerId); alert('stop'); }, 5000);
});

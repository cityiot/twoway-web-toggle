function init() {
	const toggle = document.getElementById("toggle1");

	toggle.addEventListener('change', (event) => {
		if (event.target.checked) {
			console.log('checked');
		} else {
			console.log('not checked');
		}
		});
}

window.addEventListener('DOMContentLoaded', (event) => {
	init();
});

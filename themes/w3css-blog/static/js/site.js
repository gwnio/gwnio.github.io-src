/**
 * https://www.w3schools.com/howto/howto_js_topnav_responsive.asp
 */
function topbarMenuButtonClickHandler() {
	var tb = document.getElementById("my-topbar");
	if (!tb.className.includes("responsive")) {
		tb.className += " responsive";
	} else {
		tb.className = "w3-bar w3-black";
	}
}
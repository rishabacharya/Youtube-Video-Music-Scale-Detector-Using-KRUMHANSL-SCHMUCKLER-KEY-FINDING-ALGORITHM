window.onload = function() {
	var dButton = document.getElementById('find');
	
	dButton.onclick = function(){
		console.log("button  clicked");
		chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
	    	var url = tabs[0].url;
            console.log(url);
            localStorage.setItem("url",url);
            document.getElementById("scale").onclick=function(){
                document.getElementById("scale").innerHTML=url;
            }
	    	var message  = {
	    		'url' : url
	    	};
	    	chrome.runtime.sendMessage(message);
		});
	};
}
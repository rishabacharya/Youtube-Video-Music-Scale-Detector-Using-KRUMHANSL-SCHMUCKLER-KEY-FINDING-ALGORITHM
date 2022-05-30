window.onload = function() {
	var dButton = document.getElementById('autofind');
	var dButtonf = document.getElementById('find');

	// for auto find button
	dButton.onclick = function(tab_url){
		console.log("button  clicked");
		chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
	    	var url = tabs[0].url;	
			var root_url = 'http://localhost:8000/'
			var xhr = new XMLHttpRequest();
			var path = "videofetch/?"
			var my_url = url
			var start_point = "x"
			var end_point = "x"
			var url = root_url + path + `url=${my_url}&start_time=${start_point}&end_time=${end_point}`;
			console.log(url)

			// var url = "http://192.168.100.163/rateUpdate";

		xhr.onreadystatechange = function() {
			if (this.readyState == 4 && this.status == 200) {
			// Typical action to be performed when the document is ready:
			if(xhr.responseText != null){
				console.log(xhr.responseText);
				link=xhr.responseText
				document.getElementById('scale').innerHTML=xhr.responseText;
				// localStorage.setItem("scale_title",xhr.responseText);

			}
		}
	};
	
	xhr.open("GET", url, true);
	xhr.send();
	
	
	
	
	
	
	    	// var message  = {
	    	// 	'url' : url
	    	// };

	    	// chrome.runtime.sendMessage(message);
		});
	};



	// for find button
	dButtonf.onclick = function(tab_url){
		console.log("findbutton  clicked");
		chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
	    	var url = tabs[0].url;

			var s=document.getElementById('hour').value+":"+document.getElementById('min').value+":"+document.getElementById('sec').value
			var e=document.getElementById('hour2').value+":"+document.getElementById('min2').value+":"+document.getElementById('sec2').value
			
			var root_url = 'http://localhost:8000/'

			var xhr = new XMLHttpRequest();
			var path = "videofetch/?"
			// localStorage.setItem("my_url",url);
			var my_url = url
			var start_point = s
			var end_point = e
			var url = root_url + path + `url=${my_url}&start_time=${start_point}&end_time=${end_point}`;
			console.log(url)

			// var url = "http://192.168.100.163/rateUpdate";

		xhr.onreadystatechange = function() {
			if (this.readyState == 4 && this.status == 200) {
			// Typical action to be performed when the document is ready:
			if(xhr.responseText != null){
				console.log(xhr.responseText);
				link=xhr.responseText
				document.getElementById('scale').innerHTML=xhr.responseText;
				localStorage.setItem("scale_title",xhr.responseText);

			}
		}
	};
	
	xhr.open("GET", url, true);
	xhr.send();
	
	
	
	
	
	
	    	var message  = {
	    		'url' : url
	    	};

	    	chrome.runtime.sendMessage(message);
		});
	};






	// console.log(url);
	// localStorage.setItem("url",url);
	
	
	
	
	
}
	// document.getElementById("scale").onclick=function(){

		// document.getElementById("scale").innerHTML=localStorage.getItem("scale_title");
	// }
	
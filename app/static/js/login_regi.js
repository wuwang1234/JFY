window.onload = function(){
	var Obutton_login = document.getElementById("button001")
	var Obutton_regi = document.getElementById("button002")
	var Ologin001 = document.getElementById("login001")
	var Oregi001 = document.getElementById("regi001")
	Obutton_login.onclick = function(){
		Ologin001.style.display='block'
		Oregi001.style.display='none'
		Obutton_login.style.color= 'red'
		Obutton_regi.style.color= '#333'
	}
	Obutton_regi.onclick = function(){
		Ologin001.style.display='none'
		Oregi001.style.display='block'
		Obutton_regi.style.color= 'red'
		Obutton_login.style.color = '#333'
	}
}


function checkAccount(){
	var account = document.getElementById("account").value
	if(account != 'admin'){
		return false
	}
	return true
}

function checkPwd(){
    var password = document.getElementById("password").value
	if( password != '123'){
		return false
	}
	return true
}


function checkForm() {
	if(!checkAccount()){
		alert('用户名或密码错误！')
		return false
	}
	if(!checkPwd()){
		alert('用户名或密码错误！')
		return false
    }
    
	return true
}

function rememberMeFun(){
	if (document.getElementById("rememberMe").checked){
		document.cookie="rememberMe=on";
	}else{
		document.cookie="rememberMe=off"
	}
}



function getCookie(c_name){
	// prompt('Please enter your name:',"");
	if (document.cookie.length>0){
		c_start=document.cookie.indexOf(c_name + "=")
		if (c_start!=-1){ 
			c_start=c_start + c_name.length+1 
			c_end=document.cookie.indexOf(";",c_start)
			if (c_end==-1) c_end=document.cookie.length
			return unescape(document.cookie.substring(c_start,c_end))
			}
	}
	return ""
}


function setCookies(){
	var rememberMeStatus = getCookie("rememberMe")
	if (rememberMeStatus == "on"){
		document.getElementById("rememberMe").checked = true;
	}else if(rememberMeStatus == 'off'){
		document.getElementById("rememberMe").checked=false;
	}else{
		document.getElementById("rememberMe").checked = true
		document.cookie="rememberMe=on";
	}

}

function ready(){
	setCookies()
}

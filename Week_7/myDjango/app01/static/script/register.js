function pwSame(){
    var password = document.getElementById('password').value
    var password2 = document.getElementById('password2').value
    if (password != password2 ){
        document.getElementsByClassName('pwlabel')[0].style.display = 'inline-block'
        return false
    }
    return true
}




function checkForm() {
	if( !pwSame() ){
		return false
	}

    alert('注册成功！')
	return true
}
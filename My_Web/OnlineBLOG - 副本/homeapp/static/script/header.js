
$(document).ready(function(){

    looginNickname();
    
    BGON();
    registerAjax();
});




function looginNickname(){
    $('#headerAccSpan').hide();
    if( $('#account').text()!=''){
        $('#headerVisitorSpan').hide();
        $('#headerAccSpan').show();
    }; 
}



function BGON(){
    $(".loginBGon").click(function(){
        $("#loginBG").fadeIn(500);
        $(".registerDiv").fadeOut(500);
        $(".loginDiv").fadeIn(500);
    });
    $("#loginBG").click(function(){
        $("#loginBG").fadeOut(500);
        $(".loginDiv").fadeOut(500);
    });
    
    $(".registerBGon").click(function(){
        $("#loginBG").fadeIn(500);
        $(".loginDiv").fadeOut(500);
        $(".registerDiv").fadeIn(500);
    });
    $("#loginBG").click(function(){
        $("#loginBG").fadeOut(500);
        $(".registerDiv").fadeOut(500);
    });
};

function registerAjax(){
    $("#registerSubmit").click(function(){
        var regaccount = $("#regaccount").val();
        var regpassword = $("#regpassword").val();
        var regnickname = $("#regnickname").val();
        alert(regaccount);
        alert(regpassword);
        alert(regnickname);
    
        $.ajax({
            url:"/blog/register/", 
            type:"POST", 
            headers:{"X-CSRFToken":$.cookie("csrftoken")},
            data:{"account":regaccount,"password":regpassword, "nickname":regnickname}, 
            success:function(info){ 
                alert(info);
                
                info = JSON.parse(info);
                // alert(info['status']);
                // alert(info.status);
                // alert(info['result']);
                // alert(info.result);

                if (info["status"]) {
                    $('#loginNickname').text()=info["nickname"];
                    $('#headerVisitorSpan').hide();
                    $('#headerAccSpan').show();
    
                    alert(info["result"]);
    
                } else {
    
                    alert(info["result"]);
                    alert('errr');
    
                };
            },
        });
    })

}

// {"status": true, "result": "\u6ce8\u518c\u6210\u529f\uff01", "nickname": "d"}

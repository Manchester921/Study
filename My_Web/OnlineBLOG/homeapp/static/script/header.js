
$(document).ready(function(){

    looginNickname();
    
    BGON();

    registerAjax();

    formChick();

    loginFormAjax()

});




function formChick(){
    $("#regaccount").change(function(){
        regAccOnlyAjax();
    });
    $("#regpassword").change(function(){
        chickPassword();
    });
    $("#regpassword2").change(function(){
        chickPassword2();
    });
    $("#regnickname").change(function(){
        nicknameChick();
    });
    VerCodeGet();
    $("#VerCode").change(function(){
        VerCodechick();
    });

};






function looginNickname(){
    $('#headerAccSpan').hide();
    if( $('#loginNickname').text()!=''){
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
        // alert(regaccount);
        // alert(regpassword);
        // alert(regnickname);
        if(regAccOnlyAjax()){
            alert('regAccOnlyAjax')
            return 
        };
        if(!chickPassword()){
            alert('chickPassword')
            return 
        };
        if(!chickPassword2()){
            alert('chickPassword2')
            return 
        };
        if(!nicknameChick()){
            alert('nicknameChick')
            return 
        };
        if(!VerCodechick()){
            alert('VerCodechick')
            return 
        };
        
    
        $.ajax({
            url:"/blog/register/", 
            type:"POST", 
            headers:{"X-CSRFToken":$.cookie("csrftoken")},
            data:{"account":regaccount,"password":regpassword, "nickname":regnickname}, 
            cache: false,  
            dataType: "html", 
            success:function(info, statues, xml){ 
                // alert(info);
                var info = eval ("(" + info + ")");


                if (info.status) {
                    $('#loginNickname').text(info.nickname);
                    $('#headerVisitorSpan').hide();
                    $('#headerAccSpan').show();
    
                    alert(info.result);

                    $("#loginBG").fadeOut(500);
                    $(".registerDiv").fadeOut(500);
                    $(".loginDiv").fadeOut(500);
    
                } else {
                    $('#headerVisitorSpan').hide();
                    $('#headerAccSpan').show();
                    alert('errr');
                    alert(info.result);
    
                };
            },
        });
    })

}



function regAccOnlyAjax(){
    // $(this).css("background-color","black");
    var regaccount = $("#regaccount").val();
    if(regaccount!=''){
        $.ajax({
            url:"/blog/regAccOnly/", 
            type:"POST", 
            headers:{"X-CSRFToken":$.cookie("csrftoken")},
            data:{"regaccount":regaccount,}, 
            success:function(info){ 
                if(info=='True'){
                    inputBorderColor("#regaccount", 'green');
                    return true
                }else{
                    inputBorderColor("#regaccount", 'red');
                    return false
                }
            },
        });

    };
    return false


};





function chickPassword(){
    if($("#regpassword").val().length>=6){
        inputBorderColor("#regpassword", 'green');
        return true
    }else{
        inputBorderColor("#regpassword", 'red');
        return false
    }
}



function chickPassword2(){
    if($("#regpassword").val()==$("#regpassword2").val() & $("#regpassword").val().length>=6 ){
        inputBorderColor("#regpassword", 'green');
        inputBorderColor("#regpassword2", 'green');
        $("#pwlabel").css("display","none");
        return true
    }else{
        inputBorderColor("#regpassword", 'red');
        inputBorderColor("#regpassword2", 'red');
        $("#pwlabel").css("display","inline-block");
        return false
    };
};





function nicknameChick(){
    if($("#regnickname").val().length>=3){
        inputBorderColor("#regnickname", 'green');
        return true
    }else{
        inputBorderColor("#regnickname", 'red');
        return false
    };
};


function VerCodeAjax(){
    $.ajax({
        url:"/blog/VerCodelabel/", 
        type:"GET", 
        headers:{"X-CSRFToken":$.cookie("csrftoken")},
        data:{}, 
        success:function(info){ 
            $("#VerCodelabel").text(info);

            $("#VerCodelabel").css("display","inline-block")
        },
    });
    if($("#VerCodelabel").text()==''){
    };

};

function VerCodeGet(){
    $("#VerCode").focus(function(){
        if($("#VerCodelabel").text()==''){
            VerCodeAjax();
        };
    });

    $("#VerCodelabel").click(function(){
        VerCodeAjax();
    });
    
}





function VerCodechick(){
    // console.log('VerCode:'+$("#VerCode").val());
    // console.log('VerCodelabel:'+$("#VerCodelabel").text());
    if($("#VerCode").val() == $("#VerCodelabel").text()){
        
        inputBorderColor("#VerCode", 'green')
        $("#VerCodelabel").css("display","none")
        return true
    }else{
        inputBorderColor("#VerCode", 'red')
        return false
    };
};








function inputBorderColor(inputId, color){
    $(inputId).css({
        "border": "1px solid "+color,
        "box-shadow": "0px 0px 5px inset"+color,
        "box-shadow": "0px 0px 5px "+color,
    });
};









function loginFormAjax(){
    
    $('#loginBut').click(function(){
        var loginAccount = $('#loginAccount').val();
        var loginPassword = $('#loginPassword').val();


        $.cookie('account',loginAccount,{expires:7});

        $.ajax({
            url:"/blog/login/", 
            type:"POST", 
            headers:{"X-CSRFToken":$.cookie("csrftoken")},
            data:{"loginAccount":loginAccount,"loginPassword":loginPassword}, 
            cache: false,  
            dataType: "html", 
            success:function(info, statues, xml){ 
                var info = eval ("(" + info + ")");

                if (info.status) {
                    // alert(info.status);
                    $('#loginNickname').text(info.nickname);
                    $('#headerVisitorSpan').hide();
                    $('#headerAccSpan').show();
    
    
                    $("#loginBG").fadeOut(500);
                    $(".registerDiv").fadeOut(500);
                    $(".loginDiv").fadeOut(500);
    
                } else {
                    // alert(info.status);
                    alert('用户名或密码错误！')
                    $('#loginPassword').val('')
                    // $('#headerVisitorSpan').show();
                    // $('#headerAccSpan').hide();
    
                };
            },
        });

    });
    
}







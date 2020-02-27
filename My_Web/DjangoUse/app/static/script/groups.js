$(document).ready(function(){
    CreateGroupAjax();
    ModalHideReload();

});





function ModalHideReload(){
    $('#myModalCreateGroup').on('hidden.bs.modal', function (){
        location.reload();
    });
    $('#myModaladduser').on('hidden.bs.modal', function (){
        location.reload();
    });
    $('#myModalremoveuser').on('hidden.bs.modal', function (){
        location.reload();
    });    

}




function CreateGroupAjax(){
    $("#addGroupUserSubmit").click(function(){

        var CreateGroupName = $("#CreateGroupName").val();
        // alert(CreateGroupName);

        $.ajax({
            url:"/app/user/createGroups/", 
            type:"POST", 
            headers:{"X-CSRFToken":$.cookie("csrftoken")},
            data:{"createGroups":CreateGroupName}, 
            cache: false,  
            dataType: "html", 
            success:function(info, statues, xml){ 
                // alert(info);
                var info = eval ("(" + info + ")");
                if (info.status) {
                    $("#CreateGroupName").val('')
                    $("#CreateGroupSucmsg").text('')
                    $("#CreateGroupErrormsg").text('')
                    $("#CreateGroupSucmsg").text(info.createGroupsuccessmsg)
                } else {
                    $("#CreateGroupName").val('')
                    $("#CreateGroupSucmsg").text('')
                    $("#CreateGroupErrormsg").text('')
                    $("#CreateGroupErrormsg").text(info.createGroupErrormsg)
                };
            },
        });

    });


};




// 全选复选框
function selectAllChks(chkname){
    // 获取所有复选框组件
    chks = document.getElementsByName(chkname);
    // 循环所有复选框组件
    for(var i=0; i<chks.length; i++){
        // 选中
        chks[i].checked = true;
    }
}
// 全选取消复选框
function removeAllChks(chkname){
    // 获取所有复选框组件
    chks = document.getElementsByName(chkname);
    // 循环所有复选框组件
    for(var i=0; i<chks.length; i++){
        // 取消选中
        chks[i].checked = false;              
    }
}
// 反选复选框
function reverseAllChks(chkname){
    // 获取所有复选框组件
    chks = document.getElementsByName(chkname);
    // 循环所有复选框组件
    for(var i=0; i<chks.length; i++){
        if (chks[i].checked == true){
            chks[i].checked = false;
        } else{
            chks[i].checked = true;
        }         
    }
}
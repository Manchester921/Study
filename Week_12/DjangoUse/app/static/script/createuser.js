// 步骤1：创建一个全局变量，用于存放生成的验证码
var code = "";
// 步骤2：封装验证码生成函数
function createCode(){
     // 步骤3：确定验证码的长度
    var codeLength = 5;  // 验证码由6个字符组成
    // 步骤4：初始化界面显示验证码的组件值为空
    var checkCode = document.getElementById("RegVerifyCode");
    checkCode.value = "";
    //checkCode.value = "";
    // 步骤5：使用数组生成一个字符库
    var selectedChars = new Array(0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z');
    // 步骤6：使用循环生成验证码
    // 清空原有的验证码数据
    code = "";
    for(var i=0; i<codeLength; i++){
        // 随机生成访问下标
        var charIndex = Math.floor(Math.random()*32);
        // 通过随机下标获取一个字符并进行验证码拼接
        code += selectedChars[charIndex];
    }
    console.log(code);
    // 步骤7：将最终结果添加到指定组件上
    document.getElementById("RegVerification").innerHTML = code;
}
        
function validate(){
    // 步骤1：验证两次密码是否一致
    var pass = document.getElementById("RegisterPassWord").value;
    var repass = document.getElementById("RegisterPassWord2").value;
    if(pass != repass){
        document.getElementById("RegPassWordErrormsg").innerHTML = "两次密码不一致";
        return false;
    }
    // 步骤2：获取用户输入的验证码
    var inputCode = document.getElementById("validateCode").value.toUpperCase();
    // 步骤3：使用if条件进行判断
    if(inputCode != code){
        document.getElementById("RegVerifyErrormsg").innerHTML = "验证码错误";
        createCode(); // 生成新的验证码
        return false;
    }
    // 返回OK
    return true;       
}       
var $form;
var form;
var $;
layui.use(['form', 'layer', 'upload', 'laydate'], function () {
    form = layui.form();
    var layer = parent.layer === undefined ? layui.layer : parent.layer;
    $ = layui.jquery;
    $form = $('form');
    laydate = layui.laydate;

    layui.upload({
        // url: "/static/json/userface.json",
        // success: function (res) {
        //     var num = parseInt(4 * Math.random());  //生成0-4的随机数
        //     //随机显示一个头像信息
        //     userFace.src = res.data[num].src;
        //     window.sessionStorage.setItem('userFace', res.data[num].src);
        // }
    });
})

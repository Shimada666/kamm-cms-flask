var $

layui.config({
    base: "../../js/"
}).use(['form', 'layer', 'upload', 'laydate'], function () {
    $ = layui.jquery;
    $.ajaxSetup({
        timeout: 1,
        complete: function (XMLHttpRequest, status) {
            //通过XMLHttpRequest取得响应结果
            if (status==='timeout'){
                layer.msg('timeout!')
                return
            }

            var res = XMLHttpRequest.responseText;
            try {
                var jsonData = JSON.parse(res);
                if (jsonData.error_code === -1) {
                    alert(jsonData.msg);
                    // window.location.replace("/");
                } else if (jsonData.error_code === 0) {
                    //其他的异常情况,给个提示。
                    layer.msg('正常！')
                    window.location.reload()
                } else {
                    //正常情况就不统一处理了
                }
            } catch (e) {}
        }
    })
})
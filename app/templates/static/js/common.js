layui.use(['form', 'layer', 'jquery', 'upload', 'laydate'], function () {
    var $ = layui.jquery,
        form = layui.form(),
        layer = layui.layer;
    $.ajaxSetup({
        timeout: 4000,
        contentType: "application/json",
        dataType: 'json',
        beforeSend: function (xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader('X-CSRFToken', csrf_token);
            }
        },
        complete: function (XMLHttpRequest, status) {
            //通过XMLHttpRequest取得响应结果
            // console.log(status)
            if (status === 'timeout') {
                layer.msg('请求超时!')
                return
            }
            var res = XMLHttpRequest.responseText;
            try {
                var jsonData = JSON.parse(res);
                if (jsonData.error_code === -1) {
                    alert(jsonData.msg);
                    // window.location.replace("/");
                } else if (jsonData.error_code === 999) {
                    //其他的异常情况,给个提示。
                    layer.msg('服务器未知错误!', {icon: 2})
                } else if (jsonData.error_code === 10000) {
                    //其他的异常情况,给个提示。
                    layer.msg('密码错误', {icon: 2})
                } else if (jsonData.error_code === 10020) {
                    layer.msg('资源不存在', {icon: 2})
                } else if (jsonData.error_code === 10030) {
                    layer.msg('参数错误', {icon: 2})
                } else if (jsonData.error_code === 20000) {
                    layer.msg('CSRF token缺失!', {icon: 2})
                } else {
                    //正常情况就不统一处理了
                }
            } catch (e) {
                console.log('返回数据不为json类型!')
            }
        },
        statusCode: {

        }
    });

    form.on('checkbox(all-choose)', function (data) {
        var child = $(data.elem).parents('table').find('tbody input[type="checkbox"]');
        child.each(function (index, item) {
            item.checked = data.elem.checked;
        });
        form.render('checkbox');
    });
    form.on("checkbox(choose)",function(data){
		var child = $(data.elem).parents('table').find('tbody input[type="checkbox"]:not([name="show"])');
		var childChecked = $(data.elem).parents('table').find('tbody input[type="checkbox"]:not([name="show"]):checked')
		$(data.elem).parents('table').find('thead input.all-choose').get(0).checked = childChecked.length === child.length;
		form.render('checkbox');
	})

})
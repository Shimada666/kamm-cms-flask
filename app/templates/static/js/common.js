layui.use(['form', 'layer', 'jquery'], function () {
    var $ = layui.jquery,
        form = layui.form(),
        layer = parent.layer === undefined ? layui.layer : parent.layer;
    var ajaxRequest = $.ajaxSetup({
        timeout: 4000,
        contentType: "application/json",
        dataType: 'json',
        layerIndex:-1,
        beforeSend: function (xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader('X-CSRFToken', csrf_token);
            }
            this.layerIndex = layer.msg('操作中，请稍候',{icon: 16,time:false,shade:0.8})
        },
        complete: function (XMLHttpRequest, status) {
            layer.close(this.layerIndex);
            //通过XMLHttpRequest取得响应结果
            // console.log(status)
            if (status === 'timeout') {
                layer.msg('请求超时!')
                ajaxRequest.abort();
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
            }
        },
        statusCode: {}
    });

    form.on('checkbox(all-choose)', function (data) {
        var child = $(data.elem).parents('table').find('tbody input[type="checkbox"]');
        child.each(function (index, item) {
            item.checked = data.elem.checked;
        });
        form.render('checkbox');
    });
    form.on("checkbox(choose)", function (data) {
        var child = $(data.elem).parents('table').find('tbody input[type="checkbox"]:not([name="show"])');
        var childChecked = $(data.elem).parents('table').find('tbody input[type="checkbox"]:not([name="show"]):checked')
        $(data.elem).parents('table').find('thead input[lay-filter="all-choose"]').get(0).checked = childChecked.length === child.length;
        form.render('checkbox');
    })

    // 表格单项删除及批量删除
    function deleteItems(items, url) {
        $.ajax({
            url: url,
            method: "post",
            data: JSON.stringify({items: items}),
            success: function (res, status) {
                if (res.error_code === 0) {
                    var $checkedLinks = $('.items-list tbody tr');
                    for (var i = 0; i < $checkedLinks.length; i++) {
                        var $currentItem = $($checkedLinks[i])
                        for (var j in items) {
                            if ($currentItem.attr('data-id') === items[j].toString()) {
                                $currentItem.remove();
                                break;
                            }
                        }
                    }
                    layer.msg('删除成功!', {icon: 1})
                }
            }
        })
        return false
    }

    $(".del").click(function () {
        var $this = $(this);
        var ids = [parseInt($this.attr("data-id"))];
        var deleteUrl = $("#delete-url").text()
        deleteItems(ids, deleteUrl)
    })
    $(".dels").click(function () {
        var $checkbox = $('.items-list tbody input[type="checkbox"][name="checked"]');
        var $checked = $('.items-list tbody input[type="checkbox"][name="checked"]:checked');
        var deleteUrl = $("#delete-url").text()
        if ($checkbox.is(":checked")) {
            layer.confirm('确定删除选中的信息？', {icon: 3, title: '提示信息'}, function () {
                var ids = []
                for (var i = 0; i < $checked.length; i++) {
                    var id = $checked.eq(i).parents("tr").find(".del").attr("data-id")
                    ids.push(id)
                }
                deleteItems(ids, deleteUrl)
            })
        } else {
            layer.msg("请选择需要删除的选项");
        }
    })
})
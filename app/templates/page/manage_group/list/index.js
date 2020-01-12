layui.use(['form', 'layer', 'jquery'], function () {
    var $ = layui.jquery,
        form = layui.form(),
        layer = layui.layer

    form.on('checkbox(all-auths)', function (data) {
        var child = $(data.elem).parents('.auths-form').find('.auths input[type="checkbox"]');
        child.each(function (index, item) {
            item.checked = data.elem.checked;
        });
        form.render('checkbox');
    });
    form.on("checkbox(auth)", function (data) {
        var child = $(data.elem).parents('.auths-form').find('.auths input[type="checkbox"]:not([name="show"])');
        var childChecked = $(data.elem).parents('.auths-form').find('.auths input[type="checkbox"]:not([name="show"]):checked')
        $(data.elem).parents('.auths-form').find('input.all-auths').get(0).checked = childChecked.length === child.length;
        form.render('checkbox');
    })

    $('.edit').click(function () {
        var group = $(this).parents('tr')
        var groupName = group.children('td[title=group-name]').text()
        var groupInfo = group.children('td[title=group-info]').text()
        var groupAuths = group.children('td[title=group-auths]').text().trim().split(' ')

        layer.open({
            type: 1,
            title: '信息修改',
            area: ['600px'],
            content: $('#tab1').html(),
            success: function () {
                $('input[name=name]').val(groupName)
                $('input[name=info]').val(groupInfo)
                for (var i in groupAuths) {
                    var inputs = $('input[lay-filter=auth]')
                    for (var j = 0; j < inputs.length; j++) {
                        if ($(inputs[j]).val() === groupAuths[i]) {
                            $(inputs[j]).prop('checked', 'true');
                        }
                    }
                }
                var auths = $('.auths')
                for (var i = 0; i < auths.length; i++) {
                    var child = $(auths[i]).parents('.auths-form').find('.auths input[type="checkbox"]:not([name="show"])');
                    var childChecked = $(auths[i]).parents('.auths-form').find('.auths input[type="checkbox"]:not([name="show"]):checked')
                    $(auths[i]).parents('.auths-form').find('input.all-auths').get(0).checked = childChecked.length === child.length;
                }
                form.render()
            }
        });
    })
});
layui.use(['form', 'layer'], function () {
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
});
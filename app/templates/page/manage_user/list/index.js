layui.use(['form', 'layer', 'jquery'], function () {
    var $ = layui.jquery,
        form = layui.form(),
        layer = layui.layer;

    $('.edit').click(function () {
        var user = $(this).parents('tr')
        var username = user.children('td[title=username]').text()
        var email = user.children('td[title=email]').text()
        var groupId = user.children('td[title=group-info]').attr('data-id')
        console.log(username, email)
        layer.open({
            type: 1,
            title: '信息修改',
            area: ['600px'],
            content: $('#tab1'),
            success: function () {
                $('input[name=username]').val(username)
                $('input[name=email]').val(email)
                if (groupId) $('option[title=group][value='+groupId+']').attr('selected','true')
                form.render()
            }
        });
    })
});
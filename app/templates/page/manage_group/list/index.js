layui.use(['form', 'layer'], function () {
    var $ = layui.jquery,
        form = layui.form(),
        layer = layui.layer;

    function deleteUsers(users) {
        $.ajax({
            url: "/cms/auth/user/delete",
            method: "post",
            data: JSON.stringify({users}),
            success: function (res, status) {
                if (res.error_code === 0) {
                    var $checkedLinks = $('.users-list tbody tr');
                    for (var i = 0; i < $checkedLinks.length; i++) {
                        var $currentItem = $($checkedLinks[i])
                        for (var j in users) {
                            if ($currentItem.attr('data-id') === users[j].toString()) {
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

    $(".user-del").click(function () {
        var $this = $(this);
        var ids = [parseInt($this.attr("data-id"))];
        deleteUsers(ids)
    })
    $(".users-del").click(function () {
        var $checkbox = $('.users-list tbody input[type="checkbox"][name="checked"]');
        var $checked = $('.users-list tbody input[type="checkbox"][name="checked"]:checked');
        if ($checkbox.is(":checked")) {
            layer.confirm('确定删除选中的信息？', {icon: 3, title: '提示信息'}, function () {
                var ids = []
                for (var i = 0; i < $checked.length; i++) {
                    var id = $checked.eq(i).parents("tr").find(".user-del").attr("data-id")
                    ids.push(id)
                }
                deleteUsers(ids)
            })
        } else {
            layer.msg("请选择需要删除的链接");
        }
    })
});
var areaData = address;
var $form;
var form;
var $;
layui.config({
    base: "../../js/"
}).use(['form', 'layer', 'upload', 'laydate'], function () {
    form = layui.form();
    var layer = parent.layer === undefined ? layui.layer : parent.layer;
    $ = layui.jquery;
    $form = $('form');
    laydate = layui.laydate;
    loadProvince(); //加载省信息

    layui.upload({
        // url: "/static/json/userface.json",
        // success: function (res) {
        //     var num = parseInt(4 * Math.random());  //生成0-4的随机数
        //     //随机显示一个头像信息
        //     userFace.src = res.data[num].src;
        //     window.sessionStorage.setItem('userFace', res.data[num].src);
        // }
    });

    form.on("submit(changeUser)", function (data) {
        // $.post('/cms/user/change_user_info', data.field, function (res) {
        //     console.log(res)
        //     if (res.error_code === 0) {
        //         alert('提交成功!')
        //         // window.location.reload()
        //     } else {
        //         alert('提交失败!')
        //     }
        // })
        // $.post('/cms/user/change_user_info', data.field, function (res) {
        //     window.location.reload()
        // })
        // return false
    })
})

//加载省数据
function loadProvince() {
    var proHtml = '';
    for (var i = 0; i < areaData.length; i++) {
        proHtml += '<option value="' + areaData[i].provinceCode + '_' + areaData[i].mallCityList.length + '_' + i + '">' + areaData[i].provinceName + '</option>';
    }
    //初始化省数据
    $form.find('select[name=province]').append(proHtml);
    form.render();
    form.on('select(province)', function (data) {
        $form.find('select[name=area]').html('<option value="">请选择县/区</option>');
        var value = data.value;
        var d = value.split('_');
        var code = d[0];
        var count = d[1];
        var index = d[2];
        if (count > 0) {
            loadCity(areaData[index].mallCityList);
        } else {
            $form.find('select[name=city]').attr("disabled", "disabled");
        }
    });
}

//加载市数据
function loadCity(citys) {
    var cityHtml = '<option value="">请选择市</option>';
    for (var i = 0; i < citys.length; i++) {
        cityHtml += '<option value="' + citys[i].cityCode + '_' + citys[i].mallAreaList.length + '_' + i + '">' + citys[i].cityName + '</option>';
    }
    $form.find('select[name=city]').html(cityHtml).removeAttr("disabled");
    form.render();
    form.on('select(city)', function (data) {
        var value = data.value;
        var d = value.split('_');
        var code = d[0];
        var count = d[1];
        var index = d[2];
        if (count > 0) {
            loadArea(citys[index].mallAreaList);
        } else {
            $form.find('select[name=area]').attr("disabled", "disabled");
        }
    });
}

//加载县/区数据
function loadArea(areas) {
    var areaHtml = '<option value="">请选择县/区</option>';
    for (var i = 0; i < areas.length; i++) {
        areaHtml += '<option value="' + areas[i].areaCode + '">' + areas[i].areaName + '</option>';
    }
    $form.find('select[name=area]').html(areaHtml).removeAttr("disabled");
    form.render();
    form.on('select(area)', function (data) {
    });
}
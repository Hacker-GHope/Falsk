function logout() {
    $.get("/api/logout", function(data){
        if (0 == data.errno) {
            location.href = "/";
        }
    })
}

$(document).ready(function(){
    $.ajax({
        url:'/user/user/',
        type:'GET',
        dataType:'json',
        success:function(data) {
            $('#user-avatar').attr('src',data.user.avatar);
            $('#user-name').html(data.user.name);
            $('#user-mobile').text(data.user.phone);
        },
        error:function(data){
        }
    });
})
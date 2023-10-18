
$(document).ready(function () {
    $("#login_button").click(function (event) {
        event.preventDefault();
        var username = $("#username").val();
        var password = $("#password").val();
        var data = JSON.stringify({ "username": username, "password": password });

        $.ajax({
            url: "/login",
            method: "POST",
            contentType: "application/json",
            data: data,
            success: function (response) {
                //alert("登入成功");
                window.location.href = "/";
            },
            error: function (xhr, status, error) {
                var message = xhr.responseJSON.message;
                $("#message").text(message).show();
            }
        });
    });
});

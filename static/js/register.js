$(document).ready(function () {
    console.log("starting");
    $("#register_button").click(function (event) {
        event.preventDefault();
        var username = $("#username").val();
        var password = $("#password").val();
        var data = JSON.stringify({ "username": username, "password": password });

        $.ajax({
            url: "/register",
            method: "POST",
            contentType: "application/json",
            data: data,
            success: function (response) {
                alert("註冊成功 請嘗試登入");
                window.location.href = "/login";
            },
            error: function (xhr, status, error) {
                var message = xhr.responseJSON.message;
                $("#message").text(message).show();
            }
        });
    });
});
// Alumni as mentor
function mentorhelp_users_chat(id) {
    const csrftoken = $("[name=csrfmiddlewaretoken]").val();
    const message = document.getElementById("alumni_msg").value;
    if(message != '') {
      $.ajax({
        type: "POST",
        url: "/mentor_help_users_message/",
        data: { message: message, id: id, csrfmiddlewaretoken: csrftoken},
        success: function (response) {
          $(".message_box").html(response.html);
          document.getElementById("alumni_msg").value = "";
          scroll_to_bottom();
        },
        error: () => {
          console.log("something went wrong");
        },
      });
    }
    else {
      alert("Enter Your Message")
    }
  }
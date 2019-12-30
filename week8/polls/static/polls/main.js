$(document).ready(function() {
  console.log("Connected with my JS");
  $("#submit").click(vote);
});

function getFormData($form) {
  var unindexed_array = $form.serializeArray();
  var indexed_array = {};

  $.map(unindexed_array, function(n, i) {
    indexed_array[n["name"]] = n["value"];
  });

  return indexed_array;
}

let vote = function() {
  $.ajax({
    // url: "/polls/vote_ajax/",
    url: $("form").attr("action"),
    type: $("form").attr("method"),
    data: getFormData($("form")),
    success: function(data) {
      $("#results").fadeIn();
      $("#message").text(data.msg);

      let options_html = "";
      data.data.forEach(option => {
        options_html += `<li>${option.text} - ${option.vote}</li>`;
      });

      // for (var i=0;i<data.data.length; i++){
      //   let option = data.data[i];
      //   options_html += `<li>${option.text} - ${option.vote}</li>`;
      // }

      $("#options").html(options_html);
    },
    error: function(data) {
      console.log("Error in response:", data);
    }
  });
};

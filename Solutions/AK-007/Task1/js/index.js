function myFunction() {
  $('.result').empty();
  var x = document.getElementById("value");
  var desc = x.elements[0].value;
  var loc = x.elements[1].value;
  var link =
    "https://jobs.github.com/positions.json?description=" +
    desc +
    "&location=" +
    loc;
  $.ajax({
    url: link,
    dataType: "jsonp",
    success: function(data) {
      for (var i = 0; i < data.length; i++) {
        var title = data[i].title;
        var company = data[i].company;
        var link = data[i].url;
        var description = data[i].description;
        var string =
          "<div class='set'><h3 class='title'>" +
          title +
          "</h3><h4 class='company'>Company : " +
          company +
          "</h4><div class='desc'>" +
          description +
          "</div><div class='url'><a href='" +
          link +
          "' target='_blank'>Link</a></div></div>";
        $(".result").append(string);
      }
      $(".foot").css("margin-top", "20px");
    }
  });
}
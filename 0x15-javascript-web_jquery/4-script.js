#!/usr/bin/node
$(document).ready(function () {
  var toggle_color = false;
  $("DIV#toggle_header").click(function () {
    if (toggle_color == false) {
      $("header").removeClass("red").addClass("green");
      toggle_color = true;
    } else {
      $("header").removeClass("green").addClass("red");
      toggle_color = false;
    }
  });
});

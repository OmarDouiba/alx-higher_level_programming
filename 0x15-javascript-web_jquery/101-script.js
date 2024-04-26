$("document").ready(function () {
  $("DIV#add_item").click(function () {
    $("UL.my_list").append("<li>Item</li>");
  });
  $("DIV#remove_item").click(function () {
    $("UL.my_list li:last-child").remove();
    // $("UL.my_list li:last").remove();
    // $("li").last().remove();
  });
  $("DIV#clear_list").click(function () {
    $("UL.my_list").empty(); // remove the item of the list
    // $("UL.my_list").remove(); // remove the list
  });
});

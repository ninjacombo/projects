function updateHref(item_id) {
  // var item_id = document.getElementById("task_id").value;
  console.log(item_id)

  // Create a new XMLHttpRequest object
  var xhr = new XMLHttpRequest();

  // Set up the request
  xhr.open("POST", "/delete/" + item_id, true);

  // Set the Content-Type header
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

  // Set up the callback function to handle the response
  xhr.onload = function () {
    if (xhr.status === 200) {
      // Request was successful
      console.log(xhr.responseText);
      // Handle the response data here
      // Refresh the page if necessary
      location.reload();
    } else {
      // Request failed
      console.log("Request failed. Status:", xhr.status);
    }
  };

  // Send the request with the item ID in the request body
  xhr.send("item_id=" + encodeURIComponent(item_id));
}


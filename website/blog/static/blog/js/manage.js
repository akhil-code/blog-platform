document.addEventListener("DOMContentLoaded",function(){
    //adding click listeners to button
    document.querySelectorAll(".deleteButton").forEach(function(button){
        button.onclick = function(){
            deleteBlog(this)
        }
    });
});


function deleteBlog(button) {
    
    let id = button.dataset["id"];
    var data = new FormData();
    data.append("id", id);

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        if(this.responseText == 'success')
            button.parentNode.parentNode.removeChild(button.parentNode);
        }
    };

    xhttp.open("POST", "delete-blog", true);
    xhttp.send(data);
}
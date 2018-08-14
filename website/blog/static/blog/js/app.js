
document.addEventListener('DOMContentLoaded', function(){
    document.querySelector("#addTextButton").onclick = addTextField;
    document.querySelector("#addImageButton").onclick = addImageField;
    document.querySelector("#myform").onsubmit = postBlog;
});




function addTextField(){
    // creating text area
    let textArea = document.createElement("textarea");
    textArea.rows = "10";
    textArea.cols = "100";
    textArea.placeholder = 'write your content here';
    textArea.classList.add("blogContent");
    textArea.name = "myContent[]";
    
    // adding DOM elements before buttons
    const myForm = document.getElementById('myform');
    const buttonHolder = document.getElementById('button-holder');    
    myForm.insertBefore(textArea, buttonHolder);
    const breakLine = document.createElement("br");
    myForm.insertBefore(breakLine, buttonHolder);
}

function addImageField(){
    // creating file input
    const fileInput = document.createElement("input");
    fileInput.type = "file";
    fileInput.name = "myfile[]";
    fileInput.multiple = true;
    fileInput.classList.add("blogContent");
    
    // addding DOM elemtns before buttons
    const myForm = document.getElementById('myform');
    const buttonHolder = document.getElementById('button-holder');
    myForm.insertBefore(fileInput, buttonHolder);
    const breakLine = document.createElement("br");
    myForm.insertBefore(breakLine, buttonHolder);
}

function postBlog(){
    const myForm = document.querySelector('#myform');

    // storing position order
    var positions = "";
    document.querySelectorAll(".blogContent").forEach(function(field){
        
        if(field.type == "file" && field.value !="") positions += "1";
        else if(field.value != "") positions += "0";
        else myForm.removeChild(field);
        
    });

    // creating a hidden input field for storing order of the contents
    const hiddenInput = document.createElement("input");
    hiddenInput.name = "contentOrder";
    hiddenInput.type = "hidden";
    hiddenInput.value = positions;
    myForm.appendChild(hiddenInput);

    // submit the form
    return true;
}



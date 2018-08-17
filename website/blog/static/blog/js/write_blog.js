// when document completes loading
document.addEventListener('DOMContentLoaded', function(){
    // assigning on click listeners to different buttons in the form
    document.querySelector("#addTextButton").onclick = addTextField;
    document.querySelector("#addImageButton").onclick = addImageField;
    document.querySelector("#myform").onsubmit = postBlog;
    document.querySelector("#addTag").onclick = addTag;
});

function createTextArea(){
    // creating text area
    const textArea = document.createElement("textarea");
    textArea.rows = "10";
    textArea.cols = "100";
    textArea.placeholder = 'write your content here';
    textArea.classList.add("blogContent");
    textArea.name = "myContent[]";
    return textArea;
}

function createFileInput(){
    const fileInput = document.createElement("input");
    fileInput.type = "file";
    fileInput.name = "myfile[]";
    fileInput.multiple = true;
    fileInput.classList.add("blogContent");
    return fileInput;
}

function createBreakLine(){
    return document.createElement("br");
}   

function createDeleteButton(){
    const button = document.createElement("button")
    button.innerHTML = "x";
    button.type = "button";
    button.onclick = function(){
        button.parentNode.parentNode.removeChild(button.parentNode);
    };
    return button;
}

function fillDivHolder(container, ele1, ele2, ele3){
    container.appendChild(ele1);
    container.appendChild(ele2);
    container.appendChild(ele3);
}

function insertAtEndOfForm(divHolder){
    const myForm = document.querySelector('#myform');
    const buttonHolder = document.querySelector('#button-holder');    
    myForm.insertBefore(divHolder, buttonHolder);
}

// adds new text field for user input
function addTextField(){
    // div holder holds input field, buttons, <br>
    const divHolder = document.createElement("div");
    // creating text area, deletebutton, <br>
    const textArea = createTextArea();
    const deleteButton = createDeleteButton();
    const breakLine = createBreakLine();
    // adding elements to a div element
    fillDivHolder(divHolder, textArea, deleteButton, breakLine);
    // adding DOM elements before buttons
    insertAtEndOfForm(divHolder);
}

// adds field to upload image
function addImageField(){
    const divHolder = document.createElement("div");
    // creating file input, deletebutton, <br>
    const fileInput = createFileInput();
    const deleteButton = createDeleteButton();
    const breakLine = createBreakLine();
    // adding elements to a div element
    fillDivHolder(divHolder, fileInput, deleteButton, breakLine);
    // addding DOM elemtns before buttons
    insertAtEndOfForm(divHolder);
}

// cross validates for valid image extensions
function hasValidExtension(filename){
    var validExtensions = [".png", ".jpg", ".jpeg", ".gif", ".bmp"];
    for(i=0; i<validExtensions.length; i++){
        if(filename.substr(filename.length-validExtensions[i].length, validExtensions[i].length).toLowerCase() == validExtensions[i].toLowerCase())
            return true;
    }
    return false;
}

// Intermediate steps before blog is sumitted
function postBlog(){
    // storing position order
    addContentOrderInput();
    // storing tags in the form
    addTagsInput();
    // proceed with the submission
    return true;
}

function addTagsInput(){
    var existingTags = [];
    var newTags = [];
    document.querySelectorAll("#taggedItems > li").forEach(function(itemNode){
        if(itemNode.dataset["id"] == "undefined") newTags[newTags.length] = itemNode.innerHTML;
        else existingTags[existingTags.length] = itemNode.dataset["id"]; 
    });

    
    const myForm = document.querySelector('#myform');
    let hiddenInput = document.createElement("input");
    hiddenInput.name = "existingTags";
    hiddenInput.type = "hidden";
    hiddenInput.value = JSON.stringify(existingTags);
    myForm.appendChild(hiddenInput);
    
    hiddenInput = document.createElement("input");
    hiddenInput.name = "newTags";
    hiddenInput.type = "hidden";
    hiddenInput.value = JSON.stringify(newTags);
    myForm.appendChild(hiddenInput);
}

function addContentOrderInput(){
    const myForm = document.querySelector('#myform');
    // storing position order
    var positions = "";
    document.querySelectorAll(".blogContent").forEach(function(field){
        if(field.type == "file" && field.value !="" && hasValidExtension(field.value)) positions += "1";
        else if(field.type == "textarea" && field.value != "") positions += "0";
        else myForm.removeChild(field);
    });

    // creating a hidden input field for storing order of the contents
    const hiddenInput = document.createElement("input");
    hiddenInput.name = "contentOrder";
    hiddenInput.type = "hidden";
    hiddenInput.value = positions;
    myForm.appendChild(hiddenInput);
}

function addTag(){
        let itemsHolder = document.querySelector("#taggedItems");
        let newItem = document.createElement("li");
        let inputField = document.getElementById("tagInput");
        if(inputField.value == "")
            return;
        newItem.innerHTML = inputField.value;
        newItem.dataset["id"] = getId(newItem.innerHTML);
        itemsHolder.appendChild(newItem);
        inputField.value = "";
}

function getId(tag){
    let nodes = document.querySelectorAll("datalist > option");
    for(i=0;i<nodes.length;i++){
        if(tag == nodes[i].value)
            return nodes[i].dataset["id"];
    }
    return undefined;
}
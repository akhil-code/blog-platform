document.addEventListener('DOMContentLoaded', function(){
    document.querySelector("#commentForm").onsubmit = postComment;
});

// let's submit the comment only if it is non empty
function postComment(){
    const textArea = document.querySelector("textarea");
    if(textArea.value == ''){
        alert("Please write a comment before sumitting");
        return false;
    }
    else{
        return true;
    }
}
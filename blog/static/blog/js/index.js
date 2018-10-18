document.addEventListener("DOMContentLoaded", function(){
    // animates list of home page
    startAnimation();
});

function startAnimation(){
    // variable keep trackes of the time at which items are being animated
    let time = 0;                       
    // interval between animation of two items
    let interval = 200;
    // animates title
    time = loadTitle(time, interval);
    // animates list items
    loadPanels(time, interval);
}

function loadTitle(time, interval){
    time = 500;
    let title = document.querySelector('h2');
    title.classList.add('fade-in');
    setTimeout(function(){
        title.classList.add('fade-in-show');
    }, time);
    time += interval
    return time;

}

function loadPanels(time, interval){
    document.querySelectorAll(".list-item").forEach(function(panel){
        panel.classList.add("fade-in");
        setTimeout(function(){
            panel.classList.add("fade-in-show");
        }, time);
        time += interval;
    });
    return time;
}
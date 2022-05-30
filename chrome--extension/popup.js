$(function(){
    //starting time
    $('#hour').keyup(function(){
    $('#h1').text($('#hour').val());})
    $('#min').keyup(function(){
    $('#m1').text($('#min').val());})
    $('#sec').keyup(function(){
    $('#s1').text($('#sec').val());})
    // ending time
    $('#hour2').keyup(function(){
    $('#h2').text($('#hour2').val());})
    $('#min2').keyup(function(){
    $('#m2').text($('#min2').val());})
    $('#sec2').keyup(function(){
    $('#s2').text($('#sec2').val());})

    $('#autofind').click(function(){
    $('#scale').text('auto finding..'); });

    $('#find').click(function(){
    $('#scale').text('finding..'); });

    // $('#autofind').click(function(){
    // $('#scale').text('E major'); });


    
  // $(document).ready(function(){
    //     $("#find").mouseover(function() { 
    //         $("#autofind").css('visibility', 'hidden');
    //         $("#info").css('visibility', 'visible'); 
    //     });
    //     $("#autofind").mouseover(function() { 
    //         $("#hello").css('visibility', 'visible'); 
    //     });
    //     $("#find").mouseout(function() { 
    //         $("#find").css('visibility', 'visible');
    //         $("#info").css('visibility', 'hidden');
    //         $("#autofind").css('visibility', 'visible') 
    //     });
    // });    


    // chrome.tabs.query({
    //     active: true,
    //     lastFocusedWindow: true
    // }, function(tabs) {
    //     // and use that tab to fill in out title and url
    //     var tab = tabs[0];
    //     console.log(tab.url);
    //     alert(tab.url);
    // });
})




// function find(){
//     document.getElementById("find").style.color = "red";
//     document.getElementById("starting").innerHTML = document.getElementById("hour").value+":"+document.getElementById("min").value+":"+document.getElementById("sec").value;
    
//     document.getElementById("final").innerHTML = document.getElementById("hour2").value+":"+document.getElementById("min2").value+":"+document.getElementById("sec2").value;
// }
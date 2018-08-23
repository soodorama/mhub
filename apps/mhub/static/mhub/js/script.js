$(document).ready(function() {
    $(".search_results").hide();
    // $('.loading_pingpong').hide();

    $("#submit_search").submit(function(e) {
        e.preventDefault();
        // $('.loading_pingpong').show('slow');
        // $('.loading_pingpong').hide('slow');

        $('.results_list').empty()

        $(".searchbar").css("margin-top","50px");
        $(".search_results").show("slow");

        var query = $('.search').val()
        query = query.split(' ').join('+')
        
        var max = 10 // change on click to load more results
        
        var search_type = "track" // options are track, album, artist, playlist
        
        $.get("https://www.googleapis.com/youtube/v3/search?part=snippet&q="+query+"&cateogoryId=10&order=relevance&maxResults="+max+"&key=AIzaSyAVUXSbBno7OstpWmQP-ZcsIuLlZ88mDVA", function(res) {
            i = 0
            for (var i = 0; i < 3; i++) {
                $.get("https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id="+res.items[i].id.videoId+"&key=AIzaSyAVUXSbBno7OstpWmQP-ZcsIuLlZ88mDVA", function(vid) {
                    html_render = "<div class='content_box'><a href='https://www.youtube.com/watch?v="+vid.items[0].id+"'>"
                    html_render += "<div class='img_box'><img class='result_img' src='"+vid.items[0].snippet.thumbnails.default.url+"' alt='"+vid.items[0].snippet.channelTitle+"'></div>"
                    html_render += "<div class='details_box'><ul><li>Title: "+ vid.items[0].snippet.title +
                    "</li><li>Author: " + vid.items[0].snippet.channelTitle +
                    "</li><li>Views: " + vid.items[0].statistics.viewCount +
                    "</li><li>Length: " + vid.items[0].contentDetails.duration +
                    "</li></ul></div>"
                    html_render += "</a></div>"
                    $('#youtube_results_list').append(html_render)
                },'json')
            }
        }, 'json')
        
    })
    
    // This code loads the IFrame Player API code asynchronously.
    var tag = document.createElement('script');
    
    tag.src = "https://www.youtube.com/iframe_api";
    var firstScriptTag = document.getElementsByTagName('script')[0];
    firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
    
    // This function creates an <iframe> (and YouTube player)
    // after the API code downloads.
    var player;
    function onYouTubeIframeAPIReady() {
        console.log("hi")
        player = new YT.Player('player', {
            events: {
                'onReady': onPlayerReady,
                'onStateChange': onPlayerStateChange
            }
        });
    }
    
    // The API will call this function when the video player is ready.
    function onPlayerReady(event) {
        event.target.playVideo();
    }
    
    // 5. The API calls this function when the player's state changes.
    //    The function indicates that when playing a video (state=1),
    //    the player should play for six seconds and then stop.
    var done = false;
    function onPlayerStateChange(event) {
        if (event.data == YT.PlayerState.PLAYING && !done) {
        setTimeout(stopVideo, 6000);
        done = true;
        }
    }
    function stopVideo() {
        player.stopVideo();
    }

})




// $.get("https://search.twitter.com/search.json?q=kanye",function(data) { 
    //     console.log(data) 
    // }, 'json')
    
    // $.get("https://api.spotify.com/v1/search?q="+query+"&type="+search_type+"&limit="+max,function(res) {
        //     console.log(res)
        // }, 'json')
        
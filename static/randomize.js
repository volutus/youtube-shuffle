
// JSON literal from Flask
var videos = {{ videos|tojson }};
var currentIndex = -1;

// 2. This code loads the IFrame Player API code asynchronously.
var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// 3. This function creates an <iframe> (and YouTube player)
//    after the API code downloads.
var player;
function onYouTubeIframeAPIReady()
{
    player = new YT.Player('player',
    {
        events:
        {
            'onReady': onPlayerReady,
            'onStateChange': onPlayerStateChange
        }
    });
}

// The API will call this function when the video player is ready.
function onPlayerReady(event)
{
    console.log("Player is ready. Queueing first video now.");
    loadNextVideo();
    player.setVolume(10);           // Set the volume to 10% to save my ears
    // Prevents the player from autoplaying once loaded for the first time
    // player.pauseVideo();
}

// This function is called on state changes
function onPlayerStateChange(event)
{
    if (event.data === YT.PlayerState.ENDED)
    {
        // The video has ended. Load the next one
        loadNextVideo();
    }
}

function loadNextVideo()
{
    if (currentIndex < videos.length-1)
    {
        currentIndex++;
        loadVideoWithIndex(currentIndex);
    }
}

function loadPreviousVideo()
{
    if (currentIndex > 0)
    {
        currentIndex--;
        loadVideoWithIndex(currentIndex);
    }
}

function loadVideoWithIndex(index)
{
    currentIndex = index;
    currentVideo = videos[currentIndex];
    loadVideo(currentVideo);
}


function loadVideo(video)
{
    document.getElementById("video-title").innerHTML = video.title;
    player.loadVideoById(video.id, 0, "large");

    // Tag the currently playing video with the appropriate class
    $(".currently-playing").removeClass("currently-playing");
    $("li.video").each(function()
    {
        let thisIndex = $(this).data("index");
        if (thisIndex == currentIndex)
        {
            $(this).addClass("currently-playing");
            return false;           // break out of the loop, we found the video
        }
    });
}
// Page scripts
$(document).ready(function()
{
    $("li.video").click(function()
    {
        let index = $(this).data("index");
        loadVideoWithIndex(index);
    });
});
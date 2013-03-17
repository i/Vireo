$(document).ready(function(){

    $tweetDisplay = $("#tweetDisplay");
    $tweet = $('#tweet');
    $tweetDisplay.hide();
    if($tweet.val() != ""){
        $tweetDisplay.fadeIn('slow');
    }

});

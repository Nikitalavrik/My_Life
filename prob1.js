console.log("1")

var aud = document.getElementsByTagName("audio");

$(".audio-name audio")
.on("ended", function(event) {

    let second = $(this).parent(".audio-name").next(".audio-name").find("audio");
    
    if (second.is("*")) {
      second[0].play();
    };
  });



function Volume_change(volume){
  for (i=0;i<aud.length;i++){
    aud[i].volume = volume;
  };
};

$(".play-sprite").click(function(){
  var $this = $(this),
      audio = $this.siblings('audio')[0];

  if (audio.paused === false){
    audio.pause();
    audio.removeClass("playing")
  }
  else{
    audio.play();
    audio.addClass("playing")
  }
   
})

var volumeslider = document.getElementById("vol-control");
console.log(volumeslider)



volumeslider.addEventListener("mousemove", setvolume);

function setvolume(){
  console.log("11s")
  for (i=0;i<aud.length;i++){
    var temp = function(){
      Volume_change(volumeslider.value / 100);
      console.log("23")
    };
    aud[i].addEventListener("volumechange",temp)
  };
}






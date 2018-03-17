console.log("2")


var aud = document.getElementsByTagName("audio");
var volumeslider = document.getElementsByClassName("vol-control");

var seekaudio = document.getElementsByClassName("progress-bar-grey")
var divprogress = window.getComputedStyle(document.getElementsByClassName('audio-name')[0], null),
    margin = parseFloat(divprogress.marginLeft) + parseFloat(divprogress.marginRight),
    padding = parseFloat(divprogress.paddingLeft) + parseFloat(divprogress.paddingRight)
    audio_width = document.getElementsByClassName('audio-name')[0].offsetWidth
var progressWidth = (audio_width-margin-padding) * 0.7

var repeat = false


window.onresize = function(event){
  var divprogress = window.getComputedStyle(document.getElementsByClassName('audio-name')[0], null),
  margin = parseFloat(divprogress.marginLeft) + parseFloat(divprogress.marginRight),
  padding = parseFloat(divprogress.paddingLeft) + parseFloat(divprogress.paddingRight)
  audio_width = document.getElementsByClassName('audio-name')[0].offsetWidth
  var progressWidth = (audio_width-margin-padding) * 0.7
}



$(".audio-name audio")
.on("ended", function(event) {

  current_audio = $(this).parent(".audio-name").find(".play-sprite")
  $(".top-play").removeClass("playing")
  if (repeat === false){
    
    current_audio.removeClass("playing");
    
    current_audio.nextAll().slice(2,6).removeClass("show");
  
    let second = $(this).parent(".audio-name").next(".audio-name")
    audio = second.find("audio");
    $this = second.find(".play-sprite")
    if (audio.is("*")) {
     play_audio(audio[0],$this)
    };

  }else{
    play_audio($(this)[0],current_audio)
  }
});

$(".play-sprite").click(function(){
  console.log($(".playing"))
  var $this = ($('.playing').length == 0) ? ($(this)) : ($(".playing").slice(1)),
      audio = ($this.siblings('audio').length !=0) ? ($this.siblings('audio')[0]): ($(".playing").slice(1).siblings('audio')[0]);

  console.log($this[0])
  play_audio(audio,$this)
  
});

$(".repeat").click(function(){

  if (repeat ===false){
    repeat = true
    $(this).addClass("repeat-after")

  }else{
    repeat = false
    $(this).removeClass("repeat-after")
  }
  
  
});

function volume_control(index_audio){
  var temp = function(){
      Volume_change(this.value / 100);
  };
  volumeslider[0].addEventListener("mousemove",temp);
  volumeslider[index_audio+1].addEventListener("mousemove",temp);

  volumeslider[index_audio+1].value = String(aud[index_audio].volume*100);
  volumeslider[0].value = String(aud[index_audio].volume*100);
  
};

function Volume_change(volume){
  for (i=0;i<aud.length;i++){
    aud[i].volume = volume;
    volumeslider[i].value = String(volume*100)
  };
};

function find_index(list,value){
  for (i=0;i<list.length;i++){
    if (list[i] === value){
      return i
    };
  };
};

function seek_audio(audio){
  var percent = (audio.currentTime/audio.duration)
  seekaudio[find_index(aud,audio)+1].style.width = (percent * progressWidth) + 'px';
  seekaudio[0].style.width = (percent * progressWidth) + 'px';
}
function seek_all_audio(){
  for (i=0;i<aud.length;i++){
    seek_audio(aud[i]);
  };
};

function cur_audio(audio){
  var cursor_audio = document.getElementsByClassName("progress show")[0]
  var cursot_top_audio = document.getElementsByClassName("progress show")[1]
  cursor_audio.addEventListener("click",function(event){
    
    var rect = this.getBoundingClientRect();
    console.log(rect.left)
    audio.currentTime = (event.pageX-rect.left)/progressWidth*audio.duration
    cursot_top_audio.currentTime = (event.pageX-rect.left)/progressWidth*audio.duration
  });
  cursot_top_audio.addEventListener("click",function(event){
    
    var rect = this.getBoundingClientRect();
    console.log(rect.left)
    audio.currentTime = (event.pageX-rect.left)/progressWidth*audio.duration
    cursot_top_audio.currentTime = (event.pageX-rect.left)/progressWidth*audio.duration
  });
}

function seek_time(audio){
  var cursor_time = document.getElementsByClassName("time show")[1]
  var top_cursor = document.getElementsByClassName("top-time")[0]
  console.log(cursor_time)
  
  audio.addEventListener("timeupdate", function(){
    var minute =  Math.floor(this.currentTime/60)
    var seconds = Math.floor(this.currentTime % 60)
    minute=((minute < 10) ? "0" : "") + minute;
    seconds =((seconds < 10) ? "0" : "") + seconds;
    cursor_time.getElementsByTagName("div")[0].innerHTML = minute + ":" + seconds
    top_cursor.getElementsByTagName("div")[0].innerHTML = minute + ":" + seconds
  })
  var minute =  Math.floor(audio.duration/60)
  var seconds = Math.floor(audio.duration%60)
  minute=((minute < 10) ? "0" : "") + minute;
  seconds =((seconds < 10) ? "0" : "") + seconds;
  cursor_time.getElementsByTagName("div")[1].innerHTML = minute + ":" + seconds
  top_cursor.getElementsByTagName("div")[1].innerHTML = minute + ":" + seconds

}

function play_audio(audio,$this){
  if (audio.paused === false){
    audio.pause();  
    $(".top-play").removeClass("playing")
    $this.removeClass("playing");
    $this.nextAll().slice(2,6).removeClass("show")
  }
  else{

    if ($(".playing").length != 0){
      
      
      $(".show").slice(4).removeClass("show")

      $(".playing").siblings('audio')[0].pause();
      $(".playing").removeClass("playing");


    } 
  


    audio.play();
    var song_name = $this.parent(".audio-name").find("h3").text()
    $(".top-name").html(song_name)
    $(".top_player").css("display","inline-block")
    $(".top-play").addClass("playing")
    $this.addClass("playing");
    $this.nextAll().slice(2,6).addClass("show")


    volume_control(find_index(aud,audio));
    seek_audio(audio)
    cur_audio(audio)
    seek_time(audio)
  };
  var curtime = function(){
    seek_audio(audio)
  }
  audio.addEventListener("timeupdate",curtime)
}



$('#addsongform').submit(function(e){
  var submit_button = $(this).find("input[type=submit]")
  $.post('/add/', $(this).serialize(), function(data){
      
     submit_button.addClass("added")
     
  });
  e.preventDefault();
});

$('#deletesongform').submit(function(e){
  $.post('/deletesong/', $(this).serialize(), function(data){

  });
  e.preventDefault();
});
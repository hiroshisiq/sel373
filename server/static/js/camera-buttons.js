//============================= BUTTONS =============================//
function videoButtonClick() {
  var button = document.getElementById("videoButton");

  if (button.innerHTML == "Stop Video") {
    button.innerHTML = "Start Video";
    document.getElementById("videoimage").src = "/static/img/nocamera2.gif";
    // video.scr = "/static/img/000.jpg";
  } else {
    button.innerHTML = "Stop Video";
    document.getElementById("videoimage").src = "http://highspeeddoggos.tk:8080/video_feed";
  }

  document.load();
}

function audioButtonClick() {
  var button = document.getElementById("audioButton");
  var audio = document.getElementById("audiofeed");

  if (button.innerHTML == "Start Audio") {
    button.innerHTML = "Stop Audio";
    audio.muted = false;
  } else {
    button.innerHTML = "Start Audio";
    audio.muted = true;
  }
}
function microButtonClick() {
  var button = document.getElementById("microButton");

  if (button.innerHTML == "Start Microphone") {
    button.innerHTML = "Stop Microphone";
  } else {
    button.innerHTML = "Start Microphone";
  }
}

//============================= Audio =============================//

  // function hasGetUserMedia() {
  //   return !!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia);
  // }
  //
  // if (hasGetUserMedia()) {
  //   // Good to go!
  // } else {
  //   alert('getUserMedia() is not supported by your browser');
  // }

  // const constraints = { video: false, audio: true};
  // const audio = document.querySelector('audio');
  //
  // function handleSuccess(stream) {
  //   audio.srcObject = stream;
  //   var microphone = context.createMediaStreamSource(stream);
  //   microphone.connect(context.destination);
  // }
  //
  // function handleError(error) {
  //   console.error('Reeeejected!', error);
  // }
  //
  // navigator.mediaDevices.getUserMedia(constraints).then(handleSuccess).catch(handleError);

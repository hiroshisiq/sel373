function videoButtonClick() {
  var button = document.getElementById("videoButton");

  if (button.innerHTML == "Stop Video") {
    button.innerHTML = "Start Video";
    document.getElementById("videoimage").src = "/static/img/nocamera2.gif";
    // video.scr = "/static/img/000.jpg";
  } else {
    button.innerHTML = "Stop Video";
    document.getElementById("videoimage").src = "http://127.0.0.1:5000/video_feed";
  }

  document.load();
}

function audioButtonClick() {
  var button = document.getElementById("audioButton");

  if (button.innerHTML == "Start Audio") {
    button.innerHTML = "Stop Audio";
  } else {
    button.innerHTML = "Start Audio";
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

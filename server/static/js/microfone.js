// Expose globally your audio_context, the recorder instance and audio_stream
var audio_context;
var recorder;
var audio_stream;

/**
 * Patch the APIs for every browser that supports them and check
 * if getUserMedia is supported on the browser.
 *
 */

function saveAudio(AudioBLOB){
  //[TODO] Send and save AudioBLOB to server
  // var req = null;
  // var url = "savefile.php";
  //var data = URL.createObjectURL(AudioBLOB);//document.getElementById("save").href.toString();// document.getElementById("save").innerHTML;// = xhttp.responseText;;   // you have to check how to get the data from your saveAudio() method
  //window.alert(AudioBlob);
  //console.log(data);
  // (window.XMLHttpRequest) ? req = new XMLHttpRequest() : (window.ActiveXObject) ? req = new ActiveXObject("Microsoft.XMLHTTP") : req = false;
  // req.open("POST", url, true);
  // req.setRequestHeader("Content-Type", "multipart/form-data");
  //
  // if(AudioBLOB != null) //&& data != "")
  // {
  //   //req.setRequestHeader("Content-length", data.length);
  //   req.send(AudioBLOB);
  //   console.log("Post sent from saveAudio");
  // }

  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/saveaudio', true);
  xhr.setRequestHeader('Content-Type', 'multipart/form-data');

  if(AudioBLOB != null) {
    xhr.send(AudioBLOB);
    console.log("Post sent from saveAudio");
  }

  xhr.onloadend = function () {
    // done
  };
}

function Initialize() {
    try {
        // Monkeypatch for AudioContext, getUserMedia and URL
        window.AudioContext = window.AudioContext || window.webkitAudioContext;
        navigator.getUserMedia = ( navigator.getUserMedia ||
                       navigator.webkitGetUserMedia ||
                       navigator.mozGetUserMedia ||
                       navigator.msGetUserMedia);
        window.URL = window.URL || window.webkitURL;

        // Store the instance of AudioContext globally
        audio_context = new AudioContext;
        console.log('Audio context is ready !');
        console.log('navigator.getUserMedia ' + (navigator.getUserMedia ? 'available.' : 'not present!'));
    } catch (e) {
        alert('No web audio support in this browser!');
    }
}

/**
 * Starts the recording process by requesting the access to the microphone.
 * Then, if granted proceed to initialize the library and store the stream.
 *
 * It only stops when the method stopRecording is triggered.
 */
function startRecording() {
    // Access the Microphone using the navigator.getUserMedia method to obtain a stream
    navigator.getUserMedia({ audio: true }, function (stream) {
        // Expose the stream to be accessible globally
        audio_stream = stream;
        // Create the MediaStreamSource for the Recorder library
        var input = audio_context.createMediaStreamSource(stream);
        console.log('Media stream succesfully created');

        // Initialize the Recorder Library
        recorder = new Recorder(input);
        console.log('Recorder initialised');

        // Start recording !
        recorder && recorder.record();
        console.log('Recording...');

        // Disable Record button and enable stop button !
        document.getElementById("startMicro").disabled = true;
        document.getElementById("stopMicro").disabled = false;
    }, function (e) {
        console.error('No live audio input: ' + e);
    });
}

/**
 * Stops the recording process. The method expects a callback as first
 * argument (function) executed once the AudioBlob is generated and it
 * receives the same Blob as first argument. The second argument is
 * optional and specifies the format to export the blob either wav or mp3
 */
function stopRecording(callback, AudioFormat) {
    // Stop the recorder instance
    recorder && recorder.stop();
    //console.log("Post sent!");
    // recorder.exportWAV(function(audio) {
    //     var xhr = new XMLHttpRequest();
    //     var url = 'savefile.php';
    //     xhr.open("POST", url, true);
    //     xhr.setRequestHeader("content-type", "audio/wav");
    //     xhr.onload = function(e) {
    //         // Handle the response.
    //     }
    //     xhr.send(audio);
    //     console.log("Post sent from stop recording!");
    // });

    console.log('Stopped recording.');

    // Stop the getUserMedia Audio Stream !
    audio_stream.getAudioTracks()[0].stop();

    // Disable Stop button and enable Record button !
    document.getElementById("startMicro").disabled = false;
    document.getElementById("stopMicro").disabled = true;

    // Use the Recorder Library to export the recorder Audio as a .wav file
    // The callback providen in the stop recording method receives the blob
    if(typeof(callback) == "function"){

        /**
         * Export the AudioBLOB using the exportWAV method.
         * Note that this method exports too with mp3 if
         * you provide the second argument of the function
         */
        recorder && recorder.exportWAV(function (blob) {
            callback(blob);
            saveAudio(blob);
            // create WAV download link using audio data blob
            // createDownloadLink();

            // Clear the Recorder to start again !
            recorder.clear();
        }, (AudioFormat || "audio/wav"));
    }
}

// Initialize everything once the window loads
window.onload = function(){
    // Prepare and check if requirements are filled
    Initialize();

    // Handle on start recording button
    document.getElementById("startMicro").addEventListener("click", function(){
	startRecording();
    }, false);

    // Handle on stop recording button
    document.getElementById("stopMicro").addEventListener("click", function(){
        // Use wav format
        var _AudioFormat = "audio/wav";
        // You can use mp3 to using the correct mimetype
        //var AudioFormat = "audio/mpeg";

        stopRecording(function(AudioBLOB){
            // // Note:
            // // Use the AudioBLOB for whatever you need, to download
            // // directly in the browser, to upload to the server, you name it !
            //
            // // In this case we are going to add an Audio item to the list so you
            // // can play every stored Audio
            var url = URL.createObjectURL(AudioBLOB);
            // var li = document.createElement('li');
            // var au = document.createElement('audio');
            // var hf = document.createElement('a');
            //
            // au.controls = true;
            // au.src = url;
            // hf.href = url;
            // // Important:
            // // Change the format of the file according to the mimetype
            // // e.g for audio/wav the extension is .wav
            // //     for audio/mpeg (mp3) the extension is .mp3
            // hf.download = new Date().toISOString() + '.wav';
            // hf.innerHTML = hf.download;
            // li.appendChild(au);
            // li.appendChild(hf);
            // recordingslist.appendChild(li);
            //
            console.log("Audio sent");
//            console.log(AudioBLOB);
//            saveAudio(AudioBLOB);
           // saveAudio(url)


        }, _AudioFormat);
    }, false);
};

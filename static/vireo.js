$("document").ready(function(){
  function loadRemote(path, callback) {
  var fetch = new XMLHttpRequest();
  fetch.open('GET', path);
  fetch.overrideMimeType("text/plain; charset=x-user-defined");
  fetch.onreadystatechange = function() {
    if(this.readyState == 4 && this.status == 200) {
      /* munge response into a binary string */
      var t = this.responseText || "" ;
      var ff = [];
      var mx = t.length;
      var scc= String.fromCharCode;
      for (var z = 0; z < mx; z++) {
        ff[z] = scc(t.charCodeAt(z) & 255);
      }
      callback(ff.join(""));
    }
  }
  fetch.send();
}

function play(file) {
  loadRemote(file, function(data) {
    midiFile = MidiFile(data);
    synth = Synth(44100);
    replayer = Replayer(midiFile, synth);
    audio = AudioPlayer(replayer);
  })
}

function playFile() {
  play('/compose/' + document.getElementById('quere').value);
}

<<<<<<< HEAD
if( $("#tweet").val() != ""){
  playFile();
}
=======
>>>>>>> 437fdbc019ba9d38e6c0de77f56764f110973982
});

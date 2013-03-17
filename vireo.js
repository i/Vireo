
midiFile = function (String notes) {
  var fs = require('fs');
  var Midi = require('jsmidgen');

  var file = new Midi.File();
  var track = new Midi.Track();
  file.addTrack(percussion);
  file.addTrack(piano);

};

function createTrack(String[] notes){
  for (i in notes){
      console.log(i)
  }
}

var testdata = ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4'];


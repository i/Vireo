
function createFile(notes) {
//    var fs = require('fs');
//    var Midi = require('jsmidgen');

    var file = new Midi.File();
    var track = new Midi.newTrack();
    file.addTrack(track);
    for (i in notes){
        var data = i.split(' ');
        track.addNote(0, data[0].trim(), data[1].trim());
    }

    var midifile = file.toBytes();

    fs.writeFileSync('test.mid', file.toBytes(), 'binary');
};


function playFile(melodyList) {
  createFile(melodyList);

  play('midi/test.mid');
}

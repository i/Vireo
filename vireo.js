
var midiFile = function (notes) {
    var fs = require('fs');
    var Midi = require('jsmidgen');

    var file = new Midi.File();
    var track = createTrack(notes);
    file.addTrack(track);

    fs.writeFileSync('test.mid', file.toBytes(), 'binary');
};

function createTrack(notes) {
    var track = new Midi.Track();
    for (i in notes){
        console.log(i);
        var data = i.split();
        track.addNote(0, data[0].trim(), data[1].trim());
    }
    return track;
}

var testdata = ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4'];


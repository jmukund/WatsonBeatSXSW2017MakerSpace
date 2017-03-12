workingDirectory = "/Users/jmukund/Documents/Reaper Media/amped-1/"
Kontakt5 = "Kontakt 5 (Native Instruments GmbH)"

def InitializeReaper () :

    '''
    initialize reaper
    '''

    RPR_Main_OnCommand ( 40296, 1 )  # select all tracks
    RPR_Main_OnCommand ( 40005, 1) # delete all tracks

    RPR_ShowConsoleMsg ( "\nRepear Initialized")

def getMood() :
    '''
    get mood from the watson beat thematic knob file
    '''
    file = open ( workingDirectory + "ThematicKnob.txt")
    mood = file.readline()
    file.close()

    mood = mood.split('_')
    return mood[0]

def ImportMidiFileToTrack ( file ) :

    RPR_SetEditCurPos ( 0, True, True) # sets scroll cursor to the beginning 0 on timeline
    RPR_InsertMedia ( file, 0) # inserts MIDI on new track


def CreateMelody ( mood , trackname) :
    '''
    a) get Melody file
    b) select an instrument
    c) select a preset
    d) create a track and insert midi file to the track
    e) add instrument to the track
    f) add preset to the instrument
    '''

    # get melody file
    file = workingDirectory + "melodyWB.mid"

    # select an instrument
    instrument = Kontakt5

    # get preset
    preset = mood + "_mel1"

    # inserts an empty track with no instrument added to it. 0 indicates track is inserted at 0th position
    RPR_InsertTrackAtIndex (0, True)

    RPR_Main_OnCommand (40297, 1) # unselects all tracks
    RPR_Main_OnCommand (40939, 1) # selects first track


    # add midi file to track
    ImportMidiFileToTrack ( file )

    # add VST to track and set preset
    RPR_TrackFX_GetByName ( RPR_GetTrack(0,0), instrument, True)
    RPR_TrackFX_SetPreset ( RPR_GetTrack(0,0), 0, preset)


if __name__ == '__main__' :

    InitializeReaper ()
    mood = getMood()

    RPR_ShowConsoleMsg ( "\nMood : " + mood)

    CreateMelody( mood, "MELODY")

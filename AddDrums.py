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


def CreateDrums ( mood ) :
    '''
    a) get Kick, snare, hihat and fill files
    b) select an instrument
    c) select a preset
    d) create a track and insert midi file to the track
    e) add instrument to the track
    f) add preset to the instrument
    '''

    kickFile = workingDirectory + "kick.mid"
    snareFile = workingDirectory + "snare.mid"
    hihatFile = workingDirectory + "hihat.mid"
    fillFile = workingDirectory + "fill.mid"

    # get instrument
    instrument = Kontakt5

    # get preset
    preset = mood + "_kit1"

    # set clock to 0
    RPR_SetEditCurPos ( 0, True, True )
    # insert empty track with no Instrument
    RPR_InsertTrackAtIndex ( 0, True)

    # add VST to track
    RPR_TrackFX_GetByName ( RPR_GetTrack(0,0), instrument, True)
    RPR_TrackFX_SetPreset ( RPR_GetTrack(0,0), 0, preset )

    # rename track
    trackId = RPR_GetTrack (0, 0)
    RPR_GetSetMediaTrackInfo_String (trackId, "P_NAME", "DRUM KIT", True)

    ImportMidiFileToTrack (kickFile)
    ImportMidiFileToTrack (snareFile)
    ImportMidiFileToTrack (hihatFile)
    ImportMidiFileToTrack (fillFile)

    # group all drum tracks into one
    selectedTrack = 0
    groupTrack = selectedTrack + 40939 # converts to Reaper Action ID
    RPR_Main_OnCommand (40297, 1)      # unselects all tracks
    RPR_Main_OnCommand (groupTrack, 1) # selects track passed in (selectedTrack)
    RPR_Main_OnCommand (1041, 1)       # makes current track a group folder and groups all tracks below it

if __name__ == '__main__' :

    InitializeReaper()
    mood = getMood()
    RPR_ShowConsoleMsg ( "\nMood: " + mood)

    CreateDrums ( mood )

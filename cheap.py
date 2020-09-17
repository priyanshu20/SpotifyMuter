from pycaw.pycaw import AudioUtilities
from SwSpotify import spotify
import time
from audioplayer import AudioPlayer


def muter():
    while True:
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            volume = session.SimpleAudioVolume
            # if session.Process:
            # print(session.Process.name())
            if session.Process and session.Process.name() == "Spotify.exe":
                # print(spotify.song())
                try:
                    if spotify.song() == "Advertisement":
                        print("Playing interlude song")
                        volume.SetMute(1, None)
                        AudioPlayer("soundtrack.wav").play(block=True)
                    else:
                        volume.SetMute(0, None)
                except:
                    continue


if __name__ == "__main__":
    muter()

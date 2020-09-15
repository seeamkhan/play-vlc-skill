from mycroft import MycroftSkill, intent_file_handler
from adapt.intent import IntentBuilder
from vlc import Instance
import time
import os


class PlayVlc(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.Player = Instance('--loop')

    def addPlaylist(self):
        self.mediaList = self.Player.media_list_new()
        # path = r"/Users/laila/Documents/seeam-work/toothless_skills/vlc_play"
        path = r"/home/ubuntu/Music/all_songs"
        songs = os.listdir(path)
        print(songs)
        for s in songs:
            self.mediaList.add_media(self.Player.media_new(os.path.join(path, s)))
        self.listPlayer = self.Player.media_list_player_new()
        # print(self.listPlayer)
        self.listPlayer.set_media_list(self.mediaList)
        # print(self.listPlayer)

    def play(self):
        # print(self.listPlayer)
        self.listPlayer.play()

    def next(self):
        self.listPlayer.next()

    def pause(self):
        self.listPlayer.pause()

    def previous(self):
        self.listPlayer.previous()

    def stop(self):
        self.listPlayer.stop()

    @intent_file_handler('vlc.play.intent')
    def handle_vlc_play(self, message):
        self.speak_dialog('vlc.play')

        self.addPlaylist()
        # print(player.addPlaylist())

        self.play()
        # print(player.addPlaylist())
        # time.sleep(10)

    @intent_file_handler('vlc.pause.intent')
    def handle_vlc_pause(self, message):
        try:
            self.pause()
        except Exception as e:
            print('ERROR! VLC Pause failed.')
            print(e)
            self.speak_dialog('vlc.pause')

    @intent_file_handler('vlc.next.intent')
    def handle_vlc_next(self, message):
        try:
            self.next()
        except Exception as e:
            print('ERROR! VLC next failed.')
            print(e)
            self.speak_dialog('vlc.next')


def create_skill():
    return PlayVlc()


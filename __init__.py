from mycroft import MycroftSkill, intent_file_handler


class PlayVlc(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('vlc.play.intent')
    def handle_vlc_play(self, message):
        self.speak_dialog('vlc.play')


def create_skill():
    return PlayVlc()


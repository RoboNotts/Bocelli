import rospy
from bocelli.speech.SpeechText import Speaker
from bocelli.srv import Listen, Speak, SpeakResponse, ListenResponse

#http://10.0.1.10:11311

# ROS node to interface with speaking/listening
class Bocelli:
    def __init__(self):
        self.speaker = Speaker()

        self.services = {
            "speak_request": rospy.Service('speak', Speak, self._onSpeechRequest),
            "listen_request":rospy.Service('listen', Listen, self._onListenRequest)
        }
    
    def _onSpeechRequest(self, msg):
        self.speaker.speak(msg.request)
        return SpeakResponse(1)
    
    def _onListenRequest(self, msg):
        result = self.speaker.listen(msg.duration)
        out = ListenResponse()
        out.result = result
        return out

    def main(*args, **kwargs):
        rospy.init_node('bocelli')
        d = Bocelli()
        rospy.spin()
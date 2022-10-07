from urllib import robotparser
import rospy
from speech.SpeechText import Speaker
from bocelli.msg import ListenResult, SpeechRequest, ListenRequest

class Bocelli:
    def __init__(self):
        self.speaker = Speaker()

        self.publishers = {
            "listen_result": rospy.Publisher('bocelli/hear', ListenResult,queue_size=10)
        }
        self.subscribers = {
            "speak_request": rospy.Subscriber('bocelli/speak', SpeechRequest, self._onSpeechRequest),
            "listen_request": rospy.Subscriber('bocelli/requestListen', ListenRequest, self._onListenRequest)
        }
    
    def _onSpeechRequest(self, msg):
        self.speaker.Speak(msg)
    
    def _onListenRequest(self, msg):
        result = self.speaker.Listen(msg.duration)
        out = ListenResult()
        out.result = result
        self.publishers["listen_result"].publish(out)

    def main(*args, **kwargs):
        rospy.init_node('bocelli')
        d = Bocelli()
        rospy.spin()
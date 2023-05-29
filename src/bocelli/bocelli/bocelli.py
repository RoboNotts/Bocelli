import rospy
from bocelli.speech.SpeechText import Speaker
from bocelli.srv import Listen, Speak, SpeakResponse, ListenResponse

#http://10.0.1.10:11311

# ROS node to interface with speaking/listening
class Bocelli:
    def __init__(self, micName):
        if micName != None:
            self.speaker = Speaker(micName)
        else:
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
        print("REEEEEEEEEEEEESULT", result)
        out = ListenResponse()
        out.result = result
        return out

    def main(*args, **kwargs):
        rospy.init_node('bocelli')
        print(args[0])
        d = Bocelli(args[0])
        rospy.spin()
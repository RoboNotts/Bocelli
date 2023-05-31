import rospy
from bocelli.andrea import interactions
from bocelli.srv import Request, RequestResponse

# ROS node to interface with dialogFlow and chatGPT
class Andrea:
    def __init__(self):

        self.dfInterface = interactions.dialogeFlowInterface()

        self.services = {
            "df_request": rospy.Service('df_request', Request, self._onDfRequest),
            "cmd_request": rospy.Service('cmd_request', Request, self._onCmmRequest),
            "gpt_request":rospy.Service('gpt_request',  Request, self._onGPTRequest)
        }
    
    def _onGPTRequest(self, msg):
        reply = interactions.GPTResponse(msg.request)
        
        return RequestResponse(reply[2])
    
    def _onDfRequest(self, msg):
        
        reply = self.dfInterface.dialogFlowProcess(msg.request)

        return RequestResponse(reply)
    
    def _onCmmRequest(self, msg):
        reply = self.dfInterface.processUserCommand(msg.request)
        
        return RequestResponse(reply)    

    def main(*args, **kwargs):
        rospy.init_node('andrea')
        d = Andrea()
        rospy.spin()
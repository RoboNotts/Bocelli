import rospy
from Bocelli.src.andrea import interactions
from Bocelli.srv import Request, RequestResponse

# ROS node to interface with dialogFlow and chatGPT
class Andrea:
    def __init__(self):

        self.services = {
            "df_request": rospy.Service('df_request', Request, self._onDfRequest),
            "cmm_request": rospy.Service('df_request', Request, self._onCmmRequest),
            "gpt_request":rospy.Service('gpt_request',  Request, self._onGPTRequest)
        }
    
    def _onGPTRequest(self, msg):
        reply = interactions.GPTResponse(msg)
        
        return RequestResponse(reply[1])
    
    def _onDfRequest(self, msg):
        reply = interactions.dialogeFlowProcess(msg)
        
        return RequestResponse(reply)
    
    def _onCmmRequest(self, msg):
        reply = interactions.processUserCommand(msg)
        
        return RequestResponse(reply)    

    def main(*args, **kwargs):
        rospy.init_node('andrea')
        d = Andrea()
        rospy.spin()
class Message():
    def GetMessage(message, success, error='', data={}):
        return{
            'message':message,
            'success':success,
            'error':error,
            'data':data
        }
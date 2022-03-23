class ResponseMessage():
    def __init__(self) -> None:
        pass

    def GetMessage(message, success, error = '', data = {}):
        return{
            'message': message,
            'success': success,
            'data': data,
            'error': error,
        }
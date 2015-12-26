from flask import jsonify

class utility:
    
    @staticmethod
    def jsonifyme(errorCode, errorDescription):
        return jsonify(ErrorCode=errorCode,
                       ErrorDescription=errorDescription)

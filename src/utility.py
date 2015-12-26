from flask import jsonify

class utility:
    
    @staticmethod
    def jsonifyme(errorCode, errorDescription):
        return jsonify(ResultCode=errorCode,
                       Description=errorDescription)

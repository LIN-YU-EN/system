from flask import jsonify

def ok(data=None, message="ok", status=200):
    return jsonify({"success": True, "message": message, "data": data}), status

def fail(message="error", status=400, data=None):
    return jsonify({"success": False, "message": message, "data": data}), status
from flask import jsonify

def ok(message="ok", data=None, status_code=200):
    return jsonify({
        "success": True,
        "message": message,
        "data": data
    }), status_code

def fail(message="error", status=400, data=None):
    return jsonify({"success": False, "message": message, "data": data}), status
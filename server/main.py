import io
import os
import ctypes
import json

from flask import Flask, request, jsonify

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import predict

def resource_path(relative_path):
    """
    This is needed in order for the script to find the model at runtime
    when compiled with Pyinstaller
    """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

app = Flask(__name__)

model = predict.load_model(resource_path('model.h5'))

SW_HIDE = 0

def resolve(files):
    return predict.classify(model, files)


@app.route("/", methods=["POST"])
def image_nsfw_check():
    files = request.files.get("file")
    if not files:
        return {"error": "empty list"}
    try:
        result = resolve([io.BytesIO(files.stream.read())])
    except Exception:
        return {}
    print("OK")
    return jsonify(result)


if __name__ == "__main__":
    try:
        with open("config.json", "r") as file:
            config = json.load(file)
    except FileNotFoundError:
        config = {"port": 3000, "host": "localhost", "show_console": False}

    if not config.get("show_console"):
        kernel32 = ctypes.WinDLL('kernel32')
        user32 = ctypes.WinDLL('user32')

        windowHandle = kernel32.GetConsoleWindow()
        if windowHandle:
            user32.ShowWindow(windowHandle, SW_HIDE)

    app.run(config["host"], config["port"])

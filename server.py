from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/input/<client_id>/A/', methods=['POST'])
def receive_file(client_id):
    print("received")
    file = request.files['file']
    current_path = os.getcwd()
    directoryID = os.path.join(current_path, "input", client_id)
    print(directoryID)
    if not os.path.exists(directoryID):
        os.makedirs(directoryID)
        print("New clientID, created")

    finaldir = os.path.join(directoryID, "A")
    if not os.path.exists(finaldir):
        os.makedirs(finaldir)
        print("New session, created")
    save_path = os.path.join(finaldir, file.filename)
    file.save(save_path)
    return "File received!", 200

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9999)

import os
from flask import Flask, Response, request, url_for
import plivoxml

app = Flask(__name__)


@app.route('/response/speak/', methods=['GET'])
def speak():
    # Enter the message you want to play
    text = "Congratulations! You just made a text to speech app on Plivo cloud!"
    parameters = {'loop': 1, 'language': "en-US", 'voice': "WOMAN"}

    response = plivoxml.Response()
    response.addSpeak(text, **parameters)

    return Response(str(response), mimetype='text/xml')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

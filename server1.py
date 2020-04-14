# Server run 1st
# # -----------------------------------
# activate TA
# python -m venv env
# env\Scripts\activate
# # -----------------------------------
# python -m pip install --upgrade pip
# pip install flask
# pip install jsonpickle
# pip install numpy
# pip install opencv-python
# # -----------------------------------
# set FLASK_APP=server1.py
# # -----------------------------------
# flask run

# Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


from flask import Flask, request, Response
import jsonpickle
import numpy as np
import cv2

# Initialize the Flask application
app = Flask(__name__)
 

# route http posts to this method
@app.route('/api/test', methods=['POST'])
def test():
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # do some fancy processing here....

    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
                }
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")


# start flask app
app.run(host="0.0.0.0", port=5000)
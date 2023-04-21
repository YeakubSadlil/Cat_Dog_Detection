import os
from flask import Flask, flash, request, redirect, url_for, Response
from werkzeug.utils import secure_filename
import cv2
from image_detection import bounding_image

UPLOAD_FOLDER = 'static/uploads'  # Client's uploaded image storage
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Helper function to check if the file extension is valid
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#Main route that handles file uploads and detection
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No file is selected')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            # bounding_image() function from image_detection.py to detect objects in the image
            # and draw bounding boxes around them, and returns the annotated image as a JPEG response
            image_data = bounding_image(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            _, buffer = cv2.imencode('.jpg', image_data)
            image_bytes = buffer.tobytes()
            response = Response(image_bytes, mimetype='image/jpeg')
            return response

    # HTML form for file upload 
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
    <input type=file name=file>
    <input type=submit value=Upload>
    </form>
    '''
# Start the Flask app
if __name__ == "__main__":
    app.run(debug=True)

import os
from flask import Flask, flash, request, redirect, url_for , jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token , get_jwt_identity
from werkzeug.utils import secure_filename
from Main import Runnig_Crypt_process
from datetime import time

UPLOAD_FOLDER = "C:\\Users\\Raouf\\Desktop\\Signature\\DB_Files"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'word'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 0.25 * 1024 * 1024
# JWT Config
jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = "Secret_Key"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/UploadFile', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            time.sleep(5)

            Runnig_Crypt_process("E",os.path.join(app.config['UPLOAD_FOLDER'], filename),"To_Test")

            return redirect(url_for("upload_file",
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''



@app.route('/getJwt')
def getJwt():
    user="USER_ID_To_SET_and_other_informations"
    access_token = create_access_token(identity = user)
    return jsonify(access_token=access_token)

@app.route('/protected',methods=["GET"])
@jwt_required()
def Protected():
    current_jwt = get_jwt_identity()
    return jsonify(ok=current_jwt), 200
    


if __name__== "__main__":
    app.run()

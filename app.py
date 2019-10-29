 
import os, urllib.request, requests, subprocess, shutil
from filesfunc import app
from LSB1 import hideLSB1
from UN_LSB1 import retrLSB1
from LSB2 import hideLSB2
from UN_LSB2 import retrLSB2
from MSB1 import hideMSB1
from UN_MSB1 import retrMSB1
from MSB2InFile import hideMSB2
from UN_MSB2InFile import retrMSB2
from AudioLSB1 import AudioHideLSB1
from UN_AudioLSB1 import AudiortrLSB1
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy

#Files limitation
ALLOWED_EXTENSIONS = set(['bmp', 'png', 'jpg', 'jpeg', 'gif', 'wav', 'flac'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#Default route to home page
@app.route('/')
def upload_form():
	return render_template('index.html')

#Route for upload button
@app.route('/uploadfile', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'upfile' not in request.files:
            flash('No file part')
            return redirect(request.url)
        #Upload file
        file = request.files['upfile']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded')
            return redirect('/')
        else:
            flash('Allowed file types are  png, jpg, jpeg, gif, wav, flac')
            return redirect(request.url)
#Route from "i an ready button"
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        method = request.form['method']
        action = request.form['action']
        comments = request.form['comments']
        filename = os.popen('ls file-upload/*')
        MyFile = filename.read()
        filename = os.popen('pwd')
        MyPath = filename.read()
        MyPath = MyPath.replace("\n", "")
        #ֿAll the hide methods
        if action == "HideText":
            #Detail check
            if  method == '' or comments == '          ' or MyFile == '':
                return render_template('index.html', message='Please enter required fields')
            #Method LSB1
            elif method == 'LSB1':    
                MyFile = MyFile.replace("\n", "")
                MyFile = MyFile.replace("file-upload/", "")
                print ("\n \n the path- "+ MyFile + "\n \n")
                shutil.move(MyPath+"/file-upload/"+MyFile, MyPath+"/"+MyFile)
                hideLSB1(MyFile,comments)
                shutil.move(MyPath+"/"+MyFile, MyPath+"/HidedFilesHistory/"+MyFile)
                return render_template('success.html')
            #Method LSB2
            elif method == 'LSB2':    
                MyFile = MyFile.replace("\n", "")
                MyFile = MyFile.replace("file-upload/", "")
                print ("\n \n the path- "+ MyFile + "\n \n")
                shutil.move(MyPath+"/file-upload/"+MyFile, MyPath+"/"+MyFile)
                hideLSB2(MyFile,comments)
                shutil.move(MyPath+"/"+MyFile, MyPath+"/HidedFilesHistory/"+MyFile)
                return render_template('success.html')
            #Method MSB1
            elif method == 'MSB1':    
                MyFile = MyFile.replace("\n", "")
                MyFile = MyFile.replace("file-upload/", "")
                print ("\n \n the path- "+ MyFile + "\n \n")
                shutil.move(MyPath+"/file-upload/"+MyFile, MyPath+"/"+MyFile)
                hideMSB1(MyFile,comments)
                shutil.move(MyPath+"/"+MyFile, MyPath+"/HidedFilesHistory/"+MyFile)
                return render_template('success.html')
            #Method MSB2
            elif method == 'MSB2':    
                MyFile = MyFile.replace("\n", "")
                MyFile = MyFile.replace("file-upload/", "")
                print ("\n \n the path- "+ MyFile + "\n \n")
                shutil.move(MyPath+"/file-upload/"+MyFile, MyPath+"/"+MyFile)
                hideMSB2(MyFile,comments)
                shutil.move(MyPath+"/"+MyFile, MyPath+"/HidedFilesHistory/"+MyFile)
                return render_template('success.html')
            #Method Audio
            elif method == 'AudioLSB1':    
                MyFile = MyFile.replace("\n", "")
                MyFile = MyFile.replace("file-upload/", "")
                print ("\n \n the path- "+ MyFile + "\n \n")
                shutil.move(MyPath+"/file-upload/"+MyFile, MyPath+"/"+MyFile)
                AudioHideLSB1(MyFile,comments)
                shutil.move(MyPath+"/"+MyFile, MyPath+"/HidedFilesHistory/"+MyFile)
                return render_template('success.html')

        #parallel to the hide method
        if action == "DiscoverText":
            # add file chack to the if
            if  method == '' or MyFile == '':
                return render_template('index.html', message='!You missed something!')
            #Method LSB1
            elif method == 'LSB1':
                MyFile = MyFile.replace("\n", "")
                MyFile = MyFile.replace("file-upload/", "")
                print ("\n \n the path- "+ MyFile + "\n \n")
                shutil.move(MyPath+"/file-upload/"+MyFile, MyPath+"/"+MyFile)
                HiddenText = (retrLSB1(MyFile))
                shutil.move(MyPath+"/"+MyFile, MyPath+"/DiscoverdFilesHistory/"+MyFile)
                return render_template('HiddenText.html', message=HiddenText)
            #Method LSB2
            elif method == 'LSB2':
                MyFile = MyFile.replace("\n", "")
                MyFile = MyFile.replace("file-upload/", "")
                print ("\n \n the path- "+ MyFile + "\n \n")
                shutil.move(MyPath+"/file-upload/"+MyFile, MyPath+"/"+MyFile)
                HiddenText = (retrLSB2(MyFile))
                shutil.move(MyPath+"/"+MyFile, MyPath+"/DiscoverdFilesHistory/"+MyFile)
                return render_template('HiddenText.html', message=HiddenText)
            #Method MSB1
            elif method == 'MSB1':
                MyFile = MyFile.replace("\n", "")
                MyFile = MyFile.replace("file-upload/", "")
                print ("\n \n the path- "+ MyFile + "\n \n")
                shutil.move(MyPath+"/file-upload/"+MyFile, MyPath+"/"+MyFile)
                HiddenText = (retrMSB1(MyFile))
                shutil.move(MyPath+"/"+MyFile, MyPath+"/DiscoverdFilesHistory/"+MyFile)
                return render_template('HiddenText.html', message=HiddenText)
            #Method MSB2
            elif method == 'MSB2':
                MyFile = MyFile.replace("\n", "")
                MyFile = MyFile.replace("file-upload/", "")
                print ("\n \n the path- "+ MyFile + "\n \n")
                shutil.move(MyPath+"/file-upload/"+MyFile, MyPath+"/"+MyFile)
                HiddenText = "Your messege is in the text file"
                retrMSB2(MyFile)
                shutil.move(MyPath+"/"+MyFile, MyPath+"/DiscoverdFilesHistory/"+MyFile)
                return render_template('HiddenText.html', message=HiddenText)
            #Method Audio
            elif method == 'AudioLSB1':
                MyFile = MyFile.replace("\n", "")
                MyFile = MyFile.replace("file-upload/", "")
                print ("\n \n the path- "+ MyFile + "\n \n")
                shutil.move(MyPath+"/file-upload/"+MyFile, MyPath+"/"+MyFile)
                HiddenText = (AudiortrLSB1(MyFile))
                shutil.move(MyPath+"/"+MyFile, MyPath+"/DiscoverdFilesHistory/"+MyFile)
                return render_template('HiddenText.html', message=HiddenText)

        else:
            return render_template('success.html')
        return render_template('index.html', message='You have already submitted feedback')

if __name__ == "__main__":
    app.run()

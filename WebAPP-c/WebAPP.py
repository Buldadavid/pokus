from flask import Flask, render_template, request,redirect
import csv
from openpyxl import load_workbook
import stitek
import stitekfirma
from datetime import date
import os
from werkzeug.utils import secure_filename
from PIL import Image, ImageFont, ImageDraw

app = Flask(__name__)
ALLOWED_EXTENSIONS = {'png'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

header = ['QR','Firma','SF','AKZ','DBZ','WB','MLFB','Z','cislo','Datum']

@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/', methods=['POST', 'GET'])
def indexV():
	row = []	
	QR = request.form['text']
	QR = QR.upper()
	print(QR)
	
	firma = request.form['text2']
	print(firma)
	
	sf = request.form['text3']
	print(sf)
	
	dbz = request.form['text4']
	print(dbz)
	
	wb = request.form['text5']
	print(wb)
	
	akz = request.form['text6']
	print(akz)
	
	if " " in QR :
		return render_template('error_qr.html',Imput=QR) 

	MLFB,cislo,odmer,Z,dat_v,barvaO,barvaZ = stitek.vyroba(QR)
	
	#pridani do listu
	row.append(QR)
	row.append(firma)
	row.append(sf)
	row.append(akz)
	row.append(dbz)
	row.append(wb)
	row.append(MLFB)
	row.append(Z)
	row.append(cislo)
	row.append("21.10.2022")
	
	with open('data/data.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow(row)
	
	
	return render_template('index.html')

@app.route('/tbl')
def tbl():
    return render_template('table.html')

@app.route("/tbl", methods=['POST'])
def table():
    
    sf = request.form['text']
    csv_file = csv.reader(open('data/data.csv', "r"), delimiter=",")


    #loop through the csv list
    for row in csv_file:
        #if current rows 3rd value is equal to input, print that row
        if sf == row[2]:
            #print(row[0])
            print(row[1])
            
            #print(row[2])
            print(row[3])
            print(row[4])
            print(row[5])
            print(row[6])
            print(row[7])
            print(row[8])
            print(row[9])
             #print (row)
            firma,akz,dbz,wb,mlfb,z,cislo,datum=row[1],row[3],row[4],row[5],row[6],row[7],row[8],row[9]     
    return render_template("table.html", firma=firma,akz=akz,dbz=dbz,wb=wb,mlfb=mlfb,z=z,cislo=cislo,datum=datum)


@app.route('/manualne', methods=['GET'])
def indexM():
	return render_template('indexM.html')

@app.route('/manualne', methods=['POST'])
def indexMV():
	row = []	
	
	QR = ""
	datum= "21.10.2022"
	
	mlfb = request.form['text']
	print(mlfb)	
	
	firma = request.form['text2']
	print(firma)
	
	sf = request.form['text3']
	print(sf)
	
	dbz = request.form['text4']
	print(dbz)
	
	wb = request.form['text5']
	print(wb)
	
	akz = request.form['text6']
	print(akz)
	
	cislo = request.form['text7']
	print(cislo)

	z = request.form['textz']
	print(z)

	row.append(QR)
	row.append(firma)
	row.append(sf)
	row.append(akz)
	row.append(dbz)
	row.append(wb)
	row.append(mlfb)
	row.append(z)
	row.append(cislo)
	row.append(datum)

	with open('data/data.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow(row)
    
	return redirect("/tbl")

@app.route('/home', methods=['POST'])
def home():
    return redirect('/')

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500    

app.run(host="0.0.0.0", port=5001)


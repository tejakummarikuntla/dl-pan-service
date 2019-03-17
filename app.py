from flask import Flask, jsonify

app = Flask(__name__)

panPeople = [
    {'ID': 1, 'PAN': "BPHPT8281F" , 'Name':"KUMMARIKUNTLA TEJA", 'Fname':"KUMMARIKUNTLA SRINIVASA RAO", 'Dob':"05/11/1999"},
    {'ID': 2, 'PAN': "BPHPT6281F" , 'Name':"RAMMY", 'Fname':"RAMMYFATHER", 'Dob':"23/01/1989"},
    {'ID': 3, 'PAN': "BPHPT2281F" , 'Name':"MANUJA", 'Fname':"HANIYA", 'Dob':"22/01/1989"},
    {'ID': 4, 'PAN': "BPHPT1281F" , 'Name':"INTHEN", 'Fname':"KARINA", 'Dob':"20/03/1989"}
]

dlPeople = [
    {'ID': 1, 'DL': "AP40300363542018" , 'Name':"MANI SAI PRASAD M", 'Fname':"M ANJI PRASAD", 'IssuedDate':"09-11-2018", 'Address':"11-143,EBD COLONY E.B.C.COLONY,CHITTOOR, PULICHERLA CHITTOOR-517172"},
    {'ID': 2, 'DL': "AP40330363542018" , 'Name':"MANI GAUVRAV", 'Fname':"MONAIE", 'IssuedDate':"09-11-2012", 'Address':"COLONY,CHITTOOR, PULICHERLA CHITTOOR-517172"},
    {'ID': 4, 'DL': "AP40320363542018" , 'Name':"CHIINAVINAY", 'Fname':"KANIEHA", 'IssuedDate':"09-11-2016", 'Address':"11-143,EBD.B.C.COLONY,CHITTOOR, PULICHERLA CHITTOOR-517172"},
    {'ID': 5, 'DL': "AP40380363542018" , 'Name':"ANAGAHA", 'Fname':"AYENDEH", 'IssuedDate':"09-11-2011", 'Address':"11-143,EBD .C.COLONY,CHITTOOR, PULICHERLA CHITTOOR-517172"}
]

@app.route('/')
def home():
    pass

@app.route('/pan/people', methods=['GET'])
def getPanPeople():
    return jsonify({'panPeople':panPeople})

@app.route('/dl/people', methods=['GET'])
def getDlPeople():
    return jsonify({'dlPeople':dlPeople})

@app.route('/pan/people/<string:PAN>', methods=['GET'])
def getPanPerson(PAN):
    for person in panPeople:
        if person['PAN'] == PAN:
            return jsonify(person)
    return jsonify({'message': '`PAN` not found'})

@app.route('/dl/people/<string:DL>', methods=['GET'])
def getDlPerson(DL):
    for person in dlPeople:
        if person['DL'] == DL:
            return jsonify(person)
    return jsonify({'message': '`DL` not found'})

app.run(port=5000)
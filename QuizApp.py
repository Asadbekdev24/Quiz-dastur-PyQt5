
from PyQt5.QtWidgets import QApplication, QLabel, QRadioButton, QCheckBox,QPushButton, QWidget, QMessageBox
from PyQt5.QtGui import QIcon

import os
os.system("cls")


testToplam=[
   {
       "id":1,
       "savol":"1) Savol 4*5=?",
       "javoblar":{
           "A":"20",
           "B":"10",
           "C":"24",
           "D":"16"
       },
       "to'g'riJavob":"A"

   },
   {
       "id":2,
       "savol":"2) Savol 19+3=?",
       "javoblar":{
           "A":"14",
           "B":"15",
           "C":"22",
           "D":"5"
       },
       "to'g'riJavob":"C"

   },
   {
       "id":3,
       "savol":"3) Savol 14*5=?",
       "javoblar":{
           "A":"58",
           "B":"60",
           "C":"45",
           "D":"70"
       },
       "to'g'riJavob":"D"

   },
   {
       "id":4,
       "savol":"4) Savol 8*5=?",
       "javoblar":{
           "A":"60",
           "B":"40",
           "C":"30",
           "D":"20"
       },
       "to'g'riJavob":"B"

   },
   {
       "id":5,
       "savol":"5) Savol 9*5=?",
       "javoblar":{
           "A":"48",
           "B":"41",
           "C":"42",
           "D":"45"
       },
       "to'g'riJavob":"D"

   },
   {
       "id":6,
       "savol":"6) Savol 9/0=?",
       "javoblar":{
           "A":"0",
           "B":"9",
           "C":"1",
           "D":"Mumkin emas"
       },
       "to'g'riJavob":"D"

   },
]

oxirgi=0



testApp=QApplication([])

window=QWidget()
window.show()
window.setWindowTitle("Just quiz program")
window.setWindowIcon(QIcon("quiz2.jpg"))
window.setGeometry(500,100,1000,800)

submit=QPushButton("Keyingi", window)
submit.setStyleSheet("""
font-size:20px;
color:white;
background-color:#007bff;
""")
submit.setGeometry(300,500,350,60)
submit.show()

savol=QLabel("Hozircha bo'sh", window)
savol.setGeometry(100,100,350,100)
savol.setStyleSheet("font-size:20px; font-weight:bold; color:#343a40;")


javobA=QRadioButton("A", window)
javobA.setGeometry(110,200,60,20)
javobA.setStyleSheet("font-size:18px; color:0056b3")

javobB=QRadioButton("B", window)
javobB.setGeometry(110,270,60,20)
javobB.setStyleSheet("font-size:18px; color:0056b3")

javobC=QRadioButton("C", window)
javobC.setGeometry(110,340,60,20)
javobC.setStyleSheet("font-size:18px; color:0056b3")

javobD=QRadioButton("D", window)
javobD.setGeometry(110,410,60,20)
javobD.setStyleSheet("font-size:18px; color:0056b3")

javobA.setChecked(False)
javobB.setChecked(False)
javobC.setChecked(False)
javobD.setChecked(False)

def dasturdaTestniKorsatish():

    test=testToplam[oxirgi]
    savol.setText(test["savol"])
    javobA.setText(test["javoblar"]["A"])
    javobB.setText(test["javoblar"]["B"])
    javobC.setText(test["javoblar"]["C"])
    javobD.setText(test["javoblar"]["D"])
    javobA.adjustSize()
    javobB.adjustSize()
    javobC.adjustSize()
    javobD.adjustSize()


def tekshirish(javob:str):
    xabar=QMessageBox()
    xabar.setWindowTitle("Tekshirish")
    xabar.setIcon(QMessageBox.Information)
    togriJavob=testToplam[oxirgi]["to'g'riJavob"]
    if javob==togriJavob:
        xabar.setText("Siz tog'ri javob berdingiz!")
    else:
        xabar.setText("Siz noto'g'ri javob berdingiz!")
    ans1=xabar.addButton("Testni davom ettirish",QMessageBox.AcceptRole)
    ans2=xabar.addButton("Testni tugatish",QMessageBox.RejectRole)
    xabar.exec()
    if xabar.clickedButton()==ans1:
        print("Davom ettrildi")
    if xabar.clickedButton()==ans2:
        print("Test tugatildi")
        window.close()


    # xabar.setButtonText(QMessageBox.Yes, "Testni davom ettirish")
    # xabar.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
    # retval=xabar.exec()

    # if retval==QMessageBox.Yes:
    #     print("Yes")
    # else:
    #     print("No")



def keyingiSavolniKorsatish():
    tJavob=""
    if javobA.isChecked()==True:
        tJavob=javobA.text()
    if javobB.isChecked()==True:
        tJavob=javobB.text()
    if javobC.isChecked()==True:
        tJavob=javobC.text()
    if javobD.isChecked()==True:
        tJavob=javobD.text()
    tekshirish(tJavob)
    global oxirgi
    oxirgi+=1
    if oxirgi>=len(testToplam):
        print("Test tugadi")
    else:
        dasturdaTestniKorsatish()

dasturdaTestniKorsatish()



submit.clicked.connect(keyingiSavolniKorsatish)




savol.show()
javobA.show()
javobC.show()
javobB.show()
javobD.show()



# if oxirgi>=1 and oxirgi<len(testToplam):



testApp.exec()

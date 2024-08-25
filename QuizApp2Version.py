
from PyQt5.QtWidgets import QApplication, QLabel, QRadioButton, QCheckBox,QPushButton, QWidget, QMessageBox, QComboBox
from PyQt5.QtGui import QIcon

import os
os.system("cls")


matematika=[
   {
       "id":1,
       "savol":"1) Savol 4*5=?",
       "javoblar":{
           "A":"20",
           "B":"10",
           "C":"24",
           "D":"16"
       },
       "Tjavob":"A"

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
       "Tjavob":"C"

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
       "Tjavob":"D"

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
       "Tjavob":"B"

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
       "Tjavob":"D"

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
       "Tjavob":"D"

   },
]

tarix=[
   {
       "id":1,
       "savol":"1) Savol Amir Temur?",
       "javoblar":{
           "A":"20",
           "B":"10",
           "C":"24",
           "D":"16"
       },
       "Tjavob":"A"

   },
   {
       "id":2,
       "savol":"2) Savol Navoiy",
       "javoblar":{
           "A":"14",
           "B":"15",
           "C":"22",
           "D":"5"
       },
       "Tjavob":"C"

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
       "Tjavob":"D"

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
       "Tjavob":"B"

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
       "Tjavob":"D"

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
       "Tjavob":"D"

   },
]

fanlar=[matematika,tarix]

oxirgi=0



testApp=QApplication([])

window=QWidget()
window.show()
window.setWindowTitle("Just quiz program")
window.setWindowIcon(QIcon("quiz2.jpg"))
window.setGeometry(500,100,1000,800)


testType=QLabel("Qaysi fan turidagi testni ishlamoqchisiz?", window)
testType.setGeometry(25,25,365,60)
testType.setStyleSheet("font-size:18px; font-weight:bold; color:#343a40;")
testType.show()
variantlar=QComboBox(window)
variantlar.setGeometry(25,80,150,50)
variantlar.addItem("Metematika")
variantlar.addItem("Tarix")
variantlar.addItem("Ingliz tili")
variantlar.addItem("Geografiya")
variantlar.setStyleSheet("font-size:16px; font-weight:bold; color:#343a40;")
variantlar.show()



submit=QPushButton("Keyingi", window)
submit.setStyleSheet("""
font-size:20px;
color:white;
background-color:#007bff;
""")
submit.setGeometry(300,500,350,60)
submit.show()

savol=QLabel("Hozircha bo'sh", window)
savol.setGeometry(100,150,350,100)
savol.setStyleSheet("font-size:20px; font-weight:bold; color:#343a40;")


javobA=QRadioButton("A", window)
javobA.setGeometry(110,250,60,20)
javobA.setStyleSheet("font-size:18px; color:0056b3")

javobB=QRadioButton("B", window)
javobB.setGeometry(110,320,60,20)
javobB.setStyleSheet("font-size:18px; color:0056b3")

javobC=QRadioButton("C", window)
javobC.setGeometry(110,390,60,20)
javobC.setStyleSheet("font-size:18px; color:0056b3")

javobD=QRadioButton("D", window)
javobD.setGeometry(110,460,60,20)
javobD.setStyleSheet("font-size:18px; color:0056b3")

javobA.setChecked(False)
javobB.setChecked(False)
javobC.setChecked(False)
javobD.setChecked(False)

def dasturdaTestniKorsatish():
    fan=fanlar[variantlar.currentIndex()]
    test=fan[oxirgi]
    savol.setText(test["savol"])
    javobA.setText(test["javoblar"]["A"])
    javobB.setText(test["javoblar"]["B"])
    javobC.setText(test["javoblar"]["C"])
    javobD.setText(test["javoblar"]["D"])
    javobA.adjustSize()
    javobB.adjustSize()
    javobC.adjustSize()
    javobD.adjustSize()


d=variantlar.currentIndex()

if d>0:
    dasturdaTestniKorsatish()

soni=0
def tekshirish(javob:str):
    global soni
    fan=fanlar[variantlar.currentIndex()]
    xabar=QMessageBox()
    xabar2=QMessageBox()
    xabar.setWindowTitle("Tekshirish")
    xabar.setIcon(QMessageBox.Information)
    if fan[oxirgi]["id"]<=6:
        togriJavob=fan[oxirgi]["Tjavob"]
        if javob==togriJavob:
            soni+=1
            xabar.setText("Siz tog'ri javob berdingiz!")
        else:
            xabar.setIcon(QMessageBox.Warning)
            xabar.setText("Siz noto'g'ri javob berdingiz!")
        ans1=xabar.addButton("Testni davom ettirish",QMessageBox.AcceptRole)
        ans2=xabar.addButton("Testni tugatish",QMessageBox.RejectRole)
        xabar.exec()
        if xabar.clickedButton()==ans1:
            print("Davom ettrildi")
        if xabar.clickedButton()==ans2:
            print("Test tugatildi")
            window.close()
    if fan[oxirgi]["id"]==6:
        xabar2.setWindowTitle("Natijalar")
        xabar2.setIcon(QMessageBox.Information)
        xabar2.setText(f"Test tugadi!\nSiz 6 ta testdan {soni} tasiga to'g'ri javob berdingiz!")
        xabar2.exec()
        window.close()



    # xabar.setButtonText(QMessageBox.Yes, "Testni davom ettirish")
    # xabar.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
    # retval=xabar.exec()

    # if retval==QMessageBox.Yes:
    #     print("Yes")
    # else:
    #     print("No")



def keyingiSavolniKorsatish():
    fan=fanlar[variantlar.currentIndex()]
    tJavob=""
    if javobA.isChecked()==True:
        tJavob="A"
    if javobB.isChecked()==True:
        tJavob="B"
    if javobC.isChecked()==True:
        tJavob="C"
    if javobD.isChecked()==True:
        tJavob="D"
    tekshirish(tJavob)
    global oxirgi
    oxirgi+=1
    if oxirgi>=len(fan):
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

from Myro import *
from Graphics import *
import random



class doorEnsemble:
    def __init__(self):
        self.door = Rectangle((50,200),(200,450))
        self.doorknob= Circle((175,325),15)
        self.status = "Not Chosen"
        self.door.draw(win)
        self.doorknob.draw(win)
        self.name = "default" 
        self.stillAlive = True       
    def resizeDoor(self,topRightX,topRightY,bottomLeftX,bottomLeftY):
        win.canvas.shapes.Remove(self.door)
        self.door = Rectangle((topRightX,topRightY),(bottomLeftX,bottomLeftY))
        self.door.draw(win)
    def resizeDoorknob(self,centerX,centerY,radius):
        win.canvas.shapes.Remove(self.doorknob)
        self.doorknob = Circle((centerX,centerY),radius)
        self.doorknob.draw(win)
    def removeDoorEnsemble(self):
        win.canvas.shapes.Remove(self.door)
        win.canvas.shapes.Remove(self.doorknob)
        self.stillAlive = False

def  deleteDoorFromListOfDoorEnsembles(m_doorToRemove):
    for doorEnsemble in listOfDoorEnsembles:
        print(doorEnsemble.name)     
    

#remove code

    listOfDoorEnsembles.remove(m_doorToRemove)
    for doorEnsemble in listOfDoorEnsembles:
        print(doorEnsemble.name)     

pic = Picture("fiesta.jpg")
pic.scale(0.36)

carIsInDoor = random.randint(1, 3)
if carIsInDoor == 1:
    carIsBehind = "Left"
    pic.setX(125)
    pic.setY(325)
elif carIsInDoor == 2:
    carIsBehind = "Center"
    pic.setX(425)
    pic.setY(325)
elif carIsInDoor == 3:
    carIsBehind = "Right"
    pic.setX(725)
    pic.setY(325)
else:
    print("ERROR")


win = Window("Room for Jeff", 900,900)
floor = Rectangle((0,450),(900,900))
floor.fill=Color("burlywood")
floor.draw(win)
win.setBackground(Color("Blue"))

switchBox = Rectangle((100, 25),(415, 150))
switchBox.fill=Color("Red")

stayBox = Rectangle((435,25),(750,150))
stayBox.fill=Color("Red")

leftDoorE = doorEnsemble()
leftDoorE.door.fill=Color("Saddlebrown")
leftDoorE.doorknob.fill=Color("gold")
leftDoorE.name = "Left"

centerDoorE = doorEnsemble()
centerDoorE.resizeDoor(350,200,500,450)
centerDoorE.resizeDoorknob(475,325,15)
centerDoorE.door.fill=Color("saddlebrown")
centerDoorE.doorknob.fill=Color("gold")
centerDoorE.name = "Center"

rightDoorE = doorEnsemble()
rightDoorE.resizeDoor(650,200,800,450)
rightDoorE.resizeDoorknob(775,325,15)
rightDoorE.door.fill=Color("saddlebrown")
rightDoorE.doorknob.fill=Color("gold")
rightDoorE.name = "Right"

listOfDoorEnsembles = []
listOfDoorEnsembles.append(leftDoorE)
listOfDoorEnsembles.append(centerDoorE)
listOfDoorEnsembles.append(rightDoorE)

point = Point(0,0)
switchMessage = Text(point, "Switch")
switchMessage.fill=Color("Black")
switchMessage.fontSize= 50

point2 = Point(0,0)
stayMessage = Text(point, "Stay")
stayMessage.fill=Color("Black")
stayMessage.fontSize= 50

switchDoor = []


def handleMouseDown(obj, event): 
    doorEnsemblesWeCanRemove = [] 
    for puerta in listOfDoorEnsembles:
        if puerta.door.hit(event.x,event.y) and puerta.status=="Not Chosen":
            print("Choosing Door")
            puerta.status = "Chosen"
            puerta.door.outline=Color("purple")            
            puerta.door.setWidth(8)
            for DoorD in listOfDoorEnsembles:
                if (DoorD is not puerta) and not (DoorD.name == carIsBehind):
                    doorEnsemblesWeCanRemove.append(DoorD)
            doorToRemove = random.choice(doorEnsemblesWeCanRemove)
            doorToRemove.removeDoorEnsemble()
            ###deleteDoorFromListOfDoorEnsembles(doorToRemove)
    stayBox.draw(win)
    switchBox.draw(win)
    switchMessage.setX(247.5)
    switchMessage.setY(82.5)
    switchMessage.draw(win)
    stayMessage.setX(597.5)
    stayMessage.setY(82.5)
    stayMessage.draw(win)
    print("Done intitial choice.")
    if switchBox.hit(event.x,event.y):
            print("Switch")
            #print(puerta.name)
            #THE PROBLEM IS THAT THE DOOR IS NOT DEFINED AS PUERTA, TELL WHICH DOOR TO SET BLACK AND WHICH TO REMOVE
            for aDoorE in listOfDoorEnsembles:
                if aDoorE.status == "Chosen":
                    doorToDeselect = aDoorE
                    doorToDeselect.door.outline = Color("Black")
                    doorToDeselect.door.setWidth(1)
                    doorToDeselect.stillAlive= False
            #puerta.removeDoorEnsemble()\       
            for doorE in listOfDoorEnsembles:
                if doorE.stillAlive == True: 
                    doorE.door.outline = Color("Purple")
                    doorE.door.setWidth(8)
                    win.canvas.shapes.Remove(doorE.doorknob)
                    doorE.door.fill=Color("wHiTe")
                    pic.draw(win)
    if stayBox.hit(event.x,event.y):
            for doorE in listOfDoorEnsembles:
                if doorE.stillAlive == True: 
                    win.canvas.shapes.Remove(doorE.doorknob)
                    doorE.door.fill=Color("wHiTe")
                    pic.draw(win)
                    
                      
                    

                
onMouseDown(handleMouseDown)

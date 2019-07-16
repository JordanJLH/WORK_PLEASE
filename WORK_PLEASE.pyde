def setup():  #runs once
    size(512,512)
    noStroke()
    
def draw():
    if mousePressed:
     fill(0, 128, 128)
     rect(mouseX - 50, mouseY - 50, 100, 100)
    if keyPressed and key == 'c':
        background(200, 200, 200)
        print(keyCode)
 

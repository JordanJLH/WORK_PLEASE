def setup():  #runs once
    size(512,512)
def draw():  #run multiple times
    background(255,255,255)
    translate(-50, -50)
    if (mouseX>256):
        fill(255,0,0)
    else:
        fill(0, 0, 255)
    if (mouseY>256):
        fill(255,0,0)
    else:
        fill(0, 0, 255)
        
    
    rect(mouseX - 50, mouseY -50, 100, 100)

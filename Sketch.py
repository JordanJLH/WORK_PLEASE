def setup():  
    size(512,512)
    noStroke()
    
    
    def draw():
        # background(200, 200, 200)
        if mousePressed:
            fill(0, 128, 128) 
            rect(mouseX - 50, mouseY - 50, 100, 100)

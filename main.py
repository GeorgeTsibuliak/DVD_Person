from sprites import *

class Screensaver:
    def __init__(self):
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.person = Person()
        self.run()
        
    def run(self):
        while True:
            self.event()
            self.update()
            self.draw()
                
    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
                    
    def update(self):
        self.person.update()
        
    def draw(self):
        self.screen.blit(bg_image, (0, 0))
        self.person.draw(self.screen)
        pg.display.flip()

if __name__ == "__main__":
    pg.init()
    Screensaver()

          
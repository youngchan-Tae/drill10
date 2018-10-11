import main_state
import game_framework
from pico2d import *


name = "PauseState"
image = None

class Pause:
    def __init__(self):
        self.image = load_image('pause.png')
        self.ps = 0

    def draw(self):
        if(self.ps == 1):
            self.image.draw(400, 340)

    def update(self):
        self.ps = (self.ps + 1) % 3





def enter():
    global image
    image = Pause()


def exit():
    global image
    del (image)

def update():
    image.update()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()


def draw():
    clear_canvas()
    main_state.grass.draw()
    main_state.boy.draw()
    image.draw()
    update_canvas()

def pause():
    pass

def resume():
    pass
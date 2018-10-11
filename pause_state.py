import main_state
import game_framework
from pico2d import *

name = "PauseState"
image = None


def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del (image)

def update():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state(main_state)


def draw():
    clear_canvas()
    image.draw(50, 50)
    update_canvas()

def pause():
    pass

def resume():
    pass
import pygame as pg
import objetos as objs
import viewport as vp


class WindowController:
    def __init__(self, window: objs.Window, viewport: vp.Viewport):
        self.window = window
        self.viewport = viewport
        self.mouse_state = False
        self.control_key = False

        self.mouse = (0, 0)


    def mouse_clicked(self, button, x, y):
        if button == 1:
            self.mouse_state = True
            self.mouse = self.viewport.transform_mouse(x, y)
        
        if button == 4:
            self.window.zoom(1.15)
        
        if button == 5:
            self.window.zoom(0.85)
        

    def mouse_released(self, button, x, y):
        if button == 1:
            self.mouse_state = False
    

    def key_pressed(self, key):
        pass


    def update(self):
        if self.mouse_state:
            new_pos = self.viewport.transform_mouse(*pg.mouse.get_pos())

            desloc = self.mouse - new_pos
            self.window.move(desloc[0], desloc[1])

            self.mouse = self.viewport.transform_mouse(*pg.mouse.get_pos())
        



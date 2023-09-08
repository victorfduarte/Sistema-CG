import pygame
import objetos as objs

class Viewport:

    def __init__(self, window: objs.Window):
        self.width = 800
        self.height = 600

        self.window = window

        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Transformada de Viewport")
    

    def draw(self, displayfile: 'list[objs.Objeto]'):
        xline = self.calc_xvp(0)
        yline = self.calc_yvp(0)

        pygame.draw.line(self.display, (255,0,0), (0, yline), (self.width, yline))
        pygame.draw.line(self.display, (0,255,0), (xline, 0), (xline, self.height))

        for obj in displayfile:
            objpoints = []

            for ponto in obj.pontos:
                objpoints.append(self.transform(ponto))
            
            obj.draw(self.display, objpoints)
    

    def transform(self, ponto: objs.Ponto):
        xvp = self.calc_xvp(ponto.x)
        yvp = self.calc_yvp(ponto.y)

        return objs.Ponto(xvp, yvp)
    

    def calc_xvp(self, x):
        return (x - self.window.x) / (self.window.width) * self.width

    def calc_yvp(self, y):
        return (1 - (y - self.window.y) / (self.window.height)) * self.height
    

    def transform_mouse(self, x, y):
        mx = x / self.width * self.window.width + self.window.x
        my = (1 - y / self.height) * self.window.height + self.window.y

        mx, my = round(mx, 3), round(my, 3)

        return objs.Ponto(mx, my)
    

    def clean(self):
        self.display.fill((225, 225, 225))




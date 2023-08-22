import pygame


class Window:
    def __init__(self, xmin, ymin, xmax, ymax):
        self.x = xmin
        self.y = ymin
        self.width = xmax - xmin
        self.height = ymax - ymin
    

    def move(self, x: float, y: float):
        ''' Move x pixels para a direita e y pixels para cima'''
        self.x += x
        self.y += y
    

    def zoom(self, prop: int):
        self.width *= prop
        self.height *= prop



class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.coordinate = x, y
    
    def __getitem__(self, value):
        return self.coordinate[value]
    
    def __len__(self):
        return 2



class Objeto:
    def __init__(self, nome: str, tipo: str):
        self.nome = nome
        self.tipo = tipo    # 'Reta' ou 'Poli'
        self.pontos: 'list[Ponto]' = []
    
    @classmethod
    def draw(cls, screen, *pontos: Ponto): ...



class Reta(Objeto):
    def __init__(self, nome: str, ponto1: Ponto, ponto2: Ponto):
        super().__init__(nome, 'Reta')

        self.pontos.extend((ponto1, ponto2))
    

    @classmethod
    def draw(cls, screen, pontos: Ponto):
        pygame.draw.line(screen, (0,0,0), *pontos)



class Poligono(Objeto):
    def __init__(self, nome: str, *pontos: Ponto):
        super().__init__(nome, 'Poli')

        self.pontos.extend(pontos)


    @classmethod
    def draw(cls, screen, pontos: 'list[Ponto]'):
        pygame.draw.polygon(screen, (0,0,0), pontos, width=1)


displayfile: 'list[Objeto]' = []
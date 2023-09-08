import pygame


class Window:
    def __init__(self, xmin, ymin, xmax, ymax):
        self.x = xmin
        self.y = ymin

        self.width = xmax - xmin
        self.height = ymax - ymin

        self.original_size = self.width, self.height
        self.izoom = 1
    

    def move(self, x: float, y: float):
        ''' Move x pixels para a direita e y pixels para cima'''
        self.x += x
        self.y += y
    

    def zoom(self, prop: float):
        self.izoom = round(self.izoom * prop, 2)
        self.width  = self.original_size[0] / self.izoom
        self.height = self.original_size[1] / self.izoom



class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.coordinate = x, y

    def __sub__(self, other):
        return Ponto(self.x - other.x, self.y - other.y)
    
    def __getitem__(self, value):
        return self.coordinate[value]
    
    def __len__(self):
        return 2
    
    def __repr__(self):
        return f'<Ponto(x={self.x}, y={self.y})>'



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



class DisplayFile:
    def __init__(self):
        self.objects: 'list[Objeto]' = []
        self.status = 'NONE'    # NONE, UPDATED
    

    def get_status(self):
        status = self.status
        self.status = 'NONE'
        return status
    

    def add(self, obj: Objeto):
        self.objects.append(obj)
        self.status = 'UPDATED'


    def __getitem__(self, value):
        return self.objects[value]
    
    def __len__(self):
        return len(self.objects)



displayfile = DisplayFile()
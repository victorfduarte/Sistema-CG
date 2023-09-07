import pygame
import PySimpleGUI as sg

pygame.init()

import windows as wd
import checkers
import create_objs

import objetos as objs
import viewport as vp


window = objs.Window(1.27, 0.67, 5.27, 3.67)
viewport = vp.Viewport(window)

clock = pygame.time.Clock()

# OBJETOS ---
objs.displayfile.append(
    objs.Poligono(
        'Poli1',
        objs.Ponto(1, 1),
        objs.Ponto(1.5, 1),
        objs.Ponto(1.5, 0.5),
        objs.Ponto(1, 0.5),
    )
)

objs.displayfile.append(
    objs.Poligono(
        'Poli2',
        objs.Ponto(6.5, 3.5),
        objs.Ponto(8.77, 4.01),
        objs.Ponto(8.3, 5.56),
        objs.Ponto(7.1, 6.54),
        objs.Ponto(5.6, 6.14),
        objs.Ponto(7.4, 5.56),
        objs.Ponto(4.84, 5.37),
        objs.Ponto(6.08, 4.95),
    )
)
# ------ #


painel: sg.Window = wd.window_control.create(objs.displayfile)
adicionar: sg.Window = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Fechou')
            pygame.quit()
            painel.close()
            quit()
        
    viewport.clean()
    
    viewport.draw(objs.displayfile)

    pygame.display.update()

    # ------------- #
    # --- Janela ---#

    janela, event, value = sg.read_all_windows(timeout=clock.tick(60))

    if event == '__TIMEOUT__':
        continue

    # Painel: Window
    if janela == painel:
        action = wd.window_control.read(painel, event, value)
    
        match action:
            case 'quit':
                pygame.quit()
                painel.close()
                quit()

            case 'move-right':
                window.move(0.5, 0)
            case 'move-left':
                window.move(-0.5, 0)
            case 'move-top':
                window.move(0, 0.5)
            case 'move-bottom':
                window.move(0, -0.5)

            case 'zoom+':
                window.zoom(0.75)
            case 'zoom-':
                window.zoom(1.25)
        
            case 'criar':
                adicionar = wd.window_adicionar.create()
        
    
    # Adicionar: Window
    if janela == adicionar:
        print(janela)
        action = wd.window_adicionar.read(adicionar, event, value)

        match action:
            case 'close':
                adicionar.close()
            
            case 'create-reta':
                if reta := create_objs.create_reta(adicionar):
                    objs.displayfile.append(reta)

                adicionar.close()


        wd.window_control.update(
            painel, list_objs=[obj.nome for obj in objs.displayfile]
        )

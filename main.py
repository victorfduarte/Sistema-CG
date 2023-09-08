import pygame
import PySimpleGUI as sg

pygame.init()

import windows as wd
import create_objs

import objetos as objs
import viewport as vp
import ferramentas as tools


window = objs.Window(-10, -10, 30, 20)
viewport = vp.Viewport(window)

mouse_point = objs.Ponto(0, 0)

wdcontroller = tools.window.WindowController(window, viewport)

clock = pygame.time.Clock()

# OBJETOS ---
objs.displayfile.add(
    objs.Poligono(
        'Poli1',
        objs.Ponto(1, 1),
        objs.Ponto(1.5, 1),
        objs.Ponto(1.5, 0.5),
        objs.Ponto(1, 0.5),
    )
)

objs.displayfile.add(
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
proriedades: sg.Window = wd.window_propriedades.create(window)
adicionar: sg.Window = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Fechou')
            pygame.quit()
            painel.close()
            quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
           wdcontroller.mouse_clicked(event.button, *event.pos)
        
        if event.type == pygame.MOUSEBUTTONUP:
           wdcontroller.mouse_released(event.button, *event.pos)
    
    wdcontroller.update()

        
    viewport.clean()
    
    viewport.draw(objs.displayfile)

    pygame.display.update()

    # ------------- #
    # --- Janela ---#

    janela, event, value = sg.read_all_windows(timeout=clock.tick(60))

    if event == '__TIMEOUT__':
        if objs.displayfile.get_status() == 'UPDATED':
            wd.window_control.update(
                list_objs=[obj.nome for obj in objs.displayfile]
            )
        
        wd.window_propriedades.update(window)

        continue

    # Painel: Window
    if janela == painel:
        action = wd.window_control.read(event, value)
    
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
                window.zoom(1.15)
            case 'zoom-':
                window.zoom(0.85)
        
            case 'criar':
                adicionar = wd.window_adicionar.create()
    

    if janela == proriedades:
        action = wd.window_propriedades.read(event, value)

        if action == 'close':
            pygame.quit()
            proriedades.close()
            quit()
        
    
    # Adicionar: Window
    if janela == adicionar:
        print(janela)
        action = wd.window_adicionar.read(event, value)

        if action == 'close':
            adicionar.close()
            
        elif action[0] == 'create-reta':
            if reta := create_objs.create_reta(action[1]):
                if reta == None: print('ERRO')
                objs.displayfile.add(reta)

            adicionar.close()

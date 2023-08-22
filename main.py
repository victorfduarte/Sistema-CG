import pygame
import PySimpleGUI as sg

pygame.init()

import windows as wd

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


painel = wd.windows_control.window_control(objs.displayfile)
adicionar = None

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

    if janela == painel:
        if event == sg.WIN_CLOSED:
            pygame.quit()
            painel.close()
            quit()
    
        match event:
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
        
        if event == '-criar-':
            adicionar = wd.windows_control.window_adicionar()
        
    

    if janela == adicionar:
        if event == sg.WIN_CLOSED:
            adicionar.close()
        
        if event == '-OK-':
            if adicionar['-TAB-TIPO-'].get() == '-RETA-':
                nome = adicionar['-NOME-'].get()

                xini = adicionar['-XINI-'].get()
                yini = adicionar['-YINI-'].get()
                xfim = adicionar['-XFIM-'].get()
                yfim = adicionar['-YFIM-'].get()

                if not nome or not xini or not yini or not xfim or not yfim:
                    print('Preencha os campos')
                    continue

                for obj in objs.displayfile:
                    if nome == obj.nome:
                        print('Nome já existente')
                
                pt_ini = objs.Ponto(int(xini), int(yini))
                pt_fim = objs.Ponto(int(xfim), int(yfim))

                objs.displayfile.append(
                    objs.Reta(nome, pt_ini, pt_fim)
                )
    
            obj_names = [obj.nome for obj in objs.displayfile]
            painel['-LIST-OBJS-'].update(values=obj_names)

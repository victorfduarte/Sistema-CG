import PySimpleGUI as sg

layout = [
    [sg.Text("Painel de Controle", font=('Arial', 18, 'bold'))],
    [sg.Frame('Objetos', layout=[
        [sg.Listbox(
            [], size=(1, 5),
            select_mode=sg.LISTBOX_SELECT_MODE_BROWSE,
            expand_x=True, expand_y=True, key='-LIST-OBJS-'
        )],
        [sg.Button('Criar', key='-CRIAR-', expand_x=True)]
    ], expand_x=True, expand_y=True)],
    [sg.Frame('Controles', layout=[
        [sg.Button('In', key='-ZOOM-IN-', size=(3,1), expand_x=True),
         sg.Button('▲', key='-MOVE-TOP-', size=(3,1), expand_x=True),
         sg.Button('Out', key='-ZOOM-OUT-', size=(3,1), expand_x=True)],
        [sg.Button('◄', key='-MOVE-LEFT-', size=(1,1), expand_x=True),
         sg.Button('▼', key='-MOVE-DOWN-', size=(1,1), expand_x=True),
         sg.Button('►', key='-MOVE-RIGHT-', size=(1,1), expand_x=True)],
    ], expand_x=True)]
]


def create(displaylist):
    window = sg.Window(
        "Controle", layout, font=('Arial', 12),
        finalize=True, location=(1300, 300)
    )

    window['-LIST-OBJS-'].update(values=[obj.nome for obj in displaylist])

    return window


def update(window, **updates):
    window['-LIST-OBJS-'].update(values=updates['list_objs'])


def read(window, event, value, **updates):
    if event == sg.WIN_CLOSED:
        return 'quit'

    if event == '-MOVE-RIGHT-':
        return 'move-right'
    elif event == '-MOVE-LEFT-':
        return 'move-left'
    elif event == '-MOVE-TOP-':
        return 'move-top'
    elif event == '-MOVE-DOWN-':
        return 'move-bottom'
    elif event == '-ZOOM-IN-':
        return 'zoom+'
    elif event == '-ZOOM-OUT-':
        return 'zoom-'
    
    if event == '-CRIAR-':
        return 'criar'
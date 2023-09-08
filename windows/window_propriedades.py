import PySimpleGUI as sg
import objetos as objs

window = None


def create(objwindow: objs.Window):
    global window

    window_layout = [
        [sg.HSep()],
        [sg.Text('Window Properties', font=('Arial', 13, 'bold'))],
        [sg.HSep()],
        [sg.Column([
            [sg.Text('position:')],
            [sg.Text('zoom:')]
         ], expand_x=True),
         sg.VSeparator(),
         sg.Column([
            [sg.Text(
                f'{objwindow.x},  {objwindow.y}',
                expand_x=True, justification='right', key='-WINDOW-POS-'
             )],
            [sg.Text(
                f'{objwindow.izoom}x',
                expand_x=True, justification='right', key='-WINDOW-ZOOM-'
             )]
         ], expand_x=True),
        ],
        [sg.HSep()],
    ]

    selected_object_layout = [
        []
    ]

    layout = [
        *window_layout,
        [sg.Text('Objects Properties', font=('Arial', 13, 'bold'))],
        [sg.HSep()],
        [sg.Column([
            [sg.Text('position:')],
            [sg.Text('zoom:')]
         ], expand_x=True),
         sg.VSeparator(),
         sg.Column([
            [sg.Text(
                f'{objwindow.x},  {objwindow.y}',
                expand_x=True, justification='right', key='-WINDOW-POS-'
             )],
            [sg.Text(
                '1',
                expand_x=True, justification='right', key='-WINDOW-ZOOM-'
             )]
         ], expand_x=True),
        ],
    ]

    window = sg.Window(
        "Propriedades", layout, font=('Arial', 12),
        finalize=True, location=(100, 300), margins=(2,2), resizable=True
    )
    return window


def read(event, value):
    global window

    if event == sg.WIN_CLOSED:
        return 'close'


def update(objwindow):
    global window

    window['-WINDOW-POS-'].update(value=f'{objwindow.x:.2f},  {objwindow.y:.2f}')
    window['-WINDOW-ZOOM-'].update(value=f'{objwindow.izoom}x')
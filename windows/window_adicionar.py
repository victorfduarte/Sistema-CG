import PySimpleGUI as sg
import checkers

window = None

def create():
    global window

    layout = [
        [sg.Text(
            'Criar Objeto', font=('Arial', 18, 'bold'),
            justification='center', expand_x=True
        )],
        [sg.HSeparator()],
        [sg.Text('Nome: '), sg.Input(size=(20, 1), key='-NOME-')],
        [sg.HSeparator()],
        [sg.Frame('Pontos', [
            [sg.Text('X:'), sg.Input(size=[4,1], key='-XINI-'), sg.VSeparator(),
                sg.Text('Y:'), sg.Input(size=[4,1], key='-YINI-')],
            [sg.Text('X:'), sg.Input(size=[4,1], key='-XFIM-'), sg.VSeparator(),
                sg.Text('Y:'), sg.Input(size=[4,1], key='-YFIM-')]
        ], expand_y=True)],
        [sg.Button('OK', key='-OK-', expand_x=True)]
    ]

    window = sg.Window("Controle", layout, font=('Arial', 12), modal=True, finalize=True)

    return window



def read(event, value, **updates):
    global window

    if event == sg.WIN_CLOSED:
        return 'close'
    
    if event == '-OK-':
        if checkers.is_all_empty(
                window['-NOME-'].get(), window['-XINI-'].get(),
                window['-YINI-'].get(), window['-XFIM-'].get(),
                window['-YFIM-'].get(),
        ):
            return 'pass'
        
        if not checkers.is_all_numeric(
                window['-XINI-'].get(), window['-YINI-'].get(), 
                window['-XFIM-'].get(), window['-YFIM-'].get()
        ):
            return 'pass'
        
        return (
            'create-reta',
            {
                'name': window['-NOME-'].get(),
                'x_inicial': float(window['-XINI-'].get()),
                'y_inicial': float(window['-YINI-'].get()),
                'x_final': float(window['-XFIM-'].get()),
                'y_final': float(window['-YFIM-'].get())
            }
        )

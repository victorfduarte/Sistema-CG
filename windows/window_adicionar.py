import PySimpleGUI as sg



def create():
    frame_pontos = [
        [sg.Text('X:'), sg.Input(size=[4,1]), sg.VSeparator(),
            sg.Text('Y:'), sg.Input(size=[4,1])],
        [sg.Text('X:'), sg.Input(size=[4,1]), sg.VSeparator(),
            sg.Text('Y:'), sg.Input(size=[4,1])]
    ]


    # TABS
    tab_reta = sg.Tab('Reta', key='-RETA-', layout=[
        [sg.Frame('Pontos', [
            [],
            [sg.Text('X:'), sg.Input(size=[4,1], key='-XINI-'), sg.VSeparator(),
                sg.Text('Y:'), sg.Input(size=[4,1], key='-YINI-')],
            [sg.Text('X:'), sg.Input(size=[4,1], key='-XFIM-'), sg.VSeparator(),
                sg.Text('Y:'), sg.Input(size=[4,1], key='-YFIM-')]
        ], expand_y=True)]
    ], element_justification='center')


    tab_poligono = sg.Tab('Polígono', key='-POLI-', layout=[
        [sg.Frame('Pontos', [
            *frame_pontos,
            [sg.HSeparator()],
            [sg.Button('Adicionar', key='-ADD-PONTO-', expand_x=True),
                sg.Button('Excluir', key='-EXC-PONTO-', expand_x=True)]
        ], expand_y=True)]
    ], element_justification='center')
    ##

    layout = [
        [sg.Text(
            'Criar Objeto', font=('Arial', 18, 'bold'),
            justification='center', expand_x=True
        )],
        [sg.HSeparator()],
        [sg.Text('Nome: '), sg.Input(size=(20, 1), key='-NOME-')],
        [sg.HSeparator()],
        [sg.TabGroup([[tab_reta, tab_poligono]], expand_x=True, key='-TAB-TIPO-')],
        [sg.Button('OK', key='-OK-', expand_x=True)]
    ]


    return sg.Window("Controle", layout, font=('Arial', 12), modal=True, finalize=True)



def read(window, event, value, **updates):
    if event == sg.WIN_CLOSED:
        return 'close'
    
    if event == '-OK-':
        if window['-TAB-TIPO-'].get() == '-RETA-':
            return 'create-reta'
                
    if event == '-ADD-PONTO-':
        ...

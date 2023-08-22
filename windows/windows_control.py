import PySimpleGUI as sg


def window_control(displaylist):
    layout = [
        [sg.Text("Painel de Controle", font=('Arial', 18, 'bold'))],
        [sg.Frame('Objetos', layout=[
            [sg.Listbox(
                [obj.nome for obj in displaylist], size=(1, 5),
                select_mode=sg.LISTBOX_SELECT_MODE_BROWSE,
                expand_x=True, expand_y=True, key='-LIST-OBJS-'
            )],
            [sg.Button('Criar', key='-criar-', expand_x=True)]
        ], expand_x=True, expand_y=True)],
        [sg.Frame('Controles', layout=[
            [sg.Button('In', key='zoom+', size=(3,1), expand_x=True),
             sg.Button('▲', key='move-top', size=(3,1), expand_x=True),
             sg.Button('Out', key='zoom-', size=(3,1), expand_x=True)],
            [sg.Button('◄', key='move-left', size=(1,1), expand_x=True),
             sg.Button('▼', key='move-bottom', size=(1,1), expand_x=True),
             sg.Button('►', key='move-right', size=(1,1), expand_x=True)],
        ], expand_x=True)]
    ]

    return sg.Window("Controle", layout, font=('Arial', 12), finalize=True, location=(1300, 300))



def window_adicionar():
    tab_reta = sg.Tab('Reta', key='-RETA-', layout=[
        [sg.Frame('Pontos', [
            [sg.Text('X:'), sg.Input(size=[4,1], key='-XINI-'), sg.VSeparator(),
             sg.Text('Y:'), sg.Input(size=[4,1], key='-YINI-')],
            [sg.Text('X:'), sg.Input(size=[4,1], key='-XFIM-'), sg.VSeparator(),
             sg.Text('Y:'), sg.Input(size=[4,1], key='-YFIM-')]
        ], expand_x=True, element_justification='center')]
    ])

    tab_poligono = sg.Tab('Polígono', key='-POLI-', layout=[
        [sg.Frame('Pontos', [
            [sg.Text('X:'), sg.Input(size=[4,1]), sg.VSeparator(),
             sg.Text('Y:'), sg.Input(size=[4,1])],
            [sg.Text('X:'), sg.Input(size=[4,1]), sg.VSeparator(),
             sg.Text('Y:'), sg.Input(size=[4,1])]
        ], expand_x=True, element_justification='center')]
    ])

    layout = [
        [sg.Text(
            'Criar Objeto', font=('Arial', 18, 'bold'),
            justification='center', expand_x=True
        )],
        [sg.Text('Nome: '), sg.Input(size=(20, 1), key='-NOME-')],
        [sg.TabGroup([[tab_reta, tab_poligono]], expand_x=True, key='-TAB-TIPO-')],
        [sg.Button('OK', key='-OK-', expand_x=True)]
    ]

    return sg.Window("Controle", layout, font=('Arial', 12), modal=True, finalize=True)

    
    
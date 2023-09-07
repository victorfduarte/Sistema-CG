import PySimpleGUI as sg
import checkers
import objetos as objs


def create_reta(window: sg.Window):
    if checkers.is_all_empty(
            window['-NOME-'].get(), window['-XINI-'].get(),
            window['-YINI-'].get(), window['-XFIM-'].get(),
            window['-YFIM-'].get(),
    ):
        return None

    nome = window['-NOME-'].get()

    if nome in (obj.nome for obj in objs.displayfile):
        return None

    if not checkers.is_all_numeric(
            window['-XINI-'].get(), window['-YINI-'].get(), 
            window['-XFIM-'].get(), window['-YFIM-'].get()
    ):
        return None

    positions = checkers.convert_to_int(
        window['-XINI-'].get(), window['-YINI-'].get(), 
        window['-XFIM-'].get(), window['-YFIM-'].get()
    )

    pt1 = positions[:2]
    pt2 = positions[2:]

    pt_ini = objs.Ponto(*pt1)
    pt_fim = objs.Ponto(*pt2)

    return objs.Reta(nome, pt_ini, pt_fim)
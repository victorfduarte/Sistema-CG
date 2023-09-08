import PySimpleGUI as sg
import objetos as objs


def create_reta(data: dict):
    nome = data['name']

    if nome in (obj.nome for obj in objs.displayfile):
        return None

    pt1 = data['x_inicial'], data['y_inicial']
    pt2 = data['x_final'], data['y_final']

    pt_ini = objs.Ponto(*pt1)
    pt_fim = objs.Ponto(*pt2)

    return objs.Reta(nome, pt_ini, pt_fim)
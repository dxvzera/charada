import os
import sys
import pyautogui as pag
import pyperclip as pyp


def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)


pag.alert("Tenho uma charada para você...")
charada = pag.confirm(text="Você tem um cachorro chamado nabunda, e você foi navegar com ele no seu barco, mas aí o barco afunda, você leva nabunda ou deixa nabunda?", title="Charada", buttons=['leva nabunda', 'deixa nabunda', 'nabunda nada'])
if charada is None:
    restart()

elif charada == "leva nabunda":
    resposta = pag.alert(text=f"ahhh então você leva na bunda?!", button=f"sim, eu AMO levar na bunda!")
    if resposta is None:
        restart()

elif charada == "deixa nabunda":
    resposta = pag.alert(text=f"ahhh então você deixa na bunda?!", button=f"sim, eu AMO deixar na bunda!")
    if resposta is None:
        restart()

elif charada == "nabunda nada":
    resposta = pag.alert(text="Mas nabunda não sabe nadar... se você não levar nabunda ele vai afundar!", button="Essa não!")
    if resposta is None:
        restart()

    charada2 = pag.confirm(text="então você leva nabunda ou afunda nabunda?", buttons=['leva nabunda','afunda nabunda','nabunda voa'])
    if charada2 is None:
        restart()

    elif charada2 == "leva nabunda":
        resposta = pag.alert(text=f"ahhh então você leva nabunda?!", button=f"sim, eu AMO levar nabunda!")
        if resposta is None:
            restart()


    elif charada2 == "afunda nabunda":
        resposta = pag.alert(text=f"ahhh então você afunda na bunda?!", button=f"sim, eu AMO afundar na bunda!")
        if resposta is None:
            restart()

    elif charada2 == "nabunda voa":
        resposta = pag.alert(text="mas nabunda não sabe voar!", button="Essa não!")
        if resposta is None:
            restart()

        charada3 = pag.confirm(text="Se nabunda não voa então como que você vai fazer?", buttons=['estora nabunda'])
        if charada3 is None:
            restart()

        elif charada3 == "estora nabunda":
            resposta = pag.alert(text=f"ahhh então você estora na bunda?!", button=f"sim, eu AMO estorar na bunda!")
            if resposta is None:
                restart()

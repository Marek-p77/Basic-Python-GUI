# Basic Python GUI by Marek_p

import PySimpleGUI as sg # Import staženého modulu pro GUI. Lze stáhnout příkazem: py -m pip install PySimpleGUI

layout = [  [sg.Text("Přihlašte se prosím", text_color='white', background_color='#000')], # Nadpis v GUI (první řádek)
            [sg.Text("Uživatel:", text_color='white', background_color='#000')], # Druhý řádek v GUI
            [sg.Input(background_color='#4E6578')], # Textové pole pro první hodnotu (v našem případě uživatelské jméno) (třetí řádek)
            [sg.Text("Heslo:", text_color='white', background_color='#000')], # Čtvrtý řádek
            [sg.Input(background_color='#4E6578')], # Textové pole pro druhou hodnotu (v našem případě heslo) (pátý řádek)
            [sg.Text(" ", text_color='white', background_color='#000')], # Mezera mezi textovým polem a tlačítkem (prázdný text na šestém řádku)
            [sg.Button('Přihlásit se', button_color='#08a4ff')] ] # Tlačítko pro potvrzení / ukončení programu

window = sg.Window('GalaxySystems', layout, background_color='#000') # Nadpis GUI + Barva pozadí

event, values = window.read() # Otevření GUI
print('[LOG]', values[0], "se přihlásil s heslem ", values[1]) # Vypsání textu z textových polí do příkazového řádku
window.close() # Zavření GUI

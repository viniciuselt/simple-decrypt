from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('DarkPurple2')
layout = [
    [sg.Text('Descriptografia', font=("Helvetica", 20), justification='center', expand_x=True)],
    [sg.Column([
        [sg.Text('Digite sua frase criptografada:', font=("Helvetica", 12)), sg.Input(key='chave', size=(78, 7))],
        [sg.Text('Frase descriptografada:', font=("Helvetica", 12)), sg.Input(key='saida', size=(84, 7), disabled=True)]
    ], element_justification='c'), 
     sg.Column([
         [sg.Button('Decrypt', size=(10, 2))]
     ], element_justification='c')]
]

# Janela
janela = sg.Window('Descriptografia Simples', layout)

# Ler os eventos
while True:
    events, valores = janela.read()
    if events == sg.WINDOW_CLOSED:
        break
    if events == 'Decrypt':
        chave = valores['chave']
        decrypt = ''
        for letter in chave:
            if letter in '4': decrypt += 'a'  
            elif letter in '8': decrypt += 'b'  
            elif letter in 'ç': decrypt += 'c' 
            elif letter in '0': decrypt += 'd'   
            elif letter in '3': decrypt += 'e'  
            elif letter in '*': decrypt += 'f'
            elif letter in '¨': decrypt += 'g'
            elif letter in '&': decrypt += 'h'
            elif letter in '5': decrypt += 'i'
            elif letter in '%': decrypt += 'j'
            elif letter in '|': decrypt += 'k'
            elif letter in '-': decrypt += 'L'
            elif letter in '%': decrypt += 'm'
            elif letter in '@': decrypt += 'n'
            elif letter in ':': decrypt += 'o'
            elif letter in '#': decrypt += 'p'
            elif letter in '+': decrypt += 'q'
            elif letter in '!': decrypt += 'r'
            elif letter in '>': decrypt += 's'
            elif letter in '^': decrypt += 't'
            elif letter in '<': decrypt += 'u'
            elif letter in ';': decrypt += 'v'
            else:
                decrypt += letter
        janela['saida'].update(decrypt)
        print(f'A descriptografia gerada para sua frase foi: {decrypt}')
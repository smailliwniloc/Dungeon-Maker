import PySimpleGUI as sg
import random

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Enter number and type of dice')],
            [sg.Text('How many die are you rolling?'), sg.InputText()],
            [sg.Text('How many sides does your die have'), sg.InputText()],
            [sg.Text(key='-OUTPUT-')],
            [sg.Button('Calculate Result'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
count = 0
total = 0
def main():
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'Calculate Result':
            result = []
            for i in range(int(values[0])):
                result.append(random.randint(1, int(values[1])))
            roll = sum(result)
            total += roll
            count += 1
            window['-OUTPUT-'].update('All rolls: ' + str(result) + '\n' + 'Total roll: ' + str(roll) + '\n' + 'Average of rolls: ' + str(total/count))

if __name__ == "__main__":
    main()
    window.close()


from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label



class TicTacBox(Button):
    clicked = 'not'
    markup = True

    def __init__(self, i, **kwargs):
        super(TicTacBox,self).__init__(**kwargs)
        self.id = str(i)
        self.text = ''
        self.font_size = '70px'
        self.background_color = (1, 1, 1, 0)
        self.size_hint_y = 0.333
        self.size_hint_x = 0.333
        if i == 0:
            self.pos_hint = {'x': 0, 'y': 0}
        elif i == 1:
            self.pos_hint = {'x': 0.333, 'y': 0}
        elif i == 2:
            self.pos_hint = {'x': 0.666, 'y': 0}
        elif i == 3:
            self.pos_hint = {'x': 0, 'y': 0.333}
        elif i == 4:
            self.pos_hint = {'x': 0.333, 'y': 0.333}
        elif i == 5:
            self.pos_hint = {'x': 0.666, 'y': 0.333}
        elif i == 6:
            self.pos_hint = {'x': 0, 'y': 0.666}
        elif i == 7:
            self.pos_hint = {'x': 0.333, 'y': 0.666}
        else:
            self.pos_hint = {'x': 0.666, 'y': 0.666}
        self.bind(on_press=self.click)
        #Recognize the parent:
        self.parent = self.get_parent_window()

    def click(self, instance):
        if self.clicked=='not':
            if TictactoeWindow.turn=='x':
                self.clicked = 'x'
                self.text = '[b][font=fonts/Azonix]X[/font][/b]'
                self.color = (0, 1, 1, 1)
                TictactoeWindow.turn = 'o'
                TictactoeWindow.boxvalues[int(self.id)] = 'x'
            else:
                self.clicked = 'o'
                self.text = '[b][font=fonts/Azonix]O[/font][/b]'
                self.color = (1, 0, 0, 1)
                TictactoeWindow.turn = 'x'
                TictactoeWindow.boxvalues[int(self.id)] = 'o'
        val=[]
        app=[]
        for i in range(3):
            app.append(TictactoeWindow.boxvalues[i])
        val.append(app)
        app = []
        for i in range(3,6):
            app.append(TictactoeWindow.boxvalues[i])
        val.append(app)
        app = []
        for i in range(6,9):
            app.append(TictactoeWindow.boxvalues[i])
        val.append(app)
        del app

        #X WINS!
        if (val[0][0] == val[0][1] and val[0][0] == val[0][2] and val[0][0] == 'x') or (val[1][0] == val[1][1] and val[1][0] == val[1][2] and val[1][0] == 'x') or (val[2][0] == val[2][1] and val[2][0] == val[2][2] and val[2][0] == 'x') or (val[0][0] == val[1][0] and val[0][0] == val[2][0] and val[0][0] == 'x') or (val[0][1] == val[1][1] and val[0][1] == val[2][1] and val[0][1] == 'x') or (val[0][2] == val[1][2] and val[0][2] == val[2][2] and val[0][2] == 'x') or (val[0][0] == val[1][1] and val[0][0] == val[2][2] and val[0][0] == 'x') or (val[2][0] == val[1][1] and val[2][0] == val[0][2] and val[2][0] == 'x'):
            l = Button(text="[b][size=70][font=fonts/Azonix]X Wins![/font][/size][/b]", markup=True, color=(
                0, 1, 1, 1), background_color=(0, 0, 0, 0.8), size_hint=(0.9, 0.4), pos_hint={'x': 0.05, 'y': 0.3})
            l.bind(on_release=self.parent.clearboard)
            self.parent.add_widget(l)

        #Y WINS!
        elif val[0][0] == val[0][1] and val[0][0] == val[0][2] and val[0][0] == '0' or (val[1][0] == val[1][1] and val[1][0] == val[1][2] and val[1][0] == 'o') or (val[2][0] == val[2][1] and val[2][0] == val[2][2] and val[2][0] == 'o') or (val[0][0] == val[1][0] and val[0][0] == val[2][0] and val[0][0] == 'o') or (val[0][1] == val[1][1] and val[0][1] == val[2][1] and val[0][1] == 'o') or (val[0][2] == val[1][2] and val[0][2] == val[2][2] and val[0][2] == 'o') or (val[0][0] == val[1][1] and val[0][0] == val[2][2] and val[0][0] == 'o') or (val[2][0] == val[1][1] and val[2][0] == val[0][2] and val[2][0] == 'o'):
            l = Button(text="[b][size=70][font=fonts/Azonix]O Wins![/font][/size][/b]", markup=True, color=(
                1, 0, 0, 1), background_color=(0, 0, 0, 0.8), size_hint=(0.9, 0.4), pos_hint={'x': 0.05, 'y': 0.3})
            l.bind(on_release=self.parent.clearboard)
            self.parent.add_widget(l)

        #IT'S A PAIR!
        elif not ('not' in TictactoeWindow.boxvalues):
            l = Button(text="[b][size=70][font=fonts/Azonix]It's a pair![/font][/size][/b]", markup=True, color=(
                1, 1, 1, 1), background_color=(0, 0, 0, 0.8), size_hint=(0.9, 0.4), pos_hint={'x': 0.05, 'y': 0.3})
            l.bind(on_release=self.parent.clearboard)
            self.parent.add_widget(l)



class TictactoeWindow(RelativeLayout):
    turn = 'x'
    boxvalues = ['not' for i in range(9)]

    def __init__(self, **kwargs):
        super(TictactoeWindow,self).__init__(**kwargs)
        self.set()

    def set(self):
        self.clear_widgets()
        TictactoeWindow.turn = 'x'
        TictactoeWindow.boxvalues = ['not' for i in range(9)]
        self.orientation = 'vertical'
        img = Image(source='imgs/Tic-tac-toe.png', size=Window.size)
        self.add_widget(img)
        Window.size = (600, 600)
        for i in range(9):
            box = TicTacBox(i)
            self.add_widget(box)
    
    def clearboard(self, button):
        for child in self.children:
            if isinstance(child, TicTacBox):
                child.text = ''
                child.clicked = 'not'
        self.remove_widget(button)
        TictactoeWindow.boxvalues = ['not' for i in range(9)]
        TictactoeWindow.turn = 'x'



class TicTacToeApp(App):
    def build(self):
        return TictactoeWindow()



if __name__ == '__main__':
    TicTacToeApp().run()

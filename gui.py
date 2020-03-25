from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from app import main
import time
from functools import partial
from kivy.clock import Clock

count = 0

class ClearApp(App):

    def build(self):

        self.box = BoxLayout(orientation='vertical', spacing=2)

        self.box2 = BoxLayout(orientation='horizontal', spacing=20)

        self.lblWork = Label(text='Please provide work time:', font_size='30sp', markup=True)
        self.lblPause = Label(text='Please provide pause time:', font_size='30sp', markup=True)
        self.lblCycles = Label(text='Please provide cycles:', font_size='30sp', markup=True)

        self.txtWork = TextInput(hint_text='Time in minutes', font_size="60sp")
        self.txtPause = TextInput(hint_text='Time in minutes', font_size="60sp")
        self.txtCycles = TextInput(hint_text='How many times', font_size="60sp")

        self.btn2 = Button(text='Clear All', on_press=self.clearText)
        self.btn = Button(text='Start', on_press=self.submit)

        self.box2.add_widget(self.btn)
        self.box2.add_widget(self.btn2)

        self.box.add_widget(self.lblWork)
        self.box.add_widget(self.txtWork)
        self.box.add_widget(self.lblPause)
        self.box.add_widget(self.txtPause)
        self.box.add_widget(self.lblCycles)
        self.box.add_widget(self.txtCycles)
        self.box.add_widget(self.box2)

        return self.box


    def clearText(self, instance):

        self.txtWork.text = ''
        self.txtPause.text = ''
        self.txtCycles.text = ''


    def submit(self, instance):
        btn = Button(text='Stop')
        content = Label(font_size='100sp')
        box = BoxLayout(orientation='vertical', spacing=2)
        box.add_widget(content)
        box.add_widget(btn)
        popup = Popup(content=box, auto_dismiss=False)
        btn.bind(on_press=popup.dismiss)

        def update(instance):

            def my_callback(dt):
                global count
                workMinutes = int(self.txtWork.text)
                pauseMinutes = int(self.txtPause.text)
                cycleMinutes = int(self.txtCycles.text)
                l = main(workMinutes, pauseMinutes, cycleMinutes)
                if count == len(l):
                    content.text= 'DONE!'
                    return False
                content.text = l[count]
                count += 1

            Clock.schedule_interval(my_callback, 1)

        popup.bind(on_open=update)
        popup.open()



ClearApp().run()
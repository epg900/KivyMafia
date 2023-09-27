#Mafia.py
#-*- coding: utf-8 -*-
#super(Scr1, self).__init__()
#<img src="dist/im.jpg" alt='m' />

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import random
import arabic_reshaper
import bidi.algorithm
import time

class Scr1(GridLayout):
   def __init__(self):
     super().__init__()
     self.cols=2
     file = open("mafia.txt", "r",encoding='utf-8')
     self.lst= file.readlines()
     file.close()
     random.shuffle(self.lst)
     a=len(self.lst)
     for i in range(0,a):
     	 self.btn= Button(text=str(i+1),background_color =(0.2,0.9, 1, 1),font_name='BTitr.ttf',font_size=50)
     	 self.btn.bind(on_press=self.callback)
     	 self.add_widget(self.btn)
  
   def callback(self,instance):
     
     try:
      txt=arabic_reshaper.reshape(self.lst[int(instance.text)-1])
      txt2=bidi.algorithm.get_display(txt)
      #popup = Popup(title='Your Role',content=Label(text=txt2,font_name='BTitr.ttf',font_size=50,base_direction='rtl'))
      self.popup=Popup(title='',content=Button(text=txt2,font_name='BTitr.ttf',font_size=50,base_direction='rtl' , on_press = lambda *args: self.popup.dismiss()))
      self.popup.open()
      #time.sleep(8)
      #popup.dismiss()
      instance.disabled=True
     		
     except:
     	pass

class MyApp(App):
   def build(self):
   	return Scr1()
	 

if __name__ == '__main__':
    MyApp().run()	

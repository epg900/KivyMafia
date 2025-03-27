#Mafia.py
#-*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserListView
import random
import os, subprocess
import time
import glob



class Scr1(GridLayout):
   def __init__(self):
     super().__init__()
     self.game_path=""
     self.parent_game=""
     self.cols=1
     self.rows=2
     self.btn= Button(text="Select  Folder",background_color =(0.7,0.7,0.7, 1),font_size=40,halign="center", size_hint=(1,0.2))
     self.btn.bind(on_press=self.callback)
     self.fc = FileChooserListView(dirselect = True,filters=[self.is_dir])
     self.fc.bind(selection=self.getdir)
     self.add_widget(self.fc)
     self.add_widget(self.btn)
     
   
   def callback(self,instance):
     	try:
     		self.lst =glob.glob(f"{self.game_path}/*.jpg")
     		self.lst.sort()
     		self.lst=[l.split("/")[-1] for l in self.lst]
     		
     		e=[1,2,4]
     		
     		file=open("role.txt","r",encoding="utf-8")
     		self.lst2=file.readlines()
     		file.close()
     		self.lst2=[l.split("\n")[0] for l in self.lst2]
     		
     		random.shuffle(self.lst)
     		self.lst3=[]
     		for l in self.lst2:
     			if l in self.lst:
     				self.lst3.append(l)
     		random.shuffle(self.lst3)
     		
     		for i,v in enumerate(e):
     			if e[i]:
     				ix1=self.lst.index(self.lst3[i])
     				iv1=self.lst[e[i]-1]
     				self.lst[e[i]-1]=self.lst3[i]
     				self.lst[ix1]=iv1
     		
     		self.length=len(self.lst)
     		self.j = 0
     		self.btn2=Button(text="Select Role",background_normal=' ',background_color=(0.5,0.5,0.5,1),font_size=50)
     		self.btn2.bind(on_press=self.call2)
     		self.popup=Popup(title='',content=self.btn2)
     		self.popup.open()
     	except:
     		pass
   
   def getdir(self,path, fn):
         self.game_path=fn[0]
         self.parent_game=os.path.dirname(fn[0
        ])
         txt=fn[0].split("/")[-1]
         self.btn.text=f" [ {txt} ] \n\nStart Game"
         
   def is_dir(self, directory, filename):
        return os.path.isdir(os.path.join(directory, filename))
   
   def call2(self,instance):
     	if instance.text=="End":
     		self.popup.dismiss()
     	if self.j<self.length*2:
     		self.j+=1
     	else:
     		with open(f'{self.parent_game}/all_role.txt','w') as f:
     			for i,l in enumerate(self.lst):
     				f.write(f'{i+1}  >>   {l}\n')
     		
     	if self.j%2==1:
     		instance.text=""
     		instance.background_normal=self.game_path + "/" + self.lst[int(self.j/2)]
     	else:
     		if self.j<self.length*2-1:
     			 instance.text="Select Role"
     			 instance.background_normal=' '
     		else:
     			instance.text="End"
     			instance.background_normal=' '
     			
class MyApp(App):
   def build(self):
   	return Scr1()
	 

if __name__ == '__main__':
    MyApp().run()	

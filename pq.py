from kivy.properties import ObjectProperty, ListProperty, StringProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen,SlideTransition
from pyfingerprint.pyfingerprint import PyFingerprint
from kivy.core.image import Image as CoreImage
from kivy.storage.jsonstore import JsonStore
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from pyfirmata import ArduinoMega, util
#from kivy.graphics import BorderImage
from pyfirmata.util import Iterator
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.core.image import Image
from kivy.uix.label import Label
import serial.tools.list_ports
from kivy.lang import Builder
from kivy.clock import Clock
from os.path import join
from sys import platform
from kivy.app import App
import decimal, serial
import pyfirmata
import sqlite3
import getpass
import time
import os

# password
int = ID = 0;
int = ID2 = 0;
int = ID3 = 0;
int = ID4 = 0;
int = ID5 = 0;
conn = sqlite3.connect('Test.db')
c = conn.cursor()
ID = (ID + 1)
ID2 = (ID2 + 2)
ID3 = (ID3 + 3)
ID4 = (ID4 + 4)
ID5 = (ID5 + 5)

#fingerprint
#!/usr/bin/env python
# -*- coding: utf-8 -*-




#Code arduino
def serial_ports_linux():
        ports = list(serial.tools.list_ports.comports())  
        for port_no, description, address in ports:
                if 'ACM' in description:
                        return port_no
                if 'Arduino' in description:
                        return port_no
                if 'Serial' in description:
                        return port_no

if platform == 'linux' or platform == 'linux2':
        board = ArduinoMega(serial_ports_linux())
elif platform == 'win32':
        def serial_ports_win():
                ports = list(serial.tools.list_ports.comports())  
                for port_no, description, address in ports:
                        if 'Arduino' in description:
                                return port_no
                        if 'CH340' in description:
                                return port_no
board = ArduinoMega(serial_ports_linux())
board.digital[2].mode = pyfirmata.INPUT
for a in range(0,16):
        board.analog[a].enable_reporting()
it = util.Iterator(board)
it.start()

#arduino 2


#Code screen
Builder.load_string("""
#:import random random.random
#:import NoTransition kivy.uix.screenmanager.NoTransition

<TLabel@Label>:
        bold: True
        font_size: self.height/3
        canvas.before:
                Color:
                        rgba: 255,171,0,0.7
                Rectangle:
                        pos: self.pos
                        size: self.size
                        
<MenuScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                background_color: [1, 2, 1, 2]
                text: 'Deposit'
                italic: bool
                font_size: 50
                size_text: .3,.3
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.60}
                size: 450, 100
                on_release: root.manager.current = 'deposit'
                on_release: root.manager.transition = NoTransition(duration=0)
        Button:
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                background_color: [0,255,255,0.7]
                text: 'Withdraw'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.40}
                size: 450, 100
                on_release: root.manager.current = 'Withdraw'
                on_release: root.manager.transition = NoTransition(duration=0)
        Button:
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Admin'
                size_hint: None, None
                pos_hint: {'center_x':.15, 'center_y':.10}
                size: 150, 70
                on_release: root.manager.current = 'adminchose'
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        size_hint_y:.50
                        text: 'Menu'
        
<DepositScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                orientation: 'horizontal'
                text: 'BOX 1'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':.50, 'center_y':0.60}
                size: 150, 100
                on_state: root.output_pin01(*args)
                on_release: root.manager.current = 'box1in'
        Button:
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                orientation: 'horizontal'
                text: 'BOX 2'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':.70, 'center_y':.60}
                size: 150, 100
                on_state: root.output_pin02(*args)
                on_release: root.manager.current = 'box2in'
        Button:
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'BOX 3'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':.30, 'center_y':.40}
                size: 150, 100
                on_state: root.output_pin03(*args)
                on_release: root.manager.current = 'box3in'
        Button:
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                orientation: 'horizontal'
                text: 'BOX 4'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':.50, 'center_y':.40}
                size: 150, 100
                on_state: root.output_pin04(*args)
                on_release: root.manager.current = 'box4in'
        Button:
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'BOX 5'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':.70, 'center_y':.40}
                size: 150, 100
                on_state: root.output_pin05(*args)
                on_release: root.manager.current = 'box5in'
        Button:
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                background_color: [1, 2, 1, 2]
                text: 'Main Menu'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.20}
                size: 250, 100
                on_release: root.manager.current = 'menu'
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        size_hint_y: 30
                        text: 'Deposit chose Box '

<WithdrawScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'BOX 1'
                font_size: 25 
                size_hint: None, None
                pos_hint: {'center_x':.50, 'center_y':0.60}
                size: 150, 100
                on_state: root.output_pin01(*args)
                on_release: root.manager.current = 'box1outchose'
        Button:
                text: 'BOX 2'
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':.70, 'center_y':.60}
                size: 150, 100
                on_state: root.output_pin02(*args)
                on_release: root.manager.current = 'box2outchose'
        Button:
                text: 'BOX 3'
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':.30, 'center_y':.40}
                size: 150, 100
                on_state: root.output_pin03(*args)
                on_release: root.manager.current = 'box3outchose'
        Button:
                text: 'BOX 4'
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':.50, 'center_y':.40}
                size: 150, 100
                on_state: root.output_pin04(*args)
                on_release: root.manager.current = 'box4outchose'
        Button:
                text: 'BOX 5'
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':.70, 'center_y':.40}
                size: 150, 100
                on_state: root.output_pin05(*args)
                on_release: root.manager.current = 'box5outchose'
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Main Menu'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.20}
                size: 450, 100
                on_release: root.manager.current = 'menu'
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Withdraw Chose Box'
                        
<Box1outScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Next'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.30}
                size: 200, 70
                on_state: root.output_pin01(*args)
                on_press: root.signups(password.text)
                        
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Box 1 Enter Password '
        BoxLayout:
                size_hint: .20,.17
                height: 70
                orientation: 'vertical'
                pos_hint: {'center_x':.50, 'center_y':.50}
                Label:
                        text: ''
                        halign: 'left'
                        font_size: 18
                        text_size: root.width-20, 20
                TextInput:
                        id: password
                        multiline:False
                        password:True
                        font_size: 28
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Main Menu'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':0.25, 'center_y':0.30}
                size: 200, 70
                on_release: root.manager.current = 'menu'

<Box2outScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Next'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.35}
                size: 200,70
                on_state: root.output_pin01(*args)
                on_press: root.signups(password.text)
                
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Box 2 Enter Password'
        BoxLayout:
                size_hint: .20,.17
                height: 70
                orientation: 'vertical'
                pos_hint: {'center_x':.50, 'center_y':.50}
                Label:
                        text: ''
                        halign: 'left'
                        font_size: 18
                        text_size: root.width-20, 20
                TextInput:
                        id: password
                        multiline:False
                        password:True
                        font_size: 28
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Main Menu'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':0.25, 'center_y':0.30}
                size: 200, 70
                on_release: root.manager.current = 'menu'

<Box3outScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Next'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.35}
                size: 200, 70
                on_state: root.output_pin01(*args)
                on_press: root.signups(password.text)
                        
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Box 3 Enter Password '
        BoxLayout:
                size_hint: .20,.17
                height: 70
                orientation: 'vertical'
                pos_hint: {'center_x':.50, 'center_y':.50}
                Label:
                        text: ''
                        halign: 'left'
                        font_size: 18
                        text_size: root.width-20, 20
                TextInput:
                        id: password
                        multiline:False
                        password:True
                        font_size: 28
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Main Menu'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':0.25, 'center_y':0.30}
                size: 200, 70
                on_release: root.manager.current = 'menu'

<Box4outScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Next'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.35}
                size: 200, 70
                on_state: root.output_pin01(*args)
                on_press: root.signups(password.text)
                        
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Box 4 Enter Password '
        BoxLayout:
                size_hint: .20,.17
                height: 70
                orientation: 'vertical'
                pos_hint: {'center_x':.50, 'center_y':.50}
                Label:
                        text: ''
                        halign: 'left'
                        font_size: 18
                        text_size: root.width-20, 20
                TextInput:
                        id: password
                        multiline:False
                        password:True
                        font_size: 28
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Main Menu'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':0.25, 'center_y':0.30}
                size: 200, 70
                on_release: root.manager.current = 'menu'

<Box5outScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Next'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.35}
                size: 200, 70
                on_state: root.output_pin01(*args)
                on_press: root.signups(password.text)

        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Box 5 Enter Password '
        BoxLayout:
                size_hint: .20,.17
                height: 70
                orientation: 'vertical'
                pos_hint: {'center_x':.50, 'center_y':.50}
                Label:
                        text: ''
                        halign: 'left'
                        font_size: 18
                        text_size: root.width-20, 20
                TextInput:
                        id: password
                        multiline:False
                        password:True
                        font_size: 28
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Main Menu'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':0.25, 'center_y':0.30}
                size: 200, 70
                on_release: root.manager.current = 'menu'


<Box1outchoseScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Password'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.60}
                size: 450, 100
                on_release: root.manager.current = 'box1out'
                on_release: root.manager.transition = NoTransition(duration=0)
        Button:
                background_color: [0,255,255,0.7]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Fingerprint'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.40}
                size: 450, 100
                on_release: root.manager.current = 'box1outfinger'
                on_release: root.manager.transition = NoTransition(duration=0)
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Chose to unlock '

<Box2outchoseScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Password'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.60}
                size: 450, 100
                on_release: root.manager.current = 'box2out'
                on_release: root.manager.transition = NoTransition(duration=0)
        Button:
                background_color: [0,255,255,0.7]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Fingerprint'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.40}
                size: 450, 100
                on_release: root.manager.current = 'box2outfinger'
                on_release: root.manager.transition = NoTransition(duration=0)
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Chose to unlock '

<Box3outchoseScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Password'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.60}
                size: 450, 100
                on_release: root.manager.current = 'box3out'
                on_release: root.manager.transition = NoTransition(duration=0)
        Button:
                background_color: [0,255,255,0.7]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Fingerprint'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.40}
                size: 450, 100
                on_release: root.manager.current = 'box3outfinger'
                on_release: root.manager.transition = NoTransition(duration=0)
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Chose to unlock '

<Box4outchoseScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Password'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.60}
                size: 450, 100
                on_release: root.manager.current = 'box4out'
                on_release: root.manager.transition = NoTransition(duration=0)
        Button:
                background_color: [0,255,255,0.7]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Fingerprint'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.40}
                size: 450, 100
                on_release: root.manager.current = 'box4outfinger'
                on_release: root.manager.transition = NoTransition(duration=0)
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Chose to unlock '

<Box5outchoseScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Password'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.60}
                size: 450, 100
                on_release: root.manager.current = 'box5out'
                on_release: root.manager.transition = NoTransition(duration=0)
        Button:
                background_color: [0,255,255,0.7]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Fingerprint'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.40}
                size: 450, 100
                on_release: root.manager.current = 'box5outfinger'
                on_release: root.manager.transition = NoTransition(duration=0)
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Chose to unlock '


<Box1outfingerScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'next'
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.30}
                size: 250, 50
                on_state: root.output_pin01(*args)
                on_release: root.manager.current = 'box1pay'
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Box 1 Fingerprint '

<Box2outfingerScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'next'
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.30}
                size: 250, 50
                on_state: root.output_pin01(*args)
                on_release: root.manager.current = 'box2pay'
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Box 2 Fingerprint '

<Box3outfingerScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'next'
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.30}
                size: 250, 50
                on_state: root.output_pin01(*args)
                on_release: root.manager.current = 'box3pay'
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Box 3 Fingerprint '

<Box4outfingerScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'next'
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.30}
                size: 250, 50
                on_state: root.output_pin01(*args)
                on_release: root.manager.current = 'box4pay'
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Box 4 Fingerprint '

<Box5outfingerScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'next'
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.30}
                size: 250, 50
                on_state: root.output_pin01(*args)
                on_release: root.manager.current = 'box5pay'
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Box 5 Fingerprint '


<Box1payScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'next'
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.20}
                size: 250, 70
                on_release: root.manager.current = 'box1outopen'
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Price '
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.60}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 25
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Hours total  '
        BoxLayout
                id: pay1
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.40}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 25
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'pays total  '

<Box2payScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'next'
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.20}
                size: 250, 70
                on_release: root.manager.current = 'box2outopen'
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Price '
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.60}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 25
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Hours total  '
        BoxLayout
                id: pay1
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.40}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 25
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'pays total  '

<Box3payScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'next'
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.20}
                size: 250, 70
                on_release: root.manager.current = 'box3outopen'
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Price '
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.60}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 25
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Hours total  '
        BoxLayout
                id: pay1
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.40}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 25
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'pays total  '

<Box4payScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'next'
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.20}
                size: 250, 70
                on_release: root.manager.current = 'box4outopen'
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Price '
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.60}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 25
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Hours total  '
        BoxLayout
                id: pay1
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.40}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 25
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'pays total  '
<Box5payScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'next'
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.20}
                size: 250, 70
                on_release: root.manager.current = 'box5outopen'
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Price '
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.60}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 25
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Hours total  '
        BoxLayout
                id: pay1
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.40}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 25
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'pays total  '

<Box1outopenScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Finish'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.60}
                size: 450, 100
                on_state: root.output_pin06(*args)
                on_release:
                        root.manager.current = 'menu'
        Button:
                text: 'Open'
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':.50, 'center_y':.40}
                size: 450, 100
                on_state: root.output_pin07(*args)
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Finish '

<Box2outopenScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Finish'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.60}
                size: 450, 100
                on_state: root.output_pin06(*args)
                on_release:
                        root.manager.current = 'menu'
        Button:
                text: 'Open'
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':.50, 'center_y':.40}
                size: 450, 100
                on_state: root.output_pin08(*args)
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Finish '

<Box3outopenScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Finish'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.60}
                size: 450, 100
                on_state: root.output_pin06(*args)
                on_release:
                        root.manager.current = 'menu'
        Button:
                text: 'Open'
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':.50, 'center_y':.40}
                size: 450, 100
                on_state: root.output_pin09(*args)
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Finish '

<Box4outopenScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Finish'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.60}
                size: 450, 100
                on_state: root.output_pin06(*args)
                on_release:
                        root.manager.current = 'menu'
        Button:
                text: 'Open'
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':.50, 'center_y':.40}
                size: 450, 100
                on_state: root.output_pin10(*args)
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Finish '

<Box5outopenScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Finish'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.60}
                size: 450, 100
                on_state: root.output_pin06(*args)
                on_release:
                        root.manager.current = 'menu'    
        Button:
                text: 'Open'
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':.50, 'center_y':.40}
                size: 450, 100
                on_state: root.output_pin11(*args)
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Finish  '


<Box1inopenScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Finish'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.60}
                size: 450, 100
                on_state: root.output_pin06(*args)
                on_release:
                        root.manager.current = 'menu'
        Button:
                text: 'Open'
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':.50, 'center_y':.40}
                size: 450, 100
                on_state: root.output_pin07(*args)
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Finish '

<Box2inopenScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Finish'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.60}
                size: 450, 100
                on_state: root.output_pin06(*args)
                on_release:
                        root.manager.current = 'menu'
        Button:
                text: 'Open'
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':.50, 'center_y':.40}
                size: 450, 100
                on_state: root.output_pin08(*args)
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Finish '

<Box3inopenScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Finish'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.60}
                size: 450, 100
                on_state: root.output_pin06(*args)
                on_release:
                        root.manager.current = 'menu'
        Button:
                text: 'Open'
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':.50, 'center_y':.40}
                size: 450, 100
                on_state: root.output_pin09(*args)
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Finish '

<Box4inopenScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Finish'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.60}
                size: 450, 100
                on_state: root.output_pin06(*args)
                on_release:
                        root.manager.current = 'menu'
        Button:
                text: 'Open'
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':.50, 'center_y':.40}
                size: 450, 100
                on_state: root.output_pin10(*args)
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Finish '

<Box5inopenScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Finish'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.60}
                size: 450, 100
                on_state: root.output_pin06(*args)
                on_release:
                        root.manager.current = 'menu'    
        Button:
                text: 'Open'
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':.50, 'center_y':.40}
                size: 450, 100
                on_state: root.output_pin11(*args)
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Finish  '


<Box1inScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Next'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.30}
                size: 200, 70
                on_press: root.sigups(password.text)
                on_release: root.manager.current = 'box1infinger'
        BoxLayout:
                size_hint: .5,.1
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 20
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Box 1 Enter Password '
        BoxLayout:
                size_hint: .20,.17
                height: 70
                orientation: 'vertical'
                pos_hint: {'center_x':.50, 'center_y':.50}
                Label:
                        text: ''
                        halign: 'left'
                        font_size: 18
                        text_size: root.width-20, 20
                TextInput:
                        id: password
                        multiline:False
                        password:True
                        font_size: 28
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Main Menu'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':0.25, 'center_y':0.30}
                size: 200, 70
                on_release: root.manager.current = 'menu'
<Box2inScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Next'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.30}
                size: 200, 70
                on_press: root.sigups(password.text)
                on_release:
                        root.manager.current = 'box2infinger'
                
        BoxLayout:
                size_hint: .5,.1
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 20
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Box 2 Enter Password '
        BoxLayout:
                size_hint: .20,.17
                height: 70
                orientation: 'vertical'
                pos_hint: {'center_x':.50, 'center_y':.50}
                Label:
                        text: ''
                        halign: 'left'
                        font_size: 18
                        text_size: root.width-20, 20
                TextInput:
                        id: password
                        multiline:False
                        password:True
                        font_size: 28
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Main Menu'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':0.25, 'center_y':0.30}
                size: 200, 70
                on_release: root.manager.current = 'menu'

<Box3inScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Next'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.30}
                size: 200, 70
                on_press: root.sigups(password.text)
                on_release:
                        root.manager.current = 'box3infinger'
                
        BoxLayout:
                size_hint: .5,.1
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 20
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Box 3 Enter Password '
        BoxLayout:
                size_hint: .20,.17
                height: 70
                orientation: 'vertical'
                pos_hint: {'center_x':.50, 'center_y':.50}
                Label:
                        text: ''
                        halign: 'left'
                        font_size: 18
                        text_size: root.width-20, 20
                TextInput:
                        id: password
                        multiline:False
                        password:True
                        font_size: 28
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Main Menu'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':0.25, 'center_y':0.30}
                size: 200, 70
                on_release: root.manager.current = 'menu'

<Box4inScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Next'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.30}
                size: 200, 70
                on_press: root.sigups(password.text)
                on_release:
                        root.manager.current = 'box4infinger'
                
        BoxLayout:
                size_hint: .5,.1
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 20
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Box 4 Enter Password '
        BoxLayout:
                size_hint: .20,.17
                height: 70
                orientation: 'vertical'
                pos_hint: {'center_x':.50, 'center_y':.50}
                Label:
                        text: ''
                        halign: 'left'
                        font_size: 18
                        text_size: root.width-20, 20
                TextInput:
                        id: password
                        multiline:False
                        password:True
                        font_size: 28
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Main Menu'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':0.25, 'center_y':0.30}
                size: 200, 70
                on_release: root.manager.current = 'menu'
<Box5inScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Next'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.30}
                size: 200, 70
                on_press: root.sigups(password.text)
                on_release:
                        root.manager.current = 'box5infinger'
                
        BoxLayout:
                size_hint: .5,.1
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 20
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Box 5 Enter Password '
        BoxLayout:
                size_hint: .20,.17
                height: 70
                orientation: 'vertical'
                pos_hint: {'center_x':.50, 'center_y':.50}
                Label:
                        text: ''
                        halign: 'left'
                        font_size: 18
                        text_size: root.width-20, 20
                TextInput:
                        id: password
                        multiline:False
                        password:True
                        font_size: 28
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Main Menu'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':0.25, 'center_y':0.30}
                size: 200, 70
                on_release: root.manager.current = 'menu'
<Box1infingerScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'next'
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.20}
                size: 250, 100
                on_press: root.enroll(self)
                on_release: root.manager.current = 'box1price'
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Box 1 Fingerprint '

<Box2infingerScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'next'
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.20}
                size: 250, 100
                on_release: root.manager.current = 'box2price'
        BoxLayout:
                size_hint: .6,.2
                
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Box 2 Fingerprint '

<Box3infingerScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'next'
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.20}
                size: 250, 100
                on_release: root.manager.current = 'box3price'
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Box 3 Fingerprint '

<Box4infingerScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'next'
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.20}
                size: 250, 100
                on_release: root.manager.current = 'box4price'
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Box 4 Fingerprint '

<Box5infingerScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'next'
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.20}
                size: 250, 100
                on_release: root.manager.current = 'box5price'
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Box 5 Fingerprint '

<Box1priceScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'next'
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.20}
                size: 250, 70
                on_release: root.manager.current = 'box1inopen'
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Price '
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.50}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Price 1 hour/ 10 Bath'

<Box2priceScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'next'
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.20}
                size: 250, 70
                on_release: root.manager.current = 'box2inopen'
        BoxLayout:
                size_hint: .6,.2
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        text: 'Price '
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.50}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Price 1 hour/ 10 Bath'

<Box3priceScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'next'
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.20}
                size: 250, 70
                on_release: root.manager.current = 'box3inopen'
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Price '
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.50}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Price 1 hour/ 10 Bath'

<Box4priceScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'next'
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.20}
                size: 250, 70
                on_release: root.manager.current = 'box4inopen'
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Price '
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.50}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Price 1 hour/ 10 Bath'

<Box5priceScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'next'
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.20}
                size: 250, 70
                on_release: root.manager.current = 'box5inopen'
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Price '
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.50}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 30
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Price 1 hour/ 10 Bath'
                        
<adminchoseScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Password'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.60}
                size: 450, 100
                on_release: root.manager.current = 'adminin'
                on_release: root.manager.transition = NoTransition(duration=0)
        Button:
                background_color: [0,255,255,0.7]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Fingerprint'
                font_size: 50
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.40}
                size: 450, 100
                on_release: root.manager.current = 'adminfinger'
                on_release: root.manager.transition = NoTransition(duration=0)
        Button:
                text: 'redlight 1'
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                size_hint: None, None
                pos_hint: {'center_x':.10, 'center_y':.10}
                size: 150, 70
                on_state: root.output_pin01(*args)
        Button:
                text: 'redlight 2'
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                size_hint: None, None
                pos_hint: {'center_x':.30, 'center_y':.10}
                size: 150, 70
                on_state: root.output_pin02(*args)
        Button:
                text: 'menu'
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                size_hint: None, None
                pos_hint: {'center_x':.50, 'center_y':.10}
                size: 150, 70
                on_release: root.manager.current = 'menu'
        BoxLayout:
                size_hint: .5,.1
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 20
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'ADMIN Chose to unlock '

<admininScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Next'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.30}
                size: 200, 70
                on_press: root.sigups(password.text)
                        
        BoxLayout:
                size_hint: .5,.1
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 20
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'admin Enter Password '
        BoxLayout:
                size_hint: .20,.17
                height: 70
                orientation: 'vertical'
                pos_hint: {'center_x':.50, 'center_y':.50}
                Label:
                        text: ''
                        halign: 'left'
                        font_size: 18
                        text_size: root.width-20, 20
                TextInput:
                        id: password
                        multiline:False
                        password:True
                        font_size: 28

<adminfingerScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'next'
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.20}
                size: 250, 100
                on_release:
                        root.manager.current = 'unlock'
        BoxLayout:
                size_hint: .6,.2
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 20
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'admin Fingerprint '

<unlockScreen>:
        hue: random()
        canvas.before:
                Rectangle:
                        size: self.size
                        source: "28535128_1998662417064478_597681213_n.jpg"
        Button:
                text: 'BOX 1'
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':.50, 'center_y':0.60}
                size: 150, 100
                on_state: root.output_pin01(*args)
        Button:
                text: 'BOX 2'
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':.70, 'center_y':.60}
                size: 150, 100
                on_state: root.output_pin02(*args)
        Button:
                text: 'BOX 3'
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':.30, 'center_y':.40}
                size: 150, 100
                on_state: root.output_pin03(*args)
        Button:
                text: 'BOX 4'
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':.50, 'center_y':.40}
                size: 150, 100
                on_state: root.output_pin04(*args)
        Button:
                text: 'BOX 5'
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':.70, 'center_y':.40}
                size: 150, 100
                on_state: root.output_pin05(*args)
        Button:
                background_color: [1, 2, 1, 2]
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                text: 'Main Menu'
                font_size: 25
                size_hint: None, None
                pos_hint: {'center_x':0.50, 'center_y':0.20}
                size: 250, 100
                on_release: root.manager.current = 'menu'
        Button:
                text: 'greenlight 1'
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                size_hint: None, None
                pos_hint: {'center_x':.10, 'center_y':.10}
                size: 100, 70
                on_state: root.output_pin06(*args)
        Button:
                text: 'greenlight 2'
                font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                size_hint: None, None
                pos_hint: {'center_x':.25, 'center_y':.10}
                size: 100, 70
                on_state: root.output_pin07(*args)      
        BoxLayout:
                size_hint: .5,.1
                height: 150
                pos_hint: {'center_x':.50, 'center_y':.90}
                orientation: 'vertical'
                TLabel:
                        size_hint_y: 20
                        font_name: '/usr/share/fonts/truetype/lato/Lato-SemiboldItalic.ttf'
                        text: 'Unlock Box '

""")


# Declare both screens
class MenuScreen(Screen):          
    hue = NumericProperty(0)
    pass
class DepositScreen(Screen):
        def output_pin01(self, *args):
                if args[1] == 'down':
                        board.digital[42].write(1)
                        board.digital[23].write(1)
                        board.digital[33].write(0)
                else:
                        board.digital[33].write(1)
                        board.digital[23].write(0)
                        board.digital[42].write(0)
        def output_pin02(self, *args):
                if args[1] == 'down':
                        board.digital[44].write(1)
                        board.digital[25].write(1)
                        board.digital[35].write(0)
                else:
                        board.digital[35].write(1)
                        board.digital[25].write(0)
                        board.digital[44].write(0)
        def output_pin03(self, *args):
                if args[1] == 'down':
                        board.digital[46].write(1)
                        board.digital[27].write(1)
                        board.digital[37].write(0)
                else:
                        board.digital[37].write(1)
                        board.digital[27].write(0)
                        board.digital[46].write(0)
        def output_pin04(self, *args):
                if args[1] == 'down':
                        board.digital[48].write(1)
                        board.digital[29].write(1)
                        board.digital[39].write(0)
                else:
                        board.digital[39].write(1)
                        board.digital[29].write(0)
                        board.digital[48].write(0)
        def output_pin05(self, *args):
                if args[1] == 'down':
                        board.digital[50].write(1)
                        board.digital[31].write(1)
                        board.digital[41].write(0)
                else:
                        board.digital[41].write(1)
                        board.digital[31].write(0)
                        board.digital[50].write(0)
        hue = NumericProperty(0)
        pass
class WithdrawScreen(Screen):
        def output_pin01(self, *args):
                if args[1] == 'down':
                        board.digital[42].write(1)
                        board.digital[23].write(1)
                        board.digital[33].write(0)
                else:
                        board.digital[33].write(1)
                        board.digital[23].write(0)
                        board.digital[42].write(0)
        def output_pin02(self, *args):
                if args[1] == 'down':
                        board.digital[44].write(1)
                        board.digital[25].write(1)
                        board.digital[35].write(0)
                else:
                        board.digital[35].write(1)
                        board.digital[25].write(0)
                        board.digital[44].write(0)
        def output_pin03(self, *args):
                if args[1] == 'down':
                        board.digital[46].write(1)
                        board.digital[27].write(1)
                        board.digital[37].write(0)
                else:
                        board.digital[37].write(1)
                        board.digital[27].write(0)
                        board.digital[46].write(0)
        def output_pin04(self, *args):
                if args[1] == 'down':
                        board.digital[48].write(1)
                        board.digital[29].write(1)
                        board.digital[39].write(0)
                else:
                        board.digital[39].write(1)
                        board.digital[29].write(0)
                        board.digital[48].write(0)
        def output_pin05(self, *args):
                if args[1] == 'down':
                        board.digital[50].write(1)
                        board.digital[31].write(1)
                        board.digital[41].write(0)
                else:
                        board.digital[41].write(1)
                        board.digital[31].write(0)
                        board.digital[50].write(0)
        hue = NumericProperty(0)
        pass
class Box1outScreen(Screen):
        def signups(self, passwordText):
                c.execute('SELECT * from COMPANY WHERE password ="%s"'%(passwordText))
                if c.fetchone() is not None:
                    self.manager.current = 'box1pay'
                    conn.execute("DELETE from COMPANY where ID = 1;")
                    conn.commit()
                else:
                    print "Password failed"
        def output_pin01(self, *args):
                if args[1] == 'down':
                        board.digital[10].write(0)
                else:
                        board.digital[10].write(1)
        def resetForm(self):
                self.ids['password'].text = ""
        hue = NumericProperty(0)
        pass

class Box2outScreen(Screen):
        def signups(self, passwordText):
                c.execute('SELECT * from COMPANY WHERE password ="%s"'%(passwordText))
                if c.fetchone() is not None:
                    self.manager.current = 'box2pay'
                    conn.execute("DELETE from COMPANY where ID = 2;")
                    conn.commit()
                else:
                    print "Password failed"
        def output_pin01(self, *args):
                if args[1] == 'down':
                        board.digital[10].write(0)
                else:
                        board.digital[10].write(1)
        def resetForm(self):
                self.ids['password'].text = ""
        hue = NumericProperty(0)
        pass

class Box3outScreen(Screen):
        def signups(self, passwordText):
                c.execute('SELECT * from COMPANY WHERE password ="%s"'%(passwordText))
                if c.fetchone() is not None:
                    self.manager.current = 'box3pay'
                    conn.execute("DELETE from COMPANY where ID = 3;")
                    conn.commit()
                else:
                    print "Password failed"
        def output_pin01(self, *args):
                if args[1] == 'down':
                        board.digital[10].write(0)
                else:
                        board.digital[10].write(1)
        def resetForm(self):
                self.ids['password'].text = ""
        hue = NumericProperty(0)
        pass

class Box4outScreen(Screen):
        def signups(self, passwordText):
                c.execute('SELECT * from COMPANY WHERE password ="%s"'%(passwordText))
                if c.fetchone() is not None:
                    self.manager.current = 'box4pay'
                    conn.execute("DELETE from COMPANY where ID = 4;")
                    conn.commit()
                else:
                    print "Password failed"
        def output_pin01(self, *args):
                if args[1] == 'down':
                        board.digital[10].write(0)
                else:
                        board.digital[10].write(1)
        def resetForm(self):
                self.ids['password'].text = ""
        hue = NumericProperty(0)
        pass

class Box5outScreen(Screen):
        def signups(self, passwordText):
                c.execute('SELECT * from COMPANY WHERE password ="%s"'%(passwordText))
                if c.fetchone() is not None:
                    self.manager.current = 'box5pay'
                    conn.execute("DELETE from COMPANY where ID = 5;")
                    conn.commit()
                else:
                    print "Password failed"
        def output_pin01(self, *args):
                if args[1] == 'down':
                        board.digital[10].write(0)
                else:
                        board.digital[10].write(1)
        def resetForm(self):
                self.ids['password'].text = ""
        hue = NumericProperty(0)
        pass
class Box1outchoseScreen(Screen):

        hue = NumericProperty(0)
        pass

class Box2outchoseScreen(Screen):
        hue = NumericProperty(0)
        pass

class Box3outchoseScreen(Screen):
        hue = NumericProperty(0)
        pass

class Box4outchoseScreen(Screen):
        hue = NumericProperty(0)
        pass

class Box5outchoseScreen(Screen):
        hue = NumericProperty(0)
        pass

class Box1outfingerScreen(Screen):
        def output_pin01(self, *args):
                if args[1] == 'down':
                        board.digital[10].write(0)
                else:
                        board.digital[10].write(1)
        hue = NumericProperty(0)
        pass

class Box2outfingerScreen(Screen):
        def output_pin01(self, *args):
                if args[1] == 'down':
                        board.digital[10].write(0)
                else:
                        board.digital[10].write(1)
        hue = NumericProperty(0)
        pass

class Box3outfingerScreen(Screen):
        def output_pin01(self, *args):
                if args[1] == 'down':
                        board.digital[10].write(0)
                else:
                        board.digital[10].write(1)
        hue = NumericProperty(0)
        pass

class Box4outfingerScreen(Screen):
        def output_pin01(self, *args):
                if args[1] == 'down':
                        board.digital[10].write(0)
                else:
                        board.digital[10].write(1)
        hue = NumericProperty(0)
        pass

class Box5outfingerScreen(Screen):
        def output_pin01(self, *args):
                if args[1] == 'down':
                        board.digital[10].write(0)
                else:
                        board.digital[10].write(1)
        hue = NumericProperty(0)
        pass

class Box1payScreen(Screen):
        
        hue = NumericProperty(0)
        pass
class Box2payScreen(Screen):
        
        hue = NumericProperty(0)
        pass
class Box3payScreen(Screen):
        
        hue = NumericProperty(0)
        pass

class Box4payScreen(Screen):
        
        hue = NumericProperty(0)
        pass
class Box5payScreen(Screen):
        
        hue = NumericProperty(0)
        pass
class Box1inopenScreen(Screen):
        def output_pin06(self, *args):
                if args[1] == 'down':
                        board.digital[42].write(0)
                        board.digital[23].write(1)
                        board.digital[33].write(1)
                else:
                        board.digital[42].write(1)
                        board.digital[23].write(0)
                        board.digital[33].write(0)
        def output_pin07(self, *args):
                if args[1] == 'down':
                        board.digital[3].write(1)
                        board.digital[22].write(1)
                        board.digital[32].write(0)
                        time.sleep(10)
                else:
                        board.digital[3].write(0)
                        board.digital[22].write(0)
                        board.digital[32].write(1)

        hue = NumericProperty(0)
        pass

class Box2inopenScreen(Screen):
        def output_pin06(self, *args):
                if args[1] == 'down':
                        board.digital[44].write(0)
                        board.digital[25].write(1)
                        board.digital[35].write(1)
                else:
                        board.digital[44].write(1)
                        board.digital[25].write(0)
                        board.digital[35].write(0)
        def output_pin08(self, *args):
                if args[1] == 'down':
                        board.digital[4].write(1)
                        board.digital[24].write(1)
                        board.digital[34].write(0)
                        time.sleep(10)
                else:
                        board.digital[4].write(0)
                        board.digital[24].write(0)
                        board.digital[34].write(1)
        hue = NumericProperty(0)
        pass

class Box3inopenScreen(Screen):
        def output_pin06(self, *args):
                if args[1] == 'down':
                        board.digital[46].write(0)
                        board.digital[27].write(1)
                        board.digital[37].write(1)
                else:
                        board.digital[46].write(1)
                        board.digital[27].write(0)
                        board.digital[37].write(0)
        def output_pin09(self, *args):
                if args[1] == 'down':
                        board.digital[7].write(1)
                        board.digital[26].write(1)
                        board.digital[36].write(0)
                        time.sleep(10)
                else:
                        board.digital[7].write(0)
                        board.digital[26].write(0)
                        board.digital[36].write(1)
        hue = NumericProperty(0)
        pass

class Box4inopenScreen(Screen):
        def output_pin06(self, *args):
                if args[1] == 'down':
                        board.digital[48].write(0)
                        board.digital[29].write(1)
                        board.digital[39].write(1)
                else:
                        board.digital[48].write(1)
                        board.digital[29].write(0)
                        board.digital[39].write(0)
        def output_pin10(self, *args):
                if args[1] == 'down':
                        board.digital[6].write(1)
                        board.digital[28].write(1)
                        board.digital[38].write(0)
                        time.sleep(10)
                else:
                        board.digital[6].write(0)
                        board.digital[28].write(0)
                        board.digital[38].write(1)
        hue = NumericProperty(0)
        pass

class Box5inopenScreen(Screen):
        def output_pin06(self, *args):
                if args[1] == 'down':
                        board.digital[50].write(0)
                        board.digital[31].write(1)
                        board.digital[41].write(1)
                else:
                        board.digital[50].write(1)
                        board.digital[31].write(0)
                        board.digital[41].write(0)
        def output_pin11(self, *args):
                if args[1] == 'down':
                        board.digital[5].write(1)
                        board.digital[30].write(1)
                        board.digital[40].write(0)
                        time.sleep(10)
                else:
                        board.digital[5].write(0)
                        board.digital[30].write(0)
                        board.digital[40].write(1)
        hue = NumericProperty(0)
        pass
class Box1outopenScreen(Screen):
        def output_pin06(self, *args):
                if args[1] == 'down':
                        board.digital[42].write(1)
                        board.digital[33].write(1)
                        board.digital[23].write(0)
                        board.digital[10].write(1)
                else:
                        board.digital[42].write(0)
                        board.digital[33].write(0)
                        board.digital[23].write(1)
                        board.digital[10].write(0)
        def output_pin07(self, *args):
                if args[1] == 'down':
                        board.digital[3].write(1)
                        board.digital[22].write(1)
                        board.digital[32].write(0)
                        time.sleep(10)
                else:
                        board.digital[3].write(0)
                        board.digital[22].write(0)
                        board.digital[32].write(1)

        hue = NumericProperty(0)
        pass

class Box2outopenScreen(Screen):
        def output_pin06(self, *args):
                if args[1] == 'down':
                        board.digital[44].write(1)
                        board.digital[35].write(1)
                        board.digital[25].write(0)
                        board.digital[10].write(1)
                else:
                        board.digital[44].write(0)
                        board.digital[35].write(0)
                        board.digital[25].write(1)
                        board.digital[10].write(0)
        def output_pin08(self, *args):
                if args[1] == 'down':
                        board.digital[4].write(1)
                        board.digital[24].write(1)
                        board.digital[34].write(0)
                        time.sleep(10)
                else:
                        board.digital[4].write(0)
                        board.digital[24].write(0)
                        board.digital[34].write(1)
        hue = NumericProperty(0)
        pass

class Box3outopenScreen(Screen):
        def output_pin06(self, *args):
                if args[1] == 'down':
                        board.digital[46].write(1)
                        board.digital[37].write(1)
                        board.digital[27].write(0)
                        board.digital[10].write(1)
                else:
                        board.digital[46].write(0)
                        board.digital[37].write(0)
                        board.digital[27].write(1)
                        board.digital[10].write(0)
        def output_pin09(self, *args):
                if args[1] == 'down':
                        board.digital[7].write(1)
                        board.digital[26].write(1)
                        board.digital[36].write(0)
                        time.sleep(10)
                else:
                        board.digital[7].write(0)
                        board.digital[26].write(0)
                        board.digital[36].write(1)
        hue = NumericProperty(0)
        pass

class Box4outopenScreen(Screen):
        def output_pin06(self, *args):
                if args[1] == 'down':
                        board.digital[48].write(1)
                        board.digital[39].write(1)
                        board.digital[29].write(0)
                        board.digital[10].write(1)
                else:
                        board.digital[48].write(0)
                        board.digital[39].write(0)
                        board.digital[29].write(1)
                        board.digital[10].write(0)
        def output_pin10(self, *args):
                if args[1] == 'down':
                        board.digital[6].write(1)
                        board.digital[28].write(1)
                        board.digital[38].write(0)
                        time.sleep(10)
                else:
                        board.digital[6].write(0)
                        board.digital[28].write(0)
                        board.digital[38].write(1)
        hue = NumericProperty(0)
        pass

class Box5outopenScreen(Screen):
        def output_pin06(self, *args):
                if args[1] == 'down':
                        board.digital[50].write(1)
                        board.digital[41].write(1)
                        board.digital[31].write(0)
                        board.digital[10].write(1)
                else:
                        board.digital[50].write(0)
                        board.digital[41].write(0)
                        board.digital[31].write(1)
                        board.digital[10].write(0)
        def output_pin11(self, *args):
                if args[1] == 'down':
                        board.digital[5].write(1)
                        board.digital[30].write(1)
                        board.digital[40].write(0)
                        time.sleep(10)
                else:
                        board.digital[5].write(0)
                        board.digital[30].write(0)
                        board.digital[40].write(1)
        hue = NumericProperty(0)
        pass
class Box1inScreen(Screen):
        def sigups(self, passwordText):
                
                conn.execute("INSERT INTO COMPANY VALUES (?,?)",(ID,passwordText));
                conn.commit()
                
        hue = NumericProperty(0)
        pass
class Box2inScreen(Screen):
        def sigups(self, passwordText):
                
                conn.execute("INSERT INTO COMPANY VALUES (?,?)",(ID2,passwordText));
                conn.commit()
                
        hue = NumericProperty(0)
        pass

class Box3inScreen(Screen):
        def sigups(self, passwordText):
                
                conn.execute("INSERT INTO COMPANY VALUES (?,?)",(ID3,passwordText));
                conn.commit()
                
        hue = NumericProperty(0)
        pass

class Box4inScreen(Screen):
        def sigups(self, passwordText):
                
                conn.execute("INSERT INTO COMPANY VALUES (?,?)",(ID4,passwordText));
                conn.commit()
                
        hue = NumericProperty(0)
        pass

class Box5inScreen(Screen):
        def sigups(self, passwordText):
                
                conn.execute("INSERT INTO COMPANY VALUES (?,?)",(ID5,passwordText));
                conn.commit()
                
        hue = NumericProperty(0)
        pass

class Box1inchoseScreen(Screen):
        hue = NumericProperty(0)
        pass

class Box2inchoseScreen(Screen):
        hue = NumericProperty(0)
        pass

class Box3inchoseScreen(Screen):
        hue = NumericProperty(0)
        pass

class Box4inchoseScreen(Screen):
        hue = NumericProperty(0)
        pass

class Box5inchoseScreen(Screen):
        hue = NumericProperty(0)
        pass


class Box1infingerScreen(Screen):

        hue = NumericProperty(0)
        pass

class Box2infingerScreen(Screen):
        hue = NumericProperty(0)
        pass

class Box3infingerScreen(Screen):
        hue = NumericProperty(0)
        pass

class Box4infingerScreen(Screen):
        hue = NumericProperty(0)
        pass

class Box5infingerScreen(Screen):
        hue = NumericProperty(0)
        pass

class Box1priceScreen(Screen):
        hue = NumericProperty(0)
        pass

class Box2priceScreen(Screen):
        hue = NumericProperty(0)
        pass

class Box3priceScreen(Screen):
        hue = NumericProperty(0)
        pass

class Box4priceScreen(Screen):
        hue = NumericProperty(0)
        pass
class Box5priceScreen(Screen):
        hue = NumericProperty(0)
        pass
class adminchoseScreen(Screen):
        def output_pin01(self, *args):
                if args[1] == 'down':
                        board.digital[32].write(0)
                        board.digital[34].write(0)
                        board.digital[36].write(0)
                else:
                        board.digital[32].write(1)
                        board.digital[34].write(1)
                        board.digital[36].write(1)
        def output_pin02(self, *args):
                if args[1] == 'down':
                        board.digital[38].write(0)
                        board.digital[40].write(0)
                else:
                        board.digital[38].write(1)
                        board.digital[40].write(1)      
        hue = NumericProperty(0)
        pass

class admininScreen(Screen):
        def sigups(self, passwordText):
                c.execute('SELECT * from COMPANY WHERE password ="%s"'%(passwordText))
                if c.fetchone() is not None:
                    self.manager.current = 'unlock'
                else:
                    print "Password failed"
        hue = NumericProperty(0)
        pass

class adminfingerScreen(Screen):
        hue = NumericProperty(0)
        pass

class unlockScreen(Screen):
        def output_pin01(self, *args):
                if args[1] == 'down':
                        board.digital[3].write(1)
                        time.sleep(10)
                else:
                        board.digital[3].write(0)
        def output_pin02(self, *args):
                if args[1] == 'down':
                        board.digital[4].write(1)
                        time.sleep(10)
                else:
                        board.digital[4].write(0)
        def output_pin03(self, *args):
                if args[1] == 'down':
                        board.digital[7].write(1)
                        time.sleep(10)
                else:
                        board.digital[7].write(0)
        def output_pin04(self, *args):
                if args[1] == 'down':
                        board.digital[6].write(1)
                        time.sleep(10)
                else:
                        board.digital[6].write(0)
        def output_pin05(self, *args):
                if args[1] == 'down':
                        board.digital[5].write(1)
                        time.sleep(10) 
                else:
                        board.digital[5].write(0)
        def output_pin06(self, *args):
                if args[1] == 'down':
                        board.digital[23].write(0)
                        board.digital[25].write(0)
                        board.digital[27].write(0)
                else:
                        board.digital[23].write(1)
                        board.digital[25].write(1)
                        board.digital[27].write(1)
        def output_pin07(self, *args):
                if args[1] == 'down':
                        board.digital[29].write(0)
                        board.digital[31].write(0)
                else:
                        board.digital[29].write(1)
                        board.digital[31].write(1)  
        hue = NumericProperty(0)
        pass
#SM
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(DepositScreen(name='deposit'))
sm.add_widget(WithdrawScreen(name='Withdraw'))
sm.add_widget(Box1outScreen(name='box1out'))
sm.add_widget(Box2outScreen(name='box2out'))
sm.add_widget(Box3outScreen(name='box3out'))
sm.add_widget(Box4outScreen(name='box4out'))
sm.add_widget(Box5outScreen(name='box5out'))
sm.add_widget(Box1outchoseScreen(name='box1outchose'))
sm.add_widget(Box2outchoseScreen(name='box2outchose'))
sm.add_widget(Box3outchoseScreen(name='box3outchose'))
sm.add_widget(Box4outchoseScreen(name='box4outchose'))
sm.add_widget(Box5outchoseScreen(name='box5outchose'))
sm.add_widget(Box1outfingerScreen(name='box1outfinger'))
sm.add_widget(Box2outfingerScreen(name='box2outfinger'))
sm.add_widget(Box3outfingerScreen(name='box3outfinger'))
sm.add_widget(Box4outfingerScreen(name='box4outfinger'))
sm.add_widget(Box5outfingerScreen(name='box5outfinger'))
sm.add_widget(Box1payScreen(name='box1pay'))
sm.add_widget(Box2payScreen(name='box2pay'))
sm.add_widget(Box3payScreen(name='box3pay'))
sm.add_widget(Box4payScreen(name='box4pay'))
sm.add_widget(Box5payScreen(name='box5pay'))
sm.add_widget(Box1inopenScreen(name='box1inopen'))
sm.add_widget(Box2inopenScreen(name='box2inopen'))
sm.add_widget(Box3inopenScreen(name='box3inopen'))
sm.add_widget(Box4inopenScreen(name='box4inopen'))
sm.add_widget(Box5inopenScreen(name='box5inopen'))
sm.add_widget(Box1outopenScreen(name='box1outopen'))
sm.add_widget(Box2outopenScreen(name='box2outopen'))
sm.add_widget(Box3outopenScreen(name='box3outopen'))
sm.add_widget(Box4outopenScreen(name='box4outopen'))
sm.add_widget(Box5outopenScreen(name='box5outopen'))
sm.add_widget(Box1inScreen(name='box1in'))
sm.add_widget(Box2inScreen(name='box2in'))
sm.add_widget(Box3inScreen(name='box3in'))
sm.add_widget(Box4inScreen(name='box4in'))
sm.add_widget(Box5inScreen(name='box5in'))
sm.add_widget(Box1inchoseScreen(name='box1inchose'))
sm.add_widget(Box2inchoseScreen(name='box2inchose'))
sm.add_widget(Box3inchoseScreen(name='box3inchose'))
sm.add_widget(Box4inchoseScreen(name='box4inchose'))
sm.add_widget(Box5inchoseScreen(name='box5inchose'))
sm.add_widget(Box1infingerScreen(name='box1infinger'))
sm.add_widget(Box2infingerScreen(name='box2infinger'))
sm.add_widget(Box3infingerScreen(name='box3infinger'))
sm.add_widget(Box4infingerScreen(name='box4infinger'))
sm.add_widget(Box5infingerScreen(name='box5infinger'))
sm.add_widget(Box1priceScreen(name='box1price'))
sm.add_widget(Box2priceScreen(name='box2price'))
sm.add_widget(Box3priceScreen(name='box3price'))
sm.add_widget(Box4priceScreen(name='box4price'))
sm.add_widget(Box5priceScreen(name='box5price'))
sm.add_widget(adminchoseScreen(name='adminchose'))
sm.add_widget(admininScreen(name='adminin'))
sm.add_widget(adminfingerScreen(name='adminfinger'))
sm.add_widget(unlockScreen(name='unlock'))
class Variables():
        pwm = 0
var = Variables()
class TestApp(App):
        def build(self):
                Clock.schedule_interval(self.root.update, 0)
        def on_stop(self):
                board.exit()
        def build(self):
                return sm

if __name__ == '__main__':
        TestApp().run()
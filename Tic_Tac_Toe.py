from kivy.app import App
from kivy.core import text
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.uix.popup import Popup
import random



class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)

class Add_player(Screen):
	def __init__(self, **kwargs):
		super(Add_player, self).__init__(**kwargs)
		self.lay_out=BoxLayout(orientation='horizontal')
		self.add_widget(self.lay_out)
		self.add_widget(Label(text='Player Name of O', size_hint=(.45, .1), pos_hint={'x': .05, 'y': .7}))
		self.player1 = TextInput(multiline=False, size_hint=(.45, .1), pos_hint={'x': .5, 'y': .7})
		self.add_widget(self.player1)
		self.add_widget(Label(text='Player Name of X', size_hint=(.45, .1), pos_hint={'x': .05, 'y': .5}))
		self.player2 = TextInput(multiline=False, size_hint=(.45, .1), pos_hint={'x': .5, 'y': .5})
		self.add_widget(self.player2)
		self.send_warnings=Label(text='', size_hint=(.75, .1), pos_hint={'x': .05, 'y': .3})
		self.add_widget(self.send_warnings)
		self.btn = Button(text='Play', size_hint=(.45, .2), pos_hint={'center_x': .5, 'y': .02})
		self.lay_out.add_widget(self.btn)
		self.btn.bind(on_press=self.screen_trasition)
		
	def restart(self,  *args):
		self.manager.transition.unbind(on_complete=self.restart)

	def screen_trasition(self,*args):
		# print(self.player1.text)
		if self.player1.text=='' or self.player2.text=='':
			# print("Both are empty")
			self.send_warnings.text='Please enter both player names.'
		else:
			# self.manager.transition.bind(on_complete=self.restart)
			self.manager.current='Board'
			
			


class Play_Board(Screen):
	def __init__(self, **kwargs):
		super(Play_Board, self).__init__(**kwargs)
		self.pl1=''
		self.pl2=''
		self.plr_1='O'
		self.plr_2='X'
		self.turn=''
		self.First=False
		self.def_init=''
		self.layout_draw=GridLayout(cols=3)
		self.add_widget(self.layout_draw)
		self.btn_n = Button(text="Continue")
		self.btn_n.bind(on_press=self.get_text)
		self.layout_draw.add_widget(self.btn_n)
		
	def create_layout_button(self):
		self.btn_0 = Button(text="")
		self.btn_0.bind(on_press=self.print_text)
		self.layout_draw.add_widget(self.btn_0)
		self.btn_1 = Button(text="")
		self.btn_1.bind(on_press=self.print_text)
		self.layout_draw.add_widget(self.btn_1)
		self.btn_2 = Button(text="")
		self.btn_2.bind(on_press=self.print_text)
		self.layout_draw.add_widget(self.btn_2)
		self.btn_3 = Button(text="")
		self.btn_3.bind(on_press=self.print_text)
		self.layout_draw.add_widget(self.btn_3)
		self.btn_4 = Button(text="")
		self.btn_4.bind(on_press=self.print_text)
		self.layout_draw.add_widget(self.btn_4)
		self.btn_5 = Button(text="")
		self.btn_5.bind(on_press=self.print_text)
		self.layout_draw.add_widget(self.btn_5)
		self.btn_6 = Button(text="")
		self.btn_6.bind(on_press=self.print_text)
		self.layout_draw.add_widget(self.btn_6)
		self.btn_7 = Button(text="")
		self.btn_7.bind(on_press=self.print_text)
		self.layout_draw.add_widget(self.btn_7)
		self.btn_8 = Button(text="")
		self.btn_8.bind(on_press=self.print_text)
		self.layout_draw.add_widget(self.btn_8)
		self.check_turn()
	
	def get_text(self, *args):
		if self.pl1=='' and self.pl2=='':
			self.manager.current='Players'
			self.pl1=self.manager.current_screen.player1.text
			self.pl2=self.manager.current_screen.player2.text
			print(self.pl1)
			print(self.pl2)
			self.manager.current='Board'
			print('player1 is ',self.pl1 , 'and player 2 is ', self.pl2)
			self.create_layout_button()
			self.layout_draw.remove_widget(self.btn_n)


	def check_win(self):
		def declare_win(sign):
			def dis(dt):
				popup.dismiss()
				# self.manager.current='Players'
				self.restart()
			if sign==self.plr_1:
				win_plr=self.pl1
				bg=[0,1,0,1]
			else:
				win_plr=self.pl2
				bg=[0,0,1,1]
			ly=GridLayout(cols=1,padding=10)
			ly.add_widget(Label(text=f'Winner of Game is {win_plr}'))
			closeButton = Button(text = "Replay")
			ly.add_widget(closeButton)
			popup = Popup(title='Winner',content=ly,background_color=bg,size_hint=(None, None), size=(400, 400))
			popup.open()
			closeButton.bind(on_press=dis)
			# Clock.schedule_once(dis,2)
				

		def declare_draw():
			def dis(dt):
				popup.dismiss()
				# self.manager.current='Players'
				self.restart()
			# def req_restart():
			# 	Clock.schedule_once(dis,2)
			ly=GridLayout(cols=1,padding=10)
			ly.add_widget(Label(text=f'Draw between {self.pl1} and {self.pl1}.\nGame will restart in 2 seconds'))
			closeButton = Button(text = "Replay")
			ly.add_widget(closeButton)
			popup = Popup(title='Draw',content=ly,background_color=[1,1,1,1],size_hint=(None, None), size=(400, 400))
			popup.open()
			closeButton.bind(on_press=dis)
		if self.btn_0.text==self.btn_1.text==self.btn_2.text!='':
			declare_win(self.btn_0.text)
		elif self.btn_3.text==self.btn_4.text==self.btn_5.text!='':
			declare_win(self.btn_3.text)
		elif self.btn_6.text==self.btn_7.text==self.btn_8.text!='':
			declare_win(self.btn_6.text)
		elif self.btn_0.text==self.btn_3.text==self.btn_6.text!='':
			declare_win(self.btn_0.text)
		elif self.btn_1.text==self.btn_4.text==self.btn_7.text!='':
			declare_win(self.btn_1.text)
		elif self.btn_2.text==self.btn_5.text==self.btn_8.text!='':
			declare_win(self.btn_2.text)
		elif self.btn_0.text==self.btn_4.text==self.btn_8.text!='':
			declare_win(self.btn_0.text)
		elif self.btn_2.text==self.btn_4.text==self.btn_6.text!='':
			declare_win(self.btn_2.text)
		elif self.btn_0.text!='' and self.btn_1.text!='' and self.btn_2.text!='' and self.btn_3.text!='' and self.btn_4.text!='' and self.btn_5.text!='' and self.btn_6.text!='' and self.btn_7.text!='' and self.btn_8.text!='':
			declare_draw()
		else:
			pass	


	def restart(self):
		lst=[self.btn_0,self.btn_1,self.btn_2,self.btn_3,self.btn_4,self.btn_5,self.btn_6,self.btn_7,self.btn_8]
		for x in lst:
			self.layout_draw.remove_widget(x)
		self.create_layout_button()
		self.First=False
		self.turn=''
		self.check_turn()
		

	def check_turn(self):
		if self.turn==self.plr_1:
			self.turn=self.plr_2
		elif self.turn==self.plr_2:
			self.turn=self.plr_1
		else:
			lst=[self.plr_1,self.plr_2]
			lst_nm=[self.pl1,self.pl2]
			lst_clr=[[0,1,0,1],[0,0,1,1]]
			self.turn=random.choice(lst)
			ind=lst.index(self.turn)
			def dis(dt):
				popup.dismiss()
			popup = Popup(title='First Chance of ',content=Label(text=f'First User is {lst_nm[ind]}'),background_color=lst_clr[ind],size_hint=(None, None), size=(400, 400))
			popup.open()
			Clock.schedule_once(dis,2)
		return self.turn


	def print_text(self,button):
		if self.First:
			usr=self.check_turn()
		else:
			usr=self.turn
			self.First=True
		# self.chk_btn(instance, value)
		print(button.text)
		if button.text=='':
			if usr=='O':
				button.text=usr
				button.background_color=[0,1,0,1]
			else:
				button.text=usr
				button.background_color=[0,0,1,1]
		else:
			def dis(dt):
				popup.dismiss()
			# popup = Popup(title='Test popup', content=Label(text='Hello world'),size=(200, 400),auto_dismiss=True)
			popup = Popup(title='Warning',background_color=[1,0,0,1],content=Label(text='User has filled this box'),size_hint=(None, None), size=(400, 400))
			popup.open()
			Clock.schedule_once(dis,2)
		self.check_win()


	def chk_btn(instance, value):
		print(value.text)

        # alternative:

		
class TestApp(App):
	def build(self):
		sm=ScreenManager(transition=FadeTransition())
		sm.add_widget(Add_player(name='Players'))
		sm.add_widget(Play_Board(name='Board'))
		return sm

if __name__ == "__main__":
	TestApp().run()
# python script showing battery details
import psutil
import time
import pyautogui as pya
import subprocess
def Main_class():
	# function returning time in hh:mm:ss
	def convertTime(seconds):
		minutes, seconds = divmod(seconds, 60)
		hours, minutes = divmod(minutes, 60)
		return "%d:%02d:%02d" % (hours, minutes, seconds)

	# returns a tuple
	battery = psutil.sensors_battery()

	print("Battery percentage : ", battery.percent)
	print("Power plugged in : ", battery.power_plugged)


	# converting seconds to hh:mm:ss
	print("Battery left : ", convertTime(battery.secsleft))
	print(type(battery.percent))

	return [battery.percent,battery.power_plugged]

while 1==1:
	time.sleep(2)
	battery=Main_class()[0]
	in_charge=Main_class()[1]
	print(f'{battery}=={in_charge}')
	if battery==100:
		if in_charge==True:
			pya.alert('Baterry is full please unplug charger else it will lock in 5 seconds.','Lock Notification',timeout=5000)
			chk_in_charge=Main_class()[1]
			if chk_in_charge==True:
				subprocess.call('rundll32.exe user32.dll,LockWorkStation',shell=True)
	else:
		if battery<20:
			if in_charge==False:
				pya.alert('Baterry low please plug charger else it will lock in 5 seconds.',timeout=5000)
				if Main_class()[1]==False:
					subprocess.call('rundll32.exe user32.dll,LockWorkStation',shell=True)
		else:
			print('It will sustain')
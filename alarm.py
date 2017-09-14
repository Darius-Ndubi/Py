
#modules to use
import time
import playsound

#creating a function that will produce a beeb sound as alarm tone
#the tone though depends on your linux terminal notifiction sound
def beep():
	print "\a"

#function that will continuously update time
def time_update():
	i=0
	while i<10:
		global curre_time
		curre_time=time.ctime()
		i+=1
	print "Current time is :",curre_time

#function to set rhe time when you want the alarm to ring
def set_ringz():
	print "Enter the time you want alarm to ring"
	print "Enter it in this format yyyy,mon,day,hh,mm,ss,ms,ukn_default-21,ukn_default-0"
	print "Example.....   2017,9,13,21,47,00,0,21,0"
	time_update()
	global expected_time,total_sec
	expected_time=input("Enter your ring time: ")
	ringz_at=time.asctime(expected_time)
	print "Alarm is expected at: ",ringz_at
	#now compare the time entered to time of sysyem
	#find the diffrence in time and allow the prigram to wait rill that time to ring
	diff_hours=int(curre_time[11:13])-int(ringz_at[11:13])
	diff_minus=int(curre_time[14:16])-int(ringz_at[14:16])
	diff_secos=int(curre_time[17:19])-int(ringz_at[17:19])
	total_sec=(diff_hours*3600)+(diff_minus*60)+diff_secos
	print total_sec
	#return total_sec


#function to workout the alarm ring time
def ring():
	print "Do you want alarm to ring after x seconds or at specific time"
	print "To ring after some time press 'x'"
	print "To ring at specific time press 's'"
	choice=raw_input("Enter your choice: ").lower()
	if choice=='x':
		print "Enter the duration before the alarm rings in seconds"
		wait=input("Enter time: ")
		ringz=time.time()+wait
		print "Alarm expected at: ",time.ctime(ringz)
		time_update()
		while curre_time<>ringz:
			time.sleep(wait)
			break
	#ring severally
		print "RINGING !!!!!"
		i=5
		while i>0:
			beep()
			i-=1
	#Playing sound out as alarm
		playsound.playsound('/home/dario/Music/02 - Dial Tone.mp3')

	elif choice=='s':
		set_ringz()
		time_update()
		while expected_time<>curre_time:
			time.sleep(abs(total_sec))
			break
	#ring Severally
		print "RINGING !!!!"
		j=5
		while j>0:
			beep()
			j=-1
	#Playing sound out as alarm
		playsound.playsound('/home/dario/Music/02 - Dial Tone.mp3')

ring()

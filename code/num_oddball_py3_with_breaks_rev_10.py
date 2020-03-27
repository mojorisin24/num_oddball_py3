"""
Oddball Number Task 
LEFT button press = odd
RIGHT button press = even
In this case, odds will be frequent and evens will be rare. 
Please use the adjacent script num_oddball_py3_even if you'd like evens to be frequent and odds to be rare 
* Note to experimenters you will have to change the path (line **) to point at the directory where the task has been placed specifically the sequence folder. 
Questions? Feel free to reach out: cdcarrasco@ucdavis.edu, amsimmons@ucdavis.edu  
Huge Thank you to dsmiller@ucdavis.edu and amsimmons@ucdavis.edu for helping with creation of the paradigm. 
"""
from psychopy import visual, core, event, gui, parallel
from pathlib import Path
import os, random, time, csv
from datetime import datetime

#Flag for block counterbalance set to 0 to run odds then even blocks, set to 1 to run even then odds block sequence 
#block_counterbalance = 1
full_or_test = 1 # make this 1 to run entire experiment, 0 if you are just trying to debug and make changes to code. 
#Naming CSV for Participant Sequence. // this isn't the right seq title, doesn't really mean the participant 
#actually viewd only "rare even freq odd seq". 
participant_seq = 'rare_even_freq_odd_seq.csv'
#setting path to save CSV to      
#path = Path('\\Users\\Carlos\\Documents\\oddball_task\\num_oddball_py3\\seq\\') #here you will 
#need to set the path to wherever you have saved the experiment folder, make sure to point this directory to  the seq folder. 
path = Path('/home/carlosc/Desktop/num_oddball_py3/seq/')
#path = Path('/home/amsimmon/Desktop/num_oddball_py3/seq')
#setting fpath with name of csv 
fpath = (path / participant_seq).with_suffix('.csv')
#Specifying Number of Trials do not change 
if full_or_test == 1:
    tot_trials = 2048
else:
    tot_trials = 128

num_breaks = 8
split_trials = int(tot_trials/num_breaks)
#setting up rare and freq lists
freq = num_breaks * 0.875
rare = num_breaks * 0.125

# initializing event codes - Aaron
ERP = 'N'

if ERP =='Y':
    port = parallel.ParallelPort(address='/dev/parport0')
    
    def sendTrigger(trigger):
        port.setData(int(trigger))
        core.wait(0.005)
        port.setData(0)
        
        
#get the counterbalance information! 
cb_info={"CounterBalance (1 evens rare first, 2 odds rare first):": ''}

cb_dlg = gui.DlgFromDict(dictionary=cb_info, title="Which CB")

if cb_info["CounterBalance (1 evens rare first, 2 odds rare first):"] == '1':
    block_counterbalance = 1
else:
    block_counterbalance = 2 
    
        
#House keeping
freq = int(freq)
rare = int(rare)
#Generating odds and even lists. In this case odds are freq and evens are rare 
#Evens rare and odds freq 
evens_r = [2,4,6,8]* rare * num_breaks
evens_r = list(zip(evens_r,(['r']*len(evens_r))))

odds_r = [1,3,5,7] * rare * num_breaks
odds_r = list(zip(odds_r,(['r']*len(odds_r))))

evens_f = [2,4,6,8] * freq * num_breaks
evens_f = list(zip(evens_f,(['f']*len(evens_f))))

odds_f = [1,3,5,7] * freq * num_breaks
odds_f = list(zip(odds_f,(['f']*len(odds_f))))

evens_rare_odds_freq1 = evens_r + odds_f
evens_rare_odds_freq2 = evens_r + odds_f
evens_rare_odds_freq3 = evens_r + odds_f
evens_rare_odds_freq4 = evens_r + odds_f
evens_rare_odds_freq5 = evens_r + odds_f
evens_rare_odds_freq6 = evens_r + odds_f
evens_rare_odds_freq7 = evens_r + odds_f
evens_rare_odds_freq8 = evens_r + odds_f
# Now we switch 
odds_rare_evens_freq1 = evens_f + odds_r
odds_rare_evens_freq2 = evens_f + odds_r
odds_rare_evens_freq3 = evens_f + odds_r
odds_rare_evens_freq4 = evens_f + odds_r
odds_rare_evens_freq5 = evens_f + odds_r
odds_rare_evens_freq6 = evens_f + odds_r
odds_rare_evens_freq7 = evens_f + odds_r
odds_rare_evens_freq8 = evens_f + odds_r

random.seed(datetime.now())

if block_counterbalance == 1:
    random.shuffle(evens_rare_odds_freq1)
    b1 = evens_rare_odds_freq1
    random.shuffle(odds_rare_evens_freq2)
    b2 = odds_rare_evens_freq2  
    random.shuffle(evens_rare_odds_freq3)
    b3 = evens_rare_odds_freq3
    random.shuffle(odds_rare_evens_freq4)
    b4 = odds_rare_evens_freq4
    random.shuffle(evens_rare_odds_freq5)
    b5 = evens_rare_odds_freq5
    random.shuffle(odds_rare_evens_freq6)
    b6 = odds_rare_evens_freq6
    random.shuffle(evens_rare_odds_freq7)
    b7 = evens_rare_odds_freq7
    random.shuffle(odds_rare_evens_freq8)
    b8 = odds_rare_evens_freq8
else:
    random.shuffle(odds_rare_evens_freq1)
    b1 = odds_rare_evens_freq1  
    random.shuffle(evens_rare_odds_freq2)
    b2 = evens_rare_odds_freq2
    random.shuffle(odds_rare_evens_freq3)
    b3 = odds_rare_evens_freq3  
    random.shuffle(evens_rare_odds_freq4)
    b4 = evens_rare_odds_freq4
    random.shuffle(odds_rare_evens_freq5)
    b5 = odds_rare_evens_freq5  
    random.shuffle(evens_rare_odds_freq6)
    b6 = evens_rare_odds_freq6
    random.shuffle(odds_rare_evens_freq7)
    b7 = odds_rare_evens_freq7  
    random.shuffle(evens_rare_odds_freq8)
    b8 = evens_rare_odds_freq8


if full_or_test == 1:
    
    num_total_full= b1+b2+b3+b4+b5+b6+b7+b8
    num_total, ec_total = zip(*num_total_full)
    num_total = list(num_total)
    
    # for event codes
   
    ec_total = list(ec_total)
else:
    del b1[128:]
    del b2[128:]
    num_total_full = b1 + b2 
    num_total, ec_total = zip(*num_total_full)
    num_total = list(num_total)
    ec_total = list(ec_total)
    del ec_total[128:]
    del ec_total[128:]
    



#Generating jitter information 
fix = [random.randrange(100,300) for x in range(len(num_total))] #making jitter range in integer
myint = 1000 #using 1000 to convert the jitter randomization into ms. 
fix = [x/ myint for x in fix]
# for k in range(0,int((num_breaks/2-1))):
#     random.shuffle(evens_rare_odds_freq)
#     random.shuffle(odds_rare_evens_freq)
#     num_total = num_total.append(evens_rare_odds_freq)
    
#Creating for loop in order to create list of left and right options and group index         
corr = [] 
group = [] 
for k in range(len(num_total)):
    if num_total[k]%2 != 0:
        #i.e. if number is odd (has reminder), it is "1xx" or "left" as correct answer
        corr.append('left')
        #if ec_block = 1, then the first rare condition is even numbers
        #
        group.append(1) 
        #1 = frequent = "odd" / 2 = rare = "even"
    else:
        corr.append('right')
        #i.e. if number is even (remainder =0), it is "2xx" or "right" as correct answer 
        group.append(2)
        #1 = frequent = "odd" / 2 = rare = "even" 

trial = list(range(1,len(num_total)+1))

################ EVENT CODES 
# #Creating event codes for experiment triggers in prior to writing to CSV - Aaron
# music = 1 ; #music? (write as 1 or 0)
# blight = 1; #bluelight? (write as 1 or 0)

conditions_info={"Blue Light (on/off)": '', "Music (on/off)": ''}
        
if not gui.DlgFromDict(dictionary=conditions_info, order=["Blue Light (on/off)"]).OK:
    core.quit()

if conditions_info['Blue Light (on/off)'] or conditions_info['Blue Light (on/off)']  == 'On':
    blight = 1
else:
    blight = 0
    
if conditions_info['Music (on/off)'] == 'on' or conditions_info['Music (on/off)'] == 'On':
    music = 1
else:
    music = 0 
      

if music == 1 & blight == 1:
    mbl_cond = 4 
elif music == 1 & blight == 0:
    mbl_cond = 3
elif music == 0 & blight == 1:
    mbl_cond = 2 
elif music == 0 % blight == 0:
    mbl_cond = 1


ecode = []
for i in range(len(ec_total)):
    
    #hundreds place: 1 = frequent / 2 = rare
    #in this script, odds = freq/ evens = rare
    #tens place: combination of music or blue light (mbl)
    #ones place: actual number
    if ec_total[i] == 'r':
        ec_hun = 1
    else:
        ec_hun = 2
        
    
    ecode.append(int(str(ec_hun) + str(mbl_cond) + str(num_total[i])))
##################
                                     
#Writing this all out to a CSV to be used for experiment.
with fpath.open(mode='w',newline='') as csvfile: 
    header = ['trial','num','group','corr','fix','ecode']
    thewriter = csv.DictWriter(csvfile,fieldnames=header)
    thewriter.writeheader()
    for i in range(len(num_total)): 
        thewriter.writerow({'trial':trial[i],'num': num_total[i], 'group': group[i],'corr': corr[i],'fix':fix[i],'ecode': ecode[i]})

'''constants'''
#Subject Gui
subinfo={"Participant ID": '', "Age": '',"Handedness":'',"Sex":'',"Years of Education":'',"Diode": 'l',}
        
if not gui.DlgFromDict(dictionary=subinfo, order=["Participant ID"]).OK:
    core.quit()

stime=time.strftime("%H:%M:%S")

#Lists & inputs
ID=subinfo["Participant ID"]
Age=subinfo["Age"]
Handedness=subinfo["Handedness"]
Sex=subinfo["Sex"]
Education=subinfo["Years of Education"] 
diode=subinfo["Diode"]
Blue_Light=conditions_info["Blue Light (on/off)"] 
Music=conditions_info["Music (on/off)"]

#Core elements
if Blue_Light=='on' or Blue_Light=='On':
    mywin= visual.Window(monitor="testMonitor", screen=2, units="deg",fullscr=True,color='grey')
    #mywin= visual.Window(winType="pyglet", screen=1, monitor ="testMonitor", size=(2560,1600),units="deg",fullscr=False, color='blue')
elif Blue_Light=='off' or Blue_Light=='Off':
    mywin= visual.Window(monitor="testMonitor",screen=2, units="deg",fullscr=True,color='grey')
    #mywin= visual.Window(winType="pyglet", screen=1, monitor ="testMonitor", size=(2560,1600),units="deg",fullscr=False, color='grey')
else:
    print("Please specify if you want blue light")
    core.quit()
#mywin= visual.Window(winType="pyglet", screen=1, monitor ="testMonitor", size=(2560,1600),units="deg",fullscr=False, color='blue')


scrnHz=mywin.getActualFrameRate(nIdentical=10, nMaxFrames=100, nWarmUpFrames=10, threshold=1)
clock=core.Clock()
scrnHz=mywin.getActualFrameRate(nIdentical=10, nMaxFrames=100, nWarmUpFrames=10, threshold=1)
if 59 < scrnHz <61:
    scrnHz = 60
else:
    raise NameError('SCRNHZ NOT 60') 

myMouse=event.Mouse(visible=False,win=mywin)

#write/load paths
#basepath=os.path.normpath(os.getcwd() + os.sep + os.pardir)
basepath = Path('/home/carlosc/Desktop/num_oddball_py3/')
data_path=os.path.join(basepath, 'data')+ os.sep
sequence_path=os.path.join(basepath, 'seq')+ os.sep

#objects
eot=visual.TextStim(mywin,height=4,font='Ariel',wrapWidth=35,text="End of Task. Thank you so much for your participation!" , color='black')
#black_fix=visual.Rect(mywin,width=0.1,height=1.0,lineWidth=2,fillColorSpace='rgb255',fillColor=[0,0,0],lineColor='black')
# black_fix_2=visual.Rect(mywin,width=1.0,height=0.1,lineWidth=2,fillColorSpace='rgb255',fillColor=[0,0,0],lineColor='black')
black_fix = visual.ImageStim(
    win=mywin,
    image="Fixation.png",
    units ="pix")
pass_inst=visual.TextStim(win=mywin,pos=[0,-14],height=1,text="(Press a Button on Top of the Gamepad to Continue)",color='black')
pass_break=visual.TextStim(win=mywin,pos=[0.0],wrapWidth=35,height=1,text="Please take a break! Feel free to stretch and move around.", color='black')
message=visual.TextStim(win=mywin,pos=[0.0],wrapWidth=35,height=1,text="In this task you will be identifying numbers as odd or even. Press the upper trigger key to indicate an odd number and the lower trigger key to indicate an even number. If you have any questions please let the experimenter know now.", color='black')
centerBox=visual.Rect(mywin,width=10,height=10,lineWidth=1.0,pos=(0,0),fillColorSpace='rgb255',fillColor=[128,128,128],lineColor='grey')
rectangle=visual.Rect(mywin,width=0.1,height=0.1,lineWidth=0.5,fillColorSpace='rgb255',fillColor=[0,0,0])
blue_screen=visual.Rect(mywin,width=1000,height=1000,lineWidth=1.0,pos=(0,0),fillColorSpace='rgb255',fillColor=[128,128,128],lineColor='blue')
num=visual.TextStim(win=mywin,pos=[0.0],height=3.5,text="", color='black')
restart=visual.TextStim(win=mywin,pos=[0,2],wrapWidth=35,height=1,text="Starting Experiment in...", color='black')
five=visual.TextStim(win=mywin,pos=[0.0],height=3.5,text="5", color='black')
four=visual.TextStim(win=mywin,pos=[0.0],height=3.5,text="4", color='black')
three=visual.TextStim(win=mywin,pos=[0.0],height=3.5,text="3", color='black')
two=visual.TextStim(win=mywin,pos=[0.0],height=3.5,text="2", color='black')
one=visual.TextStim(win=mywin,pos=[0.0],height=3.5,text="1", color='black')

if diode=='l' or diode=='L':
    rectangle=visual.Rect(win=mywin,width=3,height=3,pos=[-25,0],fillColor='black',lineColor='black')
elif diode=='r' or diode=='R':
    rectangle=visual.Rect(win=mywin,width=3,height=3,pos=[25,-15],fillColor='black',lineColor='black')
else:
    print("Incorrect Photodiode")
    core.quit()


#Trial types
    #Core elements
if Blue_Light=='on' or Blue_Light=='On':
    imagestim=[centerBox,rectangle,num,black_fix]
elif Blue_Light=='off' or Blue_Light=='Off':
    imagestim=[centerBox,rectangle,num,black_fix,blue_screen]
else:
    print("Please specify if you want blue light")
    core.quit()

#imagestim=[centerBox,rectangle,num,black_fix]
responsestim=[centerBox,black_fix]


def instructions():
    #grey_screen.draw()
    message.draw()
    pass_inst.draw()
    mywin.flip()
    event.waitKeys(keyList='space')

def rest_period():
    #grey_screen.draw()
    pass_break.draw()
    pass_inst.draw()
    mywin.flip()
    event.waitKeys(keyList='space')
    
#creating list for buffers
buffer = [1,2,3,4,5,6,7,8]
buffer_jitter=[random.randrange(800,1100)]
buffer_jitter = [x/ myint for x in buffer_jitter]
buff_jit = float(buffer_jitter[0])
buffer_jitter_2=[random.randrange(800,1100)]
buffer_jitter_2 = [x/ myint for x in buffer_jitter_2]
buff_jit_2 = float(buffer_jitter_2[0])

def countdown():
    restart.draw()
    mywin.flip()
    core.wait(1.0)
    restart.draw()
    five.draw()
    mywin.flip()
    core.wait(1.0)
    restart.draw()
    four.draw()
    mywin.flip()
    core.wait(1.0)
    restart.draw()
    three.draw()
    mywin.flip()
    core.wait(1.0)
    restart.draw()
    two.draw()
    mywin.flip()
    core.wait(1.0)
    restart.draw()
    one.draw()
    mywin.flip()
    core.wait(1.0)
    random_num = random.choice(buffer)
    random_num = str(random_num)
    centerBox.draw()
    black_fix.draw()
    mywin.flip()
    core.wait(buff_jit)
    buff=visual.TextStim(win=mywin,pos=[0.0],height=3.5,text=random_num, color='black')
    centerBox.draw()
    rectangle.draw()
    black_fix.draw()
    buff.draw()
    mywin.flip()
    core.wait(0.2)
    centerBox.draw()
    black_fix.draw()
    mywin.flip()
    core.wait(buff_jit_2)
    event.clearEvents()

def task(trials,save):
    Trialcount=0
    for t in trials:
        Trialcount=Trialcount+1
        TrialOnset=clock.getTime()
        num.text=t[1] #appending the current number to general object
        #this object num then gets read into imagestime 
        
        
        #flip the number
        for l in range(int(scrnHz*(0.2))):
            drawing(imagestim)
            mywin.flip()
            if ERP == 'Y':
                if l == 0:
                    sendTrigger(ecode[Trialcount])
                if l == 12:
                    sendTrigger(ecode[5])
            
        event.clearEvents()
        ChoiceOnset=clock.getTime()
        respond=0
        
        #flip the waittime 
        for l in range(int(scrnHz*(0.8))):
            if respond==0:
                keypress=event.getKeys(keyList=['left','right','q'])
                
                if not keypress:
                    Choice='N/A'
                    RT=0
                    Acc=2
                    DecisionOnset=clock.getTime()
                    
                if keypress:
                    respond=1
                    DecisionOnset=clock.getTime()
                    RT=DecisionOnset-ChoiceOnset
                    sendTrigger(6)
    
                else:
                    drawing(responsestim)
                    mywin.flip()
    
                if keypress==['left']:
                    Choice='left'
                    if t[3]=='left':
                        Acc=1
                        sendTrigger(7)
                    
                    elif t[3]=='right':
                        Acc=0
                        sendTrigger(8)
                    
                    else:
                        Acc=3
                        DecisionOnset=clock.getTime()
                        RT=0
                        
                elif keypress==['right']:
                    Choice='right'
                    if t[3]=='left':
                        Acc=0
                        sendTrigger(8)
                    
                    elif t[3]=='right':
                        Acc=1
                        sendTrigger(7)
                    
                    else:
                        DecisionOnset=clock.getTime()
                        Acc=3
                        RT=0
                
                elif keypress==['q']:
                    Choice='Quit'
                    Acc=2
                    RT=0
                    DecisionOnset=clock.getTime()
                    save.append([ID,Age,Handedness,Sex,Education,Blue_Light,Music,Trialcount,TrialOnset,ChoiceOnset,DecisionOnset,RT,t[0],t[1],t[2],t[3],t[4],t[5],Choice,Acc])
                    get_data(save)
                    core.quit()
                    
                            
            elif respond==1:
                drawing(responsestim)
                mywin.flip()
        
        sendTrigger(10) #end of trial before jitter event code 
        for l in range(int(scrnHz*(float(t[4])))):
            centerBox.draw()
            black_fix.draw()
            #black_fix_2.draw()
            mywin.flip()
        
        save.append([ID,Age,Handedness,Sex,Education,Blue_Light,Music,Trialcount,TrialOnset,ChoiceOnset,DecisionOnset,RT,t[0],t[1],t[2],t[3],t[4],t[5],Choice,Acc])
    get_data(save)
    
def get_data(Save):
    end_time=time.strftime("%Y%m%d-%H%M%S")
    etime=time.strftime("%H:%M:%S")
    header=['Participant ID','Age','Handedness','Sex','Education','Blue Light','Music','Round','TrialOnset','ChoiceOnset','DecisionOnset','RT','Trial Number','Number','Group','Corr','Fixation','ecode','Choice','Acc']
    savFrac= open(data_path + subinfo['Participant ID'] + '_' + end_time + '.txt', 'w')
    for i in header:
        savFrac.write(i)
        savFrac.write('\t')
    savFrac.write('\n')
    for l in Save:
        for x in range(len(l)):
            savFrac.write(str(l[x]))
            savFrac.write('\t')
        savFrac.write('\n')
    savFrac.write('\n')
    savFrac.write("Start Time: ")
    savFrac.write(str(stime))
    savFrac.write("\n")
    savFrac.write("End Time: ")
    savFrac.write(str(etime))


def drawing(l):
    for item in l:
        item.draw()


def get_trials():
    os.chdir(sequence_path)
    oddball_csv= participant_seq
    blocknum=-1
    save=[]
    firstdown = 0
    for block in range(1,9):
        blocknum+=1
    
        oddball_trials=[]
        trange=list(range(blocknum*split_trials+1,blocknum*split_trials+(split_trials+1)))
        
        with open(oddball_csv, 'r') as csv_file:
            if blocknum==0:
                next(csv_file)
            if firstdown != 0 :
                next(csv_file)
            for row in csv.reader(csv_file, delimiter=','):
                      
                if int(row[0]) in trange:
                    task_trial=row
                    oddball_trials.append(task_trial)
                
            if blocknum==0:
                instructions()
                countdown()
        task(oddball_trials,save)
        firstdown+=1
        
        if ERP == 'Y':
            sendTrigger(15)
        
        
        rest_period()
        countdown()
        if ERP == 'Y':
            sendTrigger(16)

        print('finshed block number' +' ' + str(blocknum))

    
if __name__ == '__main__':
    get_trials()
    

eot.draw()
mywin.flip()
event.waitKeys(keyList='space')

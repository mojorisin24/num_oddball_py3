"""
Oddball Number Task 
In this case, odds will be frequent and evens will be rare. 
Please use the adjacent script num_oddball_py3_even if you'd like evens to be frequent and odds to be rare 
* Note to experimenters you will have to change the path (line **) to point at the directory where the task has been placed specifically the sequence folder. 
Questions? Feel free to reach out: cdcarrasco@ucdavis.edu, amsimmons@ucdavis.edu  
Huge Thank you to dsmiller@ucdavis.edu and amsimmons@ucdavis.edu for helping with creation of the paradigm. 
"""
from psychopy import visual, core, event, gui, parallel
from pathlib import Path
import os, random, time, csv
#Flag for block counterbalance set to 0 to run odds then even blocks, set to 1 to run even then odds block sequence 
block_counterbalance = 1
full_or_test = 0 # make this 1 to run entire experiment, 0 if you are just trying to debug and make changes to code. 
#Naming CSV for Participant Sequence. 
participant_seq = 'rare_even_freq_odd_seq.csv'
#setting path to save CSV to      
path = Path('\\Users\\Carlos\\Documents\\oddball_task\\num_oddball_py3\\seq\\') #here you will need to set the path to wherever you have saved the experiment folder, make sure to point this directory to  the seq folder. 
#path = Path('/Users/amsimmon/Documents/LuckLabShortcut/LuckLab/Experiments/p3_carlos_2020/num_oddball_py3/seq')
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
    port = parallel.ParallelPort(address=0x2050)
    
    def sendTrigger(trigger):
        port.setData(int(trigger))
        core.wait(0.005)
        port.setData(0)
        
#House keeping
freq = int(freq)
rare = int(rare)
#Generating odds and even lists. In this case odds are freq and evens are rare 
#Evens rare and odds freq 
evens_r = [2,4,6,8] * rare * num_breaks
odds_r = [1,3,5,7] * rare * num_breaks
evens_f = [2,4,6,8] * freq * num_breaks
odds_f = [1,3,5,7] * freq * num_breaks

evens_rare_odds_freq = evens_r + odds_f
odds_rare_evens_freq = evens_f + odds_r

rare_freq_evens = [] 
for k in range(len(evens_rare_odds_freq)):
    if evens_rare_odds_freq[k]%2 != 0:
        rare_freq_evens.append(2) 
    else:
        rare_freq_evens.append(1)

rare_freq_odds = []        
 #1 = rare / 2 = frequent

for k in range(len(odds_rare_evens_freq)):
    if odds_rare_evens_freq[k]%2 != 0:
        rare_freq_odds.append(1) 
        #1 = rare / 2 = frequent
    else:
        rare_freq_odds.append(2)

even_rare_coupled = list(zip(evens_rare_odds_freq, rare_freq_evens))
odd_rare_coupled = list(zip(odds_rare_evens_freq, rare_freq_odds))


if block_counterbalance == 1: 
#Blocks follow even then odd order  
    random.shuffle(even_rare_coupled)
    c1 = even_rare_coupled
    random.shuffle(odd_rare_coupled)
    c2 = odd_rare_coupled  
    random.shuffle(even_rare_coupled)
    c3 = even_rare_coupled
    random.shuffle(odd_rare_coupled)
    c4 = odd_rare_coupled
    random.shuffle(even_rare_coupled)
    c5 = even_rare_coupled
    random.shuffle(odd_rare_coupled)
    c6 = odd_rare_coupled
    random.shuffle(even_rare_coupled)
    c7 = even_rare_coupled
    random.shuffle(odd_rare_coupled)
    c8 = odd_rare_coupled
else:
# Blocks follow odd then even order 
    random.shuffle(odd_rare_coupled)
    c1 = odd_rare_coupled  
    random.shuffle(even_rare_coupled)
    c2 = even_rare_coupled
    random.shuffle(odd_rare_coupled)
    c3 = odd_rare_coupled  
    random.shuffle(even_rare_coupled)
    c4 = even_rare_coupled
    random.shuffle(odd_rare_coupled)
    c5 = odd_rare_coupled  
    random.shuffle(even_rare_coupled)
    c6 = even_rare_coupled
    random.shuffle(odd_rare_coupled)
    c7 = odd_rare_coupled  
    random.shuffle(even_rare_coupled)
    c8 = even_rare_coupled


b1,rf1 = zip(*c1)
b2,rf2 = zip(*c2)
b3,rf3 = zip(*c3)
b4,rf4 = zip(*c4)
b5,rf5 = zip(*c5)
b6,rf6 = zip(*c6)
b7,rf7 = zip(*c7)
b8,rf8 = zip(*c8)

if full_or_test == 1:
    num_total = b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 
    rf_total = rf1 + rf2 +rf3 + rf4 + rf5 + rf6 +rf7 +rf8
else:
    del b1[128:]
    del b2[128:]
    del rf1[128:]
    del rf2[128:]
    num_total = b1 + b2 
    rf_total = rf1 + rf2 


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
        corr.append('left')
        group.append(1) 
        #1 = odd / 2 = even
    else:
        corr.append('right')
        group.append(2)

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
for i in range(len(num_total)):
    
    #hundreds place: 1 = frequent / 2 = rare
    #in this script, odds = freq/ evens = rare
    #tens place: combination of music or blue light (mbl)
    #ones place: actual number

    ecode.append(int(str(rf_total[i]) + str(mbl_cond) + str(num_total[i])))
##################
                                     
#Writing this all out to a CSV to be used for experiment.
with fpath.open(mode='w',newline='') as csvfile: 
    header = ['trial','num','group','corr','fix','ecode']
    thewriter = csv.DictWriter(csvfile,fieldnames=header)
    thewriter.writeheader()
    for i in range(len(num_total)): 
        thewriter.writerow({'trial':trial[i],'num': num_total[i], 'group': group[i],'rare_freq': rf_total[i],'corr': corr[i],'fix':fix[i],'ecode': ecode[i]})

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
    mywin= visual.Window(monitor="testMonitor",units="deg",fullscr=True,color='blue')
    #mywin= visual.Window(winType="pyglet", screen=1, monitor ="testMonitor", size=(2560,1600),units="deg",fullscr=False, color='blue')
elif Blue_Light=='off' or Blue_Light=='Off':
    mywin= visual.Window(monitor="testMonitor",units="deg",fullscr=True,color='grey')
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
basepath=os.path.normpath(os.getcwd() + os.sep + os.pardir)
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
grey_screen=visual.Rect(mywin,width=1000,height=1000,lineWidth=1.0,pos=(0,0),fillColorSpace='rgb255',fillColor=[128,128,128],lineColor='grey')
num=visual.TextStim(win=mywin,pos=[0.0],height=3.5,text="", color='black')

if diode=='l' or diode=='L':
    rectangle=visual.Rect(win=mywin,width=7,height=7,pos=[-25,-15],fillColor='black',lineColor='black')
elif diode=='r' or diode=='R':
    rectangle=visual.Rect(win=mywin,width=7,height=7,pos=[25,-15],fillColor='black',lineColor='black')
else:
    print("Incorrect Photodiode")
    core.quit()


#Trial types
imagestim=[centerBox,rectangle,num,black_fix]
responsestim=[centerBox,black_fix]

def instructions():
    grey_screen.draw()
    message.draw()
    pass_inst.draw()
    mywin.flip()
    event.waitKeys(keyList='space')

def rest_period():
    grey_screen.draw()
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
    grey_screen.draw()
    restart=visual.TextStim(win=mywin,pos=[0,2],wrapWidth=35,height=1,text="Starting Experiment in...", color='black')
    restart.draw()
    mywin.flip()
    core.wait(1.0)
    grey_screen.draw()
    restart.draw()
    five=visual.TextStim(win=mywin,pos=[0.0],height=3.5,text="5", color='black')
    five.draw()
    mywin.flip()
    core.wait(1.0)
    grey_screen.draw()
    restart.draw()
    four=visual.TextStim(win=mywin,pos=[0.0],height=3.5,text="4", color='black')
    four.draw()
    mywin.flip()
    core.wait(1.0)
    grey_screen.draw()
    restart.draw()
    three=visual.TextStim(win=mywin,pos=[0.0],height=3.5,text="3", color='black')
    three.draw()
    mywin.flip()
    core.wait(1.0)
    grey_screen.draw()
    restart.draw()
    two=visual.TextStim(win=mywin,pos=[0.0],height=3.5,text="2", color='black')
    two.draw()
    mywin.flip()
    core.wait(1.0)
    grey_screen.draw()
    restart.draw()
    one=visual.TextStim(win=mywin,pos=[0.0],height=3.5,text="1", color='black')
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
    
                else:
                    drawing(responsestim)
                    mywin.flip()
    
                if keypress==['left']:
                    Choice='left'
                    if t[3]=='left':
                        Acc=1
                    
                    elif t[3]=='right':
                        Acc=0
                    
                    else:
                        Acc=3
                        DecisionOnset=clock.getTime()
                        RT=0
                        
                elif keypress==['right']:
                    Choice='right'
                    if t[3]=='left':
                        Acc=0
                    
                    elif t[3]=='right':
                        Acc=1
                    
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
        
        
        for l in range(int(scrnHz*(float(t[4])))):
            centerBox.draw()
            black_fix.draw()
            #black_fix_2.draw()
            mywin.flip()
        
        save.append([ID,Age,Handedness,Sex,Education,Blue_Light,Music,Trialcount,TrialOnset,ChoiceOnset,DecisionOnset,RT,t[0],t[1],t[2],t[3],t[4],t[5],Choice,Acc])
    get_data(save)
    
def get_data(Save):
    end_time=time.strftime("%Y%m%d-%H%M%S")
#    etime=time.strftime("%H:%M:%S")
    header=['Participant ID','Age','Handedness','Sex','Education','Blue Light','Music','Round','TrialOnset','ChoiceOnset','DecisionOnset','RT','Trial Number','Number','Group','Corr','Fixation','ecode','Choice','Acc']
    savFrac= open(data_path + subinfo['Participant ID'] + '_' + end_time + '.csv', 'w')
    for i in header:
        savFrac.write(i)
        savFrac.write(',')
    savFrac.write('\n')
    for l in Save:
        for x in range(len(l)):
            savFrac.write(str(l[x]))
            savFrac.write(',')
        savFrac.write('\n')
    #savFrac.write('\n')
    # savFrac.write("Start Time: ")
    # savFrac.write(str(stime))
    # savFrac.write("\n")
    # savFrac.write("End Time: ")
    # savFrac.write(str(etime))


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

    
if __name__ == '__main__':
    get_trials()
    

eot.draw()
mywin.flip()
event.waitKeys(keyList='space')
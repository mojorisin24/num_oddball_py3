"""
Oddball Number Task 
In this case, odds will be frequent and evens will be rare. 
Please use the adjacent script num_oddball_py3_even if you'd like evens to be frequent and odds to be rare 
* Note to experimenters you will have to change the path (line 16) to pont at the directory where the task has been placed specifically the sequence folder. 
Questions? Feel free to reach out: cdcarrasco@ucdavis.edu 
Huge Thank you to dsmiller@ucdavis.edu for helping with creation of the paradigm.  
"""
from psychopy import visual, core, event, gui 
from pathlib import Path
import os, random, time, csv

#Naming CSV for Participant Sequence. 
participant_seq = 'rare_even_freq_odd_seq.csv'
#setting path to save CSV to      
path = Path('\\Users\\Carlos\\Documents\\oddball_task\\num_oddball_py3\\seq\\') #here you will need to set the path to wherever you have saved the experiment folder, make sure to point this directory to  the seq folder. 
#setting fpath with name of csv 
fpath = (path / participant_seq).with_suffix('.csv') 
#Setting flags for shuffle do not change at all 
done = 0
done2 = 0 
done3 = 0 
done4 = 0
#Specifying Number of Trials change tot_trials if needed and nothing else 
tot_trials = 256
split_trials = int(tot_trials/16)
#setting up rare and freq lists
freq = split_trials * 0.875
rare = split_trials * 0.125

#Generating jitter information 
fix = [random.randrange(900,1100) for x in range(tot_trials)] #making jitter range in integer
myint = 1000 #using 1000 to convert the jitter randomization into ms. 
fix = [x/ myint for x in fix]

#House keeping
freq = int(freq)
rare = int(rare)
#Generating odds and even lists. In this case odds are freq and evens are rare 
#Evens
two = [2] * rare
four = [4] * rare 
six = [6] * rare 
eight = [8] * rare 
#Odds 
one = [1] * freq
three = [3] * freq
five = [5] * freq
seven = [7] * freq

odd = one + three + five + seven 
even = two + four + six + eight 

#Concatenating said lists and generating a few repeats of the list. 
num = odd + even
num2 = odd + even 
num3 = odd + even 
num4 = odd + even 

#While loop to shuffle trial list until oddballs don't coincide with one another. 
while done < 1:
   for seq in range(len(num)-1):
       if num[seq]%2 == 0 and num[seq+1]%2 == 0:
           random.shuffle(num)
           done = 0 
           break
       elif num[seq]%2 != 0 and num[seq+1]%2 != 0:
           done = 1 

#num2 
while done2 < 1:
   for seq in range(len(num2 )-1):
       if num2 [seq]%2 == 0 and num2 [seq+1]%2 == 0:
           random.shuffle(num2 )
           done2 = 0 
           break
       elif num2 [seq]%2 != 0 and num2 [seq+1]%2 != 0:
           done2 = 1           

#num3 
while done3 < 1:
   for seq in range(len(num3 )-1):
       if num3 [seq]%2 == 0 and num3 [seq+1]%2 == 0:
           random.shuffle(num3 )
           done3 = 0 
           break
       elif num3 [seq]%2 != 0 and num3 [seq+1]%2 != 0:
           done3 = 1 
           
#num4 
while done4 < 1:
   for seq in range(len(num4 )-1):
       if num4 [seq]%2 == 0 and num4 [seq+1]%2 == 0:
           random.shuffle(num4 )
           done4 = 0 
           break
       elif num4 [seq]%2 != 0 and num4 [seq+1]%2 != 0:
           done4 = 1           

num_total = num + num2 + num3 + num4 
        
#Creating for loop in order to create list of left and right options and group index         
corr = [] 
group = [] 
for k in range(len(num_total)):
    if num_total[k]%2 != 0:
        corr.append('left')
        group.append(1)
    else:
        corr.append('right')
        group.append(2)

trial = list(range(1,len(num_total)+1))


#Writing this all out to a CSV to be used for experiment.
with fpath.open(mode='w',newline='') as csvfile: 
    header = ['trial','num','group','corr','fix']
    thewriter = csv.DictWriter(csvfile,fieldnames=header)
    thewriter.writeheader()
    for i in range(len(num_total)): 
        thewriter.writerow({'trial':trial[i],'num': num_total[i], 'group': group[i],'corr': corr[i],'fix':fix[i]})

'''constants'''
#Subject Gui
subinfo={"Participant ID": '', "Age": '',"Handedness":'',"Sex":'',"Years of Education":'',"Blue Light (on/off)":'',"Diode": 'l',}
        
if not gui.DlgFromDict(dictionary=subinfo, order=["Participant ID"]).OK:
    core.quit()


stime=time.strftime("%H:%M:%S")

#Lists & inputs
ID=subinfo["Participant ID"]
Age=subinfo["Age"]
Handedness=subinfo["Handedness"]
Sex=subinfo["Sex"]
Education=subinfo["Years of Education"] 
Blue_Light=subinfo["Blue Light (on/off)"] 
diode=subinfo["Diode"]

#Core elements
if Blue_Light=='on' or Blue_Light=='On':
    mywin= visual.Window(monitor="testMonitor",units="deg",fullscr=True,color='blue')
elif Blue_Light=='off' or Blue_Light=='Off':
    mywin= visual.Window(monitor="testMonitor",units="deg",fullscr=True,color='grey')
else:
    print("Please specify if you want blue light")
    core.quit()


#mywin= visual.Window(monitor="testMonitor",units="deg",fullscr=True,color='grey')
scrnHz=mywin.getActualFrameRate(nIdentical=10, nMaxFrames=100, nWarmUpFrames=10, threshold=1)
clock=core.Clock()
scrnHz=mywin.getActualFrameRate(nIdentical=10, nMaxFrames=100, nWarmUpFrames=10, threshold=1)
myMouse=event.Mouse(visible=False,win=mywin)

#write/load paths
basepath=os.path.normpath(os.getcwd() + os.sep + os.pardir)
data_path=os.path.join(basepath, 'data')+ os.sep
sequence_path=os.path.join(basepath, 'seq')+ os.sep

#objects
eot=visual.TextStim(mywin,height=4,font='Ariel',wrapWidth=35,text="End of Task" , color='black')
black_fix=visual.Rect(mywin,width=0.1,height=1.0,lineWidth=2,fillColorSpace='rgb255',fillColor=[0,0,0],lineColor='black')
black_fix_2=visual.Rect(mywin,width=1.0,height=0.1,lineWidth=2,fillColorSpace='rgb255',fillColor=[0,0,0],lineColor='black')
pass_inst=visual.TextStim(win=mywin,pos=[0,-14],height=1,text="(Press a Button on Top of the Gamepad to Continue)",color='black')
pass_break=visual.TextStim(win=mywin,pos=[0.0],wrapWidth=35,height=1,text="Please take a break! Feel free to stretch and move around.", color='black')
message=visual.TextStim(win=mywin,pos=[0.0],wrapWidth=35,height=1,text="In this task you will be identifying numbers as odd or even. Press the left trigger key to indicate an odd number and the right trigger key to indicate an even number. If you have any questions please let the experimenter know now.", color='black')
centerBox=visual.Rect(mywin,width=15,height=15,lineWidth=1.0,pos=(0,0),fillColorSpace='rgb255',fillColor=[128,128,128],lineColor='gray')
rectangle=visual.Rect(mywin,width=0.1,height=0.1,lineWidth=0.5,fillColorSpace='rgb255',fillColor=[0,0,0])
num=visual.TextStim(win=mywin,pos=[0.0],height=3,text="", color='black')

if diode=='l' or diode=='L':
    rectangle=visual.Rect(win=mywin,width=7,height=7,pos=[-25,-15],fillColor='black',lineColor='black')
elif diode=='r' or diode=='R':
    rectangle=visual.Rect(win=mywin,width=7,height=7,pos=[25,-15],fillColor='black',lineColor='black')
else:
    print("Incorrect Photodiode")
    core.quit()



#Trial types
imagestim=[centerBox,rectangle,num,black_fix,black_fix_2]
responsestim=[centerBox,black_fix,black_fix_2]

def instructions():
    message.draw()
    pass_inst.draw()
    mywin.flip()
    event.waitKeys(keyList='space')

def rest_period():
    pass_break.draw()
    pass_inst.draw()
    mywin.flip()
    event.waitKeys(keyList='space')
    
def task(trials,save):
    Trialcount=0
    for t in trials:
        Trialcount=Trialcount+1
        TrialOnset=clock.getTime()
        num.text=t[1]
        
        for l in range(int(scrnHz*(0.2))):
            drawing(imagestim)
            mywin.flip()
            
        event.clearEvents()
        ChoiceOnset=clock.getTime()
        respond=0
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
                    save.append([ID,Age,Handedness,Sex,Education,Blue_Light,Trialcount,TrialOnset,ChoiceOnset,DecisionOnset,RT,t[0],t[1],t[2],t[3],t[4],Choice,Acc])
                    get_data(save)
                    core.quit()
                    
                            
            elif respond==1:
                drawing(responsestim)
                mywin.flip()
        
        
        for l in range(int(scrnHz*(float(t[4])))):
            centerBox.draw()
            black_fix.draw()
            black_fix_2.draw()
            mywin.flip()
        
        save.append([ID,Age,Handedness,Sex,Education,Blue_Light,Trialcount,TrialOnset,ChoiceOnset,DecisionOnset,RT,t[0],t[1],t[2],t[3],t[4],Choice,Acc])
    get_data(save)
    
def get_data(Save):
    end_time=time.strftime("%Y%m%d-%H%M%S")
    etime=time.strftime("%H:%M:%S")
    header=['Participant ID','Age','Handedness','Sex','Education','Blue Light','Round','TrialOnset','ChoiceOnset','DecisionOnset','RT','Trial Number','Number','Group','Corr','Fixation','Choice','Acc']
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
    for block in range(1,9):
        blocknum=blocknum+1
    
        oddball_trials=[]
        trange=list(range(blocknum*split_trials+1,blocknum*split_trials+(split_trials+1)))
        
        with open(oddball_csv, 'r') as csv_file:
            if blocknum==0:
                next(csv_file)
            for row in csv.reader(csv_file, delimiter=','):
                if int(row[0]) in trange:
                    task_trial=row
                    oddball_trials.append(task_trial)
                
            if blocknum==0:
                instructions()
        task(oddball_trials,save)
        rest_period()
        core.quit()
    

if __name__ == '__main__':
    get_trials()
    

eot.draw()
mywin.flip()
event.waitKeys(keyList='space')
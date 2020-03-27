from psychopy import gui

myDlg = gui.Dlg(title="JWP's experiment")
myDlg.addText('Subject info')
myDlg.addField('Name:')
myDlg.addField('Age:', 21)
myDlg.addText('Experiment Info')
myDlg.addField('Grating Ori:',45)
myDlg.addField('Group:', choices=["Test", "Control"])
ok_data = myDlg.show()  # show dialog and wait for OK or Cancel
if myDlg.OK:  # or if ok_data is not None
    print(ok_data)
else:
    print('user cancelled')
    
    
    

subinfo={"Participant ID": '', "Age": '',"Handedness":'',"Sex":'',"Years of Education":'',"Blue Light (on/off)":'',"Music (yes/no)":'',"Diode": 'l',}
        
if not gui.DlgFromDict(dictionary=subinfo, order=["Participant ID"]).OK:
    core.quit()

#Lists & inputs
ID=subinfo["Participant ID"]
Age=subinfo["Age"]
Handedness=subinfo["Handedness"]
Sex=subinfo["Sex"]
Education=subinfo["Years of Education"] 
Blue_Light=subinfo["Blue Light (on/off)"] 
Music=subinfo["Music (yes/no)"]
diode=subinfo["Diode"]
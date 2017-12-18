# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 15:51:50 2017

@author: Wenting Ye
"""

###Constants
DISPSIZE=(800,800)
colour={'black':[1,1,1],'white':[-1,-1,-1],\
        'grey':[0,0,0],'red':[1,-1,-1],'green':[-1,1,-1]}

from psychopy import core
from psychopy.visual import Window, TextStim, ImageStim
from psychopy.event import waitKeys
from psychopy.core import wait
import random

disp=Window(size=DISPSIZE,units='pix',color='white',\
            fullscr=False)


    
#####LOGFILE
LOGFILENAME=raw_input('Participant name: ')
LOGFILE=LOGFILENAME
log=open(LOGFILE+'.tsv','w')
header=['block','tarside','congr',\
        'response','correct','RT']
line=map(str,header)
line='\t'.join(line)
line+='\n'
log.write(line)

TARSIDE=['right','left']
CONGR=['congr','incongr']
UPDOWN=['H','L']
BLOCK=['block1','block2']

###Instruction screen
inststim=ImageStim(win=disp,image="start.jpg")

###Fixation cross
fixstim=TextStim(disp,text='+',color='black', height=24)
FIXTIME=1.0

###

###Stimuli
tarstim={}
tarstim['left']={}
tarstim['left']['congr']={}
tarstim['left']['congr']['H']=ImageStim(disp,image="Lcongr_h.jpg")
tarstim['left']['congr']['L']=ImageStim(disp,image="Lcongr_l.jpg")
tarstim['left']['incongr']={}
tarstim['left']['incongr']['H']=ImageStim(disp,image="Lincongr_h.jpg")
tarstim['left']['incongr']['L']=ImageStim(disp,image="Lincongr_l.jpg")
tarstim['right']={}
tarstim['right']['congr']={}
tarstim['right']['congr']['H']=ImageStim(disp,image="Rcongr_h.jpg")
tarstim['right']['congr']['L']=ImageStim(disp,image="Rcongr_l.jpg")
tarstim['right']['incongr']={}
tarstim['right']['incongr']['H']=ImageStim(disp,image="Rincongr_h.jpg")
tarstim['right']['incongr']['L']=ImageStim(disp,image="Rincongr_l.jpg")

TARTIME=1.7

###Feedback screen
fbstim={}
fbstim[0]=TextStim(disp,text='Incorrect!',height=24,color='red')
fbstim[1]=TextStim(disp,text='Correct!',height=24,color='green')
fbstim[2]=TextStim(disp,text='Too slow!',height=24,color='red')
FEEDBACKTIME=0.8

 
inststim.draw()
disp.flip()
waitKeys(maxWait=float('inf'),keyList=["return"],timeStamped=True)
 

stopwatch=core.Clock()

TRIALREPEATS=1


alltrials1=[]
for tarside in TARSIDE:
    for congr in CONGR:
        for updown in UPDOWN:
            trial1={'tarside':tarside,'congr':congr,'updown':updown,'block':1}
            alltrials1.extend(TRIALREPEATS*[trial1])
random.shuffle(alltrials1)

alltrials2=[]
for tarside in TARSIDE:
    for congr in CONGR:
        for updown in UPDOWN:
            trial2={'tarside':tarside,'congr':congr,'updown':updown,'block':2}
            alltrials2.extend(TRIALREPEATS*[trial2])
random.shuffle(alltrials2)




###Block 1###   
for trial1  in alltrials1:
    
    stopwatch.reset(newT=0.0)
    
    fixstim.draw()
    fixonset=disp.flip()
    wait(FIXTIME)
    
    tarstim[trial1['tarside']][trial1['congr']][trial1['updown']].draw()
    taronset=disp.flip()
    
    resplist=waitKeys(keyList=['left','right'],timeStamped=True)
    presstime=stopwatch.getTime()
    response,presstime=resplist[0]
    RT=presstime-taronset
    if RT<TARTIME:
        if response==trial1['tarside']:
            correct=1
        else:
            correct=0

    elif RT>=TARTIME:
        RT='_NR_'
        correct=2
    
    
    ##Give feedback
    fbstim[correct].draw()
    disp.flip()
    wait(FEEDBACKTIME)
    
    ###LOGFILE
    line=[trial1['block'],trial1['tarside'],\
          trial1['congr'],response,correct,RT]
    line=map(str,line)
    line='\t'.join(line)
    line+='\n'
    log.write(line)
    line+='\n'

###Block 2
inststim.draw()
disp.flip()
waitKeys(maxWait=float('inf'),keyList=["return"],timeStamped=True)
 
stopwatch=core.Clock()

TRIALREPEATS=1

for trial2 in alltrials2:   

    stopwatch.reset(newT=0.0)
    
    fixstim.draw()
    fixonset=disp.flip()
    wait(FIXTIME)
    
    tarstim[trial2['tarside']][trial2['congr']][trial2['updown']].draw()
    taronset=disp.flip()
    
    resplist=waitKeys(keyList=['left','right'],timeStamped=True)
    presstime=stopwatch.getTime()
    response,presstime=resplist[0]
    RT=presstime-taronset
    if RT<TARTIME:
        if response==trial2['tarside']:
            correct=1
        else:
            correct=0

    elif RT>=TARTIME:
        RT='_NR_'
        correct=2
    
    
    ##Give feedback
    fbstim[correct].draw()
    disp.flip()
    wait(FEEDBACKTIME)
    
    ###LOGFILE
    line=[trial2['block'],trial2['tarside'],\
          trial2['congr'],response,correct,RT]
    line=map(str,line)
    line='\t'.join(line)
    line+='\n'
    log.write(line)
    line+='\n'
    
    
log.close()
disp.close()
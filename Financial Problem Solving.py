#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.6),
    on March 14, 2018, at 10:48
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Financial Problems Task'  # from the Builder filename that created this script
expInfo = {u'stimorder': u'1', u'session': u'001', u'participant': u'', u'manigroup': u'H'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1366, 768), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1.000,1.000,1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Instr1"
Instr1Clock = core.Clock()
Instr1Text = visual.TextStim(win=win, name='Instr1Text',
    text='In this experiment, you will think about financial problems while completing a simple task.\n\nYou will complete the task by pressing the "0" or "1" keys.\n\nThe key you press will depend on what image is shown.\n\n(press space to continue)',
    font='Arial',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
if expInfo['stimorder'] == '1':
    congr="TessImages/1.jpg" #Heart
    congr_txt="heart"
    incongr="TessImages/2.jpg"#Star
    incongr_txt="star"
elif expInfo['stimorder'] == '2':
    congr="TessImages/2.jpg" #Star
    congr_txt="star"
    incongr="TessImages/1.jpg"#Heart
    incongr_txt="heart"
else:
    msg="Inputs do not make sense"
    core.quit()


# Initialize components for Routine "Instr2"
Instr2Clock = core.Clock()
Instr2Text = visual.TextStim(win=win, name='Instr2Text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Instr3"
Instr3Clock = core.Clock()
Instr3Text = visual.TextStim(win=win, name='Instr3Text',
    text='Here are some examples of correct responses.\n\nPress Space to continue.',
    font='Arial',
    pos=(0, 0), height=.025, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "setimg"
setimgClock = core.Clock()


# Initialize components for Routine "InstrTrial"
InstrTrialClock = core.Clock()
Fixation = visual.TextStim(win=win, name='Fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
stim = visual.ImageStim(
    win=win, name='stim',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
answerprompt = visual.TextStim(win=win, name='answerprompt',
    text='default text',
    font='Arial',
    pos=(0, .4), height=0.025, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0);


# Initialize components for Routine "Instr4"
Instr4Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='When the image of a %s is shown you will press the key that is on the OPPOSITE side of the screen that the %s is shown on. \n\nFor example, a correct response would be pressing the "1" key when the %s is on the right side of the screen\n\nPress space to continue.' % (incongr_txt,incongr_txt,incongr_txt),
    font='Arial',
    pos=(0, 0), height=.025, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Instr3"
Instr3Clock = core.Clock()
Instr3Text = visual.TextStim(win=win, name='Instr3Text',
    text='Here are some examples of correct responses.\n\nPress Space to continue.',
    font='Arial',
    pos=(0, 0), height=.025, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "setimg"
setimgClock = core.Clock()


# Initialize components for Routine "InstrTrial"
InstrTrialClock = core.Clock()
Fixation = visual.TextStim(win=win, name='Fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
stim = visual.ImageStim(
    win=win, name='stim',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
answerprompt = visual.TextStim(win=win, name='answerprompt',
    text='default text',
    font='Arial',
    pos=(0, .4), height=0.025, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0);


# Initialize components for Routine "PractInstr"
PractInstrClock = core.Clock()
practiceinstr = visual.TextStim(win=win, name='practiceinstr',
    text="Let's Practice!\n\nPress Space to Continue",
    font='Arial',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);


# Initialize components for Routine "setimg"
setimgClock = core.Clock()


# Initialize components for Routine "spatialtrial"
spatialtrialClock = core.Clock()
Fixation2 = visual.TextStim(win=win, name='Fixation2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
stimulus = visual.ImageStim(
    win=win, name='stimulus',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)


# Initialize components for Routine "Practicecounter"
PracticecounterClock = core.Clock()


# Initialize components for Routine "breaklooproutine"
breaklooproutineClock = core.Clock()


# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
feedbacktext = visual.TextStim(win=win, name='feedbacktext',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "FinanceInstr"
FinanceInstrClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='You will see a series of financial problems.\n\nAfter you read each problem, you will play the heart and star game while you think of a solution.\n\nThen you will have a chance to enter your solution.\n\nPress space to continue.',
    font='Arial',
    pos=(0, 0), height=.025, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "setproblem"
setproblemClock = core.Clock()
import sys
if expInfo['manigroup'] is not 'H' and expInfo['manigroup'] is not 'L':
    print 'Bad manigroup entered must be H or L'
    core.quit
    

# Initialize components for Routine "FinanceProblem"
FinanceProblemClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "getready"
getreadyClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Get Ready!',
    font='Arial',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "setimg"
setimgClock = core.Clock()


# Initialize components for Routine "spatialtrial"
spatialtrialClock = core.Clock()
Fixation2 = visual.TextStim(win=win, name='Fixation2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);
stimulus = visual.ImageStim(
    win=win, name='stimulus',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)


# Initialize components for Routine "Howwouldyousolve"
HowwouldyousolveClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='default text',
    font='Arial',
    pos=(0, 0), height=.025, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instr1"-------
t = 0
Instr1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

# keep track of which components have finished
Instr1Components = [Instr1Text]
for thisComponent in Instr1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instr1"-------
while continueRoutine:
    # get current time
    t = Instr1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instr1Text* updates
    if t >= 0.0 and Instr1Text.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr1Text.tStart = t
        Instr1Text.frameNStart = frameN  # exact frame index
        Instr1Text.setAutoDraw(True)
    if Instr1Text.status == STARTED and bool(event.getKeys('space')):
        Instr1Text.setAutoDraw(False)
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr1"-------
for thisComponent in Instr1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "Instr1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instr2"-------
t = 0
Instr2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Instr2Text.setText('When the image of a %s is shown you will press the key that is on the SAME side of the screen that the %s is shown on. \n\nFor example, a correct response would be pressing the "1" key when the %s is on the left side of the screen\n\nPress space to continue.' % (congr_txt,congr_txt,congr_txt))
# keep track of which components have finished
Instr2Components = [Instr2Text]
for thisComponent in Instr2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instr2"-------
while continueRoutine:
    # get current time
    t = Instr2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instr2Text* updates
    if t >= 0.0 and Instr2Text.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr2Text.tStart = t
        Instr2Text.frameNStart = frameN  # exact frame index
        Instr2Text.setAutoDraw(True)
    if Instr2Text.status == STARTED and bool(event.getKeys('space')):
        Instr2Text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr2"-------
for thisComponent in Instr2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instr2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instr3"-------
t = 0
Instr3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Instr3Components = [Instr3Text]
for thisComponent in Instr3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instr3"-------
while continueRoutine:
    # get current time
    t = Instr3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instr3Text* updates
    if t >= 0.0 and Instr3Text.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr3Text.tStart = t
        Instr3Text.frameNStart = frameN  # exact frame index
        Instr3Text.setAutoDraw(True)
    if Instr3Text.status == STARTED and bool(event.getKeys('space')):
        Instr3Text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr3"-------
for thisComponent in Instr3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instr3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
demo1trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('demo.xls', selection='0,1'),
    seed=None, name='demo1trials')
thisExp.addLoop(demo1trials)  # add the loop to the experiment
thisDemo1trial = demo1trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDemo1trial.rgb)
if thisDemo1trial != None:
    for paramName in thisDemo1trial.keys():
        exec(paramName + '= thisDemo1trial.' + paramName)

for thisDemo1trial in demo1trials:
    currentLoop = demo1trials
    # abbreviate parameter names if possible (e.g. rgb = thisDemo1trial.rgb)
    if thisDemo1trial != None:
        for paramName in thisDemo1trial.keys():
            exec(paramName + '= thisDemo1trial.' + paramName)
    
    # ------Prepare to start Routine "setimg"-------
    t = 0
    setimgClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    if (xpos == -.25 and corrResp == 1) or (xpos == .25 and corrResp == 0):
        stimimg=congr
    elif (xpos == -.25 and corrResp == 0) or (xpos == .25 and corrResp == 1):
        stimimg=incongr
    # keep track of which components have finished
    setimgComponents = []
    for thisComponent in setimgComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "setimg"-------
    while continueRoutine:
        # get current time
        t = setimgClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in setimgComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "setimg"-------
    for thisComponent in setimgComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "setimg" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "InstrTrial"-------
    t = 0
    InstrTrialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    stim.setPos((xpos, 0))
    stim.setImage(stimimg)
    answerprompt.setText('Press %s' % corrResp)
    demoinput = event.BuilderKeyResponse()
    thisExp.addData('img', stimimg)
    # keep track of which components have finished
    InstrTrialComponents = [Fixation, stim, answerprompt, demoinput]
    for thisComponent in InstrTrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "InstrTrial"-------
    while continueRoutine:
        # get current time
        t = InstrTrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if t >= 0.0 and Fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            Fixation.tStart = t
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.setAutoDraw(True)
        
        # *stim* updates
        if t >= 0.0 and stim.status == NOT_STARTED:
            # keep track of start time/frame for later
            stim.tStart = t
            stim.frameNStart = frameN  # exact frame index
            stim.setAutoDraw(True)
        
        # *answerprompt* updates
        if t >= 0.0 and answerprompt.status == NOT_STARTED:
            # keep track of start time/frame for later
            answerprompt.tStart = t
            answerprompt.frameNStart = frameN  # exact frame index
            answerprompt.setAutoDraw(True)
        
        # *demoinput* updates
        if t >= 0.0 and demoinput.status == NOT_STARTED:
            # keep track of start time/frame for later
            demoinput.tStart = t
            demoinput.frameNStart = frameN  # exact frame index
            demoinput.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(demoinput.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if demoinput.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '0'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                demoinput.keys = theseKeys[-1]  # just the last key pressed
                demoinput.rt = demoinput.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstrTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "InstrTrial"-------
    for thisComponent in InstrTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if demoinput.keys in ['', [], None]:  # No response was made
        demoinput.keys=None
    demo1trials.addData('demoinput.keys',demoinput.keys)
    if demoinput.keys != None:  # we had a response
        demo1trials.addData('demoinput.rt', demoinput.rt)
    
    # the Routine "InstrTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'demo1trials'


# ------Prepare to start Routine "Instr4"-------
t = 0
Instr4Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Instr4Components = [text]
for thisComponent in Instr4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instr4"-------
while continueRoutine:
    # get current time
    t = Instr4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    if text.status == STARTED and bool(event.getKeys('space')):
        text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr4"-------
for thisComponent in Instr4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instr4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instr3"-------
t = 0
Instr3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Instr3Components = [Instr3Text]
for thisComponent in Instr3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instr3"-------
while continueRoutine:
    # get current time
    t = Instr3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instr3Text* updates
    if t >= 0.0 and Instr3Text.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instr3Text.tStart = t
        Instr3Text.frameNStart = frameN  # exact frame index
        Instr3Text.setAutoDraw(True)
    if Instr3Text.status == STARTED and bool(event.getKeys('space')):
        Instr3Text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr3"-------
for thisComponent in Instr3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instr3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
demo2trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('demo.xls', selection='2,3'),
    seed=None, name='demo2trials')
thisExp.addLoop(demo2trials)  # add the loop to the experiment
thisDemo2trial = demo2trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisDemo2trial.rgb)
if thisDemo2trial != None:
    for paramName in thisDemo2trial.keys():
        exec(paramName + '= thisDemo2trial.' + paramName)

for thisDemo2trial in demo2trials:
    currentLoop = demo2trials
    # abbreviate parameter names if possible (e.g. rgb = thisDemo2trial.rgb)
    if thisDemo2trial != None:
        for paramName in thisDemo2trial.keys():
            exec(paramName + '= thisDemo2trial.' + paramName)
    
    # ------Prepare to start Routine "setimg"-------
    t = 0
    setimgClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    if (xpos == -.25 and corrResp == 1) or (xpos == .25 and corrResp == 0):
        stimimg=congr
    elif (xpos == -.25 and corrResp == 0) or (xpos == .25 and corrResp == 1):
        stimimg=incongr
    # keep track of which components have finished
    setimgComponents = []
    for thisComponent in setimgComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "setimg"-------
    while continueRoutine:
        # get current time
        t = setimgClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in setimgComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "setimg"-------
    for thisComponent in setimgComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "setimg" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "InstrTrial"-------
    t = 0
    InstrTrialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    stim.setPos((xpos, 0))
    stim.setImage(stimimg)
    answerprompt.setText('Press %s' % corrResp)
    demoinput = event.BuilderKeyResponse()
    thisExp.addData('img', stimimg)
    # keep track of which components have finished
    InstrTrialComponents = [Fixation, stim, answerprompt, demoinput]
    for thisComponent in InstrTrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "InstrTrial"-------
    while continueRoutine:
        # get current time
        t = InstrTrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Fixation* updates
        if t >= 0.0 and Fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            Fixation.tStart = t
            Fixation.frameNStart = frameN  # exact frame index
            Fixation.setAutoDraw(True)
        
        # *stim* updates
        if t >= 0.0 and stim.status == NOT_STARTED:
            # keep track of start time/frame for later
            stim.tStart = t
            stim.frameNStart = frameN  # exact frame index
            stim.setAutoDraw(True)
        
        # *answerprompt* updates
        if t >= 0.0 and answerprompt.status == NOT_STARTED:
            # keep track of start time/frame for later
            answerprompt.tStart = t
            answerprompt.frameNStart = frameN  # exact frame index
            answerprompt.setAutoDraw(True)
        
        # *demoinput* updates
        if t >= 0.0 and demoinput.status == NOT_STARTED:
            # keep track of start time/frame for later
            demoinput.tStart = t
            demoinput.frameNStart = frameN  # exact frame index
            demoinput.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(demoinput.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if demoinput.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '0'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                demoinput.keys = theseKeys[-1]  # just the last key pressed
                demoinput.rt = demoinput.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstrTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "InstrTrial"-------
    for thisComponent in InstrTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if demoinput.keys in ['', [], None]:  # No response was made
        demoinput.keys=None
    demo2trials.addData('demoinput.keys',demoinput.keys)
    if demoinput.keys != None:  # we had a response
        demo2trials.addData('demoinput.rt', demoinput.rt)
    
    # the Routine "InstrTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'demo2trials'


# set up handler to look after randomisation of conditions etc
Practicing = data.TrialHandler(nReps=5, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Practicing')
thisExp.addLoop(Practicing)  # add the loop to the experiment
thisPracticing = Practicing.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticing.rgb)
if thisPracticing != None:
    for paramName in thisPracticing.keys():
        exec(paramName + '= thisPracticing.' + paramName)

for thisPracticing in Practicing:
    currentLoop = Practicing
    # abbreviate parameter names if possible (e.g. rgb = thisPracticing.rgb)
    if thisPracticing != None:
        for paramName in thisPracticing.keys():
            exec(paramName + '= thisPracticing.' + paramName)
    
    # ------Prepare to start Routine "PractInstr"-------
    t = 0
    PractInstrClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    numcorrect=0
    # keep track of which components have finished
    PractInstrComponents = [practiceinstr]
    for thisComponent in PractInstrComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "PractInstr"-------
    while continueRoutine:
        # get current time
        t = PractInstrClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practiceinstr* updates
        if t >= 0.0 and practiceinstr.status == NOT_STARTED:
            # keep track of start time/frame for later
            practiceinstr.tStart = t
            practiceinstr.frameNStart = frameN  # exact frame index
            practiceinstr.setAutoDraw(True)
        if practiceinstr.status == STARTED and bool(event.getKeys('space')):
            practiceinstr.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PractInstrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PractInstr"-------
    for thisComponent in PractInstrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "PractInstr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    PracticeTrials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('demo.xls'),
        seed=None, name='PracticeTrials')
    thisExp.addLoop(PracticeTrials)  # add the loop to the experiment
    thisPracticeTrial = PracticeTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
    if thisPracticeTrial != None:
        for paramName in thisPracticeTrial.keys():
            exec(paramName + '= thisPracticeTrial.' + paramName)
    
    for thisPracticeTrial in PracticeTrials:
        currentLoop = PracticeTrials
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
        if thisPracticeTrial != None:
            for paramName in thisPracticeTrial.keys():
                exec(paramName + '= thisPracticeTrial.' + paramName)
        
        # ------Prepare to start Routine "setimg"-------
        t = 0
        setimgClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        if (xpos == -.25 and corrResp == 1) or (xpos == .25 and corrResp == 0):
            stimimg=congr
        elif (xpos == -.25 and corrResp == 0) or (xpos == .25 and corrResp == 1):
            stimimg=incongr
        # keep track of which components have finished
        setimgComponents = []
        for thisComponent in setimgComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "setimg"-------
        while continueRoutine:
            # get current time
            t = setimgClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in setimgComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "setimg"-------
        for thisComponent in setimgComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "setimg" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "spatialtrial"-------
        t = 0
        spatialtrialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.250000)
        # update component parameters for each repeat
        stimulus.setPos((xpos,0))
        stimulus.setImage(stimimg)
        key_resp_2 = event.BuilderKeyResponse()
        thisExp.addData('img', stimimg)
        # keep track of which components have finished
        spatialtrialComponents = [Fixation2, stimulus, key_resp_2]
        for thisComponent in spatialtrialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "spatialtrial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = spatialtrialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fixation2* updates
            if t >= 0.0 and Fixation2.status == NOT_STARTED:
                # keep track of start time/frame for later
                Fixation2.tStart = t
                Fixation2.frameNStart = frameN  # exact frame index
                Fixation2.setAutoDraw(True)
            frameRemains = 0.0 + 1.25- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Fixation2.status == STARTED and t >= frameRemains:
                Fixation2.setAutoDraw(False)
            
            # *stimulus* updates
            if t >= .5 and stimulus.status == NOT_STARTED:
                # keep track of start time/frame for later
                stimulus.tStart = t
                stimulus.frameNStart = frameN  # exact frame index
                stimulus.setAutoDraw(True)
            frameRemains = .5 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
            if stimulus.status == STARTED and t >= frameRemains:
                stimulus.setAutoDraw(False)
            
            # *key_resp_2* updates
            if t >= .5 and key_resp_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_2.tStart = t
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = .5 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
            if key_resp_2.status == STARTED and t >= frameRemains:
                key_resp_2.status = STOPPED
            if key_resp_2.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '0'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if key_resp_2.keys == []:  # then this was the first keypress
                        key_resp_2.keys = theseKeys[0]  # just the first key pressed
                        key_resp_2.rt = key_resp_2.clock.getTime()
                        # was this 'correct'?
                        if (key_resp_2.keys == str(corrResp)) or (key_resp_2.keys == corrResp):
                            key_resp_2.corr = 1
                        else:
                            key_resp_2.corr = 0
                        # a response ends the routine
                        continueRoutine = False
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in spatialtrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "spatialtrial"-------
        for thisComponent in spatialtrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys=None
            # was no response the correct answer?!
            if str(corrResp).lower() == 'none':
               key_resp_2.corr = 1  # correct non-response
            else:
               key_resp_2.corr = 0  # failed to respond (incorrectly)
        # store data for PracticeTrials (TrialHandler)
        PracticeTrials.addData('key_resp_2.keys',key_resp_2.keys)
        PracticeTrials.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            PracticeTrials.addData('key_resp_2.rt', key_resp_2.rt)
        
        
        # ------Prepare to start Routine "Practicecounter"-------
        t = 0
        PracticecounterClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        numcorrect+=key_resp_2.corr
        # keep track of which components have finished
        PracticecounterComponents = []
        for thisComponent in PracticecounterComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Practicecounter"-------
        while continueRoutine:
            # get current time
            t = PracticecounterClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticecounterComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Practicecounter"-------
        for thisComponent in PracticecounterComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "Practicecounter" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'PracticeTrials'
    
    
    # ------Prepare to start Routine "breaklooproutine"-------
    t = 0
    breaklooproutineClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    if numcorrect >=7:
        Practicing.finished=True
        feedbackmsg=''
    else:
        feedbackmsg='Let\'s try again'
    # keep track of which components have finished
    breaklooproutineComponents = []
    for thisComponent in breaklooproutineComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "breaklooproutine"-------
    while continueRoutine:
        # get current time
        t = breaklooproutineClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in breaklooproutineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "breaklooproutine"-------
    for thisComponent in breaklooproutineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "breaklooproutine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Feedback"-------
    t = 0
    FeedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    feedbacktext.setText('You got %s correct. %s\n\nPress Space to Continue' % (numcorrect, feedbackmsg))
    # keep track of which components have finished
    FeedbackComponents = [feedbacktext]
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Feedback"-------
    while continueRoutine:
        # get current time
        t = FeedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedbacktext* updates
        if t >= 0.0 and feedbacktext.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedbacktext.tStart = t
            feedbacktext.frameNStart = frameN  # exact frame index
            feedbacktext.setAutoDraw(True)
        if feedbacktext.status == STARTED and bool(event.getKeys('space')):
            feedbacktext.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback"-------
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5 repeats of 'Practicing'


# ------Prepare to start Routine "FinanceInstr"-------
t = 0
FinanceInstrClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
FinanceInstrComponents = [text_2]
for thisComponent in FinanceInstrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "FinanceInstr"-------
while continueRoutine:
    # get current time
    t = FinanceInstrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    if text_2.status == STARTED and bool(event.getKeys('space')):
        text_2.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FinanceInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "FinanceInstr"-------
for thisComponent in FinanceInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "FinanceInstr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
FinanceProblems = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Problems.xls'),
    seed=None, name='FinanceProblems')
thisExp.addLoop(FinanceProblems)  # add the loop to the experiment
thisFinanceProblem = FinanceProblems.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFinanceProblem.rgb)
if thisFinanceProblem != None:
    for paramName in thisFinanceProblem.keys():
        exec(paramName + '= thisFinanceProblem.' + paramName)

for thisFinanceProblem in FinanceProblems:
    currentLoop = FinanceProblems
    # abbreviate parameter names if possible (e.g. rgb = thisFinanceProblem.rgb)
    if thisFinanceProblem != None:
        for paramName in thisFinanceProblem.keys():
            exec(paramName + '= thisFinanceProblem.' + paramName)
    
    # ------Prepare to start Routine "setproblem"-------
    t = 0
    setproblemClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    if expInfo['manigroup'] == 'H':
        problemtext=ProblemHigh
    if expInfo['manigroup'] == 'L':
        problemtext=ProblemLow
    # keep track of which components have finished
    setproblemComponents = []
    for thisComponent in setproblemComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "setproblem"-------
    while continueRoutine:
        # get current time
        t = setproblemClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in setproblemComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "setproblem"-------
    for thisComponent in setproblemComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "setproblem" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "FinanceProblem"-------
    t = 0
    FinanceProblemClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_4.setText('%s\n\nPress space when you are done reading' % problemtext)
    # keep track of which components have finished
    FinanceProblemComponents = [text_4]
    for thisComponent in FinanceProblemComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "FinanceProblem"-------
    while continueRoutine:
        # get current time
        t = FinanceProblemClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if t >= 0.0 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t
            text_4.frameNStart = frameN  # exact frame index
            text_4.setAutoDraw(True)
        if text_4.status == STARTED and bool(event.getKeys('space')):
            text_4.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FinanceProblemComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FinanceProblem"-------
    for thisComponent in FinanceProblemComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "FinanceProblem" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "getready"-------
    t = 0
    getreadyClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    getreadyComponents = [text_3]
    for thisComponent in getreadyComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "getready"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = getreadyClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_3.status == STARTED and t >= frameRemains:
            text_3.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in getreadyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "getready"-------
    for thisComponent in getreadyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    SpatialLoop = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('demo.xls'),
        seed=None, name='SpatialLoop')
    thisExp.addLoop(SpatialLoop)  # add the loop to the experiment
    thisSpatialLoop = SpatialLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSpatialLoop.rgb)
    if thisSpatialLoop != None:
        for paramName in thisSpatialLoop.keys():
            exec(paramName + '= thisSpatialLoop.' + paramName)
    
    for thisSpatialLoop in SpatialLoop:
        currentLoop = SpatialLoop
        # abbreviate parameter names if possible (e.g. rgb = thisSpatialLoop.rgb)
        if thisSpatialLoop != None:
            for paramName in thisSpatialLoop.keys():
                exec(paramName + '= thisSpatialLoop.' + paramName)
        
        # ------Prepare to start Routine "setimg"-------
        t = 0
        setimgClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        if (xpos == -.25 and corrResp == 1) or (xpos == .25 and corrResp == 0):
            stimimg=congr
        elif (xpos == -.25 and corrResp == 0) or (xpos == .25 and corrResp == 1):
            stimimg=incongr
        # keep track of which components have finished
        setimgComponents = []
        for thisComponent in setimgComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "setimg"-------
        while continueRoutine:
            # get current time
            t = setimgClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in setimgComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "setimg"-------
        for thisComponent in setimgComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # the Routine "setimg" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "spatialtrial"-------
        t = 0
        spatialtrialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.250000)
        # update component parameters for each repeat
        stimulus.setPos((xpos,0))
        stimulus.setImage(stimimg)
        key_resp_2 = event.BuilderKeyResponse()
        thisExp.addData('img', stimimg)
        # keep track of which components have finished
        spatialtrialComponents = [Fixation2, stimulus, key_resp_2]
        for thisComponent in spatialtrialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "spatialtrial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = spatialtrialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fixation2* updates
            if t >= 0.0 and Fixation2.status == NOT_STARTED:
                # keep track of start time/frame for later
                Fixation2.tStart = t
                Fixation2.frameNStart = frameN  # exact frame index
                Fixation2.setAutoDraw(True)
            frameRemains = 0.0 + 1.25- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Fixation2.status == STARTED and t >= frameRemains:
                Fixation2.setAutoDraw(False)
            
            # *stimulus* updates
            if t >= .5 and stimulus.status == NOT_STARTED:
                # keep track of start time/frame for later
                stimulus.tStart = t
                stimulus.frameNStart = frameN  # exact frame index
                stimulus.setAutoDraw(True)
            frameRemains = .5 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
            if stimulus.status == STARTED and t >= frameRemains:
                stimulus.setAutoDraw(False)
            
            # *key_resp_2* updates
            if t >= .5 and key_resp_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_2.tStart = t
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = .5 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
            if key_resp_2.status == STARTED and t >= frameRemains:
                key_resp_2.status = STOPPED
            if key_resp_2.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '0'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if key_resp_2.keys == []:  # then this was the first keypress
                        key_resp_2.keys = theseKeys[0]  # just the first key pressed
                        key_resp_2.rt = key_resp_2.clock.getTime()
                        # was this 'correct'?
                        if (key_resp_2.keys == str(corrResp)) or (key_resp_2.keys == corrResp):
                            key_resp_2.corr = 1
                        else:
                            key_resp_2.corr = 0
                        # a response ends the routine
                        continueRoutine = False
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in spatialtrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "spatialtrial"-------
        for thisComponent in spatialtrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys=None
            # was no response the correct answer?!
            if str(corrResp).lower() == 'none':
               key_resp_2.corr = 1  # correct non-response
            else:
               key_resp_2.corr = 0  # failed to respond (incorrectly)
        # store data for SpatialLoop (TrialHandler)
        SpatialLoop.addData('key_resp_2.keys',key_resp_2.keys)
        SpatialLoop.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            SpatialLoop.addData('key_resp_2.rt', key_resp_2.rt)
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'SpatialLoop'
    
    
    # ------Prepare to start Routine "Howwouldyousolve"-------
    t = 0
    HowwouldyousolveClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_5.setText('%s\n\nWrite down what you would do and press space to continue' % problemtext)
    # keep track of which components have finished
    HowwouldyousolveComponents = [text_5]
    for thisComponent in HowwouldyousolveComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Howwouldyousolve"-------
    while continueRoutine:
        # get current time
        t = HowwouldyousolveClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if t >= 0.0 and text_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_5.tStart = t
            text_5.frameNStart = frameN  # exact frame index
            text_5.setAutoDraw(True)
        if text_5.status == STARTED and bool(event.getKeys('space')):
            text_5.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in HowwouldyousolveComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Howwouldyousolve"-------
    for thisComponent in HowwouldyousolveComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Howwouldyousolve" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'FinanceProblems'














# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

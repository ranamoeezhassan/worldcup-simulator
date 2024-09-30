'''visualize_simulation.py

CS 152 A
Project 10
12/7/22

This program simulates the knockout stages of the FIFA World Cup 2022 based on their
performance in the FIFA World Cup against their opponents and makes an interactive window
for the user to visualize the world cup simulation. The user can use to control the output 
using a window.

The user should run the file from the command line by calling python3 with the first argument 
being "visualize_simulation.py" or alternatively, press the run button in VS Code. There are no other
arguments required.

The user should expect to see a tkinter window with two buttons: “Open Window” and “Simulate”. 
The “Open Window” button opens up the zelle graphics window with empty boxes. “The Simulate” 
button simulates one round of fixtures and fills in the empty boxes.'''

import physics_objects as pho #importing modules
import graphicsPlus as gr
import world_cup_simulate as wcs
import pandas as pd
from tkinter import *
from tkinter.ttk import *


count = 0 #initializing global variables
df_historical_data = pd.read_csv('clean_fifa_worldcup_matches.csv')
df_fixture= pd.read_csv('clean_fifa_worldcup_fixture.csv')
df_fixture_group_48 = df_fixture[:48]
df_fixture_knockout = df_fixture[48:56]
df_fixture_quarter = df_fixture[56:60]
df_fixture_semi = df_fixture[60:62]
df_fixture_final = df_fixture[62:]
# knockout_messages = [] #using global variables
# quarter_messages = []
# semi_messages = []
# final_message =[]
# final_winner =[]
    
def buildObstacles(win):
    '''This is a function that builds the blocks that have to be drawn on the zelle graphics window'''
    block = pho.Block( win, x0 = 6, y0 = 5, width= 8 , height= 2.5) #creating new blocks 
    block.setPosition(2.5, 2.5)
    block2 = pho.Block( win, x0 = 6, y0 = 7.5, width= 8 , height= 2.5) #creating new blocks 
    block2.setPosition(2.5, 7.5)
    block3 = pho.Block( win, x0 = 6, y0 = 15, width= 8 , height= 2.5) #creating new blocks 
    block3.setPosition(2.5, 12.5)
    block4 = pho.Block( win, x0 = 6, y0 = 20, width= 8 , height= 2.5) #creating new blocks 
    block4.setPosition(2.5, 17.5)
    block5 = pho.Block( win, x0 = 6, y0 = 5, width= 8, height= 2.5) #creating new blocks 
    block5.setPosition(2.5, 22.5)
    block6 = pho.Block( win, x0 = 6, y0 = 10, width= 8 , height= 2.5) #creating new blocks 
    block6.setPosition(2.5, 27.5)
    block7 = pho.Block( win, x0 = 6, y0 = 15, width= 8 , height= 2.5) #creating new blocks 
    block7.setPosition(2.5, 32.5)
    block8 = pho.Block( win, x0 = 6, y0 = 20, width= 8 , height= 2.5) #creating new blocks 
    block8.setPosition(2.5, 37.5)
    block9 = pho.Block( win, x0 = 6, y0 = 5, width= 8 , height= 2.5) #creating new blocks 
    block9.setPosition(12.5, 5)
    block10 = pho.Block( win, x0 = 6, y0 = 15, width= 8 , height= 2.5) #creating new blocks 
    block10.setPosition(12.5, 15)
    block11 = pho.Block( win, x0 = 6, y0 = 20, width= 8 , height= 2.5) #creating new blocks 
    block11.setPosition(12.5, 25)
    block12 = pho.Block( win, x0 = 6, y0 = 5, width= 8 , height= 2.5) #creating new blocks 
    block12.setPosition(12.5, 35)
    block13 = pho.Block( win, x0 = 6, y0 = 5, width= 8 , height= 2.5) #creating new blocks 
    block13.setPosition(22.5, 10)
    block14 = pho.Block( win, x0 = 6, y0 = 5, width= 8 , height= 2.5) #creating new blocks 
    block14.setPosition(22.5, 30)
    block15 = pho.Block( win, x0 = 6, y0 = 5, width= 8 , height= 2.5) #creating new blocks 
    block15.setPosition(32.5, 20)
    block16 = pho.Block( win, x0 = 6, y0 = 5, width= 8 , height= 2.5) #creating new blocks 
    block16.setPosition(77.5, 2.5)
    block17 = pho.Block( win, x0 = 6, y0 = 7.5, width= 8 , height= 2.5) #creating new blocks 
    block17.setPosition(77.5, 7.5)
    block18 = pho.Block( win, x0 = 6, y0 = 15, width= 8 , height= 2.5) #creating new blocks 
    block18.setPosition(77.5, 12.5)
    block19 = pho.Block( win, x0 = 6, y0 = 20, width= 8 , height= 2.5) #creating new blocks 
    block19.setPosition(77.5, 17.5)
    block20 = pho.Block( win, x0 = 6, y0 = 5, width= 8, height= 2.5) #creating new blocks 
    block20.setPosition(77.5, 22.5)
    block21 = pho.Block( win, x0 = 6, y0 = 10, width= 8 , height= 2.5) #creating new blocks 
    block21.setPosition(77.5, 27.5)
    block22 = pho.Block( win, x0 = 6, y0 = 15, width= 8 , height= 2.5) #creating new blocks 
    block22.setPosition(77.5, 32.5)
    block23 = pho.Block( win, x0 = 6, y0 = 20, width= 8 , height= 2.5) #creating new blocks 
    block23.setPosition(77.5, 37.5)
    block24 = pho.Block( win, x0 = 6, y0 = 5, width= 8 , height= 2.5) #creating new blocks 
    block24.setPosition(68.5, 5)
    block25 = pho.Block( win, x0 = 6, y0 = 15, width= 8 , height= 2.5) #creating new blocks 
    block25.setPosition(68.5, 15)
    block26 = pho.Block( win, x0 = 6, y0 = 20, width= 8 , height= 2.5) #creating new blocks 
    block26.setPosition(68.5, 25)
    block27 = pho.Block( win, x0 = 6, y0 = 5, width= 8 , height= 2.5) #creating new blocks 
    block27.setPosition(68.5, 35)
    block28 = pho.Block( win, x0 = 6, y0 = 5, width= 8 , height= 2.5) #creating new blocks 
    block28.setPosition(58.5, 10)
    block29 = pho.Block( win, x0 = 6, y0 = 5, width= 8 , height= 2.5) #creating new blocks 
    block29.setPosition(58.5, 30)
    block30 = pho.Block( win, x0 = 6, y0 = 5, width= 8 , height= 2.5) #creating new blocks 
    block30.setPosition(52.5, 20)
    #block31 = pho.Block( win, x0 = 6, y0 = 5, width= 15 , height= 7.5) #creating new blocks 
    #block31.setPosition(42.5,30 )
    
    obstacles = [ block, block2, block3, block4, block5, block6, block7, block8, block9, block10, block11, block12, block13, block14,
    block15, block16, block17,block18, block19, block20, block23, block22, block21, block24, block25, block26, block27, block28, block29,
    block30] # Create all of the obstacles in the scene and put them in a list
    return obstacles #Return the list of Things

def open_window():
    '''This is the function that creates and opens the zelle graphics window so that it can be used as
    as command for tkinter button'''
    global win
    win = gr.GraphWin("World Cup Simulator Version 4", 800, 400, False) # create a GraphWin
    shapes = buildObstacles(win) # call buildObstacles, storing the return list in a  variable
    for each in shapes:# loop over the shapes list and have each Thing call its draw method
        each.draw()

def simulate():
    '''This is the function that draws the teams' name on the zelle graphics window so that it can be used as
    as command for tkinter button'''
    global count #using the global count variable
    global knockout_messages
    global quarter_messages
    global semi_messages
    global final_message
    global final_winner
    count+=1
    if count ==1:
        for each in knockout_messages:
            each.draw(win)
    if count == 2:
        for each in quarter_messages:
            each.draw(win)
    if count == 3:
        for each in semi_messages:
            each.draw(win)
    if count == 4:
        for each in final_message:
            each.draw(win)
    if count==5:
        for each in final_winner:
            each.draw(win)
        count = 0

def reset_window():
    '''This is the function that undraws all the the teams' name on the zelle graphics window so that it 
    can be used as as command for tkinter button'''
    global count
    runSim()
    count = 0
    for each in knockout_messages:
            each.undraw()
    for each in quarter_messages:
            each.undraw()
    for each in semi_messages:
            each.undraw()
    for each in final_message:
            each.undraw()
    final_winner[0].undraw()

def runSim():
    '''This is a function that combines all the functions and runs the simulation for the tournament'''
    global knockout_messages #using global variables
    global quarter_messages
    global semi_messages
    global final_message
    global final_winner
    Simulation= wcs.Simulation(df_historical_data, df_fixture) #calling the Simulation class from the world_cup_simulate.py file
    df_fixture_knockout.loc[48, 'home'] = "Netherlands" #updating the fixture list to the latest fixtures of this year's world cup
    df_fixture_knockout.loc[48, 'away'] = "United States"
    df_fixture_knockout.loc[49, 'home'] = "Argentina"
    df_fixture_knockout.loc[49, 'away'] = "Australia"
    df_fixture_knockout.loc[50, 'home'] = "France"
    df_fixture_knockout.loc[50,'away'] = "Poland"
    df_fixture_knockout.loc[51, 'home'] = "England"
    df_fixture_knockout.loc[51, 'away'] = "Ecuador"
    df_fixture_knockout.loc[52, 'home'] = "Japan"
    df_fixture_knockout.loc[52, 'away'] = "Croatia"
    df_fixture_knockout.loc[53, 'home'] = "Brazil"
    df_fixture_knockout.loc[53, 'away'] = "South Korea"
    df_fixture_knockout.loc[54, 'home'] = "Morocco"
    df_fixture_knockout.loc[54, 'away'] = "Spain"
    df_fixture_knockout.loc[55, 'home'] = "Portugal"
    df_fixture_knockout.loc[55, 'away'] = "Switzerland"
    
    a= Simulation.get_winner(df_fixture_knockout) #getting the winners from the round of 16 phase
    Simulation.update_table(a, df_fixture_quarter)
    b = Simulation.get_winner(df_fixture_quarter) #getting the winners from the quarter final phase
    Simulation.update_table(b, df_fixture_semi)
    c = Simulation.get_winner(df_fixture_semi) #getting the winners from the semi final phase
    Simulation.update_table(c, df_fixture_final)
    d= Simulation.get_winner(df_fixture_final) #getting the winner of the final

    message = gr.Text(gr.Point(32,25), a['home'][48]) #creating text boxes which can be used with GraphWin
    message2 = gr.Text(gr.Point(25,75), a['away'][48])
    message3 = gr.Text(gr.Point(25,125), a['home'][49])
    message4 = gr.Text(gr.Point(25,175), a['away'][49])
    message5 = gr.Text(gr.Point(25,225), a['home'][52])
    message6 = gr.Text(gr.Point(25,275), a['away'][52])
    message7 = gr.Text(gr.Point(25,325), a['home'][53])
    message8 = gr.Text(gr.Point(25,375), a['away'][53])
    message9 = gr.Text(gr.Point(775,25), a['home'][51])
    message10 = gr.Text(gr.Point(775,75), a['away'][51])
    message11 = gr.Text(gr.Point(775,125), a['home'][50])
    message12 = gr.Text(gr.Point(775,175), a['away'][50])
    message13 = gr.Text(gr.Point(775,225), a['home'][54])
    message14 = gr.Text(gr.Point(775,275), a['away'][54])
    message15 = gr.Text(gr.Point(775,325), a['home'][55])
    message16 = gr.Text(gr.Point(770,375), a['away'][55])
    message18 = gr.Text(gr.Point(125,50), a['winner'][48])
    message19 = gr.Text(gr.Point(125,150), a['winner'][49])
    message20 = gr.Text(gr.Point(125,250), a['winner'][52])
    message32 = gr.Text(gr.Point(125,350), a['winner'][53])
    message21 = gr.Text(gr.Point(225,100), b['winner'][57])
    message22 = gr.Text(gr.Point(225,300), b['winner'][56])
    message23 = gr.Text(gr.Point(325,200), c['winner'][60])
    message24 = gr.Text(gr.Point(685,50), a['winner'][51])
    message25 = gr.Text(gr.Point(685,150), a['winner'][50])
    message26 = gr.Text(gr.Point(685,250), a['winner'][54])
    message27 = gr.Text(gr.Point(685,350), a['winner'][55])
    message28 = gr.Text(gr.Point(585,100), b['winner'][59])
    message29 = gr.Text(gr.Point(585,300), b['winner'][58])
    message30 = gr.Text(gr.Point(525,200), c['winner'][61])
    message31 = gr.Text(gr.Point(425, 100), (d['winner'][63]).upper())
    message33 = gr.Text(gr.Point(425, 120), "WIN THE WORLD CUP")

    #storing the messages in the following lists
    knockout_messages = [message, message2, message3, message4, message5, message6, message7, 
    message8, message9, message10, message11, message12, message13, message14, message15, 
    message16]
    quarter_messages= [message18, message19, message20, message32 ,message24, message25, 
    message26, message27]
    semi_messages = [message21, message22, message28, message29]
    final_message = [message30, message23]
    final_winner = [message31, message33]

def main():
    '''This is the main function that calls the runSim function and creates the tkinter window'''
    runSim() #calling runSim function
    window = Tk() #creating tkinter window
    data = StringVar()
    data.set("Welcome to the World Cup Predictor")
    message_label = Label(window, textvariable=data)
    message_label.grid(row=0, column=0)
    data2 = StringVar()
    data2.set("Please press the open window button to open the window and simulate button to simulate a round")
    message_label2 = Label(window, textvariable=data2)
    message_label2.grid(row=1, column=0)
    button = Button(window, text="Simulate", command=simulate) #creating a button that starts the simulation
    button.grid(row=2, column=0)
    open_window_button = Button(window, text= "Open Window", command = open_window) #creating a button that opens the zelle graphics window
    open_window_button.grid(row=3, column=0)
    window.mainloop()


if __name__ == "__main__":
    main()
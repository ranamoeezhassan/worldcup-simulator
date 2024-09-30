'''extension1.py

CS 152 A
Project 10
12/7/22

This program simulates the knockout stages of the FIFA World Cup 2022 based on their
performance in the FIFA World Cup against their opponents and makes an interactive window
for the user to visualize the world cup simulation. The user can use to control the output 
using a window.

The user should run the file from the command line by calling python3 with the first argument 
being "extension1.py" or alternatively, press the run button in VS Code. There are no other
arguments required.

The user should expect to see a tkinter window with two buttons: “Open Window” and “Simulate”. 
The “Open Window” button opens up the zelle graphics window with empty boxes. “The Simulate” 
button simulates one round of fixtures and fills in the empty boxes.

The original visualize_simulation.py file was modified in order to run the world cup
simulation was run 1000 times using the world_cup_simulate.py module and the winners
were stored in a dictionary and then using matplotlib, the winners were automatically
as a bar graph of team name against the times that team won the world cup.'''

import world_cup_simulate as wcs
import pandas as pd
import matplotlib.pyplot as plt

def runSim():   
    df_historical_data = pd.read_csv('clean_fifa_worldcup_matches.csv')
    df_fixture= pd.read_csv('clean_fifa_worldcup_fixture.csv')
    df_fixture_group_48 = df_fixture[:48]
    df_fixture_knockout = df_fixture[48:56]
    df_fixture_quarter = df_fixture[56:60]
    df_fixture_semi = df_fixture[60:62]
    df_fixture_final = df_fixture[62:]
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
    
    Simulation.get_winner(df_fixture_knockout) #getting the winners from the round of 16 phase
    Simulation.update_table(df_fixture_knockout, df_fixture_quarter)
    Simulation.get_winner(df_fixture_quarter) #getting the winners from the quarter final phase
    Simulation.update_table(df_fixture_quarter, df_fixture_semi)
    Simulation.get_winner(df_fixture_semi) #getting the winners from the semi final phase
    Simulation.update_table(df_fixture_semi, df_fixture_final)
    Simulation.get_winner(df_fixture_final) #getting the winner of the final
    return Simulation.get_winner(df_fixture_final).loc[63, 'winner']

dict_winners= dict()
winner = []
def simulateThousand():
    for i in range(1000):
        winner = runSim()
        if winner not in dict_winners:
            dict_winners[winner] = 1
        elif winner in dict_winners:
            dict_winners[winner] +=1
    return dict_winners

def main():
    winners = simulateThousand()
    x=[]
    y=[]
    for key, value in winners.items():
        x.append(key)
        y.append(value)
    plt.bar(x,y,width = 0.5) #plotting the with x and y coorindates as the list
    plt.title("World Cup Predictor Automated Simulation")
    plt.xlabel("Team Name") #labelling the axes
    plt.ylabel("Times Won")
    plt.show() #showing the axes

if __name__ == "__main__":
    main()
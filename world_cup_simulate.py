'''world_cup_simulate.py

Rana Moeez Hassan
CS 152 A
Project 10
12/7/22

This program simulates the knockout stages of the FIFA World Cup 2022 based on their
performance in the FIFA World Cup against their opponents. 

The program outputs a test function that is not useful for the user so there is no point
to running this file. This file was developed with the intention of this being a module
that we can import'''

import pandas as pd
from scipy.stats import poisson
import random

class Simulation(object):
    '''This is a class that contains the methods to simulate the FIFA World Cup. The class contains the following 
    methods: 
    1) Poisson Calculator
    2) Probablity Calculator
    3) Get Winner
    4) Update Table'''

    def __init__(self, df_historical_data, df_fixture):
        '''The initializer for the Simulation class'''
        self.df_historical_data= df_historical_data
        self.df_fixture = df_fixture
        self.df_home = self.df_historical_data[['HomeTeam', 'HomeGoals', 'AwayGoals']]
        self.df_away = self.df_historical_data[['AwayTeam', 'HomeGoals', 'AwayGoals']]
        self.df_home = self.df_home.rename(columns={'HomeTeam':'Team', 'HomeGoals': 'GoalsScored', 'AwayGoals': 'GoalsConceded'})
        self.df_away = self.df_away.rename(columns={'AwayTeam':'Team', 'HomeGoals': 'GoalsConceded', 'AwayGoals': 'GoalsScored'})
        self.df_team_strength = pd.concat([self.df_home, self.df_away], ignore_index=True).groupby(['Team']).mean()

    def poisson_calculator(self, home, away):
        '''This is a function written by Frank Andrade (https://www.youtube.com/@FrankAndrade5). The original function was
        modified in order to return the probablity of the home team winning and probablity of away team winning using the poisson
        distribution'''
        if home in self.df_team_strength.index and away in self.df_team_strength.index: #checking if home and away team 
        #in the team strength index

            lamb_home = self.df_team_strength.at[home,'GoalsScored'] * self.df_team_strength.at[away,'GoalsConceded']
            lamb_away = self.df_team_strength.at[away,'GoalsScored'] * self.df_team_strength.at[home,'GoalsConceded']
            prob_home, prob_away, prob_draw = 0, 0, 0
            for x in range(0,11): #number of goals home team
                for y in range(0, 11): #number of goals away team
                    p = poisson.pmf(x, lamb_home) * poisson.pmf(y, lamb_away) # goals_scored * goals_conceded
                    if x == y:
                        prob_draw += p #probablity of draw increases if goals scored by home team equals goals scored 
                    #away team
                    elif x > y:
                        prob_home += p #probablity of home team winning increases if goals scored by home team is
                    #greater than goals scored by away team
                    else:
                        prob_away += p #probablity of away team winning increases if goals scored by home team is
                    #lesser than goals scored by away team
            return (prob_home, prob_away)
        else:
            return (0.5, 0.5) #just returns 0.5 probablity for both team if both teams are not in the team strength index

    def probablity_calculator(self, home, away):
        '''This is a function that calculates the probablity of the home(first argument) team winning over the away team. The function 
        takes into account all the previous meetings in the FIFA World Cups and combines it with the probablity calculated by the 
        poisson calculator to give the overall probablity'''
        count= 0 #inititalizing variables that will be used later on
        times_won=0
        df_historical_data= self.df_historical_data
        (prob_home, prob_away)= self.poisson_calculator(home, away) #calculating the probablity of home and away 
#team winning by the poisson distribution

        for i in range(len(df_historical_data)): #checking the opened data file
            homegoals = self.df_historical_data['HomeGoals'][i]
            awaygoals = self.df_historical_data['AwayGoals'][i]
            if home == self.df_historical_data['HomeTeam'][i] and away == df_historical_data['AwayTeam'][i]: #checking if
#home and away team have faced off each other in the previous World Cups 
                if homegoals > awaygoals: 
                    times_won+=1 #counting the number of times home team won
                if homegoals ==awaygoals:
                    count-=1
                count+=1 #counting the total number of times home and away team face off each other
            if home == df_historical_data['AwayTeam'][i] and away == df_historical_data['HomeTeam'][i]: #checking if
#home and away team have faced off each other in the previous World Cups 
                if awaygoals > homegoals:
                    times_won+=1
                if awaygoals == homegoals:
                    count-=1
                count+=1
            if home != df_historical_data["HomeTeam"][i] and away != df_historical_data["AwayTeam"][i]:
                probablity_home_win = prob_home/(prob_home + prob_away) #calculating probablity using poisson distribution
#teams never faced each other in the world cup
        if count != 0:
            probablity_home_win= (prob_home/(prob_home + prob_away) + times_won/count)/2 #if the teams did face each other in
#the world cup, the probablity of home(first argument) team winning is the combined probablities
        return probablity_home_win #returning the probablity of home(first team) winning
    
    def get_winner(self, df_fixture_updated):
        '''This function gets a fixture list and determines the winner of those matchups'''
        for index, row in df_fixture_updated.iterrows():
            home, away = row['home'], row['away']
            prob_win_home = self.probablity_calculator(home, away) #calculating probablity of home
#team winning
            if random.random() <= prob_win_home: #determining the winner using the probablity and random package
                winner = home 
            else:
                winner = away
            
            df_fixture_updated.loc[index, 'winner'] = winner #this updates the fixture list
        return df_fixture_updated #returns the updated fixture list

    def update_table(self, df_fixture_round_1, df_fixture_round_2):
        '''This functions updates the second fixture argument by using the winners from the first fixture argument'''
        for index, row in df_fixture_round_1.iterrows():
            winner = df_fixture_round_1.loc[index, 'winner'] #locating winner from first fixture list
            match = df_fixture_round_1.loc[index, 'score']
            df_fixture_round_2.replace({f'Winners {match}':winner}, inplace=True) 

        df_fixture_round_2['winner'] = '?'
        return df_fixture_round_2 #returning the new fixtures

def test():
    '''This is a test function'''
    df_historical_data = pd.read_csv('clean_fifa_worldcup_matches.csv')
    df_fixture= pd.read_csv('clean_fifa_worldcup_fixture.csv')
    df_fixture_group_48 = df_fixture[:48]
    df_fixture_knockout = df_fixture[48:56]
    df_fixture_quarter = df_fixture[56:60]
    df_fixture_semi = df_fixture[60:62]
    df_fixture_final = df_fixture[62:]

    a = Simulation(df_historical_data, df_fixture)
    print(df_fixture)
    #PRINT(df_historical_data)
    print(a.probablity_calculator('England', 'Argentina'))
    print(a.probablity_calculator('England', 'Senegal'))
    print(a.probablity_calculator('England', 'Argentina'))
    print(a.probablity_calculator('England', 'Brazil'))
    print(a.probablity_calculator('Senegal', 'Spain'))
    print(a.probablity_calculator('Argentina', 'Brazil'))
    print(a.probablity_calculator('Senegal', 'Brazil'))
    print(a.probablity_calculator('France', 'Poland'))
    print(a.probablity_calculator('England', 'Ecuador'))
    df_fixture_knockout.loc[48, 'home'] = "Netherlands"
    df_fixture_knockout.loc[48, 'away'] = "United States"
    df_fixture_knockout.loc[49, 'home'] = "Argentina"
    df_fixture_knockout.loc[49, 'away'] = "Australia"
    df_fixture_knockout.loc[50, 'home'] = "France"
    df_fixture_knockout.loc[50,'away'] = "Poland"
    df_fixture_knockout.loc[51, 'home'] = "England"
    df_fixture_knockout.loc[51, 'away'] = "Senegal"
    df_fixture_knockout.loc[52, 'home'] = "Japan"
    df_fixture_knockout.loc[52, 'away'] = "Croatia"
    df_fixture_knockout.loc[53, 'home'] = "Brazil"
    df_fixture_knockout.loc[53, 'away'] = "South Korea"
    df_fixture_knockout.loc[54, 'home'] = "Morocco"
    df_fixture_knockout.loc[54, 'away'] = "Spain"
    df_fixture_knockout.loc[55, 'home'] = "Portugal"
    df_fixture_knockout.loc[55, 'away'] = "Switzerland"
    print(a.get_winner(df_fixture_knockout))
    a.update_table(df_fixture_knockout,df_fixture_quarter)
    print(a.get_winner(df_fixture_quarter))
    a.update_table(df_fixture_quarter,df_fixture_semi)
    print(a.get_winner(df_fixture_semi))
    
if __name__ == '__main__':
    test()
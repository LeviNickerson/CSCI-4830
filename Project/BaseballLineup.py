# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 17:04:31 2018

@author: Levi Nickerson
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
sns.set()

dk = pd.read_csv('D:\School\Summer Semester\CSCI 4830 Special Topics Information Visualization\Project\DKSalaries_8_11_18.csv')
bat = pd.read_csv('D:\School\Summer Semester\CSCI 4830 Special Topics Information Visualization\Project\mlb-player-stats-Batters_8_11_18.csv')
pit = pd.read_csv('D:\School\Summer Semester\CSCI 4830 Special Topics Information Visualization\Project\mlb-player-stats-P_8_11_18.csv' )


def plot(xnew, ynew, nnew):
    fig, ax = plt.subplots()    
    count = 0
    markers = ["o","s","*","v","+","p","+","X","D",",","^"]
    j = 0
    for i in range(len(xnew)):
        if (count == 6):
            j = 1
        if (count == 12):
            j = 2
        if (count == 18):
            j = 3
        if (count == 24):
            j = 4
        if (count == 30):
            j = 5
        if (count == 36):
            j = 6
        if (count == 42):
            j = 7
        if (count == 48):
            j = 8
        if (count == 54):
            j = 9
            
        if (ynew[i] > np.percentile(ynew, 75)):    
            plt.scatter(xnew[i], ynew[i], marker = markers[j], label = nnew[i]);
            count = count + 1

    plt.legend(loc='upper left', prop={'size':10}, bbox_to_anchor=(1,1))
    plt.xlabel("Salary")
    plt.ylabel("Effectiveness Value")

    return 

# Get Effectivenes Value 
data = [] 
for i in range(len(dk)):
    for j in range(len(bat)):
        if (dk.iloc[i,2] == bat.iloc[j,0]):
            single = round(((bat.iloc[j,6]-bat.iloc[j,7]-bat.iloc[j,8]-bat.iloc[j,9])/bat.iloc[j,4])*3, 3)
            double = round((bat.iloc[j,7]/bat.iloc[j,4])*5, 3)
            triple = round((bat.iloc[j,8]/bat.iloc[j,4])*8, 3)
            homerun = round((bat.iloc[j,9]/bat.iloc[j,4])*10, 3)
            rbi = round((bat.iloc[j,10]/bat.iloc[j,4])*2, 3)
            run = round((bat.iloc[j,5]/bat.iloc[j,4])*2, 3)
            bob = round((bat.iloc[j,13]/bat.iloc[j,4])*2, 3)
            hbp = round((bat.iloc[j,17]/bat.iloc[j,4])*2, 3)
            sb = round((bat.iloc[j,11]/bat.iloc[j,4])*5, 3)
            x = single + double + triple + homerun + rbi + run + bob + hbp + sb
            data.append([dk.iloc[i,2], dk.iloc[i,5], bat.iloc[j,2], x, bat.iloc[j,4], bat.iloc[j,1]])
    
datap = []  
for i in range(len(dk)):
    for j in range(len(pit)):
        if (dk.iloc[i,2] == pit.iloc[j,0] and pit.iloc[j,3] > 0 ):
            ip = round((pit.iloc[j,6]/pit.iloc[j,3])*2.25, 3)
            strikeouts = round((pit.iloc[j,9]/pit.iloc[j,3])*2, 3)
            wins = round((pit.iloc[j,12]/pit.iloc[j,3])*4, 3)
            er = round((pit.iloc[j,8]/pit.iloc[j,3])*(-2), 3)
            hits = round((pit.iloc[j,7]/pit.iloc[j,3])*(-.6), 3)
            bb = round((pit.iloc[j,10]/pit.iloc[j,3])*(-.6), 3)
            CG = round((pit.iloc[j,4]/pit.iloc[j,3])*2.5, 3)
            x = ip + strikeouts + wins + er + hits + bb + CG
            datap.append([dk.iloc[i,2], dk.iloc[i,5], x, pit.iloc[j,3], pit.iloc[j,1]])
        
        
        


ans = ""
while ( ans != "continue"):
    xnew = []
    ynew = []
    nnew = [] 

    
    ans = input("What position would you like to look at? (C, 1B, 2B, SS, 3B, OF, P, or continue) ")
    if (ans == "C"):
        for l in range(len(data)):
                if (data[l][2] == 'C' and data[l][4] > 50):
                    xnew.append(data[l][1])
                    ynew.append(data[l][3])
                    nnew.append(data[l][0] + "-" + data[l][5])
                    
        
        plot(xnew,ynew,nnew);
        plt.pause(0.05)
        
    if (ans == "1B"):
        for l in range(len(data)):
                if (data[l][2] == '1B' and data[l][4] > 50):
                    xnew.append(data[l][1])
                    ynew.append(data[l][3])
                    nnew.append(data[l][0] + "-" + data[l][5])   
                    
        
        
        plot(xnew,ynew,nnew);
        plt.pause(0.05);
  
    if (ans == "2B"):
        for l in range(len(data)):
                if (data[l][2] == '2B' and data[l][4] > 50):
                    xnew.append(data[l][1])
                    ynew.append(data[l][3])
                    nnew.append(data[l][0] + "-" + data[l][5])    
                   
        
        
        plot(xnew,ynew,nnew);
        plt.pause(0.05);   

    if (ans == "SS"):
        for l in range(len(data)):
                if (data[l][2] == 'SS' and data[l][4] > 50):
                    xnew.append(data[l][1])
                    ynew.append(data[l][3])
                    nnew.append(data[l][0] + "-" + data[l][5])   
                   
        
        
        plot(xnew,ynew,nnew);
        plt.pause(0.05);   
    
    if (ans == "3B"):
        for l in range(len(data)):
                if (data[l][2] == '3B' and data[l][4] > 50):
                    xnew.append(data[l][1])
                    ynew.append(data[l][3])
                    nnew.append(data[l][0] + "-" + data[l][5])    
                   
        
        
        plot(xnew,ynew,nnew);
        plt.pause(0.05);
    
    if (ans == "OF"):
        for l in range(len(data)):
                if (data[l][2] == 'OF' and data[l][4] > 50):
                    xnew.append(data[l][1])
                    ynew.append(data[l][3])
                    nnew.append(data[l][0] + "-" + data[l][5])   
                    
        
        
        plot(xnew,ynew,nnew);
        plt.pause(0.05);

    if (ans == "P"):
        for l in range(len(datap)):
                if (datap[l][3] > 5):
                    xnew.append(datap[l][1])
                    ynew.append(datap[l][2])
                    nnew.append(datap[l][0] + "-" + datap[l][4])    
        
        plot(xnew,ynew,nnew);
        plt.pause(0.05);        
        
        
        
        
    plt.show;
    plt.gcf().clear();

def get_max(data, cat):
    empty = []
    if (cat == "Ave"):
        for i in range(len(data)):
            empty.append(data[i][18])
            
        location = empty.index(max(empty))
    
    elif (cat == "Hr"):
        for i in range(len(data)):
            empty.append(data[i][9])
            
        location = empty.index(max(empty))
    
    elif (cat == "OnBase"):
        for i in range(len(data)):
            empty.append(data[i][19])
            
        location = empty.index(max(empty))
    
    elif (cat == "Run"):
        for i in range(len(data)):
            empty.append(data[i][5])
            
        location = empty.index(max(empty))    
            
    return data[location]


ans = ""
while ( ans != "continue"):
    catcher = []
    fb = []
    sb = []
    ss = []
    tb = []
    of = []
    
    ans = input("What kind of Batting Lineup would you like to see? (Ave, Hr, OnBase, Run, or continue) ")
    
    for i in range(len(bat)):
        if (bat.iloc[i,2] == 'C' and bat.iloc[i,4] > 50):
            catcher.append(bat.iloc[i,:])
        elif (bat.iloc[i,2] == '1B' and bat.iloc[i,4] > 50):
            fb.append(bat.iloc[i,:])
        elif (bat.iloc[i,2] == '2B' and bat.iloc[i,4] > 50):
            sb.append(bat.iloc[i,:])
        elif (bat.iloc[i,2] == 'SS' and bat.iloc[i,4] > 50):
            ss.append(bat.iloc[i,:])
        elif (bat.iloc[i,2] == '3B' and bat.iloc[i,4] > 50):
            tb.append(bat.iloc[i,:])
        elif (bat.iloc[i,2] == 'OF' and bat.iloc[i,4] > 50):
            of.append(bat.iloc[i,:])
            
            
    if (ans == "Ave"):
        cave = get_max(catcher, ans)
        fave = get_max(fb, ans)
        save = get_max(sb, ans)
        ssave = get_max(ss, ans)
        tave = get_max(tb, ans)
        oave = get_max(of, ans)
        
        for i in range(len(dk)):
                if (dk.iloc[i,2] == cave[0]):
                    sal = dk.iloc[i,5]
                if (dk.iloc[i,2] == fave[0]):
                    salf = dk.iloc[i,5]
                if (dk.iloc[i,2] == save[0]):
                    sals = dk.iloc[i,5]
                if (dk.iloc[i,2] == ssave[0]):
                    salss = dk.iloc[i,5]
                if (dk.iloc[i,2] == tave[0]):
                    salt = dk.iloc[i,5]
                if (dk.iloc[i,2] == oave[0]):
                    salo = dk.iloc[i,5]
        
        salss = dk.iloc[391,5]    
        print("Average Heavy Lineup")
        print("Catcher: ",cave[0], "Salary: ",sal)
        print("First Base: ",fave[0], "Salary: ",salf)
        print("Second Base: ",save[0], "Salary: ",sals)
        print("Short Stop: ",ssave[0], "Salary: ",salss)
        print("Third Base: ",tave[0], "Salary: ",salt)
        print("Outfield: ",oave[0], "Salary: ",salo)
        

    if (ans == "Hr"):
        cave = get_max(catcher, ans)
        fave = get_max(fb, ans)
        save = get_max(sb, ans)
        ssave = get_max(ss, ans)
        tave = get_max(tb, ans)
        oave = get_max(of, ans)
        
        for i in range(len(dk)):
                if (dk.iloc[i,2] == cave[0]):
                    sal = dk.iloc[i,5]
                if (dk.iloc[i,2] == fave[0]):
                    salf = dk.iloc[i,5]
                if (dk.iloc[i,2] == save[0]):
                    sals = dk.iloc[i,5]
                if (dk.iloc[i,2] == ssave[0]):
                    salss = dk.iloc[i,5]
                if (dk.iloc[i,2] == tave[0]):
                    salt = dk.iloc[i,5]
                if (dk.iloc[i,2] == oave[0]):
                    salo = dk.iloc[i,5]
        
        print("Home Run Heavy Lineup")
        print("Catcher: ",cave[0], "Salary: ",sal)
        print("First Base: ",fave[0], "Salary: ",salf)
        print("Second Base: ",save[0], "Salary: ",sals)
        print("Short Stop: ",ssave[0], "Salary: ",salss)
        print("Third Base: ",tave[0], "Salary: ",salt)
        print("Outfield: ",oave[0], "Salary: ",salo)
        

    if (ans == "OnBase"):
        cave = get_max(catcher, ans)
        fave = get_max(fb, ans)
        save = get_max(sb, ans)
        ssave = get_max(ss, ans)
        tave = get_max(tb, ans)
        oave = get_max(of, ans)

        for i in range(len(dk)):
                if (dk.iloc[i,2] == cave[0]):
                    sal = dk.iloc[i,5]
                if (dk.iloc[i,2] == fave[0]):
                    salf = dk.iloc[i,5]
                if (dk.iloc[i,2] == save[0]):
                    sals = dk.iloc[i,5]
                if (dk.iloc[i,2] == ssave[0]):
                    salss = dk.iloc[i,5]
                if (dk.iloc[i,2] == tave[0]):
                    salt = dk.iloc[i,5]
                if (dk.iloc[i,2] == oave[0]):
                    salo = dk.iloc[i,5]
        
         
        print("On Base Heavy Lineup")         
        print("Catcher: ",cave[0], "Salary: ",sal)
        print("First Base: ",fave[0], "Salary: ",salf)
        print("Second Base: ",save[0], "Salary: ",sals)
        print("Short Stop: ",ssave[0], "Salary: ",salss)
        print("Third Base: ",tave[0], "Salary: ",salt)
        print("Outfield: ",oave[0], "Salary: ",salo)
        
    
    if (ans == "Run"):
        cave = get_max(catcher, ans)
        fave = get_max(fb, ans)
        save = get_max(sb, ans)
        ssave = get_max(ss, ans)
        tave = get_max(tb, ans)
        oave = get_max(of, ans)
        
        for i in range(len(dk)):
                if (dk.iloc[i,2] == cave[0]):
                    sal = dk.iloc[i,5]
                if (dk.iloc[i,2] == fave[0]):
                    salf = dk.iloc[i,5]
                if (dk.iloc[i,2] == save[0]):
                    sals = dk.iloc[i,5]
                if (dk.iloc[i,2] == ssave[0]):
                    salss = dk.iloc[i,5]
                if (dk.iloc[i,2] == tave[0]):
                    salt = dk.iloc[i,5]
                if (dk.iloc[i,2] == oave[0]):
                    salo = dk.iloc[i,5]
        
   
        print("Run Heavy Lineup:")        
        print("Catcher: ",cave[0], "Salary: ",sal)
        print("First Base: ",fave[0], "Salary: ",salf)
        print("Second Base: ",save[0], "Salary: ",sals)
        print("Short Stop: ",ssave[0], "Salary: ",salss)
        print("Third Base: ",tave[0], "Salary: ",salt)
        print("Outfield: ",oave[0], "Salary: ",salo)
        
ans = ""
while ( ans != "exit"):
    
    ans = input("What kind of Pitcher would you like to see? (Innings, Strikeout, Win, or exit) ")
    if (ans == "Innings"):
        
        innave = []
        for i in range(len(pit)):
            innave.append(pit.iloc[i,6])
    
        location = innave.index(max(innave))
        innave[location] = 0
        location2 = innave.index(max(innave))
        sal1 = 13000
        sal2 = 10900
        
        for i in range(len(dk)):
            if (dk.iloc[i,2] == pit.iloc[location][0]):
                    sal1 = dk.iloc[i,5]
            if (dk.iloc[i,2] == pit.iloc[location2][1]):
                    sal2 = dk.iloc[i,5]
        
        print("Innings Heavy Pitchers: ")
        print("Pitcher: ",pit.iloc[location][0], "Salary: ",sal1)
        print("Pitcher: ",pit.iloc[location2][0], "Salary: ",sal2)

    if (ans == "Strikeout"):
        
        innave = []
        for i in range(len(pit)):
            innave.append(pit.iloc[i,9])
    
        location = innave.index(max(innave))
        innave[location] = 0
        location2 = innave.index(max(innave))
        
        sal1 = 13000
        sal2 = 12500
        
        for i in range(len(dk)):
            if (dk.iloc[i,2] == pit.iloc[location][0]):
                    sal1 = dk.iloc[i,5]
            if (dk.iloc[i,2] == pit.iloc[location2][1]):
                    sal2 = dk.iloc[i,5]
        
        print("Strikeout Heavy Pitchers: ")
        print("Pitcher: ",pit.iloc[location][0], "Salary: ",sal1)
        print("Pitcher: ",pit.iloc[location2][0], "Salary: ",sal2)
        
    if (ans == "Win"):
        
        innave = []
        for i in range(len(pit)):
            innave.append(pit.iloc[i,12])
    
        location = innave.index(max(innave))
        innave[location] = 0
        location2 = innave.index(max(innave))
        
        sal1 = 13000
        sal2 = 11900
        
        for i in range(len(dk)):
            if (dk.iloc[i,2] == pit.iloc[location][0]):
                    sal1 = dk.iloc[i,5]
            if (dk.iloc[i,2] == pit.iloc[location2][1]):
                    sal2 = dk.iloc[i,5]
        
        print("Win Heavy Pitchers: ")
        print("Pitcher: ",pit.iloc[location][0], "Salary: ",sal1)
        print("Pitcher: ",pit.iloc[location2][0], "Salary: ",sal2)
        
                
    
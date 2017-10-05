# -*-coding: utf-8 -*-
import random
from prettytable import PrettyTable

t1 = {"place" : 0,"name" : "Real Madrid", "wins" : 0, "losses" : 0, "draws" : 0, "goals" : 0, "miss" : 0, "score" : 0}
t2 = {"place" : 0,"name" : "Barselona", "wins" : 0, "losses" : 0, "draws" : 0, "goals" : 0, "miss" : 0, "score" : 0}
t3 = {"place" : 0,"name" : "Valensia", "wins" : 0, "losses" : 0, "draws" : 0, "goals" : 0, "miss" : 0, "score" : 0}
t4 = {"place" : 0,"name" : "Sevilla", "wins" : 0, "losses" : 0, "draws" : 0, "goals" : 0, "miss" : 0, "score" : 0}
t5 = {"place" : 0,"name" : "Atletico Madrid", "wins" : 0, "losses" : 0, "draws" : 0, "goals" : 0, "miss" : 0, "score" : 0}
t6 = {"place" : 0,"name" : "Real Betis", "wins" : 0, "losses" : 0, "draws" : 0, "goals" : 0, "miss" : 0, "score" : 0}


LaLeague = [t1,t2,t3,t4,t5,t6]
Results = []

def print_match():
    team1 = input("Введите название первой команды: ")
    team2 = input("Введите название второй команды: ")
    a = True
    for elem in Results:
        if team1.lower() == elem["team1"].lower() and team2.lower() == elem["team2"].lower():
            print(team1, elem["acc1"],"-",elem["acc2"],team2)
            a = False
            break
        elif team2.lower() == elem["team1"].lower() and team1.lower() == elem["team2"].lower():
            print(team2, elem["acc1"],"-",elem["acc2"],team1)
            a = False
            break
        elif team1.lower() == team2.lower():
            print("Тренировочные матчи не в счет ;)")
            return
    if a:
        print("\nТаких у нас не водится")
        print("Попробуйте еще разок\n")
        return

def request():
    a = input("Хотите узнать результаты матча между командами? yes/no: ")
    if a == "no":
        print("Пока!")
        return
    elif a == "yes":
        print_match()
        request()
    else:
        print("Я вас не понял, попробуйте еще разок")
        request()
    
def print_table():
    th = ["Место", "Команда", "Победы", "Поражения", "Ничьи", "Забито", "Пропущено", "Очки"]
    td = []
    collums = len(th)
    table = PrettyTable(th)
    for elem in LaLeague:
        for key in elem:
            td.append(elem[key])
    while td:
        table.add_row(td[:collums])
        td = td[collums:]
    print (table)
    
def match(team1, team2):
    x = random.randint(0,5)
    y = random.randint(0,5)
    
    team1["goals"] += x
    team1["miss"] += y
    
    team2["miss"] += x
    team2["goals"] += y
    if x > y:
        team1["wins"] += 1
        team1["score"] += 3
        
        team2["losses"] += 1
    elif y > x:
        team2["wins"] += 1
        team2["score"] += 3
        
        team1["losses"] += 1
    elif x == y:
        team1["draws"] += 1
        team1["score"] += 1
        
        team2["draws"] += 1
        team2["score"] += 1
    this = {"team1" : team1["name"], "team2" : team2["name"], "acc1" : x, "acc2" : y}
    Results.append(this)

def places():
    i = 1
    LaLeague.sort(key = lambda x : [-x["score"], -x["goals"], x["miss"]])
    for elem in LaLeague:
        elem["place"] = i
        i += 1

def turich():
    for team1 in LaLeague:
        for team2 in LaLeague:
            if team1 == team2:
                break
            match(team1,team2)
    places()
    print_table()
    
def main():
    turich()
    request()
main()

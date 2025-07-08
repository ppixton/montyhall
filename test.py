import random

#Create a set of Doors

#Select a Door

#Eliminate one False Door

#Choose to switch or stay

#Determine results 

class Set():
    doors = [False, False, True]
    revealed_door = 0
    anti_pick = 0

    chosen_door = 0
    pick = 0

    def shuffle_doors(self):
        random.shuffle(self.doors)

    def reveal_false(self, pick):
        self.pick = pick
        self.chosen_door = pick - 1
        choices = [0,1,2]
        choices.remove(self.chosen_door)

        #If the selected door is false - reveal the other false door 
        if self.doors[self.chosen_door] == False:
            for x in choices:
                if self.doors[x] == False:
                    self.revealed_door = x
        #If the selected door is True - reveal one of the false doors
        else:
            random.shuffle(choices)
            self.revealed_door = choices[0]
        self.anti_pick = self.revealed_door+1
    
    def switch(self):
        choices = [0,1,2]
        choices.remove(self.revealed_door)
        choices.remove(self.chosen_door)
        self.chosen_door = choices[0]
        self.pick = self.chosen_door+1

    def determination(self):
        return self.doors[self.chosen_door]


#Count of how many are goats and how many are prizes for switch and stay
stay_prize_count = 0
stay_goat_count = 0
switch_prize_count = 0
switch_goat_count = 0

#Door choices
choices = [1,2,3]

#Run it 1000 times randomly selecting a door, and staying
for x in range(999):
    random.shuffle(choices)
    stay = Set()
    stay.shuffle_doors()
    stay.reveal_false(choices[0])
    result = stay.determination()

    if result == False:
        stay_goat_count +=1
    if result == True:
        stay_prize_count +=1

#Run it 1000 times randomly selecting a door, and switching
for x in range(999):
    random.shuffle(choices)
    switch = Set()
    switch.shuffle_doors()
    switch.reveal_false(choices[0])
    switch.switch()
    result = switch.determination()

    if result == False:
        switch_goat_count +=1
    if result == True:
        switch_prize_count +=1

print("The person who always stays with the original door got a prize " + str(stay_prize_count) + " times, and got a goat " + str(stay_goat_count) + " times.")
print("The person who always switched from the original door got a prize " + str(switch_prize_count) + " times, and got a goat " + str(switch_goat_count) + " times.")
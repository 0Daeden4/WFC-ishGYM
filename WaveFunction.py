import numpy as np
import random
import Exercises

class WaveFC:

    
    def __init__ (self, columns, rows):
        #length of grid
        self.columns = columns
        self.rows = rows
        self.exercises = []
        self.grid = np.empty((rows, columns), dtype=object)

        exercises = [Exercises.MuscleGroup.FREE]
        self.freeExercise = Exercises.Exercise()
        self.freeExercise.setTrainedGroups(exercises)
        self.freeExercise.setFocusGroups(exercises)
        self.freeExercise.setName("FREE")
        
        
    def addExercises(self, exercises):
        self.exercises = exercises

    def initGrid(self):
        self.exercises = np.array(self.exercises, dtype=object)
        for i in range(self.rows-1):
            for j in range(self.columns-1):
                self.grid[i, j] = self.exercises
    
    def collapse(self):
        #TODO add preferences based on target muscles and try to avoid matches in 2 exercises' target groups
        #TODO figure out why 'None' gets printed at the end of the array
        #ports symbolize the Exercise groups
        portArray = []
        for i in range(self.rows-1):
            nextArray = []

            for j in range(self.columns-1):
                currentList = self.grid[i,j]
                #exercises from the previous day won't be included
                allowedToday = []
                if len(portArray) == 0:
                    allowedToday = list(currentList)
                else:
                    included = True
                    for exercise in currentList:
                        for port in exercise.port:
                            if port in portArray:
                                included = False
                                break
                        if included:
                            allowedToday.append(exercise)

                    #allowedToday = list(set(currentList) - set(portArray))
                if len(allowedToday) == 0:
                    allowedToday = [self.freeExercise]
                comparisonList = []
                for exercise in allowedToday:
                    #choose
                    if j>0:
                        #print("selfgrid" + str(self.grid[i,j-1]) + " exerc: " + str(exercise))
                        comparisonList.append(exercise if not exercise.isCompatible(self.grid[i,j-1]) else self.freeExercise)
                    else:
                        comparisonList.append(allowedToday[random.randint(0, len(allowedToday)-1)])

                #decide randomly for current from comparisonList and collapse
                self.grid[i,j] = comparisonList[random.randint(0, len(comparisonList)-1)]
                #print(self.grid[i,j])
                nextArray += self.grid[i,j].port
                #remove duplicates
                nextArray = list(set(nextArray))
                #for testing
                #print(self.grid)

            #set current ports to todays ports
            #print("nextarray: " + str(nextArray) + "\n")
            portArray = nextArray


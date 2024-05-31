from enum import Enum

class MuscleGroup(Enum):
    TRAPS = 't'
    CHEST = 'p' #pecs
    UPPER_CHEST = 'p^'
    LOWER_CHEST = 'p_'
    SHOULDERS = 's'
    FRONT_SHOULDERS = 's/'
    BACK_SHOULDERS = 's\\'
    SIDE_SHOULDERS = 's('
    LATS = 'v' #v shape
    BACK = 'b'
    BICEPS = '2'
    TRICEPS = '3'
    ABDOMEN = 'a'
    LEGS = 'l'
    GLUTES = 'g'
    HAMSTRINGS = 'h'
    QUADS = '4'
    CALVES = 'c'
    FOREARMS = 'f'

    #TRAPS_FOCUS = 't*'
    #CHEST_FOCUS = 'p*' #pecs
    #UPPER_CHEST_FOCUS = 'p^*'
    #LOWER_CHEST_FOCUS = 'p_*'
    #SHOULDERS_FOCUS = 's*'
    #FRONT_SHOULDERS_FOCUS = 's/*'
    #BACK_SHOULDERS_FOCUS = 's\\*'
    #SIDE_SHOULDERS_FOCUS = 's(*'
    #LATS_FOCUS = 'v*' #v shape
    #BACK_FOCUS = 'b*'
    #BICEPS_FOCUS = '2*'
    #TRICEPS_FOCUS = '3*'
    #ABDOMEN_FOCUS = 'a*'
    #LEGS_FOCUS = 'l*'
    #GLUTES_FOCUS = 'g*'
    #HAMSTRINGS_FOCUS = 'h*'
    #QUADS_FOCUS = '4*'
    #CALVES_FOCUS = 'c*'
    #FOREARMS_FOCUS = 'f*'

    FREE = 'F'



class Exercise:

    def __init__(self):
        self.port = []

        self.trainedGroups = []

        self.focusGroups = []

        self.name = "Unnamed"

    def setName(self, name):
        self.name = name

    #groups must contain enums from the Muscle Group enum
    def setTrainedGroups(self, groups):
        self.trainedGroups = groups
        self.port += groups
        #remove duplicates
        self.port = list(set(self.port))

    #groups must contain enums from the Muscle Group enum
    def setFocusGroups(self, groups):
        self.focusGroups = groups
        self.port += groups
        #remove duplicates
        self.port = list(set(self.port))

    def isCompatible(self, otherExercise):
        selfFocus = set(self.focusGroups)
        otherFocus = set(otherExercise.focusGroups)
        return False if selfFocus.intersection(otherFocus) == set() else True

    def __str__(self):
        return self.name
        
    def __repr__(self):
        return self.__str__()

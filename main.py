import Exercises
import WaveFunction

def main():
    #TODO implement GUI
    mg = Exercises.MuscleGroup
    y = [mg.CHEST, mg.TRICEPS, mg.FRONT_SHOULDERS]
    z = [mg.CHEST]
    chestPress = Exercises.Exercise()
    chestPress.setTrainedGroups(y)
    chestPress.setFocusGroups(z)
    chestPress.setName("chest press")

    y = [mg.TRICEPS, mg.LATS, mg.ABDOMEN]
    z = [mg.TRICEPS]
    tricepsPushdown = Exercises.Exercise()
    tricepsPushdown.setTrainedGroups(y)
    tricepsPushdown.setFocusGroups(z)
    tricepsPushdown.setName("triceps pushdown")

    y = [mg.CHEST, mg.TRICEPS, mg.FRONT_SHOULDERS]
    z = [mg.UPPER_CHEST, mg.CHEST]
    inclineChestPress = Exercises.Exercise()
    inclineChestPress.setTrainedGroups(y)
    inclineChestPress.setFocusGroups(z)
    inclineChestPress.setName("incline chest press")

    y = [mg.SHOULDERS]
    z = [mg.FRONT_SHOULDERS, mg.SHOULDERS, mg.SIDE_SHOULDERS]
    lateralRaise = Exercises.Exercise()
    lateralRaise.setTrainedGroups(y)
    lateralRaise.setFocusGroups(z)
    lateralRaise.setName("lateral raise")

    #y = [mg.CHEST, mg.TRICEPS, mg.FRONT_SHOULDERS]
    #z = [mg.CHEST]
    #x = Exercises.Exercise()
    #x.setTrainedGroups(y)
    #x.setFocusGroups(z)

    #y = [mg.CHEST, mg.TRICEPS, mg.FRONT_SHOULDERS]
    #z = [mg.CHEST]
    #x = Exercises.Exercise()
    #x.setTrainedGroups(y)
    #x.setFocusGroups(z)

    collapser = WaveFunction.WaveFC(6,7)
    collapser.addExercises([chestPress, tricepsPushdown, inclineChestPress, lateralRaise])
    collapser.initGrid()

    collapser.collapse()
    print(collapser.grid)

    

if __name__ == "__main__":
    main()

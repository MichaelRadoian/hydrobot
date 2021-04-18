class UserProfile:
    def __init__(self, user, weight, activityTime):
        self.user = user
        self.weight = weight
        self.activityTime = activityTime

    def getUser(self):
        return self.user

    def getWeight(self):
        return self.weight

    def getActivityTime(self):
        return self.activityTime

    def getDailyWaterIntake(self):
        dailyWaterIntake = self.getWeight() * (2/3)
        return dailyWaterIntake

    def getAdjustedDailyWaterIntake(self):
        adjustedWaterIntake = (float(self.getWeight()) * 0.66666) 
        adjustedWaterIntake2 = adjustedWaterIntake + ((float(self.getActivityTime()) / 30.0) * 12.0)
        return adjustedWaterIntake2

    def setUser(self, u):
        self.user = u
    
    def setWeight(self, w):
        self.weight = w
    
    def setActivityTime(self, aT):
        self.activityTime = aT

    def getStats(self):
        return 'Weight: ' + str(self.getWeight()) +  '(lbs)\nActivity Time: ' + str(self.getActivityTime()) + '(minutes)\nRecommended Daily Water Intake: ' + str(round(self.getAdjustedDailyWaterIntake())) + ' oz'
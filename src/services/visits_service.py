from src.repos.visits_repo import VisitsRepo


class VisitsService:

    global visitsRepo
    visitsRepo: VisitsRepo

    def __init__(self, visitsRepo: VisitsRepo):
        self.visitsRepo = visitsRepo

    def findAll(self):
        visitsRepo.findAll()
        # start connection with database
        # make an operation {call SQL Query that give us all visits entities form the visits table}
        # close database connection
        # return [filtered result] in compatible form with services layer
        return ''
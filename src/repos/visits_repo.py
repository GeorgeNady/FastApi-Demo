class VisitsRepo:

    # __db variable
    __db = 'my_database'

    def findAll(self):
        # start connection with database
        self.__db.connect()
        # make an operation {call SQL Query that give us all visits entities form the visits table}
        visits = self.__db.query('select * from visits')
        # close database connection
        self.__db.close()
        # return [filtered result] in compatible form with services layer
        return visits

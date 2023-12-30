
# Egypt-Japan University of Science and Technology
# Artificial Intelligence and Data Science Department
# Electronics Inventory Management System for Suppliers
# Version Settings
# ---
''' This dictionary contains all of the data
     needed to be used globally.
     In the event of failure, kindly refer to
     the version info stated in the deployed app.'''
settings = {"version": "0.0.1",
            "day": 30,
            "month": 12,
            "year": 2023}

class VersionInfo():
    ''' Class that contains all related info regarding the deployment.'''
    def get_date():
        ''' Generate date of the current application version in DD/MM/YYYY format.'''
        return "{d}/{m}/{y}".format(d = settings['day'], m = settings['month'], y = settings['year'])

    def get_title():
        ''' Generate project title'''
        return "EMS V.{v} - {d}".format(v = settings['version'], d = VersionInfo.get_date())
    
    def get_db():
        ''' Get current name of database,
        TODO: defaulted to "testdb" and to-be changed later.'''
        return "hr"
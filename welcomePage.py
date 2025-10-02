from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from homepage import Ui_MainWindow
from pybaseball import standings
from pybaseball import  playerid_lookup
import teams as teammer


#Leagues
AMERICAN_LEAGUE=103
NATIONAL_LEAGUE=104
#Divisions
AL_EAST=201
AL_CENTRAL=202
AL_WEST=200
NL_EAST=204
NL_CENTRAL=205
NL_WEST=203



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)

        self.load_ALEast()
        self.load_ALCentral()
        self.load_ALWest()
        self.load_NLEast()
        self.load_NLCentral()
        self.load_NLWest()
        


    def load_ALEast(self):
        division = teammer.get_LeagueData(AMERICAN_LEAGUE, AL_EAST)
        AlEastTeams = division[AL_EAST]['teams']
        self.lbl_ALEast.setText(division[AL_EAST]['div_name'])
        self.tblWid_ALEast.setRowCount(len(AlEastTeams))
        for tIndex, team in enumerate(AlEastTeams): 
            colIndex = 0           
            for otIndex, attr in enumerate(team):
                if attr == 'div_rank':
                    continue
                
                item = QTableWidgetItem(str(team[attr]))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.tblWid_ALEast.setItem(tIndex, colIndex, item)

                colIndex += 1



        self.tblWid_ALEast.resizeColumnsToContents()

    def load_ALCentral(self):
        division = teammer.get_LeagueData(AMERICAN_LEAGUE, AL_CENTRAL)
        AlCentralTeams = division[AL_CENTRAL]['teams']
        self.lbl_ALCentral.setText(division[AL_CENTRAL]['div_name'])
        self.tblWid_ALCentral.setRowCount(len(AlCentralTeams))
        for tIndex, team in enumerate(AlCentralTeams): 
            colIndex = 0           
            for otIndex, attr in enumerate(team):
                if attr == 'div_rank':
                    continue
                item = QTableWidgetItem(str(team[attr]))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.tblWid_ALCentral.setItem(tIndex, colIndex, item)
                colIndex += 1


        self.tblWid_ALCentral.resizeColumnsToContents()

    def load_ALWest(self):
        division = teammer.get_LeagueData(AMERICAN_LEAGUE, AL_WEST)        
        AlWestTeams = division[AL_WEST]['teams']
        self.lbl_ALWest.setText(division[AL_WEST]['div_name'])
        self.tblWid_ALWest.setRowCount(len(AlWestTeams))
        for tIndex, team in enumerate(AlWestTeams): 
            colIndex = 0           
            for otIndex, attr in enumerate(team):
                if attr == 'div_rank':
                    continue
                item = QTableWidgetItem(str(team[attr]))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.tblWid_ALWest.setItem(tIndex, colIndex, item)
                colIndex += 1


        self.tblWid_ALWest.resizeColumnsToContents()

    def load_NLEast(self):
        division = teammer.get_LeagueData(NATIONAL_LEAGUE, NL_EAST)
        NLEastTeams = division[NL_EAST]['teams']
        self.lbl_NLEast.setText(division[NL_EAST]['div_name'])
        self.tblWid_NLEast.setRowCount(len(NLEastTeams))
        for tIndex, team in enumerate(NLEastTeams): 
            colIndex = 0           
            for otIndex, attr in enumerate(team):
                if attr == 'div_rank':
                    continue
                item = QTableWidgetItem(str(team[attr]))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.tblWid_NLEast.setItem(tIndex, colIndex, item)
                colIndex += 1


        self.tblWid_NLEast.resizeColumnsToContents()

    def load_NLCentral(self):
        division = teammer.get_LeagueData(NATIONAL_LEAGUE, NL_CENTRAL)
        NLEastTeams = division[NL_CENTRAL]['teams']
        self.lbl_NLCentral.setText(division[NL_CENTRAL]['div_name'])
        self.tblWid_NLCentral.setRowCount(len(NLEastTeams))
        for tIndex, team in enumerate(NLEastTeams): 
            colIndex = 0           
            for otIndex, attr in enumerate(team):
                if attr == 'div_rank':
                    continue
                item = QTableWidgetItem(str(team[attr]))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.tblWid_NLCentral.setItem(tIndex, colIndex, item)
                colIndex += 1


        self.tblWid_NLCentral.resizeColumnsToContents()

    def load_NLWest(self):
        division = teammer.get_LeagueData(NATIONAL_LEAGUE, NL_WEST)
        NlWestTeams = division[NL_WEST]['teams']
        self.lbl_NLWest.setText(division[NL_WEST]['div_name'])
        self.tblWid_NLWest.setRowCount(len(NlWestTeams))
        for tIndex, team in enumerate(NlWestTeams): 
            colIndex = 0           
            for otIndex, attr in enumerate(team):
                if attr == 'div_rank':
                    continue
                item = QTableWidgetItem(str(team[attr]))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.tblWid_NLWest.setItem(tIndex, colIndex, item)
                colIndex += 1


        self.tblWid_NLWest.resizeColumnsToContents()
        




app = QApplication([])
window = MainWindow()
window.show()
app.exec()


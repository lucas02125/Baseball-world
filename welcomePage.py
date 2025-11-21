from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Pages.homepage import Ui_MainWindow
from standingsPage import StandingsPage
from rosterPage import RosterPage
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

        leagueData = teammer.get_LeagueData(self)

        self.btnStandings.clicked.connect(lambda:self.access_Standings())
        self.btnTeams.clicked.connect(lambda:self.access_Teams(leagueData))
        
        teammer.load_ALEast(self,leagueData,AL_EAST)
        teammer.load_ALCentral(self,leagueData,AL_CENTRAL)
        teammer.load_ALWest(self,leagueData,AL_WEST)
        teammer.load_NLEast(self,leagueData,NL_EAST)
        teammer.load_NLCentral(self,leagueData,NL_CENTRAL)
        teammer.load_NLWest(self,leagueData,NL_WEST)
        
    def access_Standings(self):
        self.standingsPage = StandingsPage()
        self.standingsPage.show()

    def access_Teams(self, leagueData):
        self.rosterPage = RosterPage(leagueData)
        self.rosterPage.show()
        
                
app = QApplication([])
window = MainWindow()
window.show()
app.exec()


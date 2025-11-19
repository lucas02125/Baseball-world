from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Pages.rosters import Ui_Roster
import teams as teamAPI

class RosterPage(QWidget):
    team_names = []
    def __init__(self, leagueData,parent=None):
        super(RosterPage,self).__init__(parent)
        self.ui = Ui_Roster()
        self.ui.setupUi(self)
        
        global team_names
        for div_id, div_data in leagueData.items():
            for team in div_data["teams"]:
                self.team_names.append({
                    "name":team["name"],
                    "team_id":team["team_id"]
                })
        
        self.team_names = sorted(self.team_names, key=lambda x: x["name"])
        recentSeason = teamAPI.getLatestSeason(self)
        divYears = [str(e) for e in range(1969,int(recentSeason['seasonId']))]
        self.ui.cmbx_Season.addItems(divYears)
        self.ui.cmbx_Season.currentTextChanged.connect(lambda: self.getCurrentTeamInfo(self.ui.cmbx_MLBTeams.currentText(), self.ui.cmbx_Season.currentText()))
        self.ui.cmbx_MLBTeams.addItems(team["name"] for team in self.team_names)
        self.ui.cmbx_MLBTeams.currentTextChanged.connect(lambda: self.getCurrentTeamInfo(self.ui.cmbx_MLBTeams.currentText(), self.ui.cmbx_Season.currentText()))        

    def getCurrentTeamInfo(self, chosenTeam, chosenYear):
        global team_names
        for aTeam in self.team_names:
            if aTeam["name"] == chosenTeam:
                print(aTeam["team_id"])
                print(chosenYear)
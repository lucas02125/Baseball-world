from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Pages.rosters import Ui_Roster
from playerPage import PlayerPage
import teams as teamAPI
#Error handling
import ctypes

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
        recentSeason = teamAPI.get_LatestSeason(self)
        divYears = [str(e) for e in range(1969,int(recentSeason['seasonId']))]
        self.ui.cmbx_Season.addItems(divYears)
        self.ui.cmbx_MLBTeams.addItems(team["name"] for team in self.team_names)
        self.ui.cmbx_Season.currentTextChanged.connect(lambda: self.getCurrentTeamInfo(self.ui.cmbx_MLBTeams.currentText(), self.ui.cmbx_Season.currentText()))
        self.ui.cmbx_MLBTeams.currentTextChanged.connect(lambda: self.getCurrentTeamInfo(self.ui.cmbx_MLBTeams.currentText(), self.ui.cmbx_Season.currentText()))        
        self.ui.tblWg_Roster.itemClicked.connect(lambda: self.onRosterItemClicked(self.ui.cmbx_Season.currentText()))

    def getCurrentTeamInfo(self, chosenTeam, chosenYear):
        global team_names
        players = []
        expansion_teams = {"Texas Rangers":1972, 
                           "Toronto Blue Jays":1977, 
                           "Tampa Bay Rays":1998, 
                           "Arizona Diamondbacks":1998,
                           "Colorado Rockies":1993,
                           "Miami Marlins":1993,
                           "Seattle Mariners":1977}
        if  chosenTeam in expansion_teams and int(chosenYear) < expansion_teams[chosenTeam]:
            ctypes.windll.user32.MessageBoxW(0, "No data for team this season", "Try again with another team/season", 1)
            return
        
        for aTeam in self.team_names:
            if aTeam["name"] == chosenTeam:
                
                # Will need to handle teams that are newer than others
                teamData = teamAPI.get_RosterData(self, aTeam["team_id"], chosenYear)                                    
                raw_data = teamData.strip().splitlines()
                
                for line in raw_data:
                    line = line.strip()

                    line = line.replace("#","")
                    parts = line.split()

                    # By 1994 we dont take in player numbers
                    if len(parts) == 3:
                        number = "--"
                        position = parts[0]
                        name = " ".join(parts[1:])
                    elif len(parts) == 4 and not parts[0].isdigit():
                        number = "--"
                        position = parts[0]
                        name = " ".join(parts[1:])
                    else:
                        number = parts[0]
                        position = parts[1]
                        name = " ".join(parts[2:])

                    players.append({
                        "number": number
                        ,"position": position
                        ,"name": name
                    })

        self.ui.tblWg_Roster.setRowCount(len(players))
        for row, player in enumerate(players):
            numberItem = QTableWidgetItem(str(player["number"]))
            numberItem.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            posItem = QTableWidgetItem(str(player["position"]))
            posItem.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

            nameItem = QTableWidgetItem(str(player['name']))
            nameItem.setForeground(QColor("blue"))
            nameItem.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            
            self.ui.tblWg_Roster.setItem(row, 0, numberItem)
            self.ui.tblWg_Roster.setItem(row, 1, posItem)
            self.ui.tblWg_Roster.setItem(row, 2, nameItem)

        self.ui.tblWg_Roster.resizeColumnsToContents()

    def onRosterItemClicked(self, chosenSeasonYear):
        playerName = self.ui.tblWg_Roster.item(self.ui.tblWg_Roster.currentRow(), 2).text()
        position = self.ui.tblWg_Roster.item(self.ui.tblWg_Roster.currentRow(), 1).text()
        #print(teamAPI.get_PlayerStatistics_Career(self, playerName, position, chosenSeasonYear))   
        playerStatData = teamAPI.get_PlayerStatistics_YBY(self, playerName, position, chosenSeasonYear)
        self.playerPage = PlayerPage(playerStatData)
        self.playerPage.show()  


                
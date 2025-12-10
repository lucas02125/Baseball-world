from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Pages.player import Ui_Player
import teams as teamAPI


class PlayerPage(QWidget):
    def __init__(self, playerStatData,parent = None):
        super(PlayerPage,self).__init__(parent)
        self.ui = Ui_Player()
        self.ui.setupUi(self)
        self.ui.lbl_playerName.setText(playerStatData['first_name'] + " " + playerStatData['last_name'])
        self.ui.lbl_teamName.setText(playerStatData['current_team'])
        self.ui.lbl_Retired.setText(playerStatData.get('last_played', '') or '')
        self.ui.lbl_Debut.setText(playerStatData['mlb_debut'])
        self.ui.lbl_positions.setText(playerStatData['position'])
        self.ui.lbl_bats.setText(playerStatData['bat_side'])
        self.ui.lbl_throws.setText(playerStatData['pitch_hand'])

        PITCHER_COLUMNS = ["Season","Age","GP","GS","CG","W","L","ERA","SO","SV","SVO","IP","H","R","ER","BB","IBB","HR","HBP","BK","HD","WP","BF","WHIP"]
        HITTER_COLUMNS = []

        PITCHER_MAP = {
            "Season":  lambda year: year.get("season"),
            "Age":     lambda year: year["stats"].get("age"),
            "GP":      lambda year: year["stats"].get("gamesPlayed"),
            "GS":      lambda year: year["stats"].get("gamesStarted"),
            "CG":      lambda year: year["stats"].get("completeGames"),
            "W":       lambda year: year["stats"].get("wins"),
            "L":       lambda year: year["stats"].get("losses"),
            "ERA":     lambda year: year["stats"].get("era"),
            "SO":      lambda year: year["stats"].get("strikeOuts"),
            "SV":      lambda year: year["stats"].get("saves"),
            "SVO":     lambda year: year["stats"].get("saveOpportunities"),
            "IP":      lambda year: year["stats"].get("inningsPitched"),
            "H":       lambda year: year["stats"].get("hits"),
            "R":       lambda year: year["stats"].get("runs"),
            "ER":      lambda year: year["stats"].get("earnedRuns"),
            "BB":      lambda year: year["stats"].get("walks"),
            "IBB":     lambda year: year["stats"].get("intentionalWalks"),
            "HR":      lambda year: year["stats"].get("homeRuns"),
            "HBP":     lambda year: year["stats"].get("hitByPitch"),
            "BK":      lambda year: year["stats"].get("balks"),
            "HD":      lambda year: year["stats"].get("holds"),
            "WP":      lambda year: year["stats"].get("wildPitches"),
            "BF":      lambda year: year["stats"].get("battersFaced"),
            "WHIP":    lambda year: year["stats"].get("whip"),
        }   
        self.ui.tblW_PlayerStats.verticalHeader().setVisible(False)
        
        if playerStatData['position'] == 'P': 
            stats = playerStatData['stats']           
            self.ui.tblW_PlayerStats.setColumnCount(len(PITCHER_COLUMNS))
            self.ui.tblW_PlayerStats.setRowCount(len(stats))
            self.ui.tblW_PlayerStats.setHorizontalHeaderLabels(PITCHER_COLUMNS)

            #Rows
            for pIndex, year in enumerate(stats):
                #Columns
                for cIndex, colName in enumerate(PITCHER_COLUMNS):
                    value = PITCHER_MAP[colName](year)
                    item = QTableWidgetItem("" if value is None else str(value))
                    item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                    self.ui.tblW_PlayerStats.setItem(pIndex, cIndex, item)

                

            self.ui.tblW_PlayerStats.resizeColumnsToContents()
        else:
            self.ui.tblW_PlayerStats.setColumnCount(len(HITTER_COLUMNS))

      
        
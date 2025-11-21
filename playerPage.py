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

        print(playerStatData)
        
        #Batting 26 columns
        #Pitching 24 columns
        
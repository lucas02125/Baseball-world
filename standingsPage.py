from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Pages.standings import Ui_Standings
from datetime import datetime
import teams as teamAPI
#Error handling
import ctypes


class StandingsPage(QWidget):
    def __init__(self, parent=None):
        super(StandingsPage,self).__init__(parent)
        self.ui = Ui_Standings()
        self.ui.setupUi(self)

        self.ui.cWdg_pickDate.setVisible(False)
        self.ui.cmBx_yearFilter.setVisible(False) 
        #combo_roll.addItems([str(e) for e in range(1, 100)])
        recentSeason = teamAPI.get_LatestSeason(self)
        divYears = [str(e) for e in range(1969,int(recentSeason['seasonId']))]
        self.ui.cmBx_yearFilter.addItems(divYears)
        self.ui.ckBx_WildCard.stateChanged.connect(lambda:self.adjust_standingCols())
        self.ui.cWdg_pickDate.clicked.connect(lambda:self.getStandings_ByDate(self.ui.cWdg_pickDate.selectedDate()))
        self.ui.cmbBx_StandingFilter.currentTextChanged.connect(lambda: self.showFilter(self.ui.cmbBx_StandingFilter.currentText()))
        self.ui.cmBx_yearFilter.currentTextChanged.connect(lambda: self.getStandings_ByYear(self.ui.cmBx_yearFilter.currentText()))

    def getStandings_ByDate(self,chosenDate):
        theChosenDate = chosenDate.toString('MM/dd/yyyy')
        isWC = self.ui.ckBx_WildCard.isChecked()
        leagueData = teamAPI.get_LeagueData(self, Date=theChosenDate, InclWC=isWC)
        if not leagueData:
            ctypes.windll.user32.MessageBoxW(0, "No data for chosen date", "Please try again", 1)
            return
        teamAPI.load_ALEast(self,leagueData=leagueData)
        teamAPI.load_ALWest(self,leagueData=leagueData)
        teamAPI.load_NLEast(self,leagueData=leagueData)
        teamAPI.load_NLWest(self,leagueData=leagueData)
        if int(chosenDate.year()) > 1994:
            self.ui.tblWid_ALCentral.show()
            self.ui.tblWid_NLCentral.show()
            self.ui.lbl_ALCentral.show()
            self.ui.lbl_NLCentral.show()
            teamAPI.load_NLCentral(self,leagueData=leagueData)
            teamAPI.load_ALCentral(self,leagueData=leagueData)
        else:
            self.ui.tblWid_ALCentral.hide()
            self.ui.tblWid_NLCentral.hide()
            self.ui.lbl_ALCentral.hide()
            self.ui.lbl_NLCentral.hide()


    def getStandings_ByYear(self, chosenYear):
        isWC = self.ui.ckBx_WildCard.isChecked()
        leagueData = teamAPI.get_LeagueData(self, Season=int(chosenYear))
        teamAPI.load_ALEast(self,leagueData=leagueData)
        teamAPI.load_ALWest(self,leagueData=leagueData)
        teamAPI.load_NLEast(self,leagueData=leagueData)
        teamAPI.load_NLWest(self,leagueData=leagueData)
        if int(chosenYear) > 1994:
            self.ui.tblWid_ALCentral.show()
            self.ui.tblWid_NLCentral.show()
            self.ui.lbl_ALCentral.show()
            self.ui.lbl_NLCentral.show()
            teamAPI.load_NLCentral(self,leagueData=leagueData)        
            teamAPI.load_ALCentral(self,leagueData=leagueData)
        else:
            self.ui.tblWid_ALCentral.hide()
            self.ui.tblWid_NLCentral.hide()
            self.ui.lbl_ALCentral.hide()
            self.ui.lbl_NLCentral.hide()            
            


    def showFilter(self,value):
        if value == "Season":
            self.ui.cWdg_pickDate.setVisible(False)
            self.ui.cmBx_yearFilter.setVisible(True)                    
        elif value == "Date":
            self.ui.cWdg_pickDate.setVisible(True)
            self.ui.cmBx_yearFilter.setVisible(False)
        else:
            self.ui.cWdg_pickDate.setVisible(False)
            self.ui.cmBx_yearFilter.setVisible(False)


    def adjust_standingCols(self):
        if bool(self.ui.ckBx_WildCard.isChecked()) == True:
            for col in [6,7,5]:
                self.ui.tblWid_ALEast.setColumnHidden(col,False)
                self.ui.tblWid_ALCentral.setColumnHidden(col,False)
                self.ui.tblWid_ALWest.setColumnHidden(col,False)
                self.ui.tblWid_NLEast.setColumnHidden(col,False)
                self.ui.tblWid_NLCentral.setColumnHidden(col,False)
                self.ui.tblWid_NLWest.setColumnHidden(col,False)               
        else:
            for col in [6,7,5]:
                self.ui.tblWid_ALEast.setColumnHidden(col,True)
                self.ui.tblWid_ALCentral.setColumnHidden(col,True)
                self.ui.tblWid_ALWest.setColumnHidden(col,True)
                self.ui.tblWid_NLEast.setColumnHidden(col,True)
                self.ui.tblWid_NLCentral.setColumnHidden(col,True)
                self.ui.tblWid_NLWest.setColumnHidden(col,True)
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import statsapi

#Leagues
AMERICAN_LEAGUE=103
NATIONAL_LEAGUE=104


def load_ALEast(self,leagueData,AL_EAST=201):
    AlEastTeams = leagueData[AL_EAST]['teams']
    if isinstance(self, QMainWindow):
        self.lbl_ALEast.setText(leagueData[AL_EAST]['div_name'])
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
    else:
        self.ui.lbl_ALEast.setText(leagueData[AL_EAST]['div_name'])
        self.ui.tblWid_ALEast.setRowCount(len(AlEastTeams))
        for tIndex, team in enumerate(AlEastTeams): 
            colIndex = 0           
            for otIndex, attr in enumerate(team):
                if attr == 'div_rank':
                    continue
                
                item = QTableWidgetItem(str(team[attr]))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.ui.tblWid_ALEast.setItem(tIndex, colIndex, item)
                colIndex += 1
        self.ui.tblWid_ALEast.resizeColumnsToContents()

def load_ALCentral(self,leagueData,AL_CENTRAL=202):
    AlCentralTeams = leagueData[AL_CENTRAL]['teams']
    if isinstance(self, QMainWindow):        
        self.lbl_ALCentral.setText(leagueData[AL_CENTRAL]['div_name'])
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
    else:
        self.ui.lbl_ALCentral.setText(leagueData[AL_CENTRAL]['div_name'])
        self.ui.tblWid_ALCentral.setRowCount(len(AlCentralTeams))
        for tIndex, team in enumerate(AlCentralTeams): 
            colIndex = 0           
            for otIndex, attr in enumerate(team):
                if attr == 'div_rank':
                    continue
                item = QTableWidgetItem(str(team[attr]))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.ui.tblWid_ALCentral.setItem(tIndex, colIndex, item)
                colIndex += 1
        self.ui.tblWid_ALCentral.resizeColumnsToContents()

def load_ALWest(self,leagueData,AL_WEST=200):
    AlWestTeams = leagueData[AL_WEST]['teams']
    if isinstance(self,QMainWindow):      
        self.lbl_ALWest.setText(leagueData[AL_WEST]['div_name'])
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
    else:
        self.ui.lbl_ALWest.setText(leagueData[AL_WEST]['div_name'])
        self.ui.tblWid_ALWest.setRowCount(len(AlWestTeams))
        for tIndex, team in enumerate(AlWestTeams): 
            colIndex = 0           
            for otIndex, attr in enumerate(team):
                if attr == 'div_rank':
                    continue
                item = QTableWidgetItem(str(team[attr]))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.ui.tblWid_ALWest.setItem(tIndex, colIndex, item)
                colIndex += 1
        self.ui.tblWid_ALWest.resizeColumnsToContents()

def load_NLEast(self,leagueData,NL_EAST=204):
    NLEastTeams = leagueData[NL_EAST]['teams']
    if isinstance(self,QMainWindow):
        self.lbl_NLEast.setText(leagueData[NL_EAST]['div_name'])
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
    else:
        self.ui.lbl_NLEast.setText(leagueData[NL_EAST]['div_name'])
        self.ui.tblWid_NLEast.setRowCount(len(NLEastTeams))
        for tIndex, team in enumerate(NLEastTeams): 
            colIndex = 0           
            for otIndex, attr in enumerate(team):
                if attr == 'div_rank':
                    continue
                item = QTableWidgetItem(str(team[attr]))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.ui.tblWid_NLEast.setItem(tIndex, colIndex, item)
                colIndex += 1
        self.ui.tblWid_NLEast.resizeColumnsToContents()
        

def load_NLCentral(self,leagueData,NL_CENTRAL=205):
    NLEastTeams = leagueData[NL_CENTRAL]['teams']
    if isinstance(self,QMainWindow):
        self.lbl_NLCentral.setText(leagueData[NL_CENTRAL]['div_name'])
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
    else:
        self.ui.lbl_NLCentral.setText(leagueData[NL_CENTRAL]['div_name'])
        self.ui.tblWid_NLCentral.setRowCount(len(NLEastTeams))
        for tIndex, team in enumerate(NLEastTeams): 
            colIndex = 0           
            for otIndex, attr in enumerate(team):
                if attr == 'div_rank':
                    continue
                item = QTableWidgetItem(str(team[attr]))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.ui.tblWid_NLCentral.setItem(tIndex, colIndex, item)
                colIndex += 1
        self.ui.tblWid_NLCentral.resizeColumnsToContents()

def load_NLWest(self,leagueData,NL_WEST=203):
    NlWestTeams = leagueData[NL_WEST]['teams']
    if isinstance(self,QMainWindow):
        self.lbl_NLWest.setText(leagueData[NL_WEST]['div_name'])
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
    else:
        self.ui.lbl_NLWest.setText(leagueData[NL_WEST]['div_name'])
        self.ui.tblWid_NLWest.setRowCount(len(NlWestTeams))
        for tIndex, team in enumerate(NlWestTeams): 
            colIndex = 0           
            for otIndex, attr in enumerate(team):
                if attr == 'div_rank':
                    continue
                item = QTableWidgetItem(str(team[attr]))
                item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.ui.tblWid_NLWest.setItem(tIndex, colIndex, item)
                colIndex += 1
        self.ui.tblWid_NLWest.resizeColumnsToContents()      

def getLatestSeason(self):
    return statsapi.latest_season()

def get_LeagueData(League="103,104", Division="All",InclWC=False,Season=None,Date=None):
    
    return statsapi.standings_data(leagueId=League,division=Division,include_wildcard=InclWC,season=Season,date=Date)

import os
import sys
from PyQt6 import QtWidgets
# from PyQt6.QtWidgets import QMainWindow, QHeaderView, QMessageBox
from PyQt6.QtWidgets import QHeaderView, QWidget
from PyQt6 import QtCore
from PyQt6.uic import loadUi
from utils.irodsConnectorAnonymous import irodsConnectorAnonymous
from gui.checkableFsTree import checkableFsTreeModel
from gui.popupWidgets import createDirectory
from gui.dataTransfer import dataTransfer

from gui.ui_files.tabTicketAccess import Ui_tabTicketAccess



class irodsTicketLogin(QWidget, Ui_tabTicketAccess):
    def __init__(self):
        self.ic = None
        self.coll = None
        self.this_application = 'iBridgesGui'

        super(irodsTicketLogin, self).__init__()
        if getattr(sys, 'frozen', False):
            super(irodsTicketLogin, self).setupUi(self)
        else:
            loadUi("gui/ui_files/tabTicketAccess.ui", self)

        # QTreeViews
        self.dirmodel = checkableFsTreeModel(self.localFsTreeView)
        self.localFsTreeView.setModel(self.dirmodel)
        # Hide all columns except the Name
        self.localFsTreeView.setColumnHidden(1, True)
        self.localFsTreeView.setColumnHidden(2, True)
        self.localFsTreeView.setColumnHidden(3, True)
        self.localFsTreeView.header().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        home_location = QtCore.QStandardPaths.standardLocations(
                               QtCore.QStandardPaths.StandardLocation.HomeLocation)[0]
        index = self.dirmodel.setRootPath(home_location)
        self.localFsTreeView.setCurrentIndex(index)
        self.dirmodel.initial_expand()

        self.connectButton.clicked.connect(self.irodsSession)
        self.homeButton.clicked.connect(self.loadTable)
        self.createDirectoryButton.clicked.connect(self.createFolder)
        self.downloadButton.clicked.connect(self.download)
        self.downloadAllButton.clicked.connect(self.downloadAll)
        self.collTable.doubleClicked.connect(self.browse)
        self.collTable.clicked.connect(self.fillInfo)
        self.enableButtons(False)
        self.connectButton.setEnabled(True)

    def irodsSession(self):
        self.infoLabel.clear()
        host = self.serverEdit.text().strip()
        path = self.pathEdit.text().strip()
        token = self.ticketEdit.text().strip()

        try:
            self.ic = irodsConnectorAnonymous(host, token, path, application_name=self.this_application)
            self.coll = self.ic.getData()
            self.loadTable()
            self.enableButtons(True)
        except Exception as e:
            self.infoLabel.setText("LOGIN ERROR: Check ticket and iRODS path.\n"+repr(e))

    def enableButtons(self, enable):
        self.connectButton.setEnabled(enable)
        self.homeButton.setEnabled(enable)
        self.createDirectoryButton.setEnabled(enable)
        self.downloadButton.setEnabled(enable)
        self.downloadAllButton.setEnabled(enable)
        self.localFsTreeView.setEnabled(enable)
    
    def loadTable(self, update=None):
        self.infoLabel.clear()
        if self.coll is None:
            self.infoLabel.setText("No data available. Check ticket and iRODS path.")
            return
        if update is None or update is False:
            update = self.coll

        self.collTable.setRowCount(0)
        self.collTable.setRowCount(len(update.subcollections)+len(update.data_objects))
        row = 0
        for subcoll in update.subcollections:
            self.collTable.setItem(row, 0, 
                    QtWidgets.QTableWidgetItem(os.path.dirname(subcoll.path)))
            self.collTable.setItem(row, 1, 
                    QtWidgets.QTableWidgetItem(subcoll.name+"/"))
            self.collTable.setItem(1, 2, QtWidgets.QTableWidgetItem(""))
            self.collTable.setItem(1, 3, QtWidgets.QTableWidgetItem(""))
            row = row + 1
        for obj in update.data_objects:
            self.collTable.setItem(row, 0,
                    QtWidgets.QTableWidgetItem(os.path.dirname(obj.path)))
            self.collTable.setItem(row, 1, QtWidgets.QTableWidgetItem(obj.name))
            self.collTable.setItem(row, 2, QtWidgets.QTableWidgetItem(str(obj.size)))
            self.collTable.setItem(row, 3, QtWidgets.QTableWidgetItem(str(obj.checksum)))
            self.collTable.setItem(row, 4, 
                    QtWidgets.QTableWidgetItem(str(obj.modify_time)))
            row = row+1
        self.collTable.resizeColumnsToContents()

    def browse(self, index):
        self.infoLabel.clear()
        # col = index.column()
        row = index.row()
        if self.collTable.item(row, 0).text() != '':
            path = self.collTable.item(row, 0).text()
            item = self.collTable.item(row, 1).text()
            if item.endswith('/'):
                item = item[:-1]
            if self.ic.session.collections.exists(path+'/'+item):
                coll = self.ic.session.collections.get(path+'/'+item)
                self.loadTable(update=coll)

    def fillInfo(self, index):
        self.previewBrowser.clear()
        self.metadataTable.setRowCount(0)
        row = index.row()
        value = self.collTable.item(row, 1).text()
        path = self.collTable.item(row, 0).text()
        try:
            self.__fillPreview(value, path)
            self.__fillMetadata(value, path)
        except Exception as e:
            self.infoLabel.setText(repr(e))
            raise

    def __fillPreview(self, value, path):
        newPath = "/"+path.strip("/")+"/"+value.strip("/")
        if self.ic.session.collections.exists(newPath):  # collection
            coll = self.ic.session.collections.get(newPath)
            content = ['Collections:', '-----------------'] +\
                      [c.name+'/' for c in coll.subcollections] + \
                      ['\n', 'Data:', '-----------------'] + \
                      [o.name for o in coll.data_objects]
            previewString = '\n'.join(content)
            self.previewBrowser.append(previewString)
        else:  # object
            subcoll = self.ic.session.collections.get(path)
            obj = [o for o in subcoll.data_objects if o.name == value][0]
            # get mimetype
            mimetype = value.split(".")[len(value.split("."))-1]
            if mimetype in ['txt', 'json', 'csv']:
                try:
                    out = []
                    with obj.open('r') as readObj:
                        for i in range(20):
                            out.append(readObj.read(50))
                    previewString = ''.join([line.decode('utf-8') for line in out])
                    self.previewBrowser.append(previewString)
                except Exception as e:
                    self.previewBrowser.append(obj.path)
                    self.previewBrowser.append(repr(e))
                    self.previewBrowser.append("Storage resource might be down.")
            else:
                self.previewBrowser.append("No preview for "+obj.path)

    def __fillMetadata(self, value, path):
        newPath = "/"+path.strip("/")+"/"+value.strip("/")
        if value.endswith("/") and self.ic.session.collections.exists(newPath):
            coll = self.ic.session.collections.get(
                        "/"+path.strip("/")+"/"+value.strip("/")
                        )
            metadata = coll.metadata.items()
        else:
            subcoll = self.ic.session.collections.get(path)
            obj = [o for o in subcoll.data_objects if o.name == value][0]
            metadata = obj.metadata.items()
        self.metadataTable.setRowCount(len(metadata))
        row = 0
        for item in metadata:
            self.metadataTable.setItem(row, 0,
                    QtWidgets.QTableWidgetItem(item.name))
            self.metadataTable.setItem(row, 1,
                    QtWidgets.QTableWidgetItem(item.value))
            self.metadataTable.setItem(row, 2,
                    QtWidgets.QTableWidgetItem(item.units))
            row = row+1
        self.metadataTable.resizeColumnsToContents()

    def createFolder(self):
        self.infoLabel.clear()
        parent = self.dirmodel.get_checked()
        if parent is None:
            self.infoLabel.setText("No parent folder selected.")
        else:
            createDirWidget = createDirectory(parent)
            createDirWidget.exec()
            # self.dirmodel.initial_expand(previous_item = parent)

    def downloadAll(self):
        self.download(allData=True)

    def download(self, allData=False):
        # irods data
        self.enableButtons(False)
        self.infoLabel.clear()
        if allData:
            collPath = os.path.dirname(self.coll.path)
            dataName = self.coll.name.strip('/')
        elif self.collTable.selectedIndexes():
            row = self.collTable.selectedIndexes()[0].row()
            if row == -1:
                self.infoLabel.setText("No iRODS data selected.")
                self.enableButtons(True)
                return
            else:
                collPath = self.collTable.item(row, 0).text()
                dataName = self.collTable.item(row, 1).text().strip('/')
        else:
            self.infoLabel.setText("No iRODS data selected.")
            self.enableButtons(True)
            return

        # filesystem data
        destination = self.dirmodel.get_checked()
        if destination is None or os.path.isfile(destination):
            self.infoLabel.setText("No download folder selected.")
            self.enableButtons(True)
            return
        
        if self.ic.session.collections.exists(collPath+'/'+dataName):
            item = self.ic.session.collections.get(collPath+'/'+dataName)
        else:  # data object with workaround for bug
            parent = self.ic.session.collections.get(collPath)
            item = [obj for obj in parent.data_objects if obj.name == dataName][0]
        self.downloadWindow = dataTransfer(self.ic, False, destination, item)
        self.downloadWindow.finished.connect(self.finishedTransfer)

    def finishedTransfer(self, success, irodsIdx):
        # Refreshes iRODS subtree and irodsIdx (set "None" if to skip)
        # Saves upload parameters if check box is set
        if success is True:
            self.infoLabel.setText("INFO UPLOAD/DOWNLOAD: completed.")
        self.uploadWindow = None  # Release
        self.enableButtons(True)

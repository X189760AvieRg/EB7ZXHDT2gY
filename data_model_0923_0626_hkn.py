# 代码生成时间: 2025-09-23 06:26:59
import sys
from PyQt5.QtCore import Qt, QAbstractListModel, QModelIndex

"""
Data Model Implementation
========================

This module provides a data model for a PyQt application.
"""

class DataModel(QAbstractListModel):
    """
    A custom data model for PyQt applications.
    """
    def __init__(self, data=None, parent=None):
        super().__init__(parent)
        self._data = data or []

    def rowCount(self, parent=QModelIndex()):
        """
        Returns the row count of the model.
        """
        return len(self._data)

    def data(self, index, role=Qt.DisplayRole):
        """
        Returns the data stored under the given role for the item specified by index.
        """
        if not index.isValid() or not 0 <= index.row() < len(self._data):
            return None
        if role == Qt.DisplayRole:
            return str(self._data[index.row()])
        return None

    def setData(self, index, value, role=Qt.EditRole):
        """
        Sets the role data for the item at index to value.
        """
        if index.isValid() and 0 <= index.row() < len(self._data):
            self._data[index.row()] = value
            self.dataChanged.emit(index, index, [role])
            return True
        return False

    def addData(self, value):
        """
        Adds a new row to the model with the given value.
        """
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._data.append(value)
        self.endInsertRows()

    def removeData(self, index):
        """
        Removes the row at the given index from the model.
        """
        if index.isValid() and 0 <= index.row() < len(self._data):
            self.beginRemoveRows(QModelIndex(), index.row(), index.row())
            del self._data[index.row()]
            self.endRemoveRows()
            return True
        return False

    def roleNames(self)::
        """
        Returns a dictionary of role names.
        """
        return {Qt.DisplayRole: b'display'}

    # Additional methods can be added here for further functionality

if __name__ == '__main__':
    # Simple test to check the functionality of the DataModel
    app = sys.modules['PyQt5.QtWidgets'].QApplication(sys.argv)
    model = DataModel(["Item 1", "Item 2", "Item 3"])
    print("Initial data: ", [str(index) for index in model._data])
    model.addData("Item 4")
    print("Data after adding Item 4: ", [str(index) for index in model._data])
    model.removeData(QModelIndex(1, 0))
    print("Data after removing Item 2: ", [str(index) for index in model._data])
    sys.exit(app.exec_())

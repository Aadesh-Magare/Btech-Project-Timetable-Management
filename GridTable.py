# Timetable Management Software - Semi Automated Approach to Timetable Design.
# Copyright (C) 2016  Aadesh Magare - aadeshmagare01@gmail.com, Abhijit A M - abhijit13@gmail.com, Sourabh Limbore - limboresourabh@gmail.com

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#!/usr/bin/python
import wx
import wx.grid as gridlib
from wx.lib.pubsub import pub
import project
import globaldata

class GenericTable(wx.grid.PyGridTableBase):
    def __init__(self, data, rowLabels=None, colLabels=None, name=None, typeOf=None):
        wx.grid.PyGridTableBase.__init__(self)
        self.data = data
        self.rowLabels = globaldata.rowLabels
        self.colLabels = globaldata.colLabels
        self.name = name
        self.type = typeOf

    def GetNumberRows(self):
        return len(self.data)
        # return globaldata.days_per_week

    def GetNumberCols(self):
        return len(self.data[0])
        # return globaldata.lectures_per_day

    def GetColLabelValue(self, col):
        if self.colLabels:
            return self.colLabels[col]
        
    def GetRowLabelValue(self, row):
        if self.rowLabels:
            return self.rowLabels[row]
        
    def IsEmptyCell(self, row, col):
        return self.data[row][col] == None

    def GetValue(self, row, col):
        if self.data[row][col] == None:
            return ''
        else:
            res = ''
            for i in range(len(self.data[row][col])):
                for j in range(len(self.data[row][col][i])):
                    if self.data[row][col][i][j] != None:
                        t = str(self.data[row][col][i][j]) + '\n'
                        res += t
                if i < len(self.data[row][col]) - 1:
                    res += '-------\n'
                else:
                    res += '\n'

            #to fix - there's some garbage at the end of line
            # print res    
            return res
            # return self.data[row][col]

    def SetValue(self, row, col, value):
        # print 'Update to', value, row, col
        if value != '':
            value = value.split()
            value = filter(None, value)
            if value[0] == 'LUNCH':
                if len(value) > 1:
                    name = self.name + '-' + value[1]
                else:
                    name = self.name
                try:
                    project.insert_lunch(name, row, col, self.type)
                    pub.sendMessage('UPDATE_VIEW', data = None)
                except Exception as e:
                    s = 'Conflict with: '
                    for t in e.value:
                        for e in t:
                            if e != None:
                                s += str(e) + ' '
                        s += '\n'
                    dlg = wx.MessageDialog(None, s , "ERROR", wx.OK|wx.ICON_INFORMATION)
                    dlg.ShowModal()
                    dlg.Destroy()
                    return
            else:
                if len(value) >= 3:
                    if self.type == 'Teacher':
                        t = self.name
                        v = value[0]
                        c = value[1]
                        s = value[2]
                        i = row
                        j = col
                        if len(value) == 4:
                            t += '-' + value[3]
                    if self.type == 'Venue':
                        t = value[0]
                        v = self.name
                        c = value[1]
                        s = value[2]
                        i = row
                        j = col
                        if len(value) == 4:
                            v += '-' + value[3]
                    if self.type == 'Class':
                        t = value[0] 
                        v = value[1]
                        c = self.name
                        s = value[2]
                        i = row
                        j = col
                        if len(value) == 4:
                            c += '-' + value[3]
                    try:
                        project.insert_entry(t, v, c, s, i, j)
                        pub.sendMessage('UPDATE_VIEW', data = None)
                    except Exception as e:
                        # print e
                        s = 'Conflict with: '
                        for t in e.value:
                            for e in t:
                                if e != None:
                                    s += str(e) + ' '
                            s += '\n'
                        dlg = wx.MessageDialog(None, s , "ERROR", wx.OK|wx.ICON_INFORMATION)
                        dlg.ShowModal()
                        dlg.Destroy()
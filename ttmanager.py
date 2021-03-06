#!/usr/bin/python

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

import os, sys
import wx
import wx.grid as gridlib
import wx.lib.scrolledpanel
from wx.lib.pubsub import setuparg1
from wx.lib.pubsub import pub
import pickle
from Dialouge import *
from GridTable import *
from MyGrid import *
import globaldata

class SaveClass(object):
    pass

class MyForm(wx.Frame):
    def update(self, value):        
        for teacher in globaldata.all_teachers:
            name = teacher.name
            if not hasattr(self, name):
                self.listboxTeacher.Append(name)
                hfirst = wx.StaticText(self.panel1, label=globaldata.header1)
                hsecond = wx.StaticText(self.panel1, label=globaldata.header2)
                hthird = wx.StaticText(self.panel1, label=globaldata.header3)
                index = globaldata.teacher_shortnames.index(teacher.name) - 1
                hfourth = wx.StaticText(self.panel1, label= 'Timetable For Teacher: Prof. ' + globaldata.teacher_fullnames[index])
                hthird.SetForegroundColour(wx.Colour(255,55,125))
                hfirst.SetFont(self.fonth1)
                hsecond.SetFont(self.fonth2)
                hthird.SetFont(self.fonth3)     
                hfourth.SetFont(self.fonth4)


                vbox = wx.BoxSizer(wx.VERTICAL)
                vbox.AddSpacer(10)
                vbox.Add(hfirst, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)
                vbox.AddSpacer(10)
                vbox.Add(hsecond, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)
                vbox.AddSpacer(2)
                vbox.Add(hthird, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)
                vbox.AddSpacer(10)
                vbox.Add(hfourth, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)
                vbox.AddSpacer(20)
                self.sizer1.Add(vbox, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)

                vbox1 = wx.BoxSizer(wx.VERTICAL)
                self.temp = MyGrid(self.panel1, teacher.mat, teacher.name, 'Teacher')

                setattr(self, name, self.temp)
                vbox1.Add(getattr(self,name), 1, flag=wx.ALIGN_CENTER_HORIZONTAL)
                vbox1.AddSpacer(20)
                self.sizer1.Add(vbox1, 1, flag=wx.ALIGN_CENTER_HORIZONTAL)
                self.sizer1.AddSpacer(200)
                self.sizer1.Layout()

        for venue in globaldata.all_venues:
            name = venue.name
            if not hasattr(self, name):
                self.listboxVenue.Append(name)
                hfirst = wx.StaticText(self.panel2, label=globaldata.header1)
                hsecond = wx.StaticText(self.panel2, label=globaldata.header2)
                hthird = wx.StaticText(self.panel2, label=globaldata.header3)
                print venue.name
                index = globaldata.venue_shortnames.index(venue.name) - 1
                hfourth = wx.StaticText(self.panel2, label='Timetable For Venue: ' + globaldata.venue_fullnames[index])
                hthird.SetForegroundColour(wx.Colour(255,55,125))
                hfirst.SetFont(self.fonth1)
                hsecond.SetFont(self.fonth2)
                hthird.SetFont(self.fonth3)     
                hfourth.SetFont(self.fonth4)

                self.temp = MyGrid(self.panel2, venue.mat, venue.name, 'Venue')        

                vbox = wx.BoxSizer(wx.VERTICAL)
                vbox.AddSpacer(10)
                vbox.Add(hfirst, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)
                vbox.AddSpacer(10)
                vbox.Add(hsecond, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)
                vbox.AddSpacer(2)
                vbox.Add(hthird, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)
                vbox.AddSpacer(10)
                vbox.Add(hfourth, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)
                vbox.AddSpacer(20)
                self.sizer2.Add(vbox, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)
                
                vbox1 = wx.BoxSizer(wx.VERTICAL)
                setattr(self, name, self.temp)
                vbox1.Add(getattr(self,name), 1, flag=wx.ALIGN_CENTER_HORIZONTAL)
                vbox1.AddSpacer(20)
                self.sizer2.Add(vbox1, 1, flag=wx.ALIGN_CENTER_HORIZONTAL)
                self.sizer2.AddSpacer(200)
                self.sizer2.Layout()

        for Class in globaldata.all_classes:
            name = Class.name
            if not hasattr(self, name):
                self.listboxClass.Append(name)
                hfirst = wx.StaticText(self.panel3, label=globaldata.header1)
                hsecond = wx.StaticText(self.panel3, label=globaldata.header2)
                hthird = wx.StaticText(self.panel3, label=globaldata.header3)
                index = globaldata.class_shortnames.index(Class.name) - 1
                hfourth = wx.StaticText(self.panel3, label='Timetable For Class: ' + globaldata.class_fullnames[index])
                hthird.SetForegroundColour(wx.Colour(255,55,125))
                hfirst.SetFont(self.fonth1)
                hsecond.SetFont(self.fonth2)
                hthird.SetFont(self.fonth3)     
                hfourth.SetFont(self.fonth4)

                self.temp = MyGrid(self.panel3, Class.mat, Class.name, 'Class')        
                
                vbox = wx.BoxSizer(wx.VERTICAL)
                vbox.AddSpacer(10)
                vbox.Add(hfirst, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)
                vbox.AddSpacer(10)
                vbox.Add(hsecond, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)
                vbox.AddSpacer(2)
                vbox.Add(hthird, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)
                vbox.AddSpacer(10)
                vbox.Add(hfourth, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)
                vbox.AddSpacer(20)
                self.sizer3.Add(vbox, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)

                vbox1 = wx.BoxSizer(wx.VERTICAL)
                setattr(self, name, self.temp)
                vbox1.Add(getattr(self,name), 1, flag=wx.ALIGN_CENTER_HORIZONTAL)
                vbox1.AddSpacer(20)
                self.sizer3.Add(vbox1, 1, flag=wx.ALIGN_CENTER_HORIZONTAL)
                self.sizer3.AddSpacer(200)
                self.sizer3.Layout()

        self.panel1.SendSizeEvent()
        self.panel1.Layout()
        self.panel2.SendSizeEvent()
        self.panel2.Layout()
        self.panel3.SendSizeEvent()
        self.panel3.Layout()
        pub.sendMessage('RESIZE_CELLS', data = None)
        self.psizer1.Layout()
        self.psizer2.Layout()
        self.psizer3.Layout()
        self.mainSizer.Layout()
        # self.SendSizeEvent()        
        # self.Layout()

    def OnListClick(self, evt):
        sel = self.listboxTeacher.GetSelection()
        if sel == -1:
            sel = self.listboxVenue.GetSelection()
            if sel == -1:
                sel = self.listboxClass.GetSelection()
                text = self.listboxClass.GetString(sel)
                self.panel3.Scroll(-1, 0)
                self.panel3.ScrollChildIntoView(getattr(self,text))
            else:
                text = self.listboxVenue.GetString(sel)
                self.panel2.Scroll(-1, 0)
                self.panel2.ScrollChildIntoView(getattr(self,text))
        else:
            text = self.listboxTeacher.GetString(sel)
            self.panel1.Scroll(-1, 0)
            self.panel1.ScrollChildIntoView(getattr(self,text))

        self.listboxTeacher.SetSelection(-1)
        self.listboxVenue.SetSelection(-1)
        self.listboxClass.SetSelection(-1)
    
        # self.panel1.SetFocus()
    # def KeyPressed(self, event):        
    #     # If PageUp is pressed...

    #     # If PageDown is pressed...
    #     k = event.GetKeyCode()
    #     if  k == 366 or k == 367:
    #         if k == 366:
    #             n = 1
    #         else:
    #             n = -1
    #         sel = self.listboxTeacher.GetSelection()
    #         if sel == -1:
    #             sel = self.listboxVenue.GetSelection()
    #             if sel == -1:
    #                 sel = self.listboxClass.GetSelection()
    #                 try:
    #                     text = self.listboxClass.GetString(sel+n)
    #                 except:
    #                     text = self.listboxClass.GetString(sel)
    #                 self.panel3.Scroll(-1, 0)
    #                 self.panel3.ScrollChildIntoView(getattr(self,text))
    #             else:
    #                 try:
    #                     text = self.listboxVenue.GetString(sel+n)
    #                 except:
    #                     text = self.listboxVenue.GetString(sel)                    
    #                 self.panel2.Scroll(-1, 0)
    #                 self.panel2.ScrollChildIntoView(getattr(self,text))
    #         else:
    #             try:
    #                 text = self.listboxTeacher.GetString(sel+n)
    #             except:
    #                 text = self.listboxVenue.GetString(sel)
    #             self.panel1.Scroll(-1, 0)
    #             self.panel1.ScrollChildIntoView(getattr(self,text))

    #     #Skip other Key events
    #     if event.GetKeyCode():
    #         print event.GetKeyCode()
    #         event.Skip()
    #         return

    def RenewUI(self, flag):

        self.mainPanel = wx.Panel(self, -1)
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.book = wx.Notebook(self.mainPanel, -1, style=(wx.NB_BOTTOM))

        self.page1 = wx.Panel(self.book, -1)
        self.psizer1 = wx.BoxSizer(wx.HORIZONTAL)
        self.left1 = wx.lib.scrolledpanel.ScrolledPanel(parent=self.page1, id = -1)
        self.left1.SetupScrolling()
        self.lsizer1 = wx.BoxSizer(wx.VERTICAL)        
        self.panel1 = wx.lib.scrolledpanel.ScrolledPanel(parent=self.page1, id = -1)
        self.panel1.SetupScrolling()
        self.sizer1 = wx.BoxSizer(wx.VERTICAL)

        self.page2 = wx.Panel(self.book, -1)
        self.psizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.left2 = wx.lib.scrolledpanel.ScrolledPanel(parent=self.page2, id = -1)
        self.left2.SetupScrolling()
        self.lsizer2 = wx.BoxSizer(wx.VERTICAL)
        self.panel2 = wx.lib.scrolledpanel.ScrolledPanel(parent=self.page2, id = -1)
        self.panel2.SetupScrolling()
        self.sizer2 = wx.BoxSizer(wx.VERTICAL)

        self.page3 = wx.Panel(self.book, -1)
        self.psizer3 = wx.BoxSizer(wx.HORIZONTAL)
        self.left3 = wx.lib.scrolledpanel.ScrolledPanel(parent=self.page3, id = -1)
        self.left3.SetupScrolling()
        self.lsizer3 = wx.BoxSizer(wx.VERTICAL)
        self.panel3 = wx.lib.scrolledpanel.ScrolledPanel(parent=self.page3, id = -1)
        self.panel3.SetupScrolling()
        self.sizer3 = wx.BoxSizer(wx.VERTICAL)


        self.fonth1 = wx.Font(18, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
        self.fonth2 = wx.Font(16, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
        self.fonth3 = wx.Font(16, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
        self.fonth4 = wx.Font(12, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
        self.sfont = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        self.sfont.SetPointSize(10)


        # self.panel1.Bind(wx.EVT_SCROLLWIN_PAGEDOWN, self.OnPageDown) 
        # self.panel1.Bind(wx.EVT_SCROLLWIN_PAGEUP, self.OnPageUp) 

        self.panel1.SetSizer(self.sizer1)
        self.panel2.SetSizer(self.sizer2)
        self.panel3.SetSizer(self.sizer3)

        # wx.EVT_KEY_DOWN(self, self.KeyPressed)  


        self.listboxTeacher = wx.ListBox(self.left1, -1,size=(90,400), style=wx.LB_SORT)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.OnListClick)
        libox = wx.BoxSizer(wx.VERTICAL)
        libox.Add(self.listboxTeacher, 1, flag=wx.EXPAND)

        labelside = wx.StaticText(self.left1, label='Jump To:')
        labelside.SetFont(self.sfont)
        lbox = wx.BoxSizer(wx.VERTICAL)
        lbox.Add(labelside, 1, flag=wx.EXPAND)

        self.lsizer1.AddSpacer(150)
        self.lsizer1.Add(libox, 1,flag=wx.EXPAND)
        self.lsizer1.AddSpacer(20)        
        self.lsizer1.Add(lbox, 1, flag=wx.EXPAND)
        self.left1.SetSizer(self.lsizer1)

        self.psizer1.AddSpacer(20)
        self.psizer1.Add(self.left1, 1, wx.ALIGN_CENTER|wx.EXPAND)
        self.psizer1.AddSpacer(50)
        self.psizer1.Add(self.panel1, 6, wx.ALIGN_CENTER|wx.EXPAND)
        self.page1.SetSizer(self.psizer1)


        self.listboxVenue = wx.ListBox(self.left2, -1,size=(90,400), style=wx.LB_SORT)
        libox = wx.BoxSizer(wx.VERTICAL)
        libox.Add(self.listboxVenue, 1, flag=wx.EXPAND)

        labelside = wx.StaticText(self.left2, label='Jump To:')
        labelside.SetFont(self.sfont)
        lbox = wx.BoxSizer(wx.VERTICAL)
        lbox.Add(labelside, 1, flag=wx.EXPAND)

        self.lsizer2.AddSpacer(150)
        self.lsizer2.Add(libox, 1, wx.EXPAND)
        self.lsizer2.AddSpacer(20)        
        self.lsizer2.Add(lbox, 1, wx.EXPAND)
        self.left2.SetSizer(self.lsizer2)

        self.psizer2.AddSpacer(20)
        self.psizer2.Add(self.left2, 1, wx.ALIGN_CENTER|wx.EXPAND)
        self.psizer2.AddSpacer(50)
        self.psizer2.Add(self.panel2, 6, wx.EXPAND)
        self.page2.SetSizer(self.psizer2)

        self.listboxClass = wx.ListBox(self.left3, -1,size=(90,400), style=wx.LB_SORT)
        libox = wx.BoxSizer(wx.VERTICAL)
        libox.Add(self.listboxClass, 1, wx.EXPAND)

        labelside = wx.StaticText(self.left3, label='Jump To:')
        labelside.SetFont(self.sfont)
        lbox = wx.BoxSizer(wx.VERTICAL)
        lbox.Add(labelside, 1, wx.EXPAND)

        self.lsizer3.AddSpacer(150)
        self.lsizer3.Add(libox, 1, wx.EXPAND)
        self.lsizer3.AddSpacer(20)        
        self.lsizer3.Add(lbox, 1, wx.EXPAND)
        self.left3.SetSizer(self.lsizer3)

        self.psizer3.AddSpacer(20)
        self.psizer3.Add(self.left3, 1, wx.ALIGN_CENTER|wx.EXPAND)
        self.psizer3.AddSpacer(50)
        self.psizer3.Add(self.panel3, 6, wx.EXPAND)
        self.page3.SetSizer(self.psizer3)

        self.book.AddPage(self.page3, "Class")
        self.book.AddPage(self.page2, "Venue") 
        self.book.AddPage(self.page1, "Teacher")

        self.mainSizer.Add(self.book, 1, wx.EXPAND)
        self.mainPanel.SetSizer(self.mainSizer)

        pub.subscribe(self.update, 'UPDATE_VIEW') 
        # self.Bind(gridlib.EVT_GRID_LABEL_RIGHT_CLICK, self.update)    

        self.Maximize(True)
        self.psizer1.Layout()
        self.psizer2.Layout()
        self.psizer3.Layout()
        self.mainSizer.Layout()
        if not flag :
            dlg = wx.MessageDialog(None, "Create a New Project:\nFile -> New\nOr Open an Existing one:\nFile -> Open","Notice", wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()


    def __init__(self, flag):
        wx.Frame.__init__(self,parent=None, title="Timetable Management", size=(1024,1000))
        self._init_menubar()
        self._init_toolbar()
        self.BasicRequirements = False
        # self.Bind(wx.EVT_ENTER_WINDOW, lambda event: self.SetFocus())
        if flag :
            self.RenewUI(flag)
            self.savefilepath = sys.argv[1]
            self.PostOpenPath(sys.argv[1])
        else:
            self.RenewUI(flag)

        wx.EVT_KEY_DOWN(self, self.KeyPressed) 

    def KeyPressed(self, event):        
        # If PageUp is pressed...

        # If PageDown is pressed...
        if event.GetKeyCode() == 366:
            print 'PageU'
            # self.parent.SetFocus()
            # print self.parent.GetViewStart()
            event.Skip()

        if event.GetKeyCode() == 367:
            print 'PageD'
            # self.parent.SetFocus()
            # print self.parent.GetViewStart()
            event.Skip()
            # return

        if event.GetKeyCode():
            # print event.GetKeyCode()
            # event.ResumePropagation(1)
            event.Skip()
            return

    def OnQuit(self, evt):
        dlg = wx.MessageDialog(None, "Do you really want to quit?", "Confirm", wx.YES_NO|wx.ICON_QUESTION)
        res = dlg.ShowModal()
        if res == wx.ID_NO:
            dlg.Destroy()
            return
        self.Close()

    def ExportODS(self, evt):
        if not self.BasicRequirements:
            self.ErrorBox('Please Define Constraints First')
            return

        import ezodf
        # ods = ezodf.newdoc('ods')

        if os.path.isfile('/usr/share/ttmanager/styling_reference.ods'):
            ods = ezodf.newdoc('ods', template='/usr/share/ttmanager/styling_reference.ods')
        else :
            try:
                ods = ezodf.newdoc('ods', template='styling_reference.ods')
            except:
                self.ErrorBox("Styling Reference Not Found")
                return
        saveFileDialog = wx.FileDialog(self, "Save Project File As", "", ".ods",
                                               "ods files (*.ods)|*.ods", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if saveFileDialog.ShowModal() == wx.ID_CANCEL:
            return
        savefilepath = saveFileDialog.GetPath()

        dlg = wx.ProgressDialog("Exporting Project",
                               "Please wait while project is exported",
                               maximum = 10,
                               parent=self,
                               style = wx.PD_APP_MODAL|wx.PD_AUTO_HIDE)
        # ods.inject_style(""" <style:style style:name="heading" style:family="table-cell" style:parent-style-name="Default"><style:text-properties style:vertical-align="top" style:use-window-font-color="true" style:repeat-content="false" style:text-outline="false" style:text-line-through-style="none" style:text-line-through-type="none" style:font-name="Liberation Serif" fo:font-size="22pt" fo:language="en" fo:country="IN" fo:font-style="normal" fo:text-shadow="none" style:text-underline-style="none" fo:font-weight="bold" style:text-underline-mode="continuous" style:text-overline-mode="continuous" style:text-line-through-mode="continuous" style:font-size-asian="22pt" style:language-asian="zh" style:country-asian="CN" style:font-style-asian="normal" style:font-weight-asian="normal" style:font-size-complex="22pt" style:language-complex="hi" style:country-complex="IN" style:font-style-complex="normal" style:font-weight-complex="normal" style:text-emphasize="none" style:font-relief="none" style:text-overline-style="none" style:text-overline-color="font-color"/></style:style>""")
        # ods.inject_style(""" <style:style style:name="cell" style:family="table-cell" style:parent-style-name="Default"><style:table-cell-properties fo:border-bottom="0.06pt solid #000000" style:text-align-source="fix" style:repeat-content="false" fo:border-left="2.49pt solid #000000" fo:border-right="0.06pt solid #000000" fo:border-top="0.06pt solid #000000" style:vertical-align="top"/><style:paragraph-properties fo:text-align="center"/><style:text-properties style:use-window-font-color="true" style:text-outline="false" style:text-line-through-style="none" style:text-line-through-type="none" style:font-name="Liberation Serif" fo:font-size="22pt" fo:language="en" fo:country="IN" fo:font-style="normal" fo:text-shadow="none" style:text-underline-style="none" fo:font-weight="bold" style:text-underline-mode="continuous" style:text-overline-mode="continuous" style:text-line-through-mode="continuous" style:font-size-asian="10pt" style:language-asian="zh" style:country-asian="CN" style:font-style-asian="normal" style:font-weight-asian="normal" style:font-size-complex="10pt" style:language-complex="hi" style:country-complex="IN" style:font-style-complex="normal" style:font-weight-complex="normal" style:text-emphasize="none" style:font-relief="none" style:text-overline-style="none" style:text-overline-color="font-color"/></style:style> """)

        #static size change it later
        dlg.Update(2)
        xx = len(globaldata.all_teachers) * 60
        yy = 50
        sheetT = ezodf.Sheet('Teacher', size=(xx,yy))
        xx = len(globaldata.all_venues) * 60
        yy = 50        
        sheetV = ezodf.Sheet('Venue', size=(xx,yy))
        xx = len(globaldata.all_classes) * 120
        yy = 50        
        sheetC = ezodf.Sheet('Class', size=(xx,yy))

        ods.sheets += sheetT
        ods.sheets += sheetV
        ods.sheets += sheetC

        del ods.sheets[0]
        i = 0
        for t in globaldata.all_venues:
            resMat = getattr(self, t.name).getODSData()
            sheetV[i+4, 5].set_value(globaldata.header1) 
            sheetV[i+4, 5].style_name = 'ce11'
            sheetV[i+6, 4].set_value(globaldata.header2) 
            sheetV[i+6, 4].style_name = 'ce1'
            sheetV[i+8, 6].set_value(globaldata.header3) 
            sheetV[i+8, 6].style_name = 'ce17'
            head = 'Timetable for Venue : %s ' % t.name
            # if t.name in globaldata.venue_class_map.keys():
            #     head += 'Class : %s ' % globaldata.venue_class_map[t.name]
            sheetV[i+10, 6].set_value(head) 
            sheetV[i+10, 6].style_name = 'ce13'
            #upper row 
            sheetV[i+12, 3].set_value('')
            sheetV[i+12, 3].style_name = 'ce5'
            for l in range(1, len(globaldata.colLabels)+1):
                sheetV[i+12, 3+l].set_value(globaldata.colLabels[l-1])
                sheetV[i+12, 3+l].style_name = "ce8"
            #fix last one in first row
            sheetV[i+12, 3+len(globaldata.colLabels)].style_name = "ce21"
            #first col
            for l in range(1, globaldata.days_per_week+1):
                sheetV[i+12+l, 3].set_value(globaldata.rowLabels[l-1])
                sheetV[i+12+l, 3].style_name = "ce6"
            #fix last one in first col
            sheetV[i+12 + globaldata.days_per_week, 3].style_name = "ce7"

            for l in range(1, globaldata.days_per_week+1):
                for m in range(1, globaldata.lectures_per_day+1):
                    # print 'yo', resMat[l-1][m-1]
                    sheetV[i+12+l, 3+m].set_value(resMat[l-1][m-1])
                    sheetV[i+12+l, 3+m].style_name = "ce9"
            #fix last row
            for m in range(1, globaldata.lectures_per_day+1):
                sheetV[i+12+globaldata.days_per_week, 3+m].style_name = "ce10"
            #fix last col
            for l in range(1, globaldata.days_per_week+1):
                sheetV[i+12+l, 3+globaldata.lectures_per_day].style_name = "ce22"
            #fix last corner
            sheetV[i+12+globaldata.days_per_week, 3+globaldata.lectures_per_day].style_name = "ce23"
            i += 25
        i = 0
        dlg.Update(5)
        for t in globaldata.all_teachers:
            resMat = getattr(self, t.name).getODSData()
            sheetT[i+4, 5].set_value(globaldata.header1) 
            sheetT[i+4, 5].style_name = 'ce11'
            sheetT[i+6, 4].set_value(globaldata.header2) 
            sheetT[i+6, 4].style_name = 'ce1'
            sheetT[i+8, 6].set_value(globaldata.header3) 
            sheetT[i+8, 6].style_name = 'ce17'
            head = 'Timetable for Teacher : %s \t\t' % t.name
            sheetT[i+10, 6].set_value(head) 
            sheetT[i+10, 6].style_name = 'ce13'
            #upper row 
            sheetT[i+12, 3].set_value('')
            sheetT[i+12, 3].style_name = 'ce5'
            for l in range(1, len(globaldata.colLabels)+1):
                sheetT[i+12, 3+l].set_value(globaldata.colLabels[l-1])
                sheetT[i+12, 3+l].style_name = "ce8"
            #fix last one in first row
            sheetT[i+12, 3+len(globaldata.colLabels)].style_name = "ce21"
            #first col
            for l in range(1, len(globaldata.rowLabels)+1):
                sheetT[i+12+l, 3].set_value(globaldata.rowLabels[l-1])
                sheetT[i+12+l, 3].style_name = "ce6"
            #fix last one in first col
            sheetT[i+12 + len(globaldata.rowLabels), 3].style_name = "ce7"

            for l in range(1, globaldata.days_per_week+1):
                for m in range(1, globaldata.lectures_per_day+1):
                    # print 'yo', resMat[l-1][m-1]
                    sheetT[i+12+l, 3+m].set_value(resMat[l-1][m-1])
                    sheetT[i+12+l, 3+m].style_name = "ce9"
            #fix last row
            for m in range(1, globaldata.lectures_per_day+1):
                sheetT[i+12+globaldata.days_per_week, 3+m].style_name = "ce10"
            #fix last col
            for l in range(1, globaldata.days_per_week+1):
                sheetT[i+12+l, 3+globaldata.lectures_per_day].style_name = "ce22"
            #fix last corner
            sheetT[i+12+globaldata.days_per_week, 3+globaldata.lectures_per_day].style_name = "ce23"
            i += 25
        i = 0
        dlg.Update(7)
        for t in globaldata.all_classes:
            resMat = getattr(self, t.name).getODSData()
            sheetC[i+4, 5].set_value(globaldata.header1) 
            sheetC[i+4, 5].style_name = 'ce11'
            sheetC[i+6, 4].set_value(globaldata.header2) 
            sheetC[i+6, 4].style_name = 'ce1'
            sheetC[i+8, 6].set_value(globaldata.header3) 
            sheetC[i+8, 6].style_name = 'ce17'
            head = 'Timetable for Class : %s \t\t' % t.name
            if t.name in globaldata.class_venue_map.keys():
                head += 'Venue : %s ' % globaldata.class_venue_map[t.name]

            sheetC[i+10, 6].set_value(head) 
            sheetC[i+10, 6].style_name = 'ce13'
            #upper row 
            sheetC[i+12, 3].set_value('')
            sheetC[i+12, 3].style_name = 'ce5'
            for l in range(1, len(globaldata.colLabels)+1):
                sheetC[i+12, 3+l].set_value(globaldata.colLabels[l-1])
                sheetC[i+12, 3+l].style_name = "ce8"
            #fix last one in first row
            sheetC[i+12, 3+len(globaldata.colLabels)].style_name = "ce21"
            #first col
            for l in range(1, len(globaldata.rowLabels)+1):
                sheetC[i+12+l, 3].set_value(globaldata.rowLabels[l-1])
                sheetC[i+12+l, 3].style_name = "ce6"
            #fix last one in first col
            sheetC[i+12 + len(globaldata.rowLabels), 3].style_name = "ce7"

            for l in range(1, globaldata.days_per_week+1):
                for m in range(1, globaldata.lectures_per_day+1):
                    # print 'yo', resMat[l-1][m-1]
                    sheetC[i+12+l, 3+m].set_value(resMat[l-1][m-1])
                    sheetC[i+12+l, 3+m].style_name = "ce9"
            #fix last row
            for m in range(1, globaldata.lectures_per_day+1):
                sheetC[i+12+globaldata.days_per_week, 3+m].style_name = "ce10"
            #fix last col
            for l in range(1, globaldata.days_per_week+1):
                sheetC[i+12+l, 3+globaldata.lectures_per_day].style_name = "ce22"
            #fix last corner
            sheetC[i+12+globaldata.days_per_week, 3+globaldata.lectures_per_day].style_name = "ce23"
            i += 25
        dlg.Update(9)
        ods.saveas(savefilepath)
        dlg.Update(10)
        dlg.Destroy()
        self.SuccessBox('Exported Successfully')

    def ExportHTML(self, evt):

        if not self.BasicRequirements:
            self.ErrorBox('Please Define Constraints First')
            return

        saveFileDialog = wx.DirDialog (None, "Choose Directory", "",
                    wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
        if saveFileDialog.ShowModal() == wx.ID_CANCEL:
            return
        savefilepath = saveFileDialog.GetPath()

        import pdfkit
        src = "<HTML><BODY>"
        html = open(savefilepath + '/teacher.html', "w")
        for t in globaldata.all_teachers:
            src += getattr(self, t.name).getHTML()
        html.write(src)
        html.close()
        # pdfkit.from_string(src, 'teacher.pdf')
        src = "<HTML><BODY>"    
        html = open(savefilepath + '/venue.html', "w")
        for t in globaldata.all_venues:
            src += getattr(self, t.name).getHTML()
        html.write(src)
        html.close()
        # pdfkit.from_string(src, 'venue.pdf')
        src = "<HTML><BODY>"    
        html = open(savefilepath + '/class.html', "w")
        for t in globaldata.all_classes:
            src += getattr(self, t.name).getHTML()
        html.write(src)
        html.close()
        # pdfkit.from_string(src,'class.pdf')

        dlg = wx.MessageDialog(None, "Exported Successfully", "Notice", wx.OK|wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def ExportPDF(self, evt):
        if not self.BasicRequirements:
            self.ErrorBox('Please Define Constraints First')
            return

        import pdfkit
        saveFileDialog = wx.DirDialog (None, "Choose Directory", "",
                    wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
        if saveFileDialog.ShowModal() == wx.ID_CANCEL:
            return
        savefilepath = saveFileDialog.GetPath()

        dlg = wx.ProgressDialog("Exporting Project",
                               "Please wait while project is exported",
                               maximum = 10,
                               parent=self,
                               style = wx.PD_APP_MODAL|wx.PD_AUTO_HIDE)
        dlg.Update(2)
        src = "<HTML><BODY>"
        # html = open('teacher.html', "w")
        for t in globaldata.all_teachers:
            src += getattr(self, t.name).getHTML()
        # html.write(src)
        # html.close()
        dlg.Update(5)
        pdfkit.from_string(src, savefilepath + '/teacher.pdf')
        src = "<HTML><BODY>"    
        # html = open('venue.html', "w")
        for t in globaldata.all_venues:
            src += getattr(self, t.name).getHTML()
        # html.write(src)
        # html.close()
        dlg.Update(8)
        pdfkit.from_string(src, savefilepath + '/venue.pdf')
        src = "<HTML><BODY>"    
        # html = open('class.html', "w")
        for t in globaldata.all_classes:
            src += getattr(self, t.name).getHTML()
        # html.write(src)
        # html.close()
        pdfkit.from_string(src, savefilepath+ '/class.pdf')
        dlg.Update(10)
        dlg = wx.MessageDialog(None, "Exported Successfully", "Notice", wx.OK|wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def CheckActualConstraints(self):
        s = []
        for c in globaldata.all_classes:
            res = c.valid_lunch_break()
            print res
            if res != True:
                for m in res:
                    for key in m:
                        if c.name == key:
                            s.append("No Lunch Breaks for %s on %s\n" % (key, m[key]))
                        else:
                            s.append("No Lunch Breaks for %s-%s on %s\n" % (c.name, key, m[key]))
            res = c.check_workload()
            if res == False:
                s.append("Workload for Class %s is not within Limits\n" % c.name)
            res = c.check_subject_credits()
            if len(res) > 0:
                for sub in res:
                    p = ''
                    for e in res[sub]:
                        p += e + ' '
                    s.append("NoOfHours not Satisfied for %s for %s" % (sub, p))

        for t in globaldata.all_teachers:
            res = t.check_workload()
            # print 'teacher', res
            if res != True :
                if res == False:
                    s.append("Extra Workload for Teacher %s\n" % t.name)
                else:
                    temp = 'Extra Workload for %s on ' % t.name
                    for i in res:
                        temp += globaldata.rowLabels[i] + ', '
                    temp += '\n'
                    s.append(temp)

        return s

    def ReplaceFile(self, data):                    
        f = open('warning.data', 'w')
        f.write(data)
        f.close()

    def CheckConstraints(self, evt):
        #Check if file is exsisting else take it from the code below
        #   s = fromfile()
        #
        if not self.BasicRequirements:
            self.ErrorBox('Please Define Constraints First')
            return
        if os.path.isfile('warning.data') == True:
            f = open('warning.data')
            s = f.read()
            d = "\n"
            s =  [e+d for e in s.split(d) if e != ""]
            f.close()
        else: 
            s = self.CheckActualConstraints()
        # print s
        dlg = WarningView(self, s)
        dlg.ShowModal()
        if hasattr(dlg, 'result'):
            self.ReplaceFile(dlg.result)
        # dlg = ListView(self, title='Add Teacher Data', key='Teacher')
        # dlg.ShowModal()

            # dlg = warningx.MessageDialog(None, s, "filepath", wx.OK|wx.ICON_ERROR)
            # dlg.ShowModal()
            # dlg.Destroy()
        # pass
        # self.Close()

    def OnUndo(self, evt):
        self.Close()

    def OnOpen(self, evt):
        openFileDialog = wx.FileDialog(self, "Open Project File", "", "",
                                       "tt files (*.tt)|*.tt", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return 
        
        self.savefilepath = openFileDialog.GetPath()
        self.PostOpenPath(self.savefilepath)

    def PostOpenPath(self, filepath):
        dlg = wx.ProgressDialog("Loading Project",
                               "Please wait while project is loaded",
                               maximum = 10,
                               parent=self,
                               style = wx.PD_APP_MODAL|wx.PD_AUTO_HIDE)
        dlg.Update(1)
        with open(filepath, 'rb') as handle:
            try:
                saveObject = pickle.load(handle)
            except:
                dlg = wx.MessageDialog(None, "Could Not Open File", "Error", wx.OK|wx.ICON_ERROR)
                dlg.ShowModal()
                dlg.Destroy()
                return

        globaldata.header1 = saveObject.header1
        globaldata.header2 = saveObject.header2
        globaldata.header3 = saveObject.header3
        dlg.Update(2)

        globaldata.all_teachers = saveObject.all_teachers
        globaldata.all_venues = saveObject.all_venues
        globaldata.all_classes = saveObject.all_classes

        globaldata.subjects = saveObject.subjects
        dlg.Update(3)

        globaldata.days_per_week = saveObject.days_per_week
        globaldata.lectures_per_day = saveObject.lectures_per_day
        globaldata.daily_max = saveObject.daily_max
        globaldata.class_max = saveObject.class_max
        globaldata.start_time = saveObject.start_time
        globaldata.weekly_max = saveObject.weekly_max
        dlg.Update(4)

        globaldata.venueCapacity = saveObject.venueCapacity
        globaldata.classCapacity = saveObject.classCapacity

        globaldata.rowLabels = saveObject.rowLabels
        globaldata.colLables = saveObject.colLables

        globaldata.teacher_fullnames = saveObject.teacher_fullnames
        globaldata.teacher_shortnames = saveObject.teacher_shortnames
        globaldata.teacher_weeklymax = saveObject.teacher_weeklymax
        globaldata.teacher_dailymax = saveObject.teacher_dailymax
        dlg.Update(6)

        globaldata.venue_fullnames = saveObject.venue_fullnames
        globaldata.venue_shortnames = saveObject.venue_shortnames
        globaldata.venue_capacity = saveObject.venue_capacity

        globaldata.class_fullnames = saveObject.class_fullnames
        globaldata.class_shortnames = saveObject.class_shortnames
        globaldata.class_capacity = saveObject.class_capacity
        dlg.Update(7)

        globaldata.subject_fullnames = saveObject.subject_fullnames
        globaldata.subject_shortnames = saveObject.subject_shortnames
        globaldata.subject_credits = saveObject.subject_credits
        dlg.Update(8)

        globaldata.clipboard = saveObject.clipboard
        globaldata.teacher_class_map = saveObject.teacher_class_map
        globaldata.class_teacher_map = saveObject.class_teacher_map
        globaldata.teacher_subject_map = saveObject.teacher_subject_map
        globaldata.subject_teacher_map = saveObject.subject_teacher_map
        globaldata.venue_class_map = saveObject.venue_class_map
        globaldata.class_venue_map = saveObject.class_venue_map
        globaldata.class_subject_map = saveObject.class_subject_map
        globaldata.subject_class_map = saveObject.subject_class_map
        dlg.Update(9)
        self.BasicRequirements = True
        # self.AppendGlobalInput(None)
        self.MakeLables(None)
        self.update(None)
        dl = wx.MessageDialog(None, "Loaded Successfully", "Notice", wx.OK|wx.ICON_INFORMATION)
        dlg.Update(10)
        dlg.Destroy()
        dl.ShowModal()
        dl.Destroy()
        pub.sendMessage('RESIZE_CELLS', data = None)

    def OnSaveAs(self, evt):
        saveFileDialog = wx.FileDialog(self, "Save Project File As", "", ".tt",
                                               "tt files (*.tt)|*.tt", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if saveFileDialog.ShowModal() == wx.ID_CANCEL:
            return
        self.savefilepath = saveFileDialog.GetPath()
        self.OnSave(None)

    def OnSave(self, evt):
        if not self.BasicRequirements:
            self.ErrorBox('Please Enter Constraints First')
            return
        print 'saveing'
        saveObject = SaveClass()
        saveObject.header1 = globaldata.header1
        saveObject.header2 = globaldata.header2
        saveObject.header3 = globaldata.header3

        saveObject.all_teachers = globaldata.all_teachers
        saveObject.all_venues = globaldata.all_venues
        saveObject.all_classes = globaldata.all_classes

        saveObject.subjects = globaldata.subjects

        saveObject.days_per_week = globaldata.days_per_week
        saveObject.lectures_per_day = globaldata.lectures_per_day
        saveObject.daily_max = globaldata.daily_max
        saveObject.class_max = globaldata.class_max
        saveObject.start_time = globaldata.start_time
        saveObject.weekly_max = globaldata.weekly_max
        saveObject.venueCapacity = globaldata.venueCapacity
        saveObject.classCapacity = globaldata.classCapacity


        saveObject.rowLabels = globaldata.rowLabels
        saveObject.colLables = globaldata.colLabels

        saveObject.teacher_fullnames = globaldata.teacher_fullnames
        saveObject.teacher_shortnames = globaldata.teacher_shortnames
        saveObject.teacher_weeklymax = globaldata.teacher_weeklymax
        saveObject.teacher_dailymax = globaldata.teacher_dailymax


        saveObject.venue_fullnames = globaldata.venue_fullnames
        saveObject.venue_shortnames = globaldata.venue_shortnames
        saveObject.venue_capacity = globaldata.venue_capacity

        saveObject.class_fullnames = globaldata.class_fullnames
        saveObject.class_shortnames = globaldata.class_shortnames
        saveObject.class_capacity = globaldata.class_capacity

        saveObject.subject_fullnames = globaldata.subject_fullnames
        saveObject.subject_shortnames = globaldata.subject_shortnames
        saveObject.subject_credits = globaldata.subject_credits

        saveObject.clipboard = globaldata.clipboard
        saveObject.teacher_class_map = globaldata.teacher_class_map
        saveObject.class_teacher_map = globaldata.class_teacher_map
        saveObject.teacher_subject_map = globaldata.teacher_subject_map
        saveObject.subject_teacher_map = globaldata.subject_teacher_map
        saveObject.venue_class_map = globaldata.venue_class_map
        saveObject.class_venue_map = globaldata.class_venue_map
        saveObject.class_subject_map = globaldata.class_subject_map
        saveObject.subject_class_map = globaldata.subject_class_map

        if not hasattr(self, "savefilepath"):
            saveFileDialog = wx.FileDialog(self, "Save Project File", "", ".tt",
                                               "tt files (*.tt)|*.tt", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
            if saveFileDialog.ShowModal() == wx.ID_CANCEL:
                return
            self.savefilepath = saveFileDialog.GetPath()

        with open(self.savefilepath, 'wb') as handle:
            try :
                pickle.dump(saveObject, handle)
            except:
                dlg = wx.MessageDialog(None, "Could Not Save File", "Error", wx.OK|wx.ICON_ERROR)
                dlg.ShowModal()
                dlg.Destroy()
                return

        dlg = wx.MessageDialog(None, "Saved Successfully", "Notice", wx.OK|wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    # def AppendGlobalInput(self, evt):
    #     if not hasattr(self, "GlobalInput"):
    #         GlobalInput = [[None for i in range(globaldata.lectures_per_day)] for j in range(globaldata.days_per_week)]
    #         self.GlobalInput = MyGrid(self.panel1, GlobalInput, "GlobalInput", 'None')

    #         hfirst = wx.StaticText(self.panel1, label=globaldata.header1)
    #         hsecond = wx.StaticText(self.panel1, label=globaldata.header2)
    #         hthird = wx.StaticText(self.panel1, label=globaldata.header3)
    #         hthird.SetForegroundColour(wx.Colour(255,55,125))
    #         hfourth = wx.StaticText(self.panel1, label='Global Input Screen :')
    #         hfirst.SetFont(self.fonth1)
    #         hsecond.SetFont(self.fonth2)
    #         hthird.SetFont(self.fonth3)
    #         hfourth.SetFont(self.fonth4)

    #         vbox = wx.BoxSizer(wx.VERTICAL)
    #         vbox.AddSpacer(150)
    #         vbox.Add(hfirst, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)
    #         vbox.AddSpacer(10)
    #         vbox.Add(hsecond, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)
    #         vbox.AddSpacer(2)
    #         vbox.Add(hthird, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)
    #         vbox.AddSpacer(10)
    #         vbox.Add(hfourth, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)
    #         vbox.AddSpacer(20)

    #         vbox1 = wx.BoxSizer(wx.VERTICAL)        
    #         vbox1.Add(self.GlobalInput, 1, flag=wx.ALIGN_CENTER_HORIZONTAL)
    #         vbox1.AddSpacer(200)
            
    #         self.sizer1.Add(vbox, 1, wx.EXPAND)
    #         self.sizer1.Add(vbox1, 1, wx.EXPAND)
    #         # self.panel1.Layout()
    #         self.sizer1.Layout()
    #         self.psizer1.Layout()
    #         # self.Close()
    #         # self.listboxTeacher.Append("GlobalInput")

    # def AppendFirstEntry(self, value, panel, sizer, typeOf):
    #     # if not hasattr(self, "GlobalInput"):
    #     temp = [[None for i in range(globaldata.lectures_per_day)] for j in range(globaldata.days_per_week)]
    #     setattr(self, value, MyGrid(panel, temp, value, typeOf))

    #     hfirst = wx.StaticText(panel, label=globaldata.header1)
    #     hsecond = wx.StaticText(panel, label=globaldata.header2)
    #     hthird = wx.StaticText(panel, label=globaldata.header3)
    #     hthird.SetForegroundColour(wx.Colour(255,55,125))
    #     hfourth = wx.StaticText(panel, label='Timetable For ' + typeOf + ':' + value)
    #     hfirst.SetFont(self.fonth1)
    #     hsecond.SetFont(self.fonth2)
    #     hthird.SetFont(self.fonth3)
    #     hfourth.SetFont(self.fonth4)

    #     vbox = wx.BoxSizer(wx.VERTICAL)
    #     vbox.AddSpacer(150)
    #     vbox.Add(hfirst, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)
    #     vbox.AddSpacer(10)
    #     vbox.Add(hsecond, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)
    #     vbox.AddSpacer(2)
    #     vbox.Add(hthird, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)
    #     vbox.AddSpacer(10)
    #     vbox.Add(hfourth, 0, flag=wx.ALIGN_CENTER_HORIZONTAL)
    #     vbox.AddSpacer(20)

    #     vbox1 = wx.BoxSizer(wx.VERTICAL)        
    #     vbox1.Add(getattr(self, value) , 1, flag=wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL)
    #     vbox1.AddSpacer(200)

    #     sizer.Add(vbox, 1, wx.EXPAND)
    #     sizer.Add(vbox1, 1, wx.EXPAND)
    #     sizer.Layout()
    #     if typeOf == "Teacher":
    #         self.listboxTeacher.Append(value)
    #     if typeOf == "Venue":
    #             self.listboxVenue.Append(value)
    #     if typeOf == "Class":
    #             self.listboxClass.Append(value)

    def MakeLables(self, evt):
        # print globaldata.start_time
        if len(globaldata.start_time) == 2:
            h = int(globaldata.start_time[0])
            m = int(globaldata.start_time[1])
            for i in range(globaldata.lectures_per_day):
                aa = str(h+i)
                bb = str(m)
                cc = str(h+i+1)
                globaldata.colLabels.append('%s:%s-%s:%s' % (aa, bb, cc, bb))
        else:
            h = int(globaldata.start_time[0])
            for i in range(globaldata.lectures_per_day):
                aa = str(h+i)
                bb = str(h+i+1)
                globaldata.colLabels.append('%s-%s' % (aa, bb))

    def GetBasicConstraints(self, evt):
        # print 'ccliked'
        dlg = BasicConstraint(self)
        dlg.ShowModal()
        if hasattr(dlg, 'days') and hasattr(dlg, 'lectures') and hasattr(dlg, 'class_max') and hasattr(dlg, 'start_time'):
            # print dlg.daily_max, dlg.weekly_max, dlg.class_max
            globaldata.days_per_week = int(dlg.days)
            globaldata.lectures_per_day = int(dlg.lectures)
            # globaldata.daily_max = int(dlg.daily_max)
            # globaldata.daily_min = int(dlg.daily_min)
            globaldata.class_max = int(dlg.class_max)
            globaldata.start_time = dlg.start_time.split(':')
            self.MakeLables(evt)
            # diff = globaldata.lectures_per_day - len(globaldata.colLabels)
            # temp = []
            # if diff > 0 :
            #     temp = ['.'] * diff
            # globaldata.colLabels.extend(temp)
            # globaldata.weekly_max = int(dlg.weekly_max)
            # globaldata.weekly_min = int(dlg.weekly_min)
        # print len(self.__dict__)
        # for i in  self.__dict__ :
        #     print i
        # self.AppendGlobalInput(None)
        self.BasicRequirements = True
    
    def OnNew(self, evt):
        # print len(self.__dict__)
        globaldata.colLabels = []
        if len(self.__dict__) > 33:    #default attr are 32
            #here add confimation to save or not
            dlg = wx.MessageDialog(None, "Do you want to save existing timetable?", "Confirm", wx.CANCEL|wx.YES_NO|wx.ICON_QUESTION)
            res = dlg.ShowModal()
            if res == wx.ID_CANCEL:
                dlg.Destroy()
                return
            if res == wx.ID_YES:
                print 'yes'
                self.OnSave(None)    
            os.execl(sys.executable, sys.executable, sys.argv[0])

        dlg = HeaderInfo(self)
        dlg.ShowModal()
        if hasattr(dlg, 'result1') and hasattr(dlg, 'result2') and hasattr(dlg, 'result3'):
            globaldata.header1 = dlg.result1
            globaldata.header2 = dlg.result2
            globaldata.header3 = dlg.result3  
        else:
            return
        self.GetBasicConstraints(evt)

        dlg = wx.MessageDialog(None, "For ease of use add Teacher, Venue and Class data under:\nData->Teacher\nData->Venue\nData->Class","Notice", wx.OK|wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    # def ShowFirstGrid(self, type):
    #     if type == 'Teacher':
    #         if len(globaldata.teacher_shortnames) > 1:
    #             project.push_object(globaldata.teacher_shortnames[1], 'Teacher')
    #             pub.sendMessage('UPDATE_VIEW', data = None)
    #             # self.AppendFirstEntry(globaldata.teacher_shortnames[1], self.panel1, self.sizer1, 'Teacher')
    #     if type == 'Venue':
    #         if len(globaldata.venue_shortnames) > 1:
    #             project.push_object(globaldata.venue_shortnames[1], 'Venue')
    #             pub.sendMessage('UPDATE_VIEW', data = None)
    #     if type == 'Class':
    #         if len(globaldata.class_shortnames) > 1:
    #             project.push_object(globaldata.class_shortnames[1], 'Class')
    #             pub.sendMessage('UPDATE_VIEW', data = None)

    def TeacherData(self, evt):
        if not self.BasicRequirements:
            self.ErrorBox('Please Define Constraints First')
            return

        # print len(self.__dict__)
        # global teacher_fullnames, teacher_shortnames
        dlg = ListView(self, title='Add Teacher Data', key='Teacher')
        dlg.ShowModal()
        if hasattr(dlg, 'result1') and hasattr(dlg, 'result2') and hasattr(dlg, 'result3') and hasattr(dlg, 'result4'):
            globaldata.teacher_fullnames = dlg.result1
            temp = ["ADD NEW"]
            temp.extend(dlg.result2)
            globaldata.teacher_shortnames = temp
            globaldata.teacher_weeklymax = dlg.result3
            globaldata.teacher_dailymax = dlg.result4
            for t in globaldata.teacher_shortnames:
                t = t.split('-')[0]
                if t != "ADD NEW" and not hasattr(self, t):
                    project.push_object(t, 'Teacher')
                    pub.sendMessage('UPDATE_VIEW', data = None)
            # if len(self.__dict__) == 32:    #default attr are 32
            #     self.ShowFirstGrid('Teacher')

    def VenueData(self, evt):
        if not self.BasicRequirements:
            self.ErrorBox('Please Define Constraints First')
            return

        # global venue_fullnames, venue_shortnames
        dlg = ListView(self, title='Add Venue Data', key='Venue')
        dlg.ShowModal()
        if hasattr(dlg, 'result1') and hasattr(dlg, 'result2') and hasattr(dlg, 'result3'):    
            globaldata.venue_fullnames = dlg.result1
            temp = ["ADD NEW"]
            temp.extend(dlg.result2) 
            globaldata.venue_shortnames =  temp      
            globaldata.venue_capacity = dlg.result3
            for t in globaldata.venue_shortnames:
                t = t.split('-')[0]
                if t != "ADD NEW" and not hasattr(self, t):
                    project.push_object(t, 'Venue')
                    pub.sendMessage('UPDATE_VIEW', data = None)

    def ClassData(self, evt):
        if not self.BasicRequirements:
            self.ErrorBox('Please Define Constraints First')
            return

        # global class_fullnames, class_shortnames
        dlg = ListView(self, title='Add Class Data', key='Class')
        dlg.ShowModal()
        if hasattr(dlg, 'result1') and hasattr(dlg, 'result2') and hasattr(dlg, 'result3'):
            globaldata.class_fullnames = dlg.result1
            temp = ["ADD NEW"]
            temp.extend(dlg.result2)
            globaldata.class_shortnames = temp
            globaldata.class_capacity = dlg.result3
            for t in globaldata.class_shortnames:
                t = t.split('-')[0]
                if t != "ADD NEW" and not hasattr(self, t):
                    project.push_object(t, 'Class')
                    pub.sendMessage('UPDATE_VIEW', data = None)

    def SubjectData(self, evt):
        if not self.BasicRequirements:
            self.ErrorBox('Please Define Constraints First')
            return

        dlg = ListView(self, title='Add Subject Data', key='Subject')
        dlg.ShowModal()
        if hasattr(dlg, 'result1') and hasattr(dlg, 'result2') and hasattr(dlg, 'result3'):
            globaldata.subject_fullnames = dlg.result1
            temp = ["ADD NEW"]  
            temp.extend(dlg.result2)
            globaldata.subject_shortnames = temp
            globaldata.subject_credits = dlg.result3
            for i in range(len(dlg.result2)):
                globaldata.subjects[dlg.result2[i]] = dlg.result3[i]

    def TeacherClass(self, evt):
        if not self.BasicRequirements:
            self.ErrorBox('Please Define Constraints First')
            return

        dlg = ListView(self, title='Add Mapping', label1="Teacher", label2="Class / Batch")
        dlg.ShowModal()
        if hasattr(dlg, 'result1') and hasattr(dlg, 'result2'):
            teacher_class_map = {}
            class_teacher_map = {}

            for i in range(len(dlg.result1)):
                teacher_class_map[dlg.result1[i]] = dlg.result2[i]
                class_teacher_map[dlg.result2[i]] = dlg.result1[i]

            globaldata.teacher_class_map = teacher_class_map
            globaldata.class_teacher_map = class_teacher_map

    def TeacherSubject(self, evt):
        if not self.BasicRequirements:
            self.ErrorBox('Please Define Constraints First')
            return

        dlg = ListView(self, title='Add Mapping', label1="Teacher", label2="Subject")
        dlg.ShowModal()
        if hasattr(dlg, 'result1') and hasattr(dlg, 'result2'):
            teacher_subject_map = {}
            subject_teacher_map = {}
            for i in range(len(dlg.result1)):
                teacher_subject_map[dlg.result1[i]] = dlg.result2[i]
                subject_teacher_map[dlg.result2[i]] = dlg.result1[i]

            globaldata.teacher_subject_map = teacher_subject_map
            globaldata.subject_teacher_map = subject_teacher_map

    def VenueClass(self, evt):
        if not self.BasicRequirements:
            self.ErrorBox('Please Define Constraints First')
            return

        dlg = ListView(self, title='Add Mapping', label1="Venue", label2="Class / Batch")
        dlg.ShowModal()
        if hasattr(dlg, 'result1') and hasattr(dlg, 'result2'):
            venue_class_map = {}
            class_venue_map = {}
            for i in range(len(dlg.result1)):
                venue_class_map[dlg.result1[i]] = dlg.result2[i]
                class_venue_map[dlg.result2[i]] = dlg.result1[i]

            globaldata.venue_class_map = venue_class_map
            globaldata.class_venue_map = class_venue_map

    def VenueUtilization(self, evt):
        if not self.BasicRequirements:
            self.ErrorBox('Please Define Constraints First')
            return

        res = project.FindVenueUtilization()
        vDialouge = wx.Dialog(self, -1, title='Venue Utilization', size=(500,500))
        lables = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun",]
        vList = wx.ListCtrl(vDialouge, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER, size=(300, 400))
        vList.Show(True)
        vList.InsertColumn(0,"Venue Name", width=wx.LIST_AUTOSIZE_USEHEADER) 
        vList.InsertColumn(1,"WeeklyUtil", width=wx.LIST_AUTOSIZE_USEHEADER)
        vList.InsertColumn(2,"Mon", width=wx.LIST_AUTOSIZE_USEHEADER)
        vList.InsertColumn(3,"Tue", width=wx.LIST_AUTOSIZE_USEHEADER)
        vList.InsertColumn(4,"Wed", width=wx.LIST_AUTOSIZE_USEHEADER)
        vList.InsertColumn(5,"Thu", width=wx.LIST_AUTOSIZE_USEHEADER)
        vList.InsertColumn(6,"Fri", width=wx.LIST_AUTOSIZE_USEHEADER)
        vList.InsertColumn(7,"Sat", width=wx.LIST_AUTOSIZE_USEHEADER)
        vList.InsertColumn(7,"Sun", width=wx.LIST_AUTOSIZE_USEHEADER)
        for key in res:
            val = res[key]
            l = [key, res[key][-1]]
            for i in range(len(val) - 1):
                l.append(val[i])
            vList.Append(l)
        vDialouge.ShowModal()

    def SuccessBox(self,msg):
        # print len(self.__dict__)
        dlg = wx.MessageDialog(None, msg, "Notice", wx.OK|wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def ErrorBox(self, msg):
        dlg = wx.MessageDialog(None, msg, "Error", wx.OK|wx.ICON_ERROR)
        dlg.ShowModal()
        dlg.Destroy()

    def ImportTeacherData(self, evt):
        # print len(self.__dict__)
        if not self.BasicRequirements:
            self.ErrorBox('Please Define Constraints First')
            return

        openFileDialog = wx.FileDialog(self, "Open Teacher Data File", "", "",
                                       "txt files (*.txt)|*.txt", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return         
        filepath = openFileDialog.GetPath()

        dlg = wx.ProgressDialog("Importing Data",
                               "Please wait while data is imported",
                               maximum = 10,
                               parent=self,
                               style = wx.PD_APP_MODAL|wx.PD_AUTO_HIDE)
        dlg.Update(1)   
        f = open(filepath, "r")
        lines = f.read().split('\n')    
        del lines[0]
        dlg.Update(6)
        lines = filter(None, lines)
        msg = 'Imported Successfully\nDuplicates:'
        try:
            imp = 0
            err = 0
            for l in lines:
                p = l.split('\t')
                p = filter(None, p)
                if p[0] in globaldata.teacher_fullnames or p[1] in globaldata.teacher_shortnames:
                    err += 1
                    msg += '\n' + p[0] + ', ' + p[1]
                    continue
                if len(p) != 4:
                    raise
                p2 = int(p[2])
                p3 = int(p[3])
                globaldata.teacher_fullnames.append(p[0])
                globaldata.teacher_shortnames.append(p[1])
                globaldata.teacher_weeklymax.append(p2)
                globaldata.teacher_dailymax.append(p3)
                imp += 1
            dlg.Update(8)
            msg += '\nTotal Imported = %s\nTotal Duplicates Ignored= %s' % (imp, err)
            self.TeacherData(evt)
            dlg.Update(10)
            dlg.Destroy()
            self.SuccessBox(msg)

        except:
            self.ErrorBox('Error in File Format at %s' % l)
            dlg.Destroy()
        # if len(globaldata.all_teachers) == 0:    #default attr are 32
        #     self.ShowFirstGrid('Teacher')

    def ImportVenueData(self, evt):
        if not self.BasicRequirements:
            self.ErrorBox('Please Define Constraints First')
            return

        openFileDialog = wx.FileDialog(self, "Open Venue Data File", "", "",
                                       "txt files (*.txt)|*.txt", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return         
        filepath = openFileDialog.GetPath()
        dlg = wx.ProgressDialog("Importing Data",
                       "Please wait while data is imported",
                       maximum = 10,
                       parent=self,
                       style = wx.PD_APP_MODAL|wx.PD_AUTO_HIDE)
        dlg.Update(1)
        f = open(filepath, "r")
        lines = f.read().split('\n')
        del lines[0]
        lines = filter(None, lines)
        msg = 'Imported Successfully\nDuplicates:'
        dlg.Update(6)
        try:
            imp = 0
            err = 0
            for l in lines:
                p = l.split('\t')
                p = filter(None, p)
                if p[0] in globaldata.venue_fullnames or p[1] in globaldata.venue_shortnames:
                    err += 1
                    msg += '\n' + p[0] + ', ' + p[1]
                    continue
                if len(p) != 3:
                    raise
                p2 = int(p[2])
                globaldata.venue_fullnames.append(p[0])
                globaldata.venue_shortnames.append(p[1])
                globaldata.venue_capacity.append(p2)
                imp += 1
            msg += '\nTotal Imported = %s\nTotal Duplicates Ignored= %s' % (imp, err)
            dlg.Update(8)
            self.VenueData(evt)
            dlg.Update(10)
            dlg.Destroy()
            self.SuccessBox(msg)    

        except:
            self.ErrorBox('Error in File Format %s' % l)
            dlg.Destroy()
        # if len(globaldata.all_venues) == 0:    #default attr are 32
        #     self.ShowFirstGrid('Venue')


    def ImportTeacherSubjectMapping(self, evt):
        if not self.BasicRequirements:
            self.ErrorBox('Please Define Constraints First')
            return

        openFileDialog = wx.FileDialog(self, "Open Teacher-Subject Data File", "", "",
                                       "txt files (*.txt)|*.txt", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return         
        filepath = openFileDialog.GetPath()
        f = open(filepath, "r")
        lines = f.read().split('\n')
        # del lines[0]
        lines = filter(None, lines)
        msg = 'Imported Successfully\nDuplicates:'
        try:
            imp = 0
            err = 0
            for l in lines:
                p = l.split('\t')
                p = filter(None, p)
                if p[0]  not in globaldata.teacher_shortnames or p[1] not in globaldata.subject_shortnames:
                    raise
                if p[0] in globaldata.teacher_subject_map and globaldata.teacher_subject_map[p[0]] == p[1]:             
                    err += 1
                    msg += '\n' + p[0] + ', ' + p[1]
                    continue
                globaldata.teacher_subject_map[p[0]] = p[1]
                globaldata.subject_teacher_map[p[1]] = p[0]
                imp += 1
            msg += '\nTotal Imported = %s\nTotal Duplicates Ignored= %s' % (imp, err)
            self.SuccessBox(msg)    
        except:
            self.ErrorBox('Error in File Format %s' % l)

    def ImportTeacherClassMapping(self, evt):
        if not self.BasicRequirements:
            self.ErrorBox('Please Define Constraints First')
            return

        openFileDialog = wx.FileDialog(self, "Open Teacher-Class Data File", "", "",
                                       "txt files (*.txt)|*.txt", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return         
        filepath = openFileDialog.GetPath()
        f = open(filepath, "r")
        lines = f.read().split('\n')
        # del lines[0]
        lines = filter(None, lines)
        msg = 'Imported Successfully\nDuplicates:'
        try:
            imp = 0
            err = 0
            for l in lines:
                p = l.split('\t')
                p = filter(None, p)
                if p[0]  not in globaldata.teacher_shortnames or p[1] not in globaldata.class_shortnames:
                    raise
                if p[0] in globaldata.teacher_class_map and globaldata.teacher_class_map[p[0]] == p[1]:             
                    err += 1
                    msg += '\n' + p[0] + ', ' + p[1]
                    continue
                globaldata.teacher_class_map[p[0]] = p[1]
                globaldata.class_teacher_map[p[1]] = p[0]
                imp += 1
            msg += '\nTotal Imported = %s\nTotal Duplicates Ignored= %s' % (imp, err)
            self.SuccessBox(msg)    
        except:
            self.ErrorBox('Error in File Format %s' % l)

    def ImportVenueClassMapping(self, evt):
        if not self.BasicRequirements:
            self.ErrorBox('Please Define Constraints First')
            return

        openFileDialog = wx.FileDialog(self, "Open Venue-Class Data File", "", "",
                                       "txt files (*.txt)|*.txt", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return         
        filepath = openFileDialog.GetPath()
        f = open(filepath, "r")
        lines = f.read().split('\n')
        # del lines[0]
        lines = filter(None, lines)
        msg = 'Imported Successfully\nDuplicates:'
        try:
            imp = 0
            err = 0
            for l in lines:
                p = l.split('\t')
                p = filter(None, p)
                if p[0]  not in globaldata.venue_shortnames or p[1] not in globaldata.class_shortnames:
                    raise
                if p[0] in globaldata.venue_class_map and globaldata.venue_class_map[p[0]] == p[1]:             
                    err += 1
                    msg += '\n' + p[0] + ', ' + p[1]
                    continue
                globaldata.venue_class_map[p[0]] = p[1]
                globaldata.class_venue_map[p[1]] = p[0]
                imp += 1
            msg += '\nTotal Imported = %s\nTotal Duplicates Ignored= %s' % (imp, err)
            self.SuccessBox(msg)    
        except:
            self.ErrorBox('Error in File Format %s' % l)

    def ImportClassData(self, evt):
        if not self.BasicRequirements:
            self.ErrorBox('Please Define Constraints First')
            return

        openFileDialog = wx.FileDialog(self, "Open Class Data File", "", "",
                                       "txt files (*.txt)|*.txt", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return         
        filepath = openFileDialog.GetPath()
        dlg = wx.ProgressDialog("Importing Data",
                       "Please wait while data is imported",
                       maximum = 10,
                       parent=self,
                       style = wx.PD_APP_MODAL|wx.PD_AUTO_HIDE)
        dlg.Update(1)

        f = open(filepath, "r")
        lines = f.read().split('\n')
        del lines[0]
        lines = filter(None, lines)
        msg = 'Imported Successfully\nDuplicates:'
        dlg.Update(6)
        try:
            err = 0
            imp = 0
            for l in lines:
                p = l.split('\t')
                p = filter(None, p)
                if p[0] in globaldata.class_fullnames or p[1] in globaldata.class_shortnames:
                    err += 1
                    msg += '\n' + p[0] + ', ' + p[1]
                    continue
                if len(p) != 3:
                    raise
                p2 = int(p[2])
                globaldata.class_fullnames.append(p[0])
                globaldata.class_shortnames.append(p[1])
                globaldata.class_capacity.append(p2)
                imp += 1

            msg += '\nTotal Imported = %s\nTotal Duplicates Ignored= %s' % (imp, err)
            dlg.Update(8)
            self.ClassData(evt)
            dlg.Update(10)
            dlg.Destroy()
            self.SuccessBox(msg)    

        except:
            self.ErrorBox('Error in File Format %s' % l)
            dlg.Destroy()   
        # if len(globaldata.all_classes) == 0:    #default attr are 32
        #     self.ShowFirstGrid('Class')

    def ImportSubjectData(self, evt):
        if not self.BasicRequirements:
            self.ErrorBox('Please Define Constraints First')
            return

        openFileDialog = wx.FileDialog(self, "Open Subject Data File", "", "",
                                       "txt files (*.txt)|*.txt", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return         
        filepath = openFileDialog.GetPath()
        f = open(filepath, "r")
        lines = f.read().split('\n')
        del lines[0]
        lines = filter(None, lines)
        errorStr = 'Error in File Format'
        msg = 'Imported Successfully\nDuplicates:'
        err = 0
        imp = 0
        try:
            for l in lines:
                p = l.split('\t')
                p = filter(None, p)

                if p[0] in globaldata.subject_fullnames or p[1] in globaldata.subject_shortnames:
                    err += 1
                    msg += '\n' + p[0] + ', ' + p[1]
                    continue
                if len(p) < 3:
                    raise
                p2 = int(p[2])
                for className in p[3:]:
                    if className not in globaldata.class_shortnames:
                        errorStr += '\nInvalid Class ' + className
                        raise  
                    globaldata.subject_class_map[p[1]] = className
                    if className in globaldata.class_subject_map:
                        globaldata.class_subject_map[className].append(p[1])
                    else:
                        globaldata.class_subject_map[className] = [p[1]]
                globaldata.subject_fullnames.append(p[0])
                globaldata.subject_shortnames.append(p[1])
                globaldata.subject_credits.append(p2)
                globaldata.subjects[p[1]] = p2
                imp += 1

            msg += '\nTotal Imported = %s\nTotal Duplicates Ignored= %s' % (imp, err)    
            self.SuccessBox(msg) 

        except:
            self.ErrorBox(errorStr + '\n%s' % l)                
        

        # for i in globaldata.class_subject_map:
        #     print i, globaldata.class_subject_map[i]

        # for i in globaldata.subject_class_map:
        #     print i, globaldata.subject_class_map[i]

    def KeyboardShortcuts(self, evt):
        dlg = HelpWindow(self)
        dlg.ShowModal()
        dlg.Destroy()

    def ExportData(self, evt):
        t = open('teachers.txt', "w")
        msg = ''
        for i in range(len(globaldata.teacher_fullnames)):
            msg += globaldata.teacher_fullnames[i] + '\t' + globaldata.teacher_shortnames[i+1] + '\t' + str(globaldata.teacher_weeklymax[i]) + '\t' + str(globaldata.teacher_dailymax[i]) + '\n'
        t.write(msg)
        t.close()

        v = open('venue.txt', "w")
        msg = ''
        for i in range(len(globaldata.venue_fullnames)):
            msg += globaldata.venue_fullnames[i] + '\t' + globaldata.venue_shortnames[i+1] + '\t' + str(globaldata.venue_capacity[i]) + '\n'
        v.write(msg)
        v.close()

        c = open('class.txt', "w")
        msg = ''
        for i in range(len(globaldata.class_fullnames)):
            msg += globaldata.class_fullnames[i] + '\t' + globaldata.class_shortnames[i+1] + '\t' + str(globaldata.class_capacity[i]) + '\n'
        c.write(msg)
        c.close()

        s = open('subjects.txt', "w")
        msg = ''
        for i in range(len(globaldata.subject_fullnames)):
            msg += globaldata.subject_fullnames[i] + '\t' + globaldata.subject_shortnames[i+1] + '\t' + str(globaldata.subject_credits[i]) + '\n'
        s.write(msg)
        s.close()

        st = open('subjectsTeachersMap.txt', "w")
        msg = ''
        for i in globaldata.subject_teacher_map:
            msg += i + '\t' + globaldata.subject_teacher_map[i] + '\n'
        st.write(msg)
        st.close()

        sc = open('subjectsClassMap.txt', "w")
        msg = ''
        for i in globaldata.subject_class_map:
            msg += i 
            for c in globaldata.subject_class_map[i]:
                msg += '\t' + c
            msg += '\n'
        sc.write(msg)
        sc.close()

        self.SuccessBox("Exported Successfully")
        
    def UpdateHeaders(self, evt):
        dlg = HeaderInfo(self)
        dlg.ShowModal()
        if hasattr(dlg, 'result1') and hasattr(dlg, 'result2') and hasattr(dlg, 'result3'):
            globaldata.header1 = dlg.result1
            globaldata.header2 = dlg.result2
            globaldata.header3 = dlg.result3  

            child = self.panel1.GetChildren()
            for i in range(0, len(child), 5):
                if i+2 < len(child):
                    child[i].SetLabel(globaldata.header1)
                    child[i+1].SetLabel(globaldata.header2)
                    child[i+2].SetLabel(globaldata.header3)
            self.panel1.Layout()

            child = self.panel2.GetChildren()
            # print child
            for i in range(0, len(child), 5):
                if i+2 < len(child):
                    child[i].SetLabel(globaldata.header1)
                    child[i+1].SetLabel(globaldata.header2)
                    child[i+2].SetLabel(globaldata.header3)
            self.panel2.Layout()

            child = self.panel3.GetChildren()
            # print child
            for i in range(0, len(child), 5):
                if i+2 < len(child):
                    child[i].SetLabel(globaldata.header1)
                    child[i+1].SetLabel(globaldata.header2)
                    child[i+2].SetLabel(globaldata.header3)
            self.panel3.Layout()

        dlg.Destroy()

    def _init_menubar(self):

        menubar = wx.MenuBar()
        file = wx.Menu()
        fnew = file.Append(wx.ID_NEW,'&New', '&New\tCtrl+N')
        self.Bind(wx.EVT_MENU, self.OnNew, fnew)
        fopen = file.Append(wx.ID_OPEN,'&Open', '&Open\tCtrl+O')
        self.Bind(wx.EVT_MENU, self.OnOpen, fopen)
        save = file.Append(wx.ID_SAVE,'&Save', '&Save\tCtrl+S')
        self.Bind(wx.EVT_MENU, self.OnSave, save)
        saveas = file.Append(wx.ID_SAVEAS,'&Save As')
        self.Bind(wx.EVT_MENU, self.OnSaveAs, saveas)

        imp = wx.Menu()
        exhtml = imp.Append(-1,'Export HTML')
        self.Bind(wx.EVT_MENU, self.ExportHTML, exhtml)
        exdata = imp.Append(-1,'Export Data')
        self.Bind(wx.EVT_MENU, self.ExportData, exdata)
        expdf = imp.Append(-1,'Export Pdf')
        self.Bind(wx.EVT_MENU, self.ExportPDF, expdf)
        exods = imp.Append(-1,'Export Ods')
        self.Bind(wx.EVT_MENU, self.ExportODS, exods)
        file.AppendMenu(-1,'Export', imp)
        file.AppendSeparator()

        quit = file.Append(wx.ID_EXIT, 'Quit', '&Quit\tCtrl+Q')
        # quit.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_QUIT))
        # quit.SetBitmap(wx.Bitmap('exit.png'))
        self.Bind(wx.EVT_MENU, self.OnQuit, quit)

        edit = wx.Menu()
        head = edit.Append(-1,'&Header Info')
        self.Bind(wx.EVT_MENU, self.UpdateHeaders, head)
        checkC = edit.Append(-1,'&Check Constraints')
        self.Bind(wx.EVT_MENU, self.CheckConstraints, checkC)
 

        data = wx.Menu()
        basic = data.Append(-1,'&Basic Constraints')
        self.Bind(wx.EVT_MENU, self.GetBasicConstraints, basic)
 
        imp = wx.Menu()
        imp1 = imp.Append(-1,'&Import Teacher Data')
        self.Bind(wx.EVT_MENU, self.ImportTeacherData, imp1)
        imp2 = imp.Append(-1,'&Import Venue Data')
        self.Bind(wx.EVT_MENU, self.ImportVenueData, imp2)
        imp3 = imp.Append(-1,'&Import Class Data')
        self.Bind(wx.EVT_MENU, self.ImportClassData, imp3)
        imp4 = imp.Append(-1,'&Import Subject Data')
        self.Bind(wx.EVT_MENU, self.ImportSubjectData, imp4)

        imp5 = imp.Append(-1,'&Teacher-Class Mapping')
        self.Bind(wx.EVT_MENU, self.ImportTeacherClassMapping, imp5)

        imp6 = imp.Append(-1,'&Teacher-Subject Mapping')
        self.Bind(wx.EVT_MENU, self.ImportTeacherSubjectMapping, imp6)

        imp7 = imp.Append(-1,'&Venue-Class Mapping')
        self.Bind(wx.EVT_MENU, self.ImportVenueClassMapping, imp7)

        data.AppendMenu(-1,'Import From File', imp)
 
        teacher = data.Append(-1,'&Teachers')
        self.Bind(wx.EVT_MENU, self.TeacherData, teacher)
        venue = data.Append(-1,'&Venues')
        self.Bind(wx.EVT_MENU, self.VenueData, venue)
        classes = data.Append(-1,'&Classes')
        self.Bind(wx.EVT_MENU, self.ClassData, classes)
        sub = data.Append(-1,'&Subjects')
        self.Bind(wx.EVT_MENU, self.SubjectData, sub)

        mp = wx.Menu()
        ts = mp.Append(-1,'Teacher <-> Subject')
        self.Bind(wx.EVT_MENU, self.TeacherSubject, ts)
        tc = mp.Append(-1,'Teacher <-> Class')
        self.Bind(wx.EVT_MENU, self.TeacherClass, tc)
        vc = mp.Append(-1,'Venue <-> Class')
        self.Bind(wx.EVT_MENU, self.VenueClass, vc)
        data.AppendMenu(-1,'Mapping', mp)


        view = wx.Menu()
        self.toolbarBoolean = view.Append(-1,'&Show Toolbar', kind=wx.ITEM_CHECK)
        view.Check(self.toolbarBoolean.GetId(), True)
        self.Bind(wx.EVT_MENU, self.ToggleToolbar, self.toolbarBoolean)

        venueUtil = view.Append(-1,'&Venue Utilization')
        self.Bind(wx.EVT_MENU, self.VenueUtilization, venueUtil)
        #chuck it isnt much useful -- lot of work
        # self.fullscreenBoolean = view.Append(-1,'Fullscreen', kind=wx.ITEM_CHECK)
        # view.Check(self.fullscreenBoolean.GetId(), False)
        # self.Bind(wx.EVT_MENU, self.ToggleFullscreen, self.fullscreenBoolean)



        help = wx.Menu()
        ks = help.Append(-1,'Keyboard Shortcuts')
        self.Bind(wx.EVT_MENU, self.KeyboardShortcuts, ks)
        help.Append(-1,'About')

        menubar.Append(file, '&File')
        menubar.Append(edit, '&Edit')
        menubar.Append(data, '&Data')
        menubar.Append(view, '&View')
        menubar.Append(help, '&Help')

        self.SetMenuBar(menubar)
        self.Center()

    # def ToggleFullscreen(self, evt):

    #     if self.fullscreenBoolean.IsChecked():
    #         pass
    #         # self.ShowFullScreen(True)
    #     else:
    #         pass
    #         # self.ShowFullScreen(False)
             # self.toolbar.Hide()

    def ToggleToolbar(self, evt):

        if self.toolbarBoolean.IsChecked():
            self.toolbar.Show()
        else:
            self.toolbar.Hide()

    def _init_toolbar(self):
        iconSize= (24,24)
        self.toolbar = self.CreateToolBar()
        self.toolbar.AddLabelTool(wx.ID_NEW, '',wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR, iconSize))
        self.toolbar.AddLabelTool(wx.ID_OPEN, '',wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR, iconSize))
        self.toolbar.AddLabelTool(wx.ID_SAVE, '',wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_TOOLBAR, iconSize))
        self.toolbar.AddLabelTool(wx.ID_SAVEAS, '',wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE_AS, wx.ART_TOOLBAR, iconSize))
        self.toolbar.AddLabelTool(wx.ID_FIND, '',wx.ArtProvider.GetBitmap(wx.ART_FIND, wx.ART_TOOLBAR, iconSize))
        self.toolbar.AddLabelTool(wx.ID_EXIT, '',wx.ArtProvider.GetBitmap(wx.ART_QUIT, wx.ART_TOOLBAR, iconSize))

        self.Bind(wx.EVT_TOOL,self.OnNew, id=wx.ID_NEW)
        self.Bind(wx.EVT_TOOL,self.OnOpen, id=wx.ID_OPEN)
        self.Bind(wx.EVT_TOOL,self.OnSave, id=wx.ID_SAVE)
        self.Bind(wx.EVT_TOOL,self.OnSaveAs, id=wx.ID_SAVEAS)
        self.Bind(wx.EVT_TOOL,self.CheckConstraints, id=wx.ID_FIND)
        self.Bind(wx.EVT_TOOL,self.OnQuit, id=wx.ID_EXIT)
        self.toolbar.SetToolBitmapSize((24,24))
        # self.toolbar.AddLabelTool(wx.ID_NEW, '',wx.Bitmap('icons/new.png'))
        # self.toolbar.AddLabelTool(wx.ID_UNDO, '',wx.Bitmap('icons/undo.png'))
        # self.toolbar.AddLabelTool(wx.ID_REDO, '',wx.Bitmap('icons/redo.png'))
        # self.toolbar.AddLabelTool(wx.ID_CUT, '',wx.Bitmap('icons/cut.png'))
        # self.toolbar.AddLabelTool(wx.ID_SAVE, '',wx.Bitmap('icons/save.png'))
        # self.toolbar.AddLabelTool(wx.ID_EXIT, '',wx.Bitmap('icons/exit.png'))
        # self.toolbar.Realize()
        self.toolbar.Show()
        self.Show(True)

def main(flag):
    app = wx.App(False)
    frame = MyForm(flag).Show()
    # import wx.lib.inspection
    # wx.lib.inspection.InspectionTool().Show()
    app.MainLoop()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if os.path.isfile(sys.argv[1]):
            main(True)
        else:
            print 'Not a valid tt file'
    else:
        main(False)

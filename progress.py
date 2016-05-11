import wx
 
########################################################################
class MyForm(wx.Frame):
 
    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          "ProgressDialog Tutorial")
        panel = wx.Panel(self, wx.ID_ANY)
        b = wx.Button(panel, label="Create and Show a ProgressDialog")
        b.Bind(wx.EVT_BUTTON, self.onButton)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(b, 0, wx.ALL|wx.CENTER, 5)
        panel.SetSizer(sizer)
 
    #----------------------------------------------------------------------
    def onButton(self, evt):
        """
        Copied from the wxPython demo
        """
        max = 80
 
        dlg = wx.ProgressDialog("Progress dialog example",
                               "An informative message",
                               maximum = max,
                               parent=self,
                               style = wx.PD_APP_MODAL)
 
        keepGoing = True
        count = 0
 
        while keepGoing and count < max:
            count += 1
            wx.MilliSleep(250)
 
            if count >= max / 2:
                (keepGoing, skip) = dlg.Update(count, "Half-time!")
            else:
                (keepGoing, skip) = dlg.Update(count)
 
        dlg.Destroy()
 
#----------------------------------------------------------------------
# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
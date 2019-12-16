#201444032 정성준

import wx

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Calc")
        self.SetSize(300,170)
        self.mainPanel = wx.Panel(self)
  
        
        self.gridSizer = wx.GridSizer(rows=4, cols=5, hgap=5, vgap=5)
        self.textField = wx.TextCtrl(self.mainPanel, value="0", style=wx.TE_RIGHT)
        

        self.buttons = (
            wx.Button(self.mainPanel, label="7"),
            wx.Button(self.mainPanel, label="8"),
            wx.Button(self.mainPanel, label="9"),
            wx.Button(self.mainPanel, label="/"),
            wx.Button(self.mainPanel, label="C"),
            wx.Button(self.mainPanel, label="4"),
            wx.Button(self.mainPanel, label="5"),
            wx.Button(self.mainPanel, label="6"),
            wx.Button(self.mainPanel, label="*"),
            wx.Button(self.mainPanel, label="BS"),
            wx.Button(self.mainPanel, label="1"),
            wx.Button(self.mainPanel, label="2"),
            wx.Button(self.mainPanel, label="3"),
            wx.Button(self.mainPanel, label="-"),
            wx.Button(self.mainPanel, label="+-"),
            wx.Button(self.mainPanel, label="0"),
            wx.Button(self.mainPanel, label="."),
            wx.Button(self.mainPanel, label="="),
            wx.Button(self.mainPanel, label="+"),
            wx.Button(self.mainPanel, label="CE")
            )

        for button in self.buttons:
            self.gridSizer.Add(button, 0, wx.EXPAND)

        self.vtBoxSizer = wx.BoxSizer(wx.VERTICAL)
        self.vtBoxSizer.Add(self.textField, 0, wx.EXPAND | wx.LEFT | wx.RIGHT| wx.TOP, 5)
        self.vtBoxSizer.Add(self.gridSizer, 1, wx.EXPAND | wx.ALL, 3)
        self.mainPanel.SetSizer(self.vtBoxSizer)

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

if __name__ == "__main__":
    MyApp().MainLoop()

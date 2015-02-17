import wx
import os
from subprocess import Popen
import pyperclip
import thread

class windowClass(wx.Frame):
	def __init__(self, *args, **kwargs):
		super(windowClass, self).__init__(*args, **kwargs)
		self.basicGUI()
		
	def basicGUI(self):
		self.panel = wx.Panel(self)
	
		# Define Menu Bar
		menuBar = wx.MenuBar()
		
		# Define File Button
		fileButton = wx.Menu()
		exitItem = fileButton.Append(wx.ID_EXIT, 'Exit', 'Exit the program')
		
		# Append Buttons to Menu Bar
		menuBar.Append(fileButton, 'File')
		
		self.SetMenuBar(menuBar)
		
		# Bind Button Values
		self.Bind(wx.EVT_MENU, self.Quit, exitItem)
		
		# Refresh Button and Link Text
		link = pyperclip.paste()
		try:
			self.myLink = wx.TextCtrl(self.panel,value=link,pos=(100,11), size=(275, 25));
		except:
			self.myLink = wx.TextCtrl(self.panel,value='Copy Link and press Refresh or Paste Here',pos=(100,11), size=(275, 25));
		refreshButton = wx.Button(self.panel, 1, 'Refresh Link', (10, 10))
		
		# Radio Buttons for Video/Audio Download
		self.rb1_audio = wx.RadioButton(self.panel, -1, "Audio/MP3",(10,50))
		self.rb2_video = wx.RadioButton(self.panel, -1, "Video/MPEG4", (10,70))
		#default to audio
		self.rb1_audio.SetValue(True)
		
		# Download Button
		downloadButton = wx.Button(self.panel, 2, 'Download', (10, 370))

		# Bind Buttons
		self.Bind(wx.EVT_BUTTON, self.Refresh, refreshButton)
		self.Bind(wx.EVT_RADIOBUTTON, self.SetType, self.rb1_audio)
		self.Bind(wx.EVT_RADIOBUTTON, self.SetType, self.rb2_video)
		self.Bind(wx.EVT_BUTTON, self.Download, downloadButton)
		
		# Set Title and Show GUI
		self.SetTitle('Pre\'s Youtube Downloader')
		self.SetBackgroundColour('#ECF1EF')
		self.statusbar = self.CreateStatusBar(1)
		self.statusbar.SetStatusText("Downloading Audio",0)
		self.Show(True)
		
	
	def Refresh(self, e):
		#Update Link Here
		link = pyperclip.paste()
		try:
			self.myLink.SetValue(link)
		except:
			self.myLink.SetValue('Copy Link and press Refresh or Paste Here')
	
	def SetType(self,e):
		state_audio = self.rb1_audio.GetValue()
		state_video = self.rb2_video.GetValue()
		if(state_audio):
			self.statusbar.SetStatusText("Downloading Audio",0)
		elif(state_video):
			self.statusbar.SetStatusText("Downloading Video",0)
		else:
			self.statusbar.SetStatusText("No Ops Selected",0)
	
	def Download(self, e):
		genLink = self.myLink.GetValue()
		cdir = os.getcwd()
		pdir = os.path.dirname(cdir)
		EXT = "NA"
		if(self.rb1_audio.GetValue()):
			EXT = "%(ext)s"
		elif(self.rb2_video.GetValue()):
			EXT = "mp4"
		proc = ["youtube-dl.exe", "-o", pdir+"/%(playlist)s/%(title)s."+EXT, "--no-playlist"]
		if(self.rb1_audio.GetValue()):
			proc.append("--extract-audio")
			proc.append("--audio-format")
			proc.append("mp3")
			proc.append(genLink)
		elif(self.rb2_video.GetValue()):
			proc.append(genLink)
		#wx.StaticText(self.panel, -1, "Executing Command:\n"+"".join(proc), pos=(110,370), size=(300,100))
		print "".join(proc)
		Popen(proc)
	
	def Quit(self, e):
		self.Close()
	

def main():
	#Change into correct directory for execution
	d = os.getcwd()
	#print "Current Directory: " + d
	os.chdir(d+"/bin")
	#print "New Directory: " + d

	app = wx.App()
	windowClass(None, -1, size = (390,480), style=wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION)
	
	app.MainLoop()
	
main()
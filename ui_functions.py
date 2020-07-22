from main import *

class UIFunctions(Ui) :
	def toggle_menu(self, maxWidth, enable) :
		if enable :
			width = self.ui.frame_left_menu.width()
			maxExtend = maxWidth
			standard = 70

			if width ==70 :
				widthExtended = maxExtend
			else : 
				widthExtended = standard

			self.animation = QpropertyAnimation(self.ui.frame_left_menu,b"minimumWidth" )
			self.animation.setDuration(400)
			self.animation.setStartValue(width)
			self.animation.setEndValue(widthExtended)
			self.animation.start()
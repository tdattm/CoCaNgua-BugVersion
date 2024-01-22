class Button:
	def __init__(self, image, pos, text_Input, font, baseColor):
		self.image = image
		self.xPos = pos[0]
		self.yPos = pos[1]
		self.text_Input = text_Input
		self.font = font
		self.baseColor = baseColor
		self.text = self.font.render(self.text_Input, True, self.baseColor)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.xPos, self.yPos))
		self.textRect = self.text.get_rect(center=(self.xPos, self.yPos))

	def checkForInput(self, pos):
		if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

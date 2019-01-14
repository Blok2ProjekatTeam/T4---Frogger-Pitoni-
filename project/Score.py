class Score:

	def __init__(self):
		self.score = 0
		self.lives = 3
		self.level = 1
		self.mode = "Normal"
		self.y = 1005

	def reset(self):
		self.score = 0
		self.lives = 3
		self.level = 1
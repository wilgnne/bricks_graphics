from bricks_toolkit.graphics import *
from bricks_toolkit.bricks_behaviour import *

class BricksWall():
	"""docstring for BricksWall"""
	def __init__(self,tam = 20, itam = 5, esp = 2, off = color_rgb(216, 216, 191), on = color_rgb(77, 77, 255)):
		self.i = 20
		self.j = 10
		self.esp = esp
		self.tam = tam
		self.itam = itam
		self.off = off
		self.on = on
		width = self.j * (self.tam + self.esp) + 105
		height = self.i * (self.tam + self.esp) + 6
		self.win = GraphWin('Briks', width, height, autoflush=False)
		self.win.setBackground(color_rgb(217, 217, 243))
		self.contruction()
		self.win.redraw()

	def contruction(self):
		self.wall = []
		for i in range(0, self.i):
			line = []
			for j in range(0, self.j):
				rec = Rectangle(Point(0, 0), Point(self.tam, self.tam))
				irec = Rectangle(Point(self.itam, self.itam), Point(self.tam - self.itam, self.tam - self.itam))
				rec.setOutline(self.off)
				irec.setFill(self.off)
				irec.setOutline(self.off)
				dx = (j * self.tam) + (j * self.esp) + self.esp
				dy = (i * self.tam) + (i * self.esp) + self.esp
				rec.move(dx, dy)
				irec.move(dx, dy)
				rec.draw(self.win)
				irec.draw(self.win)
				line.append([rec, irec])
			self.wall.append(line)
		b = Rectangle(Point(-5, -5), Point(rec.getP2().x + 5, rec.getP2().y + 5))
		b.setWidth(2)
		b.setOutline(color_rgb(255, 165, 0))
		b.draw(self.win)
		self.auxWall = []
		for i in range(0, 4):
			line = []
			for j in range(0, 4):
				rec = Rectangle(Point(0, 0), Point(self.tam, self.tam))
				irec = Rectangle(Point(self.itam, self.itam), Point(self.tam - self.itam, self.tam - self.itam))
				rec.setOutline(self.off)
				irec.setFill(self.off)
				irec.setOutline(self.off)
				dx = (j * self.tam) + (j * self.esp) + self.esp + self.wall[0][self.j - 1][0].getP2().x + 10
				dy = (i * self.tam) + (i * self.esp) + self.esp + self.wall[int(self.i / 2) - 2][0][0].getP2().y
				rec.move(dx, dy)
				irec.move(dx, dy)
				rec.draw(self.win)
				irec.draw(self.win)
				line.append([rec, irec])
			self.auxWall.append(line)

	def clean(self, wall):
		for i in range(0, len(wall)):
			for j in range(0, len(wall[0])):
				wall[i][j][0].setOutline(self.off)
				wall[i][j][1].setFill(self.off)
				wall[i][j][1].setOutline(self.off)

	def overlap(self, objects):
		self.clean(self.wall)
		for gameObject in objects:
			for i in range(0, len(gameObject.mesh)):
				for j in range(0, len(gameObject.mesh[0])):
					x = gameObject.position.x + j
					y = gameObject.position.y + i
					if gameObject.mesh[i][j] == '1' and x < self.j and y < self.i and x >= 0 and y >= 0:
						self.wall[y][x][0].setOutline(self.on)
						self.wall[y][x][1].setOutline(self.on)
						self.wall[y][x][1].setFill(self.on)
		#self.win.redraw()

	def pointWall(self, wall):
		self.clean(self.auxWall)
		for i in range(0, 4):
			for j in range(0,4):
				if wall[i][j] == '1':
					self.auxWall[i][j][0].setOutline(self.on)
					self.auxWall[i][j][1].setOutline(self.on)
					self.auxWall[i][j][1].setFill(self.on)

def lifeBricks(life):
	if life == 4:
		return [['1', '0', '0', '0'],
		 		['1', '0', '0', '0'],
		 		['1', '0', '0', '0'],
		 		['1', '0', '0', '0']]
	elif life == 3:
		return [['0', '0', '0', '0'],
		 		['1', '0', '0', '0'],
		 		['1', '0', '0', '0'],
		 		['1', '0', '0', '0']]
	elif life == 2:
		return [['0', '0', '0', '0'],
		 		['0', '0', '0', '0'],
		 		['1', '0', '0', '0'],
		 		['1', '0', '0', '0']]
	elif life == 1:
		return [['0', '0', '0', '0'],
		 		['0', '0', '0', '0'],
		 		['0', '0', '0', '0'],
		 		['1', '0', '0', '0']]
	elif life < 1 or life > 4:
		return [['0', '0', '0', '0'],
		 		['0', '0', '0', '0'],
		 		['0', '0', '0', '0'],
		 		['0', '0', '0', '0']]

def dieBricks(frame):
	if frame == 0:
		return [['1', '0', '0', '1'],
		 		['0', '1', '1', '0'],
		 		['0', '1', '1', '0'],
		 		['1', '0', '0', '1']]
	elif frame == 1:
		return [['0', '1', '1', '0'],
		 		['1', '0', '0', '1'],
		 		['1', '0', '0', '1'],
		 		['0', '1', '1', '0']]
	elif frame == 2:
		return [['1', '0', '0', '1'],
		 		['0', '1', '1', '0'],
		 		['0', '1', '1', '0'],
		 		['1', '0', '0', '1']]
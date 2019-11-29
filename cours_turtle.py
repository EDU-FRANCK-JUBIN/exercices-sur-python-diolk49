import turtle as tu

a = tu.Turtle()

dic = [
	['red', 0-200, 0+300, 500, 150],
	['blue', 0-200, -150+300, 100, 500],
	['orange', 100-200, -450+300, 100, 200],
	['green', 200-200, -150+300, 300, 500],
	['grey', 100-200, -150+300, 100, 300],
]

for t in dic:
	a.up()
	a.setpos(t[1], t[2])
	print(a.pos())
	a.down()

	a.color = t[0]

	a.fillcolor(t[0])
	
	a.begin_fill()
	a.forward(t[3])
	a.right(90)
	a.forward(t[4])
	a.right(90)
	a.forward(t[3])
	a.right(90)
	a.forward(t[4])
	a.right(90)

	a.end_fill()

tu.done()



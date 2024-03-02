import turtle
tree=turtle.Turtle()        #Making object
tree.screen.bgcolor("Black")
tree.pensize(2)
tree.color("green")
tree.left(90)
tree.backward(100)
tree.speed(200)
tree.shape('turtle')
def treee(i):
    if i<10:
        return
    else:
        tree.forward(i)
        tree.color("pink")
        tree.circle(2)
        tree.color("green")
        tree.left(30)
        treee(3*i/4)
        tree.right(60)
        treee(3*i/4)
        tree.left(30)
        tree.backward(i)
treee(100)
turtle.done()
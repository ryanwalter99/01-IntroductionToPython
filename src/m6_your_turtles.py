"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Ryan Walter.
"""
###############################################################################
# done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################
import rosegraphics as rg
###############################################################################
# TODO: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
window = rg.TurtleWindow()
tim = rg.SimpleTurtle('square')
bob = rg.SimpleTurtle('circle')

tim.pen = rg.Pen('green',15)
bob.pen = rg.Pen('blue', 25)
tim.speed = 10
bob.speed = 10

size = 100
size2 = 50

for k in range(11):
    tim.draw_circle(size)
    bob.draw_circle(size2)

    size = size - 10
    size2 = size2 + 10

window.close_on_mouse_click()
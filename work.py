def pythogaras():
    [(x,y,z) for x in range (1,100) for y in range (x,100) for z in range (y,100) if x*x + y*y == z*z]

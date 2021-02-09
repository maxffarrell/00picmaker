def draw():
    image=open('image.ppm','w')
    image.write('P3\n500 500\n255\n')

    r=0
    g=0
    b=255
    i=1
    for x in range(500):
        for y in range(500):
            image.write('0 '+str(abs(g%255))+' '+str(abs(b%255))+' ')
            g+=i
            b-=i
            i+=5
draw()

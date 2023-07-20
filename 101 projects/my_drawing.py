"""
File: SC101Assignment1
Name: Eydie
----------------------
TODO: draw a solar system, the sun and 8 planets
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GPolygon
from campy.graphics.gwindow import GWindow

WINDOWWIDTH = 800
WINDOWHEIGHT = 500


def main():
    """
    Title: Mom is like a sun
    mom, my friend so dear, loves planets. as the mothers day is coming, this will be her card that her daughter
    made from nothing, which she should be proud of LOL
    she is the best mom in the universe, she lights us up with warmth and bright when we were kids and will do so
    till end of the world.
    """
    window = GWindow(width=WINDOWWIDTH, height=WINDOWHEIGHT, title='solar')
    rect = GRect(WINDOWWIDTH, WINDOWHEIGHT)
    rect.filled = True
    window.add(rect)
    oral1 = GOval(750, 450)
    oral1.color = 'white'
    oral2 = GOval(680, 400)
    oral2.color = 'white'
    oral3 = GOval(610, 350)
    oral3.color = 'white'
    oral4 = GOval(540, 300)
    oral4.color = 'white'
    oral5 = GOval(470, 250)
    oral5.color = 'white'
    oral6 = GOval(400, 200)
    oral6.color = 'white'
    oral7 = GOval(330, 150)
    oral7.color = 'white'
    oral8 = GOval(260, 100)
    oral8.color = 'white'
    sun = GOval(150, 150)
    sun.filled = True
    sun.color = sun.fill_color = 'gold'
    sunshadow = GOval(158, 158)
    sunshadow.filled = True
    sunshadow.color = sunshadow.fill_color = 'goldenrod'
    sun1 = GOval(50, 50)
    sun1.filled = True
    sun1.color = sun1.fill_color = 'lightgoldenrodyellow'
    sun2 = GOval(50, 50)
    sun2.filled = True
    sun2.color = sun2.fill_color = 'sandybrown'
    sun3 = GOval(30, 30)
    sun3.filled = True
    sun3.color = sun3.fill_color = 'goldenrod'
    sun4 = GOval(30, 30)
    sun4.filled = True
    sun4.color = sun4.fill_color = 'goldenrod'
    sun5 = GOval(20, 20)
    sun5.filled = True
    sun5.color = sun5.fill_color = 'darkgoldenrod'

    squaresun1 = GPolygon()
    squaresun1.filled = True
    squaresun1.fill_color = squaresun1.color = 'khaki'
    squaresun1.add_vertex((365, 17))
    squaresun1.add_vertex((400, 67))
    squaresun1.add_vertex((420, 27))
    squaresun2 = GPolygon()
    squaresun2.filled = True
    squaresun2.fill_color = squaresun2.color = 'khaki'
    squaresun2.add_vertex((405, 157))
    squaresun2.add_vertex((380, 77))
    squaresun2.add_vertex((450, 90))
    squaresun3 = GPolygon()
    squaresun3.filled = True
    squaresun3.fill_color = squaresun3.color = 'yellow'
    squaresun3.add_vertex((340, 77))
    squaresun3.add_vertex((380, 47))
    squaresun3.add_vertex((400, 60))
    squaresun4 = GPolygon()
    squaresun4.filled = True
    squaresun4.fill_color = squaresun4.color = 'yellow'
    squaresun4.add_vertex((440, 145))
    squaresun4.add_vertex((470, 87))
    squaresun4.add_vertex((420, 130))
    squaresun5 = GPolygon()
    squaresun5.filled = True
    squaresun5.fill_color = squaresun5.color = 'yellow'
    squaresun5.add_vertex((440, 75))
    squaresun5.add_vertex((460, 37))
    squaresun5.add_vertex((420, 60))
    solar8 = GOval(20, 20)
    solar8.filled = True
    solar8.color = 'palegreen'
    solar8.fill_color = 'lawngreen'
    square8 = GPolygon()
    square8.filled = True
    square8.fill_color = square8.color = 'darkcyan'
    square8.add_vertex((490, 172))
    square8.add_vertex((509, 174))
    square8.add_vertex((510, 168))
    line8 = GArc(40, 20, 20, 100)
    line8.color = 'sage'
    solar7 = GOval(50, 50)
    solar7.filled = True
    solar7.color = 'gray'
    solar7.fill_color = 'slategray'
    square7 = GPolygon()
    square7.filled = True
    square7.fill_color = square7.color = 'darkslategray'
    square7.add_vertex((300, 200))
    square7.add_vertex((251, 207))
    square7.add_vertex((250, 200))
    square71 = GPolygon()
    square71.filled = True
    square71.fill_color = square71.color = 'lightgrey'
    square71.add_vertex((295, 215))
    square71.add_vertex((252, 210))
    square71.add_vertex((255, 216))
    square72 = GPolygon()
    square72.filled = True
    square72.fill_color = square72.color = 'gray'
    square72.add_vertex((299, 195))
    square72.add_vertex((297, 188))
    square72.add_vertex((255, 187))
    solar6 = GOval(80, 80)
    solar6.filled = True
    solar6.color = 'dodgerblue'
    solar6.fill_color = 'blue'
    line6 = GArc(118, 80, 20, 100)
    line6.color = 'dodgerblue'
    line61 = GArc(116, 80, 20, 100)
    line61.color = 'dodgerblue'
    line62 = GArc(145, 80, 20, 100)
    line62.color = 'dodgerblue'
    line63 = GArc(136, 90, 20, 100)
    line63.color = 'dodgerblue'
    line64 = GArc(133, 90, 20, 100)
    line64.color = 'dodgerblue'
    square6 = GPolygon()
    square6.filled = True
    square6.fill_color = square6.color = 'royalblue'
    square6.add_vertex((450, 260))
    square6.add_vertex((452, 250))
    square6.add_vertex((528, 250))
    square62 = GPolygon()
    square62.filled = True
    square62.fill_color = square62.color = 'deepskyblue'
    square62.add_vertex((530, 260))
    square62.add_vertex((528, 250))
    square62.add_vertex((450, 260))
    solar5 = GOval(40, 40)
    solar5.filled = True
    solar5.color = 'brown'
    solar5.fill_color = 'maroon'
    line5 = GArc(33, 25, 180, 180)
    line5.color = 'bisque'
    line52 = GArc(35, 25, 180, 180)
    line52.color = 'bisque'
    line53 = GArc(39, 30, 180, 180)
    line53.color = 'bisque'
    line54 = GArc(39, 30, 180, 180)
    line54.color = 'bisque'
    line55 = GArc(22, 20, 180, 170)
    line55.color = 'bisque'
    solar4 = GOval(60, 60)
    solar4.filled = True
    solar4.color = 'gray'
    solar4.fill_color = 'silver'
    line4 = GArc(60, 50, 180, 180)
    line4.color = 'sienna'
    line40 = GArc(60, 50, 180, 180)
    line40.color = 'sienna'
    line41 = GArc(50, 40, 180, 180)
    line41.color = 'sienna'
    line42 = GArc(50, 40, 180, 180)
    line42.color = 'sienna'
    line45 = GArc(50, 40, 180, 180)
    line45.color = 'sienna'
    line46 = GArc(48, 40, 180, 180)
    line46.color = 'sienna'
    line43 = GArc(60, 50, 180, 180)
    line43.color = 'sienna'
    line44 = GArc(60, 50, 180, 180)
    line44.color = 'sienna'
    line47 = GArc(55, 48, 180, 180)
    line47.color = 'sienna'
    line48 = GArc(61, 50, 180, 180)
    line48.color = 'maroon'
    line481 = GArc(61, 50, 180, 180)
    line481.color = 'maroon'
    line482 = GArc(60, 50, 180, 180)
    line482.color = 'maroon'
    line483 = GArc(59, 50, 180, 180)
    line483.color = 'maroon'
    line484 = GArc(58, 50, 180, 180)
    line484.color = 'maroon'
    line49 = GArc(53, 40, 180, 180)
    line49.color = 'maroon'
    line491 = GArc(30, 24, 180, 180)
    line491.color = 'maroon'
    solar3 = GOval(30, 30)
    solar3.filled = True
    solar3.color = 'ivory'
    solar3.fill_color = 'red'
    line3 = GArc(30, 30, 0, 180)
    line3.color = 'snow'
    line31 = GArc(30, 30, 0, 180)
    line31.color = 'snow'
    line32 = GArc(27, 27, 0, 180)
    line32.color = 'snow'
    line33 = GArc(26, 26, 0, 180)
    line33.color = 'snow'
    line34 = GArc(20, 20, 0, 180)
    line34.color = 'snow'
    solar2 = GOval(120, 120)
    solar2.filled = True
    solar2.color = solar2.fill_color = 'saddlebrown'
    solar2ring = GOval(200, 30)
    solar2ring.filled = True
    solar2ring.color = solar2ring.fill_color = 'black'
    solar2ring2 = GOval(250, 40)
    solar2ring2.filled = True
    solar2ring2.color = solar2ring2.fill_color = 'olive'
    belt = GPolygon()
    belt.filled = True
    belt.color = belt.fill_color = 'olive'
    belt.add_vertex((200, 418))
    belt.add_vertex((200, 428))
    belt.add_vertex((320, 428))
    belt.add_vertex((320, 418))
    solar1 = GOval(40, 40)
    solar1.filled = True
    solar1.color = 'ivory'
    solar1.fill_color = 'coral'
    line1 = GArc(39, 40, 0, 180)
    line1.color = 'bisque'
    line12 = GArc(36, 38, 0, 180)
    line12.color = 'brown'
    line13 = GArc(36, 38, 0, 180)
    line13.color = 'brown'
    line14 = GArc(32, 32, 0, 180)
    line14.color = 'brown'
    line15 = GArc(38, 43, 0, 170)
    line15.color = 'brown'
    line16 = GArc(41, 45, 0, 170)
    line16.color = 'brown'

    window.add(oral2, x=WINDOWWIDTH / 2 - oral2.width / 2, y=30)
    window.add(oral3, x=WINDOWWIDTH / 2 - oral3.width / 2, y=40)
    window.add(oral4, x=WINDOWWIDTH / 2 - oral4.width / 2, y=50)
    window.add(oral5, x=WINDOWWIDTH / 2 - oral5.width / 2, y=60)
    window.add(oral6, x=WINDOWWIDTH / 2 - oral6.width / 2, y=70)
    window.add(oral7, x=WINDOWWIDTH / 2 - oral7.width / 2, y=80)
    window.add(oral8, x=WINDOWWIDTH / 2 - oral8.width / 2, y=90)
    window.add(solar8, x=WINDOWWIDTH / 2 + oral8.width / 2 - 40, y=160)
    window.add(square8)
    window.add(line8, x=483, y=165)
    window.add(solar7, x=250, y=176)
    window.add(square7)
    window.add(square71)
    window.add(square72)
    window.add(solar6, x=450, y=220)
    window.add(line6, x=435, y=280)
    window.add(line61, x=435, y=282)
    window.add(line62, x=425, y=270)
    window.add(line63, x=432, y=236)
    window.add(line64, x=433, y=234)
    window.add(square6)
    window.add(square62)
    window.add(solar5, x=580, y=100)
    window.add(line55, x=589, y=98)
    window.add(line5, x=583, y=103)
    window.add(line52, x=582, y=104)
    window.add(line53, x=580, y=112)
    window.add(line54, x=580, y=113)
    window.add(solar4, x=635, y=180)
    window.add(line4, x=635, y=190)
    window.add(line40, x=635, y=191)
    window.add(line43, x=635, y=192)
    window.add(line44, x=635, y=193)
    window.add(line41, x=640, y=184)
    window.add(line42, x=640, y=183)
    window.add(line45, x=640, y=182)
    window.add(line46, x=641, y=181)
    window.add(line47, x=638, y=186)
    window.add(line48, x=635, y=200)
    window.add(line481, x=635, y=201)
    window.add(line482, x=635, y=202)
    window.add(line483, x=635, y=203)
    window.add(line484, x=636, y=204)
    window.add(line49, x=639, y=215)
    window.add(solar3, x=605, y=320)
    window.add(line3, x=605, y=325)
    window.add(line31, x=605, y=328)
    window.add(line32, x=606, y=335)
    window.add(line33, x=607, y=336)
    window.add(line34, x=610, y=342)
    window.add(solar2ring2, x=135, y=390)
    window.add(solar2ring, x=158, y=390)
    window.add(solar2, x=200, y=351)
    window.add(belt)
    window.add(oral1, x=WINDOWWIDTH / 2 - oral1.width / 2, y=20)
    window.add(solar1, x=700, y=340)
    window.add(line1, x=700, y=353)
    window.add(line12, x=702, y=360)
    window.add(line13, x=702, y=361)
    window.add(line14, x=704, y=366)
    window.add(line15, x=701, y=343)
    window.add(line16, x=700, y=346)
    window.add(sunshadow, x=WINDOWWIDTH / 2 - sunshadow.width / 2, y=7)
    window.add(sun, x=WINDOWWIDTH / 2 - sun.width / 2, y=7)

    window.add(sun1, x=390, y=30)
    window.add(sun2, x=350, y=67)
    window.add(sun3, x=440, y=60)
    window.add(sun4, x=360, y=120)
    window.add(sun5, x=345, y=35)
    window.add(squaresun1)
    window.add(squaresun3)
    window.add(squaresun2)
    window.add(squaresun4)
    window.add(squaresun5)



if __name__ == '__main__':
    main()

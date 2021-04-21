"""
File: my_drawing.py
Name: Peggy
----------------------
TODO: inspired by the famous iceland chocolate brand OmNom.
"""

from campy.graphics.gobjects import GOval, GRect,GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO: use different kinds of rectangles, triangles to create a wolf
    """
    window = GWindow(width=500, height=500, title='wolf')

    head = GPolygon()
    head.add_vertex((225, 100))
    head.add_vertex((275, 100))
    head.add_vertex((250, 225))
    head.filled = True
    head.fill_color = 'thistle'
    window.add(head)

    ear = GPolygon()
    ear.add_vertex((170, 190))
    ear.add_vertex((130, 120))
    ear.add_vertex((100, 200))
    ear.filled = True
    ear.fill_color = 'wheat'
    window.add(ear)

    ear = GPolygon()
    ear.add_vertex((330, 190))
    ear.add_vertex((370, 120))
    ear.add_vertex((400, 200))
    ear.filled = True
    ear.fill_color = 'wheat'
    window.add(ear)

    ear = GPolygon()
    ear.add_vertex((200, 145))
    ear.add_vertex((150, 120))
    ear.add_vertex((100, 100))
    ear.add_vertex((100, 130))
    ear.add_vertex((170, 180))
    ear.filled = True
    ear.fill_color = 'peru'
    window.add(ear)


    ear = GPolygon()
    ear.add_vertex((300, 145))
    ear.add_vertex((350, 120))
    ear.add_vertex((400, 100))
    ear.add_vertex((400, 130))
    ear.add_vertex((330, 180))
    ear.filled = True
    ear.fill_color = 'peru'
    window.add(ear)

    head4 = GPolygon()
    head4.add_vertex((200, 110))
    head4.add_vertex((250, 225))
    head4.add_vertex((210, 225))
    head4.add_vertex((190, 215))
    head4.add_vertex((180, 120)) #ear point
    head4.add_vertex((200, 110))
    head4.filled = True
    head4.fill_color = 'coral'
    window.add(head4)

    head4 = GPolygon()
    head4.add_vertex((320, 110))
    head4.add_vertex((250, 225))
    head4.add_vertex((290, 225))
    head4.add_vertex((310, 215))
    head4.add_vertex((320, 120))
    head4.add_vertex((320, 110))
    head4.filled = True
    head4.fill_color = 'cornsilk'
    window.add(head4)

    ear = GPolygon()
    ear.add_vertex((300, 115))
    ear.add_vertex((400, 70))
    ear.add_vertex((410, 70))
    ear.add_vertex((405, 100))
    ear.add_vertex((330, 150))
    ear.filled = True
    ear.fill_color = 'brown'
    window.add(ear)

    ear = GPolygon()
    ear.add_vertex((200, 115))
    ear.add_vertex((100, 70))
    ear.add_vertex((90, 70))
    ear.add_vertex((95, 100))
    ear.add_vertex((170, 150))
    ear.filled = True
    ear.fill_color = 'brown'
    window.add(ear)


    ear = GPolygon()
    ear.add_vertex((180, 130))
    ear.add_vertex((120, 90))
    ear.add_vertex((125, 120))
    ear.add_vertex((130, 160))
    ear.add_vertex((140, 170))
    ear.add_vertex((170, 200))
    ear.filled = True
    ear.fill_color = 'burlywood'
    window.add(ear)

    ear = GPolygon()
    ear.add_vertex((320, 130))
    ear.add_vertex((380, 90))
    ear.add_vertex((375, 120))
    ear.add_vertex((370, 160))
    ear.add_vertex((360, 170))
    ear.add_vertex((330, 200))
    ear.filled = True
    ear.fill_color = 'burlywood'
    window.add(ear)

    head2 = GPolygon()
    head2.add_vertex((225, 100))
    head2.add_vertex((180, 110))
    head2.add_vertex((250, 225))
    head2.filled = True
    head2.fill_color = 'peru'
    window.add(head2)

    head3 = GPolygon()
    head3.add_vertex((275, 100))
    head3.add_vertex((320, 110))
    head3.add_vertex((250, 225))
    head3.filled = True
    head3.fill_color = 'khaki'
    window.add(head3)

    head5 = GPolygon()
    head5.add_vertex((181, 138))
    head5.add_vertex((170, 140))
    head5.add_vertex((140, 225))
    head5.add_vertex((190, 225))
    head5.add_vertex((190, 225))
    head5.filled = True
    head5.fill_color = 'mistyrose'
    window.add(head5)

    head6 = GPolygon()
    head6.add_vertex((319, 138))
    head6.add_vertex((330, 140))
    head6.add_vertex((360, 225))
    head6.add_vertex((310, 225))
    head6.add_vertex((310, 225))
    head6.filled = True
    head6.fill_color = 'orange'
    window.add(head6)

    eye_left = GPolygon() # eyes up
    eye_left.add_vertex((190, 205))
    eye_left.add_vertex((170, 225))
    eye_left.add_vertex((225, 225))
    eye_left.filled = True
    eye_left.fill_color = 'black'
    window.add(eye_left)

    eye_left = GPolygon()  # eyes down
    eye_left.add_vertex((190, 225))
    eye_left.add_vertex((200, 235))
    eye_left.add_vertex((225, 225))
    eye_left.filled = True
    eye_left.fill_color = 'black'
    window.add(eye_left)

    eye_right = GPolygon()  # eyes up
    eye_right.add_vertex((310, 205))
    eye_right.add_vertex((330, 225))
    eye_right.add_vertex((275, 225))
    eye_right.filled = True
    eye_right.fill_color = 'black'
    window.add(eye_right)

    eye_right = GPolygon()  # eyes down
    eye_right.add_vertex((310, 225))
    eye_right.add_vertex((300, 235))
    eye_right.add_vertex((275, 225))
    eye_right.filled = True
    eye_right.fill_color = 'black'
    window.add(eye_right)

    head7 = GPolygon()
    head7.add_vertex((250, 225))
    head7.add_vertex((220, 225))
    head7.add_vertex((200, 235))
    head7.add_vertex((220, 330))
    head7.add_vertex((250, 225))
    head7.filled = True
    head7.fill_color = 'purple'
    window.add(head7)

    head8 = GPolygon()
    head8.add_vertex((250, 225))
    head8.add_vertex((280, 225))
    head8.add_vertex((300, 235))
    head8.add_vertex((280, 330))
    head8.add_vertex((250, 225))
    head8.filled = True
    head8.fill_color = 'skyblue'
    window.add(head8)

    head9 = GPolygon()
    head9.add_vertex((250, 225))
    head9.add_vertex((250, 320))
    head9.add_vertex((220, 330))
    head9.filled = True
    head9.fill_color = 'sage'
    window.add(head9)

    head9 = GPolygon()
    head9.add_vertex((250, 225))
    head9.add_vertex((250, 320))
    head9.add_vertex((280, 330))
    head9.filled = True
    head9.fill_color = 'lightpink'
    window.add(head9)

    nose = GPolygon()
    nose.add_vertex((250, 320))
    nose.add_vertex((280, 330))
    nose.add_vertex((270, 345))
    nose.add_vertex((250, 350))
    nose.add_vertex((230, 345))
    nose.add_vertex((220, 330))
    nose.filled = True
    nose.fill_color = 'black'
    window.add(nose)

    cheek = GPolygon()
    cheek.add_vertex((310, 225))
    cheek.add_vertex((330, 225))
    cheek.add_vertex((350, 240))
    cheek.add_vertex((320, 300))
    cheek.filled = True
    cheek.fill_color = 'salmon'
    window.add(cheek)

    cheek = GPolygon()
    cheek.add_vertex((310, 225))
    cheek.add_vertex((320, 300))
    cheek.add_vertex((305, 325))
    cheek.add_vertex((300, 235))
    cheek.filled = True
    cheek.fill_color = 'gold'
    window.add(cheek)

    cheek = GPolygon()
    cheek.add_vertex((190, 225))
    cheek.add_vertex((180, 300))
    cheek.add_vertex((195, 325))
    cheek.add_vertex((200, 235))
    cheek.filled = True
    cheek.fill_color = 'magenta'
    window.add(cheek)

    cheek = GPolygon()
    cheek.add_vertex((190, 225))
    cheek.add_vertex((170, 225))
    cheek.add_vertex((150, 240))
    cheek.add_vertex((180, 300))
    cheek.filled = True
    cheek.fill_color = 'lavenderblush'
    window.add(cheek)

    cheek = GPolygon()
    cheek.add_vertex((300, 235))
    cheek.add_vertex((270, 345))
    cheek.add_vertex((290, 345))
    cheek.filled = True
    cheek.fill_color = 'yellow'
    window.add(cheek)

    cheek = GPolygon()
    cheek.add_vertex((200, 235))
    cheek.add_vertex((230, 345))
    cheek.add_vertex((210, 345))
    cheek.filled = True
    cheek.fill_color = 'yellow'
    window.add(cheek)

    cheek = GPolygon()
    cheek.add_vertex((200, 235))
    cheek.add_vertex((210, 345))
    cheek.add_vertex((200, 370))
    cheek.add_vertex((195, 330))
    cheek.filled = True
    cheek.fill_color = 'brown'
    window.add(cheek)

    cheek = GPolygon()
    cheek.add_vertex((300, 235))
    cheek.add_vertex((290, 345))
    cheek.add_vertex((300, 370))
    cheek.add_vertex((305, 330))
    cheek.filled = True
    cheek.fill_color = 'brown'
    window.add(cheek)

    cheek = GPolygon()
    cheek.add_vertex((300, 235))
    cheek.add_vertex((310, 310))
    cheek.add_vertex((305, 355))
    cheek.add_vertex((300, 330))
    cheek.filled = True
    cheek.fill_color = 'violet'
    window.add(cheek)

    cheek = GPolygon()
    cheek.add_vertex((200, 235))
    cheek.add_vertex((190, 310))
    cheek.add_vertex((195, 355))
    cheek.add_vertex((200, 330))
    cheek.filled = True
    cheek.fill_color = 'aliceblue'
    window.add(cheek)

    cheek = GPolygon()
    cheek.add_vertex((330, 225))
    cheek.add_vertex((325, 200))
    cheek.add_vertex((350, 230))
    cheek.add_vertex((360, 250))
    cheek.filled = True
    cheek.fill_color = 'grey'
    window.add(cheek)

    cheek = GPolygon()
    cheek.add_vertex((325, 200))
    cheek.add_vertex((355, 210))
    cheek.add_vertex((365, 245))
    cheek.add_vertex((350, 230))
    cheek.filled = True
    cheek.fill_color = 'green'
    window.add(cheek)

    cheek = GPolygon()
    cheek.add_vertex((325, 200))
    cheek.add_vertex((350, 195))
    cheek.add_vertex((375, 230))
    cheek.add_vertex((350, 220))
    cheek.filled = True
    cheek.fill_color = 'blue'
    window.add(cheek)

    cheek = GPolygon()
    cheek.add_vertex((170, 225))
    cheek.add_vertex((175, 200))
    cheek.add_vertex((150, 230))
    cheek.add_vertex((140, 250))
    cheek.filled = True
    cheek.fill_color = 'grey'
    window.add(cheek)

    cheek = GPolygon()
    cheek.add_vertex((175, 200))
    cheek.add_vertex((145, 210))
    cheek.add_vertex((135, 245))
    cheek.add_vertex((150, 230))
    cheek.filled = True
    cheek.fill_color = 'green'
    window.add(cheek)

    cheek = GPolygon()
    cheek.add_vertex((175, 200))
    cheek.add_vertex((150, 195))
    cheek.add_vertex((125, 230))
    cheek.add_vertex((150, 220))
    cheek.filled = True
    cheek.fill_color = 'greenyellow'
    window.add(cheek)

    line = GLabel("WOLF",220,420)
    line.font = 'courier-25-italic'
    window.add(line)



if __name__ == '__main__':
    main()

#######################################################
#   John Zetterman
#   Assignment 1: Bonus
#   Date: 6/8/2025
#
#   Description: This program draws a German Shepherd using tkinter
#   Inputs: No inputs required
#   Reference Art (because I'm not artistic): https://cdn2.vectorstock.com/i/1000x1000/27/21/german-shepherd-pixel-art-top-vector-25592721.jpg
#######################################################

import tkinter as tk

root = tk.Tk()
root.title("Dog")

canvas = tk.Canvas(root, height=1300, width=1300, bg="white")
canvas.pack()

# Left ear
canvas.create_line(150, 80, 170, 80, width=20, fill="#523624")
canvas.create_line(130, 100, 170, 100, width=20, fill="#523624")
canvas.create_line(130, 120, 190, 120, width=20, fill="#523624")
canvas.create_line(130, 140, 210, 140, width=20, fill="#523624")
canvas.create_line(130, 160, 210, 160, width=20, fill="#523624")
canvas.create_line(130, 180, 230, 180, width=20, fill="#523624")

# Right ear
canvas.create_line(330, 80, 350, 80, width=20, fill="#523624")
canvas.create_line(310, 100, 350, 100, width=20, fill="#523624")
canvas.create_line(310, 120, 370, 120, width=20, fill="#523624")
canvas.create_line(290, 140, 370, 140, width=20, fill="#523624")
canvas.create_line(290, 160, 370, 160, width=20, fill="#523624")
canvas.create_line(270, 180, 370, 180, width=20, fill="#523624")

# Head
canvas.create_line(130, 200, 370, 200, width=20, fill="#523624")
canvas.create_line(130, 220, 370, 220, width=20, fill="#523624")
canvas.create_line(130, 240, 350, 240, width=20, fill="#523624")
canvas.create_line(150, 260, 350, 260, width=20, fill="#523624")
canvas.create_line(130, 280, 370, 280, width=20, fill="#523624")
canvas.create_line(130, 300, 370, 300, width=20, fill="#523624")
canvas.create_line(130, 320, 390, 320, width=20, fill="#523624")
canvas.create_line(150, 340, 390, 340, width=20, fill="#523624")
canvas.create_line(150, 360, 410, 360, width=20, fill="#523624")
canvas.create_line(150, 380, 430, 380, width=20, fill="#523624")
canvas.create_line(150, 400, 450, 400, width=20, fill="#523624")

# Body
canvas.create_line(170, 420, 730, 420, width=20, fill="#523624")
canvas.create_line(190, 440, 890, 440, width=20, fill="#523624")
canvas.create_line(190, 460, 970, 460, width=20, fill="#523624")
canvas.create_line(190, 460, 970, 460, width=20, fill="#523624")
canvas.create_line(210, 480, 990, 480, width=20, fill="#523624")
canvas.create_line(210, 500, 1010, 500, width=20, fill="#523624")
canvas.create_line(210, 520, 1030, 520, width=20, fill="#523624")
canvas.create_line(210, 540, 1050, 540, width=20, fill="#523624")
canvas.create_line(210, 560, 1050, 560, width=20, fill="#523624")
canvas.create_line(210, 580, 1050, 580, width=20, fill="#523624")
canvas.create_line(210, 600, 1050, 600, width=20, fill="#523624")
canvas.create_line(230, 620, 1050, 620, width=20, fill="#523624")
canvas.create_line(230, 640, 1050, 640, width=20, fill="#523624")
canvas.create_line(230, 660, 1070, 660, width=20, fill="#523624")
canvas.create_line(250, 680, 1070, 680, width=20, fill="#523624")

# Front Legs
canvas.create_line(250, 700, 770, 700, width=20, fill="#523624")
canvas.create_line(270, 720, 710, 720, width=20, fill="#523624")
canvas.create_line(290, 740, 670, 740, width=20, fill="#523624")
canvas.create_line(290, 760, 530, 760, width=20, fill="#523624")
canvas.create_line(290, 780, 530, 780, width=20, fill="#523624")
canvas.create_line(310, 800, 530, 800, width=20, fill="#523624")
canvas.create_line(310, 820, 530, 820, width=20, fill="#523624")
canvas.create_line(310, 840, 530, 840, width=20, fill="#523624")
canvas.create_line(310, 860, 530, 860, width=20, fill="#523624")
canvas.create_line(310, 880, 530, 880, width=20, fill="#523624")
canvas.create_line(310, 900, 530, 900, width=20, fill="#523624")
canvas.create_line(310, 920, 530, 920, width=20, fill="#523624")
canvas.create_line(290, 940, 530, 940, width=20, fill="#523624")
canvas.create_line(270, 960, 510, 960, width=20, fill="#523624")
canvas.create_line(250, 980, 510, 980, width=20, fill="#523624")
canvas.create_line(250, 1000, 490, 1000, width=20, fill="#523624")
canvas.create_line(330, 1020, 490, 1020, width=20, fill="#523624")
canvas.create_line(310, 1040, 470, 1040, width=20, fill="#523624")

# Back Legs
canvas.create_line(790, 700, 1070, 700, width=20, fill="#523624")
canvas.create_line(830, 720, 1070, 720, width=20, fill="#523624")
canvas.create_line(850, 740, 1070, 740, width=20, fill="#523624")
canvas.create_line(870, 760, 1090, 760, width=20, fill="#523624")
canvas.create_line(890, 780, 1090, 780, width=20, fill="#523624")
canvas.create_line(910, 800, 1110, 800, width=20, fill="#523624")
canvas.create_line(950, 820, 1110, 820, width=20, fill="#523624")
canvas.create_line(930, 840, 1130, 840, width=20, fill="#523624")
canvas.create_line(870, 860, 1130, 860, width=20, fill="#523624")
canvas.create_line(870, 860, 1010, 860, width=20, fill="#856C53")
canvas.create_line(870, 860, 950, 860, width=20, fill="#433630")
canvas.create_line(930, 860, 970, 860, width=20, fill="#634B3B")
canvas.create_line(970, 860, 990, 860, width=20, fill="#FFFFFF")
canvas.create_line(870, 880, 1130, 880, width=20, fill="#523624")
canvas.create_line(870, 880, 1030, 880, width=20, fill="#856C53")
canvas.create_line(870, 880, 950, 880, width=20, fill="#433630")
canvas.create_line(950, 880, 990, 880, width=20, fill="#FFFFFF")
canvas.create_line(1010, 900, 1110, 900, width=20, fill="#523624")
canvas.create_line(1010, 900, 1050, 900, width=20, fill="#856C53")
canvas.create_line(1030, 920, 1110, 920, width=20, fill="#523624")
canvas.create_line(1030, 920, 1050, 920, width=20, fill="#856C53")
canvas.create_line(1050, 940, 1110, 940, width=20, fill="#B09479")
canvas.create_line(1030, 960, 1110, 960, width=20, fill="#B09479")
canvas.create_line(1010, 980, 1090, 980, width=20, fill="#433630")
canvas.create_line(1010, 1000, 1090, 1000, width=20, fill="#433630")

canvas.create_text(700, 300, text="German Shepherd", fill="black", font="Arial 16 bold")

root.mainloop()

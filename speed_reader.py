from drawingpanel import *
import time
class WordGenerator:
    def __init__(self, file):
        self.words = []
        self.data = open(file);
        self.lines = self.data.read().splitlines()
        for x in range(0, (len(self.lines))):
            self.line = self.lines[x]
            self.words.append(self.line.split(" "))
        self.words = sum(self.words, []) 
        self.quote_count = 0

    def is_empty(self):
        return len(self.words) == 0

    def next_word(self):
       return self.words.pop(0)

    
    def in_Quotes(self, word):
        if(word.count('\"') == 2):
            return True
        if("\"" in word):
            self.quote_count += 1
            return True
        elif(self.quote_count > 1):
            self.quote_count = 0
            return False
        elif(self.quote_count == 1):
            if "\"" in word:
                self.quote_count += 1  
            return True
        return False


def animate_text(gen, width, height, size, wpm):
    panal = DrawingPanel(width,height)
    canvas = panal.canvas
    while(not gen.is_empty()):
        print_word(gen.next_word(), canvas, size, width, height, gen)
        panal.sleep(60000/wpm)
        canvas.delete('all')


def print_word(word, canvas, size, width, height, gen):
    if(gen.in_Quotes(word)):
        if len(word) == 1:
            canvas.create_text(width / 2,height / 2,text = word, font = ("Courier", size),fill = "red") 
            canvas.create_text(width / 2,height / 2,text = word[0], font = ("Courier",size, "bold"), fill = "green")
        elif len(word) == 2:
            canvas.create_text(width / 2,height / 2,text = word + (" ") , font = ("Courier",size), fill = "red") 
            canvas.create_text(width / 2,height / 2,text = word[1], font = ("Courier",size, "bold"), fill = "green")
        elif len(word) >= 3 and len(word) <= 5:
            canvas.create_text(width / 2,height / 2,text = (" " * (len(word) - 3)) + word, font = ("Courier",size), fill = "red") 
            canvas.create_text(width / 2,height / 2,text = word[1], font = ("Courier",size, "bold"), fill = "green")
        elif len(word) >= 6 and len(word) <= 9:
            canvas.create_text(width / 2,height / 2,text = (" " * (len(word) -  5)) + word, font = ("Courier",size), fill = "red") 
            canvas.create_text(width / 2,height / 2,text = word[2], font = ("Courier",size, "bold"), fill = "green")
        elif len(word) >= 10 and len(word) <= 13:
            canvas.create_text(width / 2,height / 2,text = (" " * (len(word) - 7)) + word, font = ("Courier",size), fill = "red") 
            canvas.create_text(width / 2,height / 2,text = word[3], font = ("Courier",size, "bold"), fill = "green")
        elif len(word) > 13:
            canvas.create_text(width / 2,height / 2,text = (" " * (len(word) - 9)) + word, font = ("Courier",size), fill = "red") 
            canvas.create_text(width / 2,height / 2,text = word[4], font = ("Courier",size, "bold"), fill = "green")
    else:
        if len(word) == 1:
            canvas.create_text(width / 2,height / 2,text = word, font = ("Courier", size),fill = "black") 
            canvas.create_text(width / 2,height / 2,text = word[0], font = ("Courier",size, "bold"), fill = "orange")
        elif len(word) == 2:
            canvas.create_text(width / 2,height / 2,text = word + (" ") , font = ("Courier",size), fill = "black") 
            canvas.create_text(width / 2,height / 2,text = word[1], font = ("Courier",size, "bold"), fill = "orange")
        elif len(word) >= 3 and len(word) <= 5:
            canvas.create_text(width / 2,height / 2,text = (" " * (len(word) - 3)) + word, font = ("Courier",size), fill = "black") 
            canvas.create_text(width / 2,height / 2,text = word[1], font = ("Courier",size, "bold"), fill = "orange")
        elif len(word) >= 6 and len(word) <= 9:
            canvas.create_text(width / 2,height / 2,text = (" " * (len(word) -  5)) + word, font = ("Courier",size), fill = "black") 
            canvas.create_text(width / 2,height / 2,text = word[2], font = ("Courier",size, "bold"), fill = "orange")
        elif len(word) >= 10 and len(word) <= 13:
            canvas.create_text(width / 2,height / 2,text = (" " * (len(word) - 7)) + word, font = ("Courier",size), fill = "black") 
            canvas.create_text(width / 2,height / 2,text = word[3], font = ("Courier",size, "bold"), fill = "orange")
        elif len(word) > 13:
            canvas.create_text(width / 2,height / 2,text = (" " * (len(word) - 9)) + word, font = ("Courier",size), fill = "black") 
            canvas.create_text(width / 2,height / 2,text = word[4], font = ("Courier",size, "bold"), fill = "orange")

        
animate_text(WordGenerator('futbol.txt'), 400, 200, 30, 900)
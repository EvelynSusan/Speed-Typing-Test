from tkinter import *
import random
import ttkthemes
from tkinter import ttk
from time import sleep
import threading

# FUNCTIONALITIES
def start():
    thread1 = threading.Thread(target=start_timer)
    thread1.start()

    thread2 = threading.Thread(target=count)
    thread2.start()

# # Global declarations
totaltime = 60
time = 0
wrong_words = 0
elapsedtimeinminutes = 0
def reset():
    global time,elapsedtimeinmintues
    time = 0
    elapsedtimeinmintues = 0
    start_button.config(state=NORMAL)
    reset_button.config(state=DISABLED) # In between reset is disabled
    textarea.config(state=NORMAL)
    textarea.delete(1.0,END)
    textarea.config(state=DISABLED)
    timer_label.config(text='60')
    accuracy_percent_label.config(text='0')
    total_words_count_label.config(text='0')
    wrong_words_count_label.config(text='0')
    wpm_count_label.config(text='0')

def start_timer():
    start_button.config(state=DISABLED)
    global time
    textarea.config(state=NORMAL)
    textarea.focus()

    for time in range(1, 61):
        remainingtime = totaltime - time
        timer_label.config(text=remainingtime)
        sleep(1)
        root.update()

    textarea.config(state=DISABLED)
    reset_button.config(state=NORMAL)
def count():
    global wrong_words
    while time != totaltime:
        entered_paragraph = textarea.get(1.0, END).split()
        totalwords = len(entered_paragraph)

    total_words_count_label.config(text=totalwords)
    para_word_list = label_paragraph['text'].split()

    for pair in list(zip(para_word_list, entered_paragraph)):
        if pair[0] != pair[1]:
             wrong_words += 1

    wrong_words_count_label.config(text=wrong_words)

    elapsedtimeinminutes = time/60
    wpm = int((totalwords-wrong_words)/elapsedtimeinminutes)
    wpm_count_label.config(text=wpm)
    gross_wpm = totalwords/elapsedtimeinminutes
    accuracy = (wpm/gross_wpm)*100
    accuracy = round(accuracy)
    accuracy_percent_label.config(text=str(accuracy)+'%')

# GUI SECTION
root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.geometry('850x600+200+10')
root.resizable(0, 0)
root.overrideredirect(True)

mainframe = Frame(root, bd=4)
mainframe.grid()  # by default row and column is 0,0

titleframe = Frame(mainframe, bg='grey')
titleframe.grid()

titleLabel = Label(titleframe, text='SPEED TYPING', font=('times', 28, 'bold'), bg='black', fg='white', width=38)
titleLabel.grid(pady=5)

paragraph_frame = Frame(mainframe)
paragraph_frame.grid(row=1, column=0)
paragraph_list = [
    'The sun dipped below the horizon, painting the sky in hues of orange and pink. As darkness descended, the stars began to twinkle overhead, casting their gentle light on the world below. In the stillness of the night, the world seemed to hold its breath, as if waiting for something miraculous to happen. And perhaps it would, for in the quiet moments between dusk and dawn, anything was possible. So I stood there, bathed in the soft glow of moonlight, and let myself believe that maybe, just maybe, tomorrow would bring with it something extraordinary.',
    'The waves crashed against the shore, a rhythmic melody of the sea. Seagulls soared overhead, their cries carried on the breeze. With each step along the sandy beach, worries melted away, replaced by a sense of tranquility and awe. In that moment, everything felt perfect and whole.',
    "The city streets hummed with activity, a constant stream of people and cars. Yet amidst the hustle and bustle, there were pockets of quiet waiting to be discovered. A hidden park, a quaint café tucked away on a side street—these were the hidden gems of the city, offering respite from the chaos. And as I wandered through the streets, I couldn't help but marvel at the beauty and diversity of urban life.",
    "The jagged peaks of the mountains soared into the sky, their snow-capped summits glistening in the sunlight. Below, a winding trail snaked its way through the valley, beckoning adventurers to explore its rugged terrain. I set out with a sense of determination, the crisp mountain air filling my lungs with each breath. As I ascended higher and higher, the world below seemed to shrink away, replaced by a sense of awe and wonder at the majesty of nature.",
    "The aroma of freshly brewed coffee filled the cozy café as patrons chatted over steaming cups. Outside, rain pattered against the windows, casting a soft glow over the scene. I sat in a corner, lost in a book, the world around me fading into the background. In that moment, it felt as if time stood still, the only thing that mattered was the story unfolding before me. And as I turned the pages, I was transported to another world, one filled with adventure and possibility.",
    "The ancient castle loomed majestically against the backdrop of the rugged mountains, its weathered stone walls standing as a testament to centuries of history and tradition. As I stepped through the imposing gates, I felt a sense of awe wash over me, as if I had been transported back in time to a bygone era of knights and kings. The air was thick with the scent of moss and decay, a reminder of the passage of time and the inevitable march of progress. Yet despite its age, the castle retained an air of grandeur and mystery, its secrets whispered through the corridors and hidden passageways that wound their way through its labyrinthine depths. As I explored its ancient halls, I couldn't help but wonder about the lives of those who had come before me, and the stories that lay buried within these ancient stones.",
    "The waves crashed against the rocky shore, sending plumes of spray into the air. Seagulls circled overhead, their cries echoing across the expanse of the sea. With each step along the rugged coastline, I felt a sense of awe and wonder. In the vastness of the ocean, I found solace, a reminder of the beauty and power of the natural world.",
    "Amidst the quiet of the library, the scent of old books hung in the air like a comforting blanket. Sunlight streamed through the stained-glass windows, casting colorful patterns on the polished wooden tables. Each shelf was a treasure trove of knowledge, waiting to be explored. I ran my fingers along the spines of the books, feeling the weight of centuries of wisdom at my fingertips. In that moment, surrounded by the collective knowledge of humanity, I felt a profound sense of awe and gratitude."]

random.shuffle(paragraph_list)

label_paragraph = Label(paragraph_frame, text=paragraph_list[0], wraplength=840, justify=LEFT, font=('times', 16))
label_paragraph.grid(row=0, column=0, pady=8)

textarea_frame = Frame(mainframe)
textarea_frame.grid(row=2, column=0, pady=10)

textarea = Text(textarea_frame, font=('times', 12), width=100, height=10, bd=4, relief=GROOVE, wrap='word',
                state=DISABLED)
textarea.grid()

frame_output = Frame(mainframe)
frame_output.grid(row=3, column=0)

time_label = Label(frame_output, text='Time', font=('Tahoma', 12, 'bold'), fg='red')
time_label.grid(row=0, column=0, padx=5)

timer_label = Label(frame_output, text='60', font=('Tahoma', 12, 'bold'))
timer_label.grid(row=0, column=1, padx=5)

wpm_label = Label(frame_output, text='WPM', font=('Tahoma', 12, 'bold'), fg='red')
wpm_label.grid(row=0, column=2, padx=5)

wpm_count_label = Label(frame_output, text='0', font=('Tahoma', 12, 'bold'))
wpm_count_label.grid(row=0, column=3, padx=5)

total_words_label = Label(frame_output, text='Total Words', font=('Tahoma', 12, 'bold'), fg='red')
total_words_label.grid(row=0, column=4, padx=5)

total_words_count_label = Label(frame_output, text='0', font=('Tahoma', 12, 'bold'))
total_words_count_label.grid(row=0, column=5, padx=5)

wrong_words_label = Label(frame_output, text='Wrong Words', font=('Tahoma', 12, 'bold'), fg='red')
wrong_words_label.grid(row=0, column=6, padx=5)

wrong_words_count_label = Label(frame_output, text='0', font=('Tahoma', 12, 'bold'))
wrong_words_count_label.grid(row=0, column=7, padx=5)

accuracy_label = Label(frame_output, text='Accuracy', font=('Tahoma', 12, 'bold'), fg='red')
accuracy_label.grid(row=0, column=8, padx=5)

accuracy_percent_label = Label(frame_output, text='0', font=('Tahoma', 12, 'bold'))
accuracy_percent_label.grid(row=0, column=9, padx=5)

buttons_frame = Frame(mainframe)
buttons_frame.grid(row=4, column=0)

start_button = ttk.Button(buttons_frame, text='Start', command=start)
start_button.grid(row=0, column=0, padx=10, pady=10)

reset_button = ttk.Button(buttons_frame, text='Reset', state=DISABLED,command=reset)
reset_button.grid(row=0, column=1, padx=10, pady=10)

exit_button = ttk.Button(buttons_frame, text='Exit', command=root.destroy)
exit_button.grid(row=0, column=2, padx=10, pady=10)

root.mainloop()

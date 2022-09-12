from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
clocktime = None

# ---------------------------- TIMER RESET ------------------------------- #
def reseter():
    global reps, clocktime
    reps = 0
    window.after_cancel(clocktime)
    timer.place(x=40, y=-50)
    timer.config(text="Work", foreground=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps == 8:
        timer.place(x=-30, y=-50)
        timer.config(text="Long Break", foreground=RED)
        countdown(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        timer.place(x=-50, y=-50)
        timer.config(text="Short Break", foreground=PINK)
        countdown(SHORT_BREAK_MIN * 60)
    elif reps % 2 == 1:
        timer.place(x=40, y=-50)
        timer.config(text="Work", foreground=GREEN)
        countdown(10)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    if count_min < 10:
        count_min = "0" + str(count_min)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global clocktime
        clocktime = window.after(1000, countdown, count - 1)
    else:
        checker = ""
        for n in range(math.floor(reps / 2)):
            checker = checker + "✔"
        check.config(text=checker)
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=220, height=250, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(110, 125, image=tomato_img)
timer_text = canvas.create_text(110, 145, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()


# Reset button
reset = Button(text="Reset", font=(FONT_NAME, 10, "bold"), command=reseter)
reset.place(x=245, y=240)


# Start button
start = Button(text="Start", font=(FONT_NAME, 10, "bold"), command=start_timer)
start.place(x=-80, y=240)


# Timer
timer = Label(text="Timer", font=(FONT_NAME, 35, "bold"), foreground=GREEN, background=YELLOW)
timer.place(x=40, y=-50)

# Check
check = Label(font=(FONT_NAME, 15), foreground=GREEN, background=YELLOW)
check.place(x=95, y=260)
window.mainloop()

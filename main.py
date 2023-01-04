import math
import time
from tkinter import *
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
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global btn_start
    global reps
    reps += 1

    btn_start["state"] = "disabled"
    time_to_work = 1 * 60
    short_break = 0.3 * 60
    long_break = 0.4 * 60

    if reps % 2 == 0:
        if reps == 8:
            count_down(long_break)
        else:
            count_down(short_break)
    else:
        count_down(time_to_work)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global btn_start
    count_minute = math.floor(count / 60)
    count_seconds = math.floor(count % 60)

    if int(count_seconds) <= 9:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        btn_start["state"] = "normal"


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo_image)
timer_text = canvas.create_text(100, 112, text="0:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

lbl_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
lbl_timer.grid(column=1, row=0)

lbl_check = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
lbl_check.grid(column=1, row=3)

btn_start = Button(text="Start", command=start_timer)
btn_start.grid(column=0, row=2)

btn_reset = Button(text="Reset")
btn_reset.grid(column=2, row=2)

window.mainloop()

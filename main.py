import math
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
reps = -1
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    reps = -1
    window.after_cancel(timer)
    lbl_timer.config(text="Timer")
    canvas.itemconfig(timer_text, text="0:00")
    btn_start["state"] = "normal"

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    btn_start["state"] = "disabled"
    time_to_work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        if reps == 7:
            count_down(long_break)
            lbl_timer.config(text="Long break", fg=RED)
        else:
            count_down(short_break)
            lbl_timer.config(text="Short break", fg=PINK)
    else:
        count_down(time_to_work)
        lbl_timer.config(text="Working", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps
    count_minute = math.floor(count / 60)
    count_seconds = math.floor(count % 60)
    check_marks = ""

    if int(count_seconds) <= 9:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        working_sessions = math.floor(reps / 2)
        for _ in range(working_sessions):
            check_marks += "✔"
        lbl_check.config(text=check_marks)

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

lbl_check = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
lbl_check.grid(column=1, row=3)

btn_start = Button(text="Start", command=start_timer)
btn_start.grid(column=0, row=2)

btn_reset = Button(text="Reset", command=reset_timer)
btn_reset.grid(column=2, row=2)

window.mainloop()

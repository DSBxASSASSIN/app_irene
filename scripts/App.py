import tkinter as tk
HEIGHT = 800
WIDTH = 1200

def button_test(entry):
    if entry == "":
        label["text"] = "you have typed nothing" 
    else:
        label["text"] = "this is what you typed: " + entry



root = tk.Tk()
root.title("test app v1.0")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='../images/main.gif')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#7C0D13", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame, font=40, bg="grey", fg="#7C0D13")
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="test button", font=40, bg="grey", fg="#7C0D13", command=lambda: button_test(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg="#7C0D13", bd=10, )
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = tk.Label(lower_frame, font=100, text='type something to continue', bg="grey", fg="#7C0D13")
label.place(relwidth=1, relheight=1)

root.mainloop()
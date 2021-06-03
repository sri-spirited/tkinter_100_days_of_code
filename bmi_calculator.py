import tkinter

# Create the window
window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=200)

welcome_label = tkinter.Label()
# Label
my_label = tkinter.Label(font=("Arial", 15))
my_label.config(text="Please input your weight & height below:")
# my_label.pack()  # Pack the label onto the screen
my_label.grid(column=1, row=1)

# Weight text
weight_label = tkinter.Label(font=("Arial", 14))
weight_label.config(text="Weight")
weight_label.grid(row=2, column=0)

# Weight entry
weight_input = tkinter.Entry(width=10)
weight_input.grid(row=2, column=1)

# Weight metric text
weight_label = tkinter.Label(font=("Arial", 14))
weight_label.config(text="KG")
weight_label.grid(row=2, column=2)

# Height text
height_label = tkinter.Label(font=("Arial", 14))
height_label.config(text="Height")
height_label.grid(row=3, column=0)

# Height entry
height_input = tkinter.Entry(width=10)
height_input.grid(row=3, column=1)

# Height metric text
height_label = tkinter.Label(font=("Arial", 14))
height_label.config(text="M")
height_label.grid(row=3, column=2)


def button_clicked():
    try:
        my_label.config(
            text=f"Your BMI is {round(int(weight_input.get()) / float(height_input.get()) ** 2, 2)}"
        )
    except:
        my_label.config(text="Please enter some numeric values!")


button = tkinter.Button(text="Calculate", font=(14), command=button_clicked)
button.grid(column=1, row=4)

# # Entry
# inp = tkinter.Entry(width=10)
# get_text = inp.get()
# # my_label.config(text=get_text)
# # entry.pack()
# inp.grid(column=2, row=2)

# Getting the window to run
window.mainloop()

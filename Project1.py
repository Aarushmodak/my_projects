import tkinter as tk

window = tk.Tk()
window.title("My Project1")
window.geometry("1000x600")

label1 = tk.Label(text='Hello World!')
label1.config(font = ("Times New Roman", "30"))
label1.pack()

btn1 = tk.Button(text="Exit", font=('Times new roman', '20', 'bold'), bg='Yellow', command=window.destroy)
btn1.pack()


window.mainloop()
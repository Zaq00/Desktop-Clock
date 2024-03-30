import tkinter as tk
import time

    
def changeTime():
    curTime = time.strftime('%H:%M:%S')
    label.config(text=curTime)
    label.after(1000, changeTime)

def closeWindow():
    window.destroy()
    
def moveWindow(event):
    x, y = event.x_root, event.y_root
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    if 0 < x < screen_width and 0 < y < screen_height:
        window.geometry('+{0}+{1}'.format(x, y))

window = tk.Tk()
window.title('Digital Clock')
window.geometry('500x200')
window.configure(bg = 'black')
window.overrideredirect(True)


bar = tk.Frame(window, bg= 'black', relief= 'raised', bd= 2, borderwidth=0, highlightthickness=0)
bar.pack(fill='x')
    
closeButton = tk.Button(bar, text="X", bg="black", fg="white", font=('Poppins', 16, 'bold'), command=closeWindow, borderwidth=0, highlightthickness=0)
closeButton.pack(side="right", padx=1)


label = tk.Label(window, text='', font=("Poppins", 84), foreground='white',  background='black')
label.pack(padx=20, pady=20)

changeTime()

bar.bind('<B1-Motion>', moveWindow)

window.mainloop()
 # this is the data Visualize app which is use data in csv or excel file. it can be show data in x and y axis
# basic requirement for this app
# 1 pip install pands
# 2 pip install tkinter
# 3 pip install matplotlib
# run these above commands in terminal to get all requirement


# Intialize Tkintere app
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def load_file(file_path):
    if file_path.endswith(".csv"):    
        return pd.read_csv(file_path)
    elif file_path.endswith(".xlsx"):
        return pd.read_excel(file_path)
    else:
        raise ValueError("unexpacted file format")
    

def plot_data(df, column_x, column_y):
    fig = Figure(figsize=(6,4),dpi=100)
    ax= fig.add_subplot(111)
    ax.plot(df[column_x],df[column_y], marker= "0")
    ax.set_title(f"{column_x,} vs {column_y}")
    ax.set_xlabel(column_x)
    ax.set_ylabel(column_y)


    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=20)


def update_dropdowns(columns):
    x_dropdown.set("")
    y_dropdown.set("")
    x_manu["manu"].delete(0,"end")
    y_manu["manu"].delete(0,"end")
    for column in  columns:
        x_manu["manu"].add_commands(lable=column, command= lambda value= column: x_dropdown.set(value))
        y_manu["manu"].add_commands(lable=column, command= lambda value= column: y_dropdown.set(value))


def  open_file():
    file_path = filedialog.askopenfilename(filetypes=[("csv files", "*.csv")])
    print(f"file selected: {file_path}")
    return file_path

def handle_file():
    global df
    file_path = open_file()
    try:
        df = load_file(file_path)
        update_dropdowns(df.columns)
        print(f"column available {df.columns}")
    except Exception as e:
        print(f"Eroor {e}")

def handle_plot():
    try:
        column_x = x_dropdown.get()
        column_y = y_dropdown.get()
        if not column_x or not column_y:
            print("please select boath")
            return
        plot_data(df, column_x, column_y)
    except Exception as e:
        print(f"error {e}")

#initialize my tikinker app
root = tk.Tk()
root.title("Data Visualizer")
root.geometry("800x600")

upload_button = tk.Button(root, text="upload file", command= open_file)
upload_button.pack(pady=10)

# dropdown for selecting
x_label = tk.Label(root, text="select x axis")
x_label.pack(pady=5)
x_dropdown= tk.stringVar()
x_manu = tk.OptionMenu(root, x_dropdown,[])
x_manu.pack(pady=5)

y_label = tk.Label(root, text="select y axis")
y_label.pack(pady=5)
y_dropdown= tk.stringVar()
y_manu = tk.OptionMenu(root, y_dropdown,[])
y_manu.pack(pady=5)

plot_buttom= tk.Button(root, text = "ganerate a plot", command=handle_plot)
plot_buttom.pack(pady=10)
root.mainloop()

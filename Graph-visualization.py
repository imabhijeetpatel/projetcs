# this is the simple Graph represtentaion of  data into a diffrent Graph format

# Requirment 
# pip install matplotlib

import matplotlib.pyplot as plt
import pands as pd

# This is the main program of the code which is user rated graph
def plot_graph():
    print("Welcome to the Graph Visualization")
    print("Choose a graph type")
    print("1 Line Chart")
    print("2 Bar chart")
    print("3 Scatter Chart")

    choice = input("Enter the number of the choice")
    if choice not in ["1", "2", "3"]:
        print("Invalid number")
        return

    print("Choice data input method:")
    print("1 enter data manually")
    print("2 Load the dat form the csv file")

    data_choice = input("Enter the number of ytour choice:")

    if data_choice =="1":
        x= list(map(float, input("Enter the x values separate by space").split()))
        y= list(map(float, input("Enter the y values separate by space").split()))
    elif data_choice == "2":
        file_path = input("Enter the path of the csv file")
        try:
            data = pd.read_csv(file_path)
            x =data.iloc[:, 0]
            y =data.iloc[:, 1]
        except Exception as e:
            print("Error is loading to csv file", e)
            return
    else:
        print("Invalid choice")
        return
    
    if choice == "1":
        plt.plot(x, y, label= "Line graph", maker ="0")
    elif choice == "2":
        plt.bar(x, y, color= "skyblue")
    elif choice == "3":
        plt.scatter(x,y , color= "red")

        plt.title("Graph Plotter")
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.legend()
        plt.grid(True)

        save_choice = input("Do you want to save the Graph").lower()
        if save_choice == "yes":
            file_name = ("Enter the name of  the file > file_name.png")
            plt.savefig(file_name)
            print(f"graph saved as {file_name}")

if __name__ == "__main__":
        plot_graph()

################################ THIS IS THE  SEPARATE PART ###################################

#data is for plot for line Chart

x= [1,2,3,4,5]
y=[2,4,6,8,10]
# plot is line chart
plt.plot(x,y, label="line")
plt.title("Line graph")
plt.xlabel("X- axis")
plt.ylabel("Y- axis")
plt.legend()
plt.show()

#Data is for bar chart
categories= ["A","B","C","D"]
values= [10,20,30,40]
#plot is for Bar chart
plt.bar(categories, values, color="skyblue")
plt.title("Bar chart")
plt.xlabel("categories")
plt.ylabel("values")
plt.show()

# data is scatter plot
x= [1,2,3,4,5,6]
y= [1.0,2.5,3.0,4.2,5.0]
#Plot is for scatter plot
plt.scatter(x,y, color="red")
plt.title("Scatter plot")
plt.xlabel("X-axis")
plt.ylabel("Y- axis")
plt.show

x= [1,2,3,4,5]
y=[2,4,6,8,10]
#plot
plt.plot(x, y, label="Line", color="Green", linestyle="--", marker="0")
plt.title("Customized line Graph")
plt.xlabel("X- axis")
plt.ylabel("Y- axis")
plt.grid(True)
plt.annotate("Max value", xy=y(5, 10), xytext=(4, 8),
             arrowprops=dict(facecolor="black", arrowstyle="->"))
plt.legend()
plt.show()

# this is use for three data graph
x= [1,2,3,4,5]
y1=[2,4,6,8,10]
y2=[1,2,3,4,5]
plt.subplot(1,2,1)
plt.plot(x, y1,color="blue")
plt.title("Graph 1")

plt.subplot(1,2,2)
plt.plot(x,y2, color="green")
plt.title("Graph 2")

plt.tight_layout()
plt.show()


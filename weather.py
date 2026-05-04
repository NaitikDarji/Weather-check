from tkinter import*
import requests
from tkinter import  ttk



def get_weather():
    city= city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q=" +city+ "&appid=0c99894a9b1d9e4e279974fabbe2c675").json()
    print(data)
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    t_label1.config(text=str(int(data["main"]["temp"]-273.15))+"°C")
    p_label1.config(text=str(data["main"]["humidity"])+"%")









win = Tk()
win.title("Weather App")
win.config(bg="lightblue")
win.geometry("700x700")

name_label= Label(win, text="Weather Checker", font=("Arial", 24, "bold") , bg="lightblue")
name_label.place(x=200, y=50, height=50, width=300 )


city_name= StringVar()
name_state= Label(win, text="Select State:", font=("Arial", 14) , bg="lightblue")
name_state.place(x=50, y=150, height=30, width=120)
list_states =[
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", 
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", 
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", 
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", 
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", 
    "Uttar Pradesh", "Uttarakhand", "West Bengal"
]
city_entry= ttk.Combobox(win, font=("Arial", 14),values=list_states,text_variable=city_name)
city_entry.place(x=200, y=150, height=30, width=300)

btn= Button(win, text="Check Weather", font=("Arial", 14), bg="blue", fg="white", command=get_weather)
btn.place(x=250, y=250, height=40, width=200)

w_label= Label(win, text="Weather Climate:", font=("Arial", 14) , bg="lightblue")
w_label.place(x=70, y=350, height=30, width=150)
w_label1= Label(win, text="", font=("Arial", 14) , bg="lightblue")
w_label1.place(x=300, y=350, height=30, width=150)

wb_label= Label(win, text="Weather Description:", font=("Arial", 14) , bg="lightblue")
wb_label.place(x=50, y=400, height=30, width=200)
wb_label1= Label(win, text="", font=("Arial", 14) , bg="lightblue")
wb_label1.place(x=300, y=400, height=30, width=150)

t_label= Label(win, text="Temperature:", font=("Arial", 14) , bg="lightblue")
t_label.place(x=50, y=450, height=30, width=150)
t_label1= Label(win, text="", font=("Arial", 14) , bg="lightblue")
t_label1.place(x=200, y=450, height=30, width=150)

p_label= Label(win, text="Humidity:", font=("Arial", 14) , bg="lightblue")
p_label.place(x=50, y=500, height=30, width=150)
p_label1= Label(win, text="", font=("Arial", 14) , bg="lightblue")
p_label1.place(x=200, y=500, height=30, width=150)












win.mainloop()
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import platform
import psutil
import socket
import os
import get_data

# Function to open system settings
def open_system_settings(setting):
    os.startfile(setting)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("570x700")
window.configure(bg = "#bdc3c7")


canvas = Canvas(
    window,
    bg = "#bdc3c7",
    height = 700,
    width = 570,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    30.0,
    50.0,
    545.0,
    180.0,
    fill="#7f8c8d",
    outline=""
    )

canvas.create_text(
    149.73545837402344,
    78.79977416992188,
    anchor="nw",
    text="Computer Name",
    fill="#000000",
    font=("Poppins Regular", 14 * -1)
)

canvas.create_text(
    147.0,
    110.0,
    anchor="nw",
    text= socket.gethostname() +"\n" + platform.version(),
    fill="#333333",
    font=("Poppins SemiBold", 14 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("windows.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_system_settings("ms-settings:about"),
    relief="flat"
)
button_1.place(
    x=50.2232666015625,
    y=78.79977416992188,
    width=80.0,
    height=80.0
)

canvas.create_text(
    438.70355220609375,
    77.92706298828125,
    anchor="nw",
    text="Last Reboot",
    fill="#000000",
    font=("Poppins Regular", 14 * -1)
)

canvas.create_text(
    439.0,
    121.0,
    anchor="nw",
    text= get_data.get_uptime(),
    fill="#333333",
    font=("Poppins SemiBold", 14 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("reboot.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_system_settings("ms-settings:windowsupdate"),
    relief="flat"
)
button_2.place(
    x=339.19134521484375,
    y=77.92706298828125,
    width=80.0,
    height=80.0
)

canvas.create_rectangle(
    284.60787604807905,
    76.0543212890625,
    285.6078796386719,
    152.9810028076172,
    fill="#F0F0F0",
    outline="")

canvas.create_rectangle(
    30.0,
    190.0,
    545.0,
    320.0,
    fill="#7f8c8d",
    outline="")

canvas.create_text(
    147.73545837402344,
    218.7998046875,
    anchor="nw",
    text="Ask Sammy",
    fill="#000000",
    font=("Poppins Regular", 14 * -1)
)

canvas.create_text(
    145.0,
    260.0,
    anchor="nw",
    text="Available to Help!",
    fill="#333333",
    font=("Poppins SemiBold", 14 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("chat.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_3.place(
    x=48.2232666015625,
    y=218.79978942871094,
    width=80.0,
    height=80.0
)

canvas.create_text(
    436.70355220609375,
    217.9270782070703,
    anchor="nw",
    text="Storage Used",
    fill="#000000",
    font=("Poppins Regular", 14 * -1)
)

canvas.create_text(
    437.0,
    260.0,
    anchor="nw",
    text=str(psutil.disk_usage('/').percent) + "%",
    fill="#333333",
    font=("Poppins SemiBold", 14 * -1)
)

button_image_4 = PhotoImage(
    file=relative_to_assets("database.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_system_settings("ms-settings:storagesense"),
    relief="flat"
)
button_4.place(
    x=337.19134521484375,
    y=217.9270782070703,
    width=80.0,
    height=80.0
)

canvas.create_rectangle(
    282.60787604807905,
    216.05433654785156,
    283.6078796386719,
    292.98101806640625,
    fill="#F0F0F0",
    outline="")

canvas.create_rectangle(
    30.0,
    330.0,
    545.0,
    461.7807922363281,
    fill="#7f8c8d",
    outline="")

canvas.create_text(
    145.73545837402344,
    358.7998046875,
    anchor="nw",
    text="Network Info",
    fill="#000000",
    font=("Poppins Regular", 14 * -1)
)

canvas.create_text(
    143.0,
    400.0,
    anchor="nw",
    text=get_data.get_network_info(),
    fill="#333333",
    font=("Poppins SemiBold", 14 * -1)
)

button_image_5 = PhotoImage(
    file=relative_to_assets("wifi.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_system_settings("ms-settings:network"),
    relief="flat"
)
button_5.place(
    x=46.2232666015625,
    y=358.7997741699219,
    width=80.0,
    height=80.0
)

canvas.create_text(
    434.70355220609375,
    357.92706298828125,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("Poppins Regular", 14 * -1)
)

canvas.create_text(
    435.0,
    400.0,
    anchor="nw",
    text="189",
    fill="#333333",
    font=("Poppins SemiBold", 14 * -1)
)

button_image_6 = PhotoImage(
    file=relative_to_assets("key.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=335.19134521484375,
    y=357.92706298828125,
    width=80.0,
    height=80.0
)

canvas.create_rectangle(
    280.60787604807905,
    356.0543212890625,
    281.6078796386719,
    432.9810028076172,
    fill="#F0F0F0",
    outline="")

canvas.create_rectangle(
    30.0,
    470.0,
    545.0,
    570.0,
    fill="#7f8c8d",
    outline="")

canvas.create_text(
    103.53213500976562,
    491.9176025390625,
    anchor="nw",
    text="Active \n Now",
    fill="#000000",
    font=("Poppins Regular", 14 * -1)
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=37.439178466796875,
    y=491.9176025390625,
    width=55.0,
    height=55.0
)

canvas.create_text(
    295.4559020996094,
    491.25341796875,
    anchor="nw",
    text="Active \n Now",
    fill="#000000",
    font=("Poppins Regular", 14 * -1)
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=229.36294555664062,
    y=491.25341796875,
    width=55.0,
    height=55.0
)

canvas.create_text(
    448.99725341796875,
    492.0,
    anchor="nw",
    text="Active \n Now",
    fill="#000000",
    font=("Poppins Regular", 14 * -1)
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=382.904296875,
    y=492.0,
    width=55.0,
    height=55.0
)

canvas.create_rectangle(
    192.77444216330608,
    489.5892639160156,
    193.77444458007812,
    548.3720016479492,
    fill="#F0F0F0",
outline="")

canvas.create_rectangle(
    359.8968176515873,
    486.0,
    360.8968200683594,
    544.7827377319336,
    fill="#F0F0F0",
outline="")

canvas.create_rectangle(
    30.0,
    578.0,
    545.0,
    678.0,
    fill="#7f8c8d",
outline="")

canvas.create_text(
    106.5321273803711,
    599.9176025390625,
    anchor="nw",
    text="Active \n Now",
    fill="#000000",
    font=("Poppins Regular", 14 * -1)
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=40.43916320800781,
    y=599.9176025390625,
    width=55.0,
    height=55.0
)

canvas.create_text(
    298.4559020996094,
    599.25341796875,
    anchor="nw",
    text="Active \n Now",
    fill="#000000",
    font=("Poppins Regular", 14 * -1)
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=232.36294555664062,
    y=599.25341796875,
    width=55.0,
    height=55.0
)

canvas.create_text(
    451.99725341796875,
    600.0,
    anchor="nw",
    text="Active \n Now",
    fill="#000000",
    font=("Poppins Regular", 14 * -1)
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_12 clicked"),
    relief="flat"
)
button_12.place(
    x=385.9043273925781,
    y=600.0,
    width=55.0,
    height=55.0
)

canvas.create_rectangle(
    195.77442690451701,
    597.5892944335938,
    196.77442932128906,
    656.3720321655273,
    fill="#F0F0F0",
outline="")

canvas.create_rectangle(
    362.8968176515873,
    594.0,
    363.8968200683594,
    652.7827377319336,
    fill="#F0F0F0",
outline="")

canvas.create_text(
    53.0,
    14.0,
    anchor="nw",
    text="Sammy V3 For Windows",
    fill="#000000",
    font=("Poppins Regular", 20 * -1)
)

window.resizable(False, False)
window.mainloop()
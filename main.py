# 世界时钟
# 2023年3月

# pyinstaller -F -w main.py

import os
import json
import datetime
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()

# 更新系统时间
system_time_str = ""  # 系统时间

def update_system_time():
    global system_time_str
    system_time = datetime.datetime.now()
    system_time_str = system_time.strftime("%Y-%m-%d %H:%M:%S")
    root.title(system_time_str)
    time_label.after(1000, update_system_time)

# 获取城市时间
last_city = None
frame = tk.Frame(root)
frame.pack()

def get_local_time(city):
    global last_city
    timezone = city["timezone"]
    timezone_hour = int(timezone[4:].replace(":", ""))
    if timezone[3] == "-":
        timezone_hour = -timezone_hour
    local_time = datetime.datetime.utcnow() + datetime.timedelta(hours=timezone_hour)
    local_time_str = local_time.strftime("%Y-%m-%d %H:%M:%S")
    result_label = tk.Label(
        frame, text=f"{timezone}\n{city['name']}", font=("Arial", 12), width=10)  # 时区，城市
    result_label2 = tk.Label(
        frame, text=f"{local_time_str[-8:]}", font=("Arial", 30))  # 时间
    result_label.grid(row=0, column=0, padx=10, pady=10)
    result_label2.grid(row=0, column=1, padx=10, pady=10)
    if last_city:
        result_label.after_cancel(last_city)
    last_city = result_label.after(1000, lambda: get_local_time(city))

# 记录搜索历史
def record_search_history(system_time_str, user_input):
    with open('search_history.txt', 'a+', encoding='utf-8') as f:
        f.write(system_time_str + " 搜索： " + user_input['name'] + "\n")

# 显示搜索历史
def show_search_history():
    search_history_frame = tk.Frame(root)
    search_history_frame.place(
        in_=root, anchor="c", relx=0.5, y=350, width=350, height=300)
    search_history_scrollbar = tk.Scrollbar(search_history_frame)
    search_history_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    search_history_listbox = tk.Listbox(search_history_frame, font=(
        "Arial", 12), yscrollcommand=search_history_scrollbar.set)
    with open('search_history.txt', 'r', encoding='utf-8') as f:
        search_history = f.readlines()
    search_history.reverse()  # 将结果倒序显示
    for history in search_history:
        search_history_listbox.insert(tk.END, history.strip("\n"))
    search_history_listbox.pack(fill=tk.BOTH, expand=True)

# 清空搜索历史
def clear_search_history():
    with open('search_history.txt', 'w', encoding='utf-8') as f:
        f.truncate(0)
    show_search_history()  # 显示搜索历史

# 查找城市
def search_city():
    user_input = input_entry.get().lower()
    matched_cities = []
    for city in cities:
        if user_input in city["name"].lower() or user_input in city["country"].lower():
            matched_cities.append(city)
    if len(matched_cities) == 0:
        messagebox.showinfo("温馨提示", "抱歉，未找到相关信息。")
    elif len(matched_cities) == 1:
        get_local_time(matched_cities[0])
        record_search_history(system_time_str, matched_cities[0])  # 记录搜索历史
        show_search_history()  # 显示搜索历史
    else:
        # 创建一个显示匹配城市的新窗口
        window = tk.Toplevel(root)
        window.title("查找城市")
        window.geometry("300x200")
        city_listbox = tk.Listbox(window, font=("Arial", 12))
        for city in matched_cities:
            city_listbox.insert(tk.END, f"{city['name']}-{city['country']}")
        city_listbox.pack(fill=tk.BOTH, expand=True)
        # 获取所选城市并关闭窗口
        def on_select(event):
            index = city_listbox.curselection()[0]
            selected_city = matched_cities[index]
            city_listbox.itemconfig(index, bg="blue", fg="white")
            root.after(300, lambda: window.destroy())
            input_entry.delete(0, tk.END)
            input_entry.insert(
                0, f"{selected_city['name']}")
            get_local_time(selected_city)
            record_search_history(system_time_str, selected_city)  # 记录搜索历史
            show_search_history()  # 显示搜索历史
            input_entry.config(fg="black")  # 将文本框中的文字改成黑色
        city_listbox.bind("<<ListboxSelect>>", on_select)

# GUI窗体
root.geometry("350x180")
# 显示当前时间
time_label = tk.Label(root, font=("Arial", 12))
time_label.pack()
update_system_time()  # 更新系统时间
get_local_time({
    "name": "北京",
    "country": "中国",
    "timezone": "UTC+8"
})  # 初始化，获取北京时间
input_entry = tk.Entry(root, font=("Arial", 12))  # 输入框
input_entry.pack(side=tk.TOP, padx=0, pady=0)
input_entry.insert(0, "请输入城市或国家名称")  # 提示文字
input_entry.config(fg="grey")
# 清空提示文字
def on_entry_click(event):
    if input_entry.get() == "请输入城市或国家名称":
        input_entry.delete(0, tk.END)
        input_entry.config(fg="black")
input_entry.bind('<FocusIn>', on_entry_click)
search_button = tk.Button(root, text="查询", font=(
    "Arial", 12), command=search_city)  # 查询按钮
search_button.pack(side=tk.TOP, padx=0, pady=0)

# 窗体模式
def mini_mode():
    global state
    if state == 1:
        root.geometry("350x80")
        state = 2
        menubar.entryconfigure(0, label="迷你模式")
    elif state == 2:
        root.geometry("350x500")
        state = 3
        menubar.entryconfigure(0, label="搜索历史")
    else:
        root.geometry("350x180")
        state = 1
        menubar.entryconfigure(0, label="窗体模式")

# 置顶
def toggle_topmost():
    global is_topmost
    is_topmost = not is_topmost
    root.attributes("-topmost", is_topmost)
    menu_label = "置顶[开]" if is_topmost else "置顶[关]"
    menubar.entryconfigure(2, label=menu_label)

# 创建菜单标题
menubar = tk.Menu(root)
state = 1
is_topmost = False
menubar = tk.Menu(root, tearoff=False)
menubar.add_command(label="窗体模式", command=mini_mode)
menubar.add_command(label="清空历史", command=clear_search_history)
menubar.add_command(label="置顶[关]", command=toggle_topmost)
root.config(menu=menubar)  # 将菜单栏添加到主窗口

# 生成城市数据模板
def generate_city_json():
    # 判断当前工作目录下是否已存在 city.json 文件
    if os.path.exists('city.json'):
        messagebox.showinfo("温馨提示", "文件已存在，请重启程序！")
        return
    # 定义城市列表
    cities = [
        {
            "name": "北京",
            "country": "中国",
            "timezone": "UTC+8"
        },
        {
            "name": "上海",
            "country": "中国",
            "timezone": "UTC+8"
        },
        {
            "name": "莫斯科",
            "country": "俄罗斯",
            "timezone": "UTC+3"
        },
        {
            "name": "伦敦",
            "country": "英国",
            "timezone": "UTC+0"
        },
        {
            "name": "纽约",
            "country": "美国",
            "timezone": "UTC-4"
        }
    ]
    # 将城市列表写入 city.json 文件
    with open('city.json', 'w', encoding='utf-8') as f:
        json.dump(cities, f, ensure_ascii=False, indent=4)
    messagebox.showinfo("温馨提示", "生成成功，请重启程序！")

if os.path.exists('city.json'):
    with open('city.json', 'r', encoding='utf-8') as f:
        cities = json.load(f)
else:
    messagebox.showinfo("错误", "无法读取city.json文件！")
    search_button.config(state="disabled")  # 禁用查询按钮函数
    menubar.add_command(label="生成城市模板", command=generate_city_json)
    root.config(menu=menubar)  # 将菜单栏添加到主窗口

# 销毁窗体
def on_closing():
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()

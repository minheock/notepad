from tkinter import *
from tkinter import colorchooser
import tkinter.font
from tkinter.filedialog import *
from help import helped

# 기본뼈대
window = Tk()
window.title("메모장")
window.geometry("500x500")
window.resizable(False, False)

#폰트
font=tkinter.font.Font(family="맑은 고딕", size=20, slant="italic")
# 동작추가
def new_file() :
    text_area.delete(1.0, END)

def new_font() :
    Text(font=font)

def new_color() :
    color= colorchooser.askcolor()
def save_file() :
    f = asksaveasfile(mode="W", defaultextension=".txt", filetypes=[('Text files', '.txt')])
    text_save = str(text_area.get(1.0, END))
    f.write(text_save)
    f.close()
def maker() :
    help_view = Toplevel(window)
    help_view.geometry("300x50")
    help_view.title("Maker")
    lb = Label(help_view, text='minheock이 만든 메모장입니다.')
    lb.pack()




# 메뉴
menu = Menu(window)
menu_1 = Menu(menu, tearoff=0)
menu_1.add_command(label='새파일', command=new_file)
menu_1.add_separator()
menu_1.add_command(label='저장하기', command=save_file)
menu_1.add_separator()
menu_1.add_command(label='종료', command=window.destroy)
menu.add_cascade(label='파일', menu=menu_1)

menu_2 = Menu(menu, tearoff=0)
menu_2.add_command(label='min', command=maker)
menu.add_cascade(label='만든이', menu=menu_2)

menu_3 = Menu(menu, tearoff=0)
menu_3.add_command(label='확대하기')
menu_3.add_command(label='축소하기')
menu_3.add_command(label='폰트 변경', command=new_font)
menu_3.add_command(label='컬러 변경', command=new_color)
menu.add_cascade(label='보기', menu=menu_3)

menu_4 = Menu(menu, tearoff=0)
menu_4.add_command(label='도움말 보기', command=helped)
menu_4.add_command(label='피드백 보내기')
menu.add_cascade(label='도움말', menu=menu_4)
# 텍스트
text_area = Text(window, bg='black', fg='ivory', font='italic')
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky= N + E + S + W)


window.config(menu=menu)
window.mainloop()

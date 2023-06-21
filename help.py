from tkinter import *
from tkinter.filedialog import *


def helped() :
    help_view2 = Toplevel()
    help_view2.geometry("300x300")
    help_view2.title("도움말")
    lb2 = Label(help_view2, text=
            '''머릿글 도움말 Windows 10/11에서 메모장을 사용하는 경우
            머리글과 바닥글을 제거하거나 변경할 수 있습니다. 
            메모장의 기본 머리글 및 바닥글 설정은 다음과 같습니다. 
            머리글: &f 바닥글: &p페이지 이러한 명령으로 페이지 상단의
            문서 제목과 하단의 페이지 번호를 지정할 수 있습니다. 
            이러한 설정은 저장되지 않으므로, 문서를 인쇄할 때마다
            이를 포함하려면 모든 머리글 및 바닥글 설정을
            수동으로 입력해야 합니다.'
            '''       
    )
    lb2.pack()
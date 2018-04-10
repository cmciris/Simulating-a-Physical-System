# coding=utf-8
# 引入库
from Tkinter import *
import string
import tkMessageBox
from ideagas import *
import gas
import thread
import time
import pyaudio
import wave
import winsound


class App:

    def __init__(self,master):

        # appear in the center of screen
        root.title('ideaGas')
        root.geometry('%dx%d+%d+%d' % (self.gen_coordinate(900, 600)))  # ensure the window appears at the center in the screen
        root.resizable(width=False, height=False)  # user can't fix the width and height
        root.attributes("-alpha", 0.9)

        # open the background image
        self.background = PhotoImage(file='bg.gif')  # background
        self.canvas = Canvas(root, width=900, height=600, background='black')
        self.canvas.create_image(450, 300, image=self.background, tag='bg_s')  # show background
        # the text on the UI
        self.create_text_wisha(450, 60, 'Welcome!', 'Arial 34 bold italic', 'lightyellow', 'center', 2, 'black', 'a', 'b')

        self.create_text_wisha(100, 125, 'Molecules', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'c', 'd')
        self.create_text_wisha(150, 150, 'Quantity:', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'e', 'f')
        self.create_text_wisha(270, 150, 'N = ', 'LucidaFamily 30 bold italic', 'lightyellow', 'left', 2, 'black', 'g', 'h')

        self.create_text_wisha(80, 220, 'System', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'i', 'j')
        self.create_text_wisha(125, 245, 'State:', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'k', 'l')

        self.create_text_wisha(105, 315, 'Simulation', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'm', 'n')
        self.create_text_wisha(120, 340, 'Step:', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'o', 'p')  # tag is to simplify
        #  deleting procedure


        # radio button
        self.v = IntVar()  # variable which is type int
        self.v.set(0)  # v == 0
        self.state1()  # before users choose, default state is  1
        self.statebutton1 = Radiobutton(self.canvas,
                                   variable=self.v,  # when variable == value, the button is chosen
                                   text='State 1  ',
                                   value=0,
                                   bg='lightyellow',
                                   fg='black',
                                   font='Centaur 13 italic',
                                   height=0,
                                   width=6,
                                   relief='ridge',
                                   bd=2,
                                   command=self.state1)
        self.statebutton2 = Radiobutton(self.canvas,  # similarly
                                   variable=self.v,
                                   text='State 2  ',
                                   value=1,
                                   bg='lightyellow',
                                   fg='black',
                                   font='Centaur 13 italic',
                                   height=0,
                                   width=6,
                                   relief='ridge',
                                   bd=2,
                                   command=self.state2)
        self.canvas.create_window((220, 245), window=self.statebutton1)  # show these two radiobutton
        self.canvas.create_window((301, 245), window=self.statebutton2)

        # users' entry
        self.var_entry = StringVar()  # variable which is type str
        self.entry = Entry(self.canvas,
                      textvariable=self.var_entry,
                      font='Centaur 16 italic',
                      bg='lightyellow',
                      fg='black',
                      relief='ridge',
                      bd='2',
                      width='9')
        self.var_entry.set('Input  here')  # the initial text
        self.canvas.create_window((320, 150), window=self.entry, anchor='w')  # show entry

        self.var_entry2 = StringVar()  # similar to the entry above
        self.entry2 = Entry(self.canvas,
                       textvariable=self.var_entry2,
                       font='Centaur 16 italic',
                       bg='lightyellow',
                       fg='black',
                       relief='ridge',
                       bd='2',
                       width='5')
        self.var_entry2.set('3000')
        self.canvas.create_window((170, 345), window=self.entry2, anchor='w')

        self.f = 0
        self.k = 0

        self.button_q = PhotoImage(file='quit.gif') # images for buttons
        self.button_d1 = PhotoImage(file='show_demon_t.gif')
        self.CS_d1 = PhotoImage(file='CS_d1.gif')
        self.CC_d1 = PhotoImage(file='CC_d1.gif')
        self.JA_d1 = PhotoImage(file='JA_d1.gif')
        self.KO_d1 = PhotoImage(file='KO_d1.gif')
        self.button_d2 = PhotoImage(file='show_demon.gif')
        self.CS_d2 = PhotoImage(file='CS_d2.gif')
        self.CC_d2 = PhotoImage(file='CC_d2.gif')
        self.JA_d2 = PhotoImage(file='JA_d2.gif')
        self.KO_d2 = PhotoImage(file='KO_d2.gif')
        self.button_31 = PhotoImage(file='show_3D.gif')
        self.CS_31 = PhotoImage(file='CS_31.gif')
        self.CC_31 = PhotoImage(file='CC_31.gif')
        self.JA_31 = PhotoImage(file='JA_31.gif')
        self.KO_31 = PhotoImage(file='KO_31.gif')
        self.resume_EN = PhotoImage(file='resume.gif')
        self.resume_CS = PhotoImage(file='resume_CS.gif')
        self.resume_CC = PhotoImage(file='resume_CC.gif')
        self.resume_JA = PhotoImage(file='resume_JA.gif')
        self.resume_KO = PhotoImage(file='resume_KO.gif')
        self.temp1 = self.button_d1
        self.temp2 = self.button_d2
        self.show_demon = Button(self.canvas,  # start button
                            image=self.button_d1,
                            font='Centaur 15  bold italic',
                            command=self.start_simulate,
                            fg='black',
                            bg='black',
                            activeforeground='purple',
                            activebackground='lightblue',
                            width=230,
                            height=150,
                            relief='ridge',
                            bd='0',
                            anchor='center',
                            state='normal')  # this button is enabled initially
        self.canvas.create_window((360, 295), window=self.show_demon, anchor='w')  # show the button

        self.show_3D = Button(self.canvas,  # close_fig button
                           image=self.button_31,
                           font='Centaur 15 italic',
                           command=self.start_3D,
                           fg='black',
                           bg='black',
                           activeforeground='purple',
                           activebackground='lightblue',
                           width=230,
                           height=70,
                           relief='ridge',
                           bd='0',
                           anchor='center',
                           state='normal')
        self.canvas.create_window((350, 400), window=self.show_3D, anchor='w')  # show the button on canvas

        self.resume = Button(self.canvas,
                        image = self.resume_EN,
                        font='Centaur 15 italic',
                        command=self.close_figure,
                        fg='green',
                        bg='lightyellow',
                        activeforeground='purple',
                        activebackground='lightblue',
                        width=125,
                        height=80,
                        relief='ridge',
                        bd='0',
                        anchor='center')
        self.canvas.create_window((510, 190), window=self.resume, anchor='w')  # show the button on canvas


        self.quit = Button(self.canvas,  # quit button
                      image=self.button_q,
                      text='QUIT',
                      font='Arial 13 bold',
                      command=self.quit_canvas,
                      fg='red',
                      bg='lightyellow',
                      activeforeground='purple',
                      activebackground='black',
                      width=40, height=40,
                      relief='flat',
                      bd='0',
                      anchor='center')
        self.canvas.create_window((850, 30), window=self.quit, anchor='w')  # show it

        # the body of menu
        self.menubar = Menu(root)  # menu in stage 1
        self.filemenu1 = Menu(self.menubar, tearoff=0)  # can not be tear off
        self.filemenu2 = Menu(self.menubar, tearoff=0)
        self.filemenu3 = Menu(self.menubar, tearoff=1)  # except this button group
        self.filemenu21 = Menu(self.filemenu2, tearoff=0)  # menu in stage 2
        self.filemenu22 = Menu(self.filemenu2, tearoff=0)
        self.menubar.add_cascade(label='View', menu=self.filemenu1)  # add cascade
        self.menubar.add_cascade(label='Options', menu=self.filemenu2)
        self.menubar.add_cascade(label='Run', menu=self.filemenu3)
        self.menubar.add_command(label='Help', command=self.help)
        self.menubar.add_command(label='About', command=self.about)
        self.filemenu1.add_cascade(label='Initialise UI', command=self.initial)
        self.filemenu1.add_separator()  # an separator here
        self.filemenu1.add_radiobutton(label='Show All Figures', variable=0, command=self.show_all)
        self.filemenu1.add_radiobutton(label='Molecule Velocity only', variable=0, command=self.separate_1)  # add checkbutton
        self.filemenu1.add_radiobutton(label='Demon Energy only', variable=0, command=self.separate_2)
        self.filemenu1.add_radiobutton(label='Demon Energy Time only', variable=0, command=self.separate_3)
        self.filemenu1.add_separator()  # an separator here
        self.filemenu1.add_radiobutton(label='Painting style 1', variable=1, command=self.style_g1)  # add checkbutton
        self.filemenu1.add_radiobutton(label='Painting style 2', variable=1, command=self.style_g2)
        self.filemenu1.add_radiobutton(label='Painting style 3', variable=1, command=self.style_g3)
        self.filemenu2.add_cascade(label='Language', menu=self.filemenu21)  # add cascade
        self.filemenu2.add_cascade(label='Transparency', menu=self.filemenu22)
        self.filemenu2.add_separator()  # an separator here
        self.filemenu2.add_command(label='Music ON', command=self.start_bgm)
        #self.filemenu2.add_command(label='Music OFF')
        self.filemenu21.add_radiobutton(label='English', variable=3, command=self.language_EN)  # add radiobutton
        self.filemenu21.add_radiobutton(label='中文简体', variable=3, command=self.language_CS)
        self.filemenu21.add_radiobutton(label='中文繁體', variable=3, command=self.language_CC)
        self.filemenu21.add_radiobutton(label='日本語', variable=3, command=self.language_JA)
        self.filemenu21.add_radiobutton(label='한국의', variable=3, command=self.language_KO)
        self.filemenu22.add_radiobutton(label='50%', variable=4, command=self.transparancy1)
        self.filemenu22.add_radiobutton(label='75%', variable=4, command=self.transparancy2)
        self.filemenu22.add_radiobutton(label='85%', variable=4, command=self.transparancy3)
        self.filemenu22.add_radiobutton(label='90%', variable=4, command=self.transparancy4)
        self.filemenu22.add_radiobutton(label='95%', variable=4, command=self.transparancy5)
        self.filemenu22.add_radiobutton(label='100%', variable=4, command=self.transparancy6)
        self.filemenu3.add_command(label='Start with demon', command=self.start_simulate)  # add command
        self.filemenu3.add_command(label='Start with 3D', command=self.start_3D)
        self.filemenu3.add_command(label='Refresh data', command=self.start_simulate)
        self.filemenu3.add_command(label='Resume', command=self.close_figure)
        self.filemenu3.add_separator()  # another separator here
        self.filemenu3.add_command(label='Exit', command=self.canvas.quit)  # add command
        root['menu'] = self.menubar  # show the menu on root

        self.canvas.pack()  # finish canvas building and show it

    # function for playing WinSound
    def playsound(self, s):
        winsound.PlaySound(s, winsound.SND_ASYNC)  #立即返回，支持异步播放

    # function for playing background music
    def bgm(self):
        #定义数据流块
        chunk = 1024

        #只读方式打开wav文件
        f = wave.open(r"bgm.wav","rb")

        p = pyaudio.PyAudio()

        #打开数据流
        stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                        channels = f.getnchannels(),
                        rate = f.getframerate(),
                        output = True)

        #读取数据
        data = f.readframes(chunk)

        #播放
        while data !="":
            stream.write(data)
            data = f.readframes(chunk)

        #停止数据流
        stream.stop_stream()
        stream.close()

        #关闭 PyAudio
        p.terminate()

    # fuction for calculating where root locates
    def gen_coordinate(self, w, h):
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        x = (sw / 2) - (w / 2)
        y = (sh / 2) - (h / 2) - 45
        return w, h, x, y

    # function to generate text with shadow
    def create_text_wisha(self, x, y, tex, fon, fil, jus, delta, bg, s1, s2):
        self.canvas.create_text(x, y,
                           text=tex,
                           font=fon,
                           fill=bg,
                           justify=jus,
                           tag=s1)
        self.canvas.create_text(x + delta, y - delta,
                           text=tex,
                           font=fon,
                           fill=fil,
                           justify=jus,
                           tag=s2)


    def state1(self):  # command designed for radiobutton 1
        self.state = 1


    def state2(self):  # command designed for radiobutton 1
        self.state = 0


    def show_all(self):
        self.f = 0


    def separate_1(self):
        self.f = 1


    def separate_2(self):
        self.f = 2


    def separate_3(self):
        self.f = 3


    def style_g1(self):
        self.k = 0


    def style_g2(self):
        self.k = 1


    def style_g3(self):
        self.k = 2

    # function for leading users to input legally
    def input_check(self):
        # only mark == True the program can continue
        self.mark = False
        e = self.var_entry.get()  # user input in entry1
        e2 = self.var_entry2.get()  # user input in entry2
        if e in ['Input  here', '在此输入', '在此輸入', '    입력' , '入力ここ']:  # user didn't do any thing
            self.playsound('SystemExclamation')
            tkMessageBox.showwarning('You should input N', 'Please input an "N" first,\nthen try again!')  # warn
        else:
            judge = list(e)  # judge that the input is an int
            judge2 = list(e2)
            for i in range(len(judge)):
                if judge[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and judge[i] in string.digits:
                    self.mark = True
                else:
                    self.playsound('SystemAsterisk')
                    tkMessageBox.showwarning('Your input is not so well', 'Please input an integer (like "550")!')
                    self.mark = False
                    break
            if self.mark:  # if e is ok, then check e2
                for i in range(len(judge2)):
                    if judge2[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and judge2[i] in string.digits:
                        self.mark = True
                    else:
                        self.playsound('SystemAsterisk')
                        tkMessageBox.showwarning('Your input is not so well',
                                                       'Please input an integer (like "3000")!')
                        self.mark = False
                        break


    def start_simulate(self):
        self.input_check()
        if self.mark:  # e and e2 are both int
            e2_check = int(self.var_entry2.get())  # check whether e2 is too large or too small
            if e2_check >= 5000:  # e2 is too large
                self.playsound('SystemQuestion')
                if tkMessageBox.askokcancel('Are you sure?',
                                                  'Step is so large that you will wait for a long time!\n\t      Clear to continue?'):
                    pass
                else:
                    self.mark = False
            if e2_check < 1000:  # e2 is too small
                self.playsound('SystemQuestion')
                if tkMessageBox.askokcancel('Are you sure?',
                                                  'Step is so small that your result may be not acute!\n\t      Clear to continue?'):
                    pass
                else:
                    self.mark = False
        if self.mark:  # the program is ready for launch
            self.show_demon.config(state='disable',
                              image=self.temp2)  # if click ban the button at once
            self.show_3D.config(state='disable')
            e = int(self.var_entry.get())
            e2 = int(self.var_entry2.get())
            g = Gas(e, 500, e2, self.state)
            if self.f == 0:
                g.showAll(self.k)
                print(self.f)  # We want to ensure here, this row can be deleted
            elif self.f == 1:
                g.show1()
                print(self.f)
            elif self.f == 2:
                g.show2()
                print(self.f)
            elif self.f == 3:
                g.show3(self.k)
                print(self.f)
            print(self.state)

    # the function realize 3D visualization
    def start_3D(self):
        self.playsound('SystemHand')
        if tkMessageBox.askquestion('Confirm', 'You will exit the program after 3D simulation!\nDo you still want to continue?') == 'yes':
            gas.visualization()
            self.show_demon.config(state='disable')
            self.show_3D.config(state='disable')

    # the function for button close_figures
    def close_figure(self):
        pylab.close()
        pylab.close()
        self.show_demon.config(state='normal',  # re-enable the start button
                          image=self.temp1)
        self.show_3D.config(state='normal')

    # the function for button quit
    def quit_canvas(self):
        self.playsound('SystemHand')
        if tkMessageBox.askquestion('Confirm', 'Do you want to quit?') == 'yes':  # ensure to quit
            thread.exit()# quit

    # a series of functions which are used to set the transparancy
    def transparancy1(self):
        root.attributes("-alpha", 0.5)


    def transparancy2(self):
        root.attributes("-alpha", 0.75)


    def transparancy3(self):
        root.attributes("-alpha", 0.85)


    def transparancy4(self):
        root.attributes("-alpha", 0.9)


    def transparancy5(self):
        root.attributes("-alpha", 0.95)


    def transparancy6(self):
        root.attributes("-alpha", 1)

    # function to get UI to initial state
    def initial(self):
        self.language_EN()
        self.close_figure()
        self.transparancy4()
        self.var_entry2.set('3000')

    # function to change language to Chinese Simple
    def language_CS(self):
        self.canvas.delete('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                      'p')  # delete the original text
        self.create_text_wisha(450, 60, '欢迎！', 'Arial 43 bold italic', 'lightyellow', 'center', 2, 'black', 'a', 'b')

        self.create_text_wisha(130, 123, '分子', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'c', 'd')
        self.create_text_wisha(170, 152, '数量：', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'e', 'f')
        self.create_text_wisha(270, 150, 'N = ', 'LucidaFamily 30 bold italic', 'lightyellow', 'left', 2, 'black', 'g', 'h')

        self.create_text_wisha(80, 218, '系统', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'i', 'j')
        self.create_text_wisha(125, 245, '状态：', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'k', 'l')

        self.create_text_wisha(80, 320, '模拟', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'm', 'n')
        self.create_text_wisha(120, 350, '步数：', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'o', 'p')
        self.var_entry.set('在此输入')
        self.statebutton1.config(text='状态 1')
        self.statebutton2.config(text='状态 2')  # language switching is finished
        self.show_demon.config(image=self.CS_d1)
        self.show_3D.config(image=self.CS_31)
        self.resume.config(image=self.resume_CS)
        self.temp1 = self.CS_d1
        self.temp2 = self.CS_d2
        self.canvas.update()  # update the screen show new canvas

    # function to change language to English
    def language_EN(self):
        self.canvas.delete('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                      'p')  # delete the original text
        self.create_text_wisha(450, 60, 'Welcome!', 'Arial 34 bold italic', 'lightyellow', 'center', 2, 'black', 'a', 'b')

        self.create_text_wisha(100, 125, 'Molecules', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'c', 'd')
        self.create_text_wisha(150, 150, 'Quantity:', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'e', 'f')
        self.create_text_wisha(270, 150, 'N = ', 'LucidaFamily 30 bold italic', 'lightyellow', 'left', 2, 'black', 'g', 'h')

        self.create_text_wisha(80, 220, 'System', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'i', 'j')
        self.create_text_wisha(125, 245, 'State:', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'k', 'l')

        self.create_text_wisha(105, 315, 'Simulation', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'm', 'n')
        self.create_text_wisha(120, 340, 'Step:', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'o', 'p')
        self.var_entry.set('Input  here')
        self.statebutton1.config(text='State 1  ')
        self.statebutton2.config(text='State 2  ')  # language switching is finished
        self.show_demon.config(image=self.button_d1)
        self.show_3D.config(image=self.button_31)
        self.resume.config(image=self.resume_EN)
        self.temp1 = self.button_d1
        self.temp2 = self.button_d2
        self.canvas.update()  # update the screen show new canvas

    # function to change language to Chinese Complex
    def language_CC(self):
        self.canvas.delete('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                      'p')  # delete the original text
        self.create_text_wisha(450, 60, '歡迎！', 'Arial 43 bold italic', 'lightyellow', 'center', 2, 'black', 'a', 'b')

        self.create_text_wisha(130, 123, '分子', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'c', 'd')
        self.create_text_wisha(170, 152, '數量：', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'e', 'f')
        self.create_text_wisha(270, 150, 'N = ', 'LucidaFamily 30 bold italic', 'lightyellow', 'left', 2, 'black', 'g', 'h')

        self.create_text_wisha(80, 218, '系統', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'i', 'j')
        self.create_text_wisha(125, 245, '狀態：', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'k', 'l')

        self.create_text_wisha(80, 320, '模擬', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'm', 'n')
        self.create_text_wisha(120, 350, '步數：', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'o', 'p')
        self.var_entry.set('在此輸入')
        self.statebutton1.config(text='狀態 1')
        self.statebutton2.config(text='狀態 2')  # language switching is finished
        self.show_demon.config(image=self.CC_d1)
        self.show_3D.config(image=self.CC_31)
        self.resume.config(image=self.resume_CC)
        self.temp1 = self.CC_d1
        self.temp2 = self.CC_d2
        self.canvas.update()  # update the screen show new canvas

    # function to change language to Japanese
    def language_JA(self):
        self.canvas.delete('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                      'p')  # delete the original text
        self.create_text_wisha(450, 60, 'ようこそ！', 'Arial 34 bold italic', 'lightyellow', 'center', 2, 'black', 'a', 'b')

        self.create_text_wisha(130, 123, '分子', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'c', 'd')
        self.create_text_wisha(170, 152, 'の数：', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'e', 'f')
        self.create_text_wisha(270, 150, 'N = ', 'LucidaFamily 30 bold italic', 'lightyellow', 'left', 2, 'black', 'g', 'h')

        self.create_text_wisha(80, 218, 'システム', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'i', 'j')
        self.create_text_wisha(110, 245, 'ステータス：', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'k', 'l')

        self.create_text_wisha(150, 315, 'シミュレーション', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'm', 'n')
        self.create_text_wisha(120, 345, '度数：', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'o', 'p')
        self.var_entry.set('入力ここ')
        self.statebutton1.config(text='状態 1')
        self.statebutton2.config(text='状態 2')  # language switching is finished
        self.show_demon.config(image=self.JA_d1)
        self.show_3D.config(image=self.JA_31)
        self.resume.config(image=self.resume_JA)
        self.temp1 = self.JA_d1
        self.temp2 = self.JA_d2
        self.canvas.update()  # update the screen show new canvas

    # function to change language to Korean
    def language_KO(self):  # Something wrong happens when Pycharm display the Korean character, but it can shown well in UI
        self.canvas.delete('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                      'p')  # delete the original text
        self.create_text_wisha(450, 60, '환영！', 'Arial 34 bold italic', 'lightyellow', 'center', 2, 'black', 'a',
                          'b')  # so just ignore these strange signs here

        self.create_text_wisha(130, 123, '분자', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'c', 'd')
        self.create_text_wisha(170, 152, '의 수：', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'e', 'f')
        self.create_text_wisha(270, 150, 'N = ', 'LucidaFamily 30 bold italic', 'lightyellow', 'left', 2, 'black', 'g', 'h')

        self.create_text_wisha(80, 215, '시스템', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'i', 'j')
        self.create_text_wisha(125, 247, '상태：', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'k', 'l')

        self.create_text_wisha(80, 320, '시뮬레이션', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'm', 'n')
        self.create_text_wisha(120, 350, '단계：', 'Times 23 bold', 'lightyellow', 'left', 2, 'black', 'o', 'p')
        self.var_entry.set('    입력')
        self.statebutton1.config(text='지위 1')
        self.statebutton2.config(text='지위 2')  # language switching is finished
        self.show_demon.config(image=self.KO_d1)
        self.show_3D.config(image=self.KO_31)
        self.resume.config(image=self.resume_KO)
        self.temp1 = self.KO_d1
        self.temp2 = self.KO_d2
        self.canvas.update()  # update the screen show new canvas


    def start_bgm(self):
        thread.start_new_thread(self.bgm,())


    def help(self):
                #　要打开的图像
        instruction_bg = PhotoImage(file='instruction.gif')
        tl = Toplevel() # config
        tl.title('Instruction')
        tl.geometry('450x600')
        # 初始坐标
        x0 = 240
        y0 = 900
        # 列表将包含所有的x和y坐标.到目前为止，他们只包含初始坐标
        x = [x0]
        y = [y0]
        # 图片间隔时间,要动画效果，此处设为每秒４０帧
        sleep_time = 0.025
        step = 195
        # 添加新的值到列表
        for i in range(step):
            x.append(x0)
            y.append(y[i] - 3)

        # 开始使用ｔｋ绘图
        photo = Canvas(tl, width=450, height=600, background='black')
        photo.create_image(225, 300, image=instruction_bg)
        photo.create_text(x[0], y[0], text='Designed by',
                              font='Times 13 bold', fill='lightyellow', tag = "tex1")
        photo.create_text(x[0], y[0]+10, text='Archiris',
                              font='Times 23 bold', fill='lightyellow', tag = "tex2")
        photo.create_text(x[0], y[0]+15, text='Wang JiaLu &',
                              font='Times 13 bold', fill='lightyellow', tag = "tex3")
        photo.create_text(x[0], y[0]+20, text='Chen MingCheng',
                              font='Times 13 bold', fill='lightyellow', tag = "tex4")
        photo.create_text(x[0], y[0]+25, text='2016. 1. 1.',
                              font='Times 13 bold', fill='lightyellow', tag = "tex5")
        photo.pack()

        # 每次的移动
        for t in range(0,step+1):
            photo.delete('pic', 'tex1', 'tex2', 'tex3', 'tex4')

            photo.create_image(225, 300, image=instruction_bg, tag='pic')
            photo.create_text(x[t]-2, y[t]+1, text="""<1> Input the molecules quantity
N in the corresponding entry.
    Rem: This N would be better to
be an integer which is around 500,
so that you can get the best simu-
lation effect.
<2> Choose an state of the system
from two choices.
<3> Set the simulation step by inpu-
tting in the corresponding entry.
    Rem: This number would be better
to be an integer which is between
1000 and 5000, so that you can get
the best simulation effect.
<4> Click button: Start with Demon
Algorithm to get the figures.
<5> Wait for the result coming out.
<6> Click Resume to get ready for
next simulation.
<7> Click button: Start with 3D Si-
mulation to get the 3D dynamic graph.
    Rem: You will have to exit the
program after running 3D simulation.""",
            font='Times 15 bold', fill='black', tag = "tex1")
            photo.create_text(x[t], y[t], text="""<1> Input the molecules quantity
N in the corresponding entry.
    Rem: This N would be better to
be an integer which is around 500,
so that you can get the best simu-
lation effect.
<2> Choose an state of the system
from two choices.
<3> Set the simulation step by inpu-
tting in the corresponding entry.
    Rem: This number would be better
to be an integer which is between
1000 and 5000, so that you can get
the best simulation effect.
<4> Click button: Start with Demon
Algorithm to get the figures.
<5> Wait for the result coming out.
<6> Click Resume to get ready for
next simulation.
<7> Click button: Start with 3D Si-
mulation to get the 3D dynamic graph.
    Rem: You will have to exit the
program after running 3D simulation.""",
                font='Times 15 bold', fill='lightyellow', tag = "tex2")
            photo.create_text(x[t]-20, y[t]-283, text='READ ME',
                              font='Times 23 bold', fill='black', tag = "tex3")
            photo.create_text(x[t]-18, y[t]-285, text='READ ME',
                              font='Times 23 bold', fill='lightyellow', tag = "tex4")
            photo.update()
            # 暂停0.05妙
            time.sleep(sleep_time)
        photo.mainloop()



    def about(self):
        #　要打开的图像
        about_bg = PhotoImage(file='about.gif')
        tl = Toplevel() # config
        tl.title('R&D team')
        tl.geometry('580x483')
        # 初始坐标
        x0 = 280
        y0 = 490
        # 列表将包含所有的x和y坐标.到目前为止，他们只包含初始坐标
        x = [x0]
        y = [y0]
        # 图片间隔时间,要动画效果，此处设为每秒４０帧
        sleep_time = 0.025
        step = 60
        # 添加新的值到列表
        for i in range(step):
            x.append(x0)
            y.append(y[i] - 3)

        # 开始使用ｔｋ绘图
        photo = Canvas(tl, width=580, height=483, background='black')
        photo.create_image(290, 241.5, image=about_bg)
        photo.create_text(x[0], y[0], text='Designed by',
                              font='Times 15 bold', fill='lightyellow', tag = "tex1")
        photo.create_text(x[0], y[0]+10, text='Archiris',
                              font='Times 23 bold', fill='lightyellow', tag = "tex2")
        photo.create_text(x[0], y[0]+15, text='Wang JiaLu &',
                              font='Times 13 bold', fill='lightyellow', tag = "tex3")
        photo.create_text(x[0], y[0]+20, text='Chen MingCheng',
                              font='Times 13 bold', fill='lightyellow', tag = "tex4")
        photo.create_text(x[0], y[0]+25, text='2016. 1. 1.',
                              font='Times 13 bold', fill='lightyellow', tag = "tex5")
        photo.pack()

        # 每次的移动
        for t in range(0,step+1):
            photo.delete('pic', 'tex1', 'tex2', 'tex3', 'tex4', 'tex5')

            photo.create_image(290, 241.5, image=about_bg, tag='pic')
            photo.create_text(x[t], y[t], text='Designed by',
                              font='Times 15 bold', fill='lightyellow', tag = "tex1")
            photo.create_text(x[t], y[t]+30, text='—— Archiris ——',
                              font='Times 25 bold', fill='lightyellow', tag = "tex2")
            photo.create_text(x[t]-50, y[t]+60, text='Wang JiaLu &',
                              font='Times 15 bold', fill='lightyellow', tag = "tex3")
            photo.create_text(x[t]+50, y[t]+80, text='Chen MingCheng',
                              font='Times 15 bold', fill='lightyellow', tag = "tex4")
            photo.create_text(x[t], y[t]+110, text='- 2016. 1. 1. -',
                              font='Times 15 bold', fill='lightyellow', tag = "tex5")
            photo.update()
            # 暂停0.05妙
            time.sleep(sleep_time)
        photo.mainloop()

# create the playground for tk
root = Tk()

app = App(root)

root.mainloop()  # wait for operation



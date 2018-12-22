from tkinter import *
from webbrowser import *
import requests
from bs4 import BeautifulSoup

site_url="https://www.hackerrank.com/contests"

html_code=requests.get(site_url)
html_text=html_code.text
main_code=BeautifulSoup(html_text,"html.parser")

def url_opener(site):
    open(site,2)

main=Tk()

main.title('HackerRank Contest')

main.configure(bg='grey90')
main.wm_maxsize(900,670)
main.wm_minsize(900,670)

main_icon=PhotoImage(file='HackerRank_MainIcon.png')
main_label=Label(main)
main_label.configure(image=main_icon,bg='grey90')
main_label.place(x=140,y=30)

'''------------------------------------------------------------------------------------------------------------------'''
contest_canvas=Canvas(main,width=750,height=350,bg='grey90', highlightthickness=0,relief='ridge')
contest_canvas.place(x=70,y=180)

'''------------------------------------------------------------------------------------------------------------------'''
i = 0

for contest_name, contest_url in zip(main_code.findAll('div', {'class': 'contest-name head-col truncate txt-navy'}),
                                     main_code.findAll('a', {'class': 'psR psL fnt-wt-500 xsmall details-link'})):
    text = contest_name.string
    text2 = contest_url.get('href')
    final_url = 'https://www.hackerrank.com' + str(text2)

    rectangle=contest_canvas.create_text(100,75*i+100,text=text,width=750,anchor=W,font=('comic sans','21','bold'),
                                         fill='grey23',activefill='grey40')


    button=Button(main,text='Details',command=lambda final_url=final_url:url_opener(final_url))
    button.configure(bg='springgreen4',fg='white',font=('comic sans','15','bold'),relief=SUNKEN,borderwidth=0,
                     width=8,height=1)
    button.place(x=660,y=75*i+255)

    i = i + 1


'''------------------------------------------------------------------------------------------------------------------'''
footer=Label(main,text='     Anudish Jain')
footer.configure(bg='springgreen4',fg='white',height=3,width=120,anchor=W,font=('vedanata','12','bold italic'))
footer.place(x=0,y=617)
'''------------------------------------------------------------------------------------------------------------------'''
github_url='https://github.com/anudishjain'
icon1=PhotoImage(file='github-logo.png')
git=Button(main,command=lambda :url_opener(github_url))
git.configure(bg='springgreen4',image=icon1,borderwidth=0,relief=SUNKEN,)
git.place(x=810,y=625)
'''------------------------------------------------------------------------------------------------------------------'''
linkedin_url='https://www.linkedin.com/in/anudishjain/'
icon2=PhotoImage(file='linkedin-logo.png')
linkedin=Button(main,command=lambda :url_opener(linkedin_url))
linkedin.configure(bg='springgreen4',image=icon2,borderwidth=0,relief=SUNKEN)
linkedin.place(x=850,y=625)


main.mainloop()

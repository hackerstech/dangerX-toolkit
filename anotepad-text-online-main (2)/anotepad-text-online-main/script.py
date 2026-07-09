import requests 
import os
os.system('touch cookie.txt')
k=open("cookie.txt",'r+')

o=k.read()
if   o!="" or o.isspace!=True or o!=" ":
     co={'AnotepadId': o.split(":")[1].strip("' }") }

else :
     print("no cookies found in cookies.txt")

def normal_create(title,content):
 
    data_user={"notetype":"PlainText","noteaccess":2,"notepassword":" ","notequickedit":"false","notequickeditpassword":" ","notetitle":title,"notecontent":content}
    cnc=requests.request("POST","https://anotepad.com/note/create/",data=data_user)

    if str(o).isspace==True or o=='' or str(o)==''or o.isspace==True:
         k.write(str(cnc.cookies.get_dict()))
    print("created sucessfully")


def pass_note_create(title,pass_ph,cook):
  
    data_user={"notetype":"PlainText","noteaccess":3,"notepassword":pass_ph,"notequickedit":"false","notequickeditpassword":" ","notetitle":title,"notecontent":content}
    cnc=requests.request("POST","https://anotepad.com/note//",data=data_user)
    



# def read_user(id,url):


#     cook={'AnotepadId': id }
#     r=requests.request("GET",url,cookies=cook)
#     r=r.content

#     c=str(r).split('Note Content" ')
#     msg=c[1].split(" ")[1]
#     title="title->",str(r).split('value="')[1].split('"')[0]
#     print("\033[31m",title,"\n\033[32mtext [",msg.split(">")[1].split("</")[0],"]")


def edit(uid,title,content,cook,passwd=''):
     if passwd!='' or passwd!=" " or passwd.isspace()!=True:
         data_save={
             "number":id,"notetype":"PlainText","noteaccess":2,"notepassword":passwd,"notequickedit":"false","notequickeditpassword":"","notetitle":title,"notecontent":content}
         c=requests.request("POST","https://anotepad.com/note/save",data=data_save,cookies=cook,headers={"Referer": f"https://anotepad.com/notes/{uid}"})
     else:
          
         data_save={
             "number":id,"notetype":"PlainText","noteaccess":3,"notepassword":'',"notequickedit":"false","notequickeditpassword":"","notetitle":title,"notecontent":content}
         ccn=requests.request("POST","https://anotepad.com/note/save",data=data_save,cookies=cook,headers={"Referer": f"https://anotepad.com/notes/{uid}"})
   
     


def delete():
     i=input('note uid delete :')
     d=requests.request("POST",f"https://anotepad.com/note/delete/{i}")


## private data save ( cookie require ) 

def create_private(cook,title,content):
    data_user={"notetype":"PlainText","noteaccess":1,"notepassword":" ","notequickedit":"false","notequickeditpassword":" ","notetitle":title,"notecontent":content}
    cnc=requests.request("POST","https://anotepad.com/note/create/",data=data_user,cookies=cook )
    


####  accesss code notes 3 & ### access by url


def read_url(url):
    c=requests.request("GET",f"https://anotepad.com/note/read/{url}")
    c=c.content
    try:
        title=str(c).split('class="note_title">')[1].split("</span")[0]
        c=str(c).split('plaintext ">')
        msg=c[1].split("</div>")[0]
        print('\033[31mtitle=',title,'\n\033[32mtext=',msg)
    except:
        i=input("\033[1;32m access code-> " )
       
        acn=requests.request("POST",f"https://anotepad.com/note/access/{url}",data={"postback":"true","accesscode":i} )
        
        acn=acn.content
        try:
            c=str(acn).split('plaintext ">')
            msg=c[1].split("</div>")[0]
            print("\033[34mtitle->",str(acn).split('note_title">')[1].split("</span>")[0],"\n\033[32mtext-> [",msg,"]")
        except:
            print('error in access code try again ')


def show(cook):
    sh=requests.request("POST","https://anotepad.com/note/list/",cookies=cook)
    a=sh.content.decode().split("note_")
    le=len(a)
    n=1
    kk=sh.content.decode().split('note-title">')
    print("note uid's     | TILTLE")
    for  i in range(1,le):
     print(n,") ",a[i].split('"')[0]," | ",kk[i].split("<")[0].strip())
     n+=1
print("\033[1;31mthis tool uses anotepad.com this is used for saving notes on cloud directly through command line \n ~ security softwares ")

print("""
options
\033[34m1) create notes 
\033[31m2) create private notes (owner can access only)
\033[32m3) show all notes (saved on server)
\033[33m4) delete  a text note from server
\033[37m5) access notes by uid 
\033[0m6) password protected notes
\033[35m7) edit notes public/private
\033[0m""")
cin=int(input("enter option:"))
if cin==1:
    normal_create(input('enter title :'),input("paste content : "))
if cin==2:
    create_private(co,input('enter title :'),input('enter content :'))    
if cin==4:
    delete()


if cin==5:
    read_url(input('enter uid of note :'))
if cin==3:
     show(co)
if cin==6:
     pass_note_create(input("enter title :"),input("enter passphrase"),co)
     
if cin==7:
     edit(input('enter uid of note:'),input('\nchange title ? else put the same as it is :'),input("\nchange content or put the same content as it had :"),input('\nenter password or leave blank : '),co)


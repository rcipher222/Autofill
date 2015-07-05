import mechanize
import random
import string
br=mechanize.Browser()
br.open('https://docs.google.com/forms/d/1_jB9kkBq_pl-eiQhmQNLe2KnDB24jRgBX_PvSRGrFW8/viewform')
br.select_form(nr=0)
#br['entry.1415313175']='Username' 
#for form in br.forms():
   #print "Form name:", form.name
    #print form
    #br.select_form(form.name)  
    #br.form = list(br.forms())[0] 
names=[]

handler=open("names.txt")

for line in handler:
	names.append(line.split()[0])


i=0
for control in br.form.controls:
                if control.type == "select":
                        print "type=%s, name=%s value=%s" % (control.type, control.name, br[control.name])
			r=random.randint(0,len(list(control.items))-1)
			print r
			li=list(control.items)
			control.value=[li[r].name]	
		elif control.type == "radio":
                        print "type=%s, name=%s value=%s" % (control.type, control.name, br[control.name])
			r=random.randint(0,len(list(control.items))-1)
			print r
			li=list(control.items)
			control.value=[li[r].name]			
		elif control.type=="text":
			i==random.randint(0,len(names))
			control.value=names[i]
		elif control.type=="submit":
			submit_name=control.name
	        
br.submit()



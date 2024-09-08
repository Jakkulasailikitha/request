import requests
import json
a=requests.get("http://saral.navgurukul.org/api/courses")
# the content should change in to json then it will print
b=json.loads(a.text)   
c=open("course.json","w")
json.dump(b,c,indent=4)
# print(c)
d=b["availableCourses"]
# print(d)
serial_number=1
e=[]
for i in range(len(d)):
    print(i+1,d[i]['name'],d[i]["id"])
    # print(d[i]['id'])
    e.append(d[i]['name'])

# taking user input to print all topic of one specific courses:

topic=int(input("Enter the topic number:"))

#taking user input for next or previous:

a=input("Enter whether you want to go next or previous(n/p):")
serial_number=topic
print(e[serial_number-1])

# if user input is previous then the below code will be executed :

if a=="p":
    serial_number=1
    for i in d["availableCourses"]:
        print(serial_number,"-",i["name"],i["id"])
        serial_number+=1
    topic=int(input("Enter the topic number:"))

# calling parents Api:

y=requests.get("http://saral.navgurukul.org/api/courses/"+str(d["availableCourses"][topic-1]["id"])+"/exercises")

# converting parent data into Json:

data=y.json()

# pushing data into json file:

with open("parent.json","w") as f:
    json.dump(data,f,indent=4)
serial_no=1
serial_no1=1
topic_list=[]
#for printing the details of the specific courses:

for i1 in data["data"]:
    if len(i1["childExercises"])==0:
        print("   ",serial_no,".",i1["name"])
        topic_list.append(i1["name"])
        print("           ",serial_no1,".",i1["slug"])
        serial_no+=1
    else:
        serial_no2=1
        print("   ",serial_no,".",i1["name"])
        topic_list.append(i1["name"])
        for questions in i1["childExercises"]:
            print("         ",serial_no2,".",questions["name"])
            serial_no2+=1
        serial_no+=1


#taking user input for next or previous:

a=input("Enter whether you want to go next or previous(n/p):")

# if user input is previous then the below code will be executed :
serial_no=1
serial_no1=1
if a=="p":
    for index1 in data["data"]:
        if len(index1["childExercises"])==0:
            print("   ",serial_no,".",index1["name"])
            print("           ",serial_no1,".",index1["slug"])
            serial_no+=1
        else:
            serial_no2=1
            print("   ",serial_no,".",index1["name"])
            for questions in index1["childExercises"]:
                print("         ",serial_no2,".",questions["name"])
                serial_no2+=1
            serial_no+=1

# taking user input asking for specific parent course:

slug=int(input("Enter the topic number:"))
question_list=[]
slug_list=[]
print("     ",slug,".",topic_list[slug-1])

#code for slug having childExercise(More than one question):

for index1 in data["data"][slug-1]["childExercises"]:
    s_num=1
    for index1 in data["data"][slug-1]["childExercises"]:
        print("           ",s_num,".",index1["name"])
        question_list.append(index1["name"])
        s_num+=1

    que=int(input("Enter question number:")) 
    w=requests.get("http://saral.navgurukul.org/api/courses/"+str(d["availableCourses"][topic-1]["id"])+"/exercise/getBySlug?slug="+str(data["data"][slug-1]["childExercises"][que-1]["slug"]))
    DATA=w.json()
    with open("question.json","w") as f:
        json.dump(DATA,f,indent=4)
        print(DATA["content"])
        break

for i in range(len(question_list)):
    a=input("Enter whether you want to go next or previous(n/p):")
    if a=="n":
        if que==len(question_list): 
            print("Next page.")
            break
        else:
            w=requests.get("http://saral.navgurukul.org/api/courses/"+str(d["availableCourses"][topic-1]["id"])+"/exercise/getBySlug?slug="+str(data["data"][slug-1]["childExercises"][que]["slug"]))
            DATA=w.json()
            with open("question.json","w") as f:
                json.dump(DATA,f,indent=4)
                print(DATA["content"])
                que=que+1
    if a=="p":
        if que==len(question_list):
            print("No more questions")
            break
        else:
            w=requests.get("http://saral.navgurukul.org/api/courses/"+str(d["availableCourses"][topic-1]["id"])+"/exercise/getBySlug?slug="+str(data["data"][slug-1]["childExercises"][que-2]["slug"]))
            DATA=w.json()
            with open("question.json","w") as f:
                json.dump(DATA,f,indent=4)
                print(DATA["content"])
                que=que-1
                
# code for slug having no childExercise:

else:
    s_no=1
    print("         ",s_no,".",data["data"][slug-1]["slug"])
    slug_list.append(data["data"][slug-1]["slug"])

    que=int(input("Enter question number:"))
    v=requests.get("http://saral.navgurukul.org/api/courses/"+str(d["availableCourses"][topic-1]["id"])+"/exercise/getBySlug?slug="+str(data["data"][slug-1]["slug"]))
    d=v.json()
    with open("questions.json","w") as f:
        json.dump(d,f,indent=4)
        print(d["content"])
    for i in range(len(slug_list)):
        a=input("Enter whether you want to go next or previous:(n/p)")
        if a=="n":
            print("Next page.")
            break
        if a=="p":
            print("No more questions.")
            break




import os
import signal
import tkinter
import openai
from tkinter import *

#creates a global variable on click of button for the results of the prompts
def submit():
  r1 = entry1.get()
  r2 = entry2.get()
  r3 = v.get()
  r4 = entry4.get()
  r5 = entry5.get()
  r6 = w.get()

  global results
  results = [r1,r2,r3,r4,r5,r6]


frame = Tk()


frame.geometry("600x600")
frame.title("Input your parameters")

#Submit button, runs the submit function
submitter = Button(frame, text = "submit", command = submit) 
submitter.pack(pady = 20, side = "bottom")

#label for and text box for first entry
labelText=StringVar()
labelText.set("Enter the Name of Your Website")
labelDir=Label(frame, textvariable=labelText, height=4)
labelDir.pack()
entry1 = Entry(width=50)
entry1.pack(padx=10)

#label for and text box for second entry
labelText=StringVar()
labelText.set("Enter What Your Website is About")
labelDir=Label(frame, textvariable=labelText, height=4)
labelDir.pack()
entry2 = Entry(width=50)
entry2.pack(padx=10)

#label for and text box for radio button for images or not
labelText=StringVar()
labelText.set("Would you Like Images on Your Website?")
labelDir=Label(frame, textvariable=labelText, height=4)
labelDir.pack()
v = tkinter.IntVar()
tkinter.Radiobutton(frame, 
               text="Yes",
               padx = 20, 
               variable=v, 
               value=1).pack()

tkinter.Radiobutton(frame, 
               text="No",
               padx = 20, 
               variable=v, 
               value=2).pack()


#label for and text box for fourth entry
labelText=StringVar()
labelText.set("Enter the Name of Your Website")
labelDir=Label(frame, textvariable=labelText, height=4)
labelDir.pack()
entry4 = Entry(width=50)
entry4.pack(padx=10)

#label for and text box for fifth entry
labelText=StringVar()
labelText.set("Enter the Name of Your Website")
labelDir=Label(frame, textvariable=labelText, height=4)
labelDir.pack()
entry5 = Entry(width=50)
entry5.pack(padx=10)
labelText=StringVar()
labelText.set("Select a Maximum Length of the Generation")
labelDir=Label(frame, textvariable=labelText, height=1)
labelDir.pack(pady = 10)
#Slider for the maximun length of GPT-3 prompt
w = Scale(frame, from_=250, to=1000, length= 250, orient=HORIZONTAL)
w.pack(pady = 0)

frame.mainloop()

# Attempt to check and make sure all parameters are filled
for x in results:
  if (not x):
    print("Parameter missing, killing program")
    # attempt to kill program
    # os.kill(pid, signal.SIGTERM) 


# Prompt construction
# Constructs a full prompt out of the parameters from the input
prompt = "We are trying to build a website titled " + results[0] + ". "
prompt += results[1] 
if (results[2] == 1):
  prompt+= ". We want this website to have images with external links"
else:
  prompt+="We do not want this website to have any images"
prompt += ". The HTML code for this website looks like this:"

print(prompt)

openai.api_key = "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"

response = openai.Completion.create(
  model="text-davinci-002",
  prompt= prompt,
  temperature=0.7,
  max_tokens=results[5], #max tokens set by the user in the prompted field
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(prompt,": ",response.choices[0].text)

file = open("text.txt", "w")

file.write(response.choices[0].text)

file.close()
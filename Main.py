import os
import customtkinter as ctk
import tkinter as tk
import threading
import wordCloud
from CTkMessagebox import CTkMessagebox
from PIL import Image  

import EditText
import emoticons
from spellingChecker import *
from translator import *
from synonymsAndAntonyms import synonymsAndAntonyms
from ConvertTextToSpeech import convertTextToSpeech
from EntityRelationshipAnalysis import namedEntityRecognition, relationshipRecognition

'''
centerWindow()
Input:
Output:
Constraints:
'''
def centerWindow(Screen: ctk, width, height, scaleFactor):
    screenWidth = Screen.winfo_screenwidth()
    screenHeight = Screen.winfo_screenheight()
    x = int(((screenWidth/2) - (width/2)) * scaleFactor)
    y = int(((screenHeight/2) - (height/2)) * scaleFactor)
    return f'{width}x{height}+{x}+{y}'
'''
███╗   ███╗ █████╗ ██╗███╗   ██╗    ██╗    ██╗██╗███╗   ██╗██████╗  ██████╗ ██╗    ██╗
████╗ ████║██╔══██╗██║████╗  ██║    ██║    ██║██║████╗  ██║██╔══██╗██╔═══██╗██║    ██║
██╔████╔██║███████║██║██╔██╗ ██║    ██║ █╗ ██║██║██╔██╗ ██║██║  ██║██║   ██║██║ █╗ ██║
██║╚██╔╝██║██╔══██║██║██║╚██╗██║    ██║███╗██║██║██║╚██╗██║██║  ██║██║   ██║██║███╗██║
██║ ╚═╝ ██║██║  ██║██║██║ ╚████║    ╚███╔███╔╝██║██║ ╚████║██████╔╝╚██████╔╝╚███╔███╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝  ╚══╝╚══╝                                                         
'''

'''
initApp():
Input:
- app (CTK)
- logo (CTKImage)
Output:
- modifies the app
Constraints:
There are no Constraints
'''
def initApp(app):        
    app.title("Emotional Advanced Text Editor")
    app.geometry(centerWindow(app, 500, 600, app._get_window_scaling()))
    app.iconbitmap(os.path.join('GUI/icon.ico'))
    app.resizable(False, False)
    
    app.columnconfigure((0), weight = 1)
    app.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11), weight = 1)
    
    logo = ctk.CTkImage(light_image=Image.open(os.path.join('GUI/logo.png')), size=(360, 70))
    
    app.img = ctk.CTkLabel(app, image=logo, text="")
    app.img.grid(row=0, column=0, rowspan=1, padx=20, pady=5)
    
    
'''
applyButtons():
Input:
- app (CTK)
Output:
- Applies the buttons.
Constraints:
There are no Constraints
'''
def applyButtons(app):
    interpretEmoticonsButton = ctk.CTkButton(master= app,
                                 fg_color='#FFADB6',
                                 font = ('', 20),
                                 width=120,
                                 height=32,
                                 border_width=2,
                                 text_color = '#FFFFFF',
                                 border_color= '#FF6674',
                                 corner_radius=7,
                                 text="Interpret Emoticons",
                                 command=interpretEmojisSubMenu,
                                 hover_color = '#FF6674')
    textToSpeechButton = ctk.CTkButton(master= app,
                                 fg_color='#FFADB6',
                                 font = ('', 20),
                                 width=120,
                                 height=32,
                                 border_width=2,
                                 text_color = '#FFFFFF',
                                 border_color= '#FF6674',
                                 corner_radius=7,
                                 text="Text to Speech",
                                 command=textToSpeechSubMenu,
                                 hover_color = '#FF6674')
    textEditorButton = ctk.CTkButton(master= app,
                                 fg_color='#FFADB6',
                                 font = ('', 20),
                                 width=120,
                                 height=32,
                                 border_width=2,
                                 text_color = '#FFFFFF',
                                 border_color= '#FF6674',
                                 corner_radius=7,
                                 text="Text Editor",
                                 command=textEditorSubMenu,
                                 hover_color = '#FF6674')
    collocationAnalysisButton = ctk.CTkButton(master= app,
                                 fg_color='#FFADB6',
                                 font = ('', 20),
                                 width=120,
                                 height=32,
                                 border_width=2,
                                 text_color = '#FFFFFF',
                                 border_color= '#FF6674',
                                 corner_radius=7,
                                 text="Collocation Analysis",
                                 command=print('Req4'),
                                 hover_color = '#FF6674')
    
    entityRelationshipAnalysisButton = ctk.CTkButton(master= app,
                                 fg_color='#FFADB6',
                                 font = ('', 20),
                                 width=120,
                                 height=32,
                                 border_width=2,
                                 text_color = '#FFFFFF',
                                 border_color= '#FF6674',
                                 corner_radius=7,
                                 text="Entity-Relationship Analysis",
                                 command=entityRelationShipSubMenu,
                                 hover_color = '#FF6674')
    translatorButton = ctk.CTkButton(master= app,
                                 fg_color='#FFADB6',
                                 font = ('', 20),
                                 width=120,
                                 height=32,
                                 border_width=2,
                                 text_color = '#FFFFFF',
                                 border_color= '#FF6674',
                                 corner_radius=7,
                                 text="Traslator",
                                 command=translatorMenu,
                                 hover_color = '#FF6674')
    wordCloudButton = ctk.CTkButton(master= app,
                                 fg_color='#FFADB6',
                                 font = ('', 20),
                                 width=120,
                                 height=32,
                                 border_width=2,
                                 text_color = '#FFFFFF',
                                 border_color= '#FF6674',
                                 corner_radius=7,
                                 text="Word Cloud",
                                 command=wordCloudSubMenu,
                                 hover_color = '#FF6674')
    textEncoderButton = ctk.CTkButton(master= app,
                                 fg_color='#FFADB6',
                                 font = ('', 20),
                                 width=120,
                                 height=32,
                                 border_width=2,
                                 text_color = '#FFFFFF',
                                 border_color= '#FF6674',
                                 corner_radius=7,
                                 text="Text Encoder",
                                 command=print('Req9'),
                                 hover_color = '#FF6674')    
    spellingCheckerButton = ctk.CTkButton(master= app,
                                 fg_color='#FFADB6',
                                 font = ('', 20),
                                 width=120,
                                 height=32,
                                 border_width=2,
                                 text_color = '#FFFFFF',
                                 border_color= '#FF6674',
                                 corner_radius=7,
                                 text="Spelling Checker",
                                 command=spellingCheckerMenu,
                                 hover_color = '#FF6674')
    synonymsAndAntonymsButton = ctk.CTkButton(master= app,
                                 fg_color='#FFADB6',
                                 font = ('', 20),
                                 width=120,
                                 height=32,
                                 border_width=2,
                                 text_color = '#FFFFFF',
                                 border_color= '#FF6674',
                                 corner_radius=7,
                                 text="synonyms and antonyms",
                                 command=synonymsAntonyms,
                                 hover_color = '#FF6674')    
    
    interpretEmoticonsButton.grid(row = 1, column = 0)
    textToSpeechButton.grid(row=2, column= 0)
    textEditorButton.grid(row=3, column=0)
    collocationAnalysisButton.grid(row=4, column=0)
    entityRelationshipAnalysisButton.grid(row=5, column=0)
    translatorButton.grid(row=6, column=0)
    wordCloudButton.grid(row=7, column=0)
    textEncoderButton.grid(row=8, column = 0)
    spellingCheckerButton.grid(row=9, column=0)
    synonymsAndAntonymsButton.grid(row=10, column=0)

'''
███████╗██╗   ██╗██████╗       ███╗   ███╗███████╗███╗   ██╗██╗   ██╗███████╗
██╔════╝██║   ██║██╔══██╗      ████╗ ████║██╔════╝████╗  ██║██║   ██║██╔════╝
███████╗██║   ██║██████╔╝█████╗██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║███████╗
╚════██║██║   ██║██╔══██╗╚════╝██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║╚════██║
███████║╚██████╔╝██████╔╝      ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝███████║
╚══════╝ ╚═════╝ ╚═════╝       ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
'''
'''
interpretEmojisSubMenu()
'''
def interpretEmojisSubMenu():
    subMenu = ctk.CTk()
    subMenu.iconbitmap(os.path.join('GUI/icon.ico'))
    subMenu.title('Interpret Emojis')
    
    subMenu.geometry(centerWindow(subMenu, 600, 300, subMenu._get_window_scaling()))
    subMenu.resizable(False, False)
    subMenu.focus_set()
    
    subMenu.rowconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=2)
    subMenu.columnconfigure(0, weight=10)
    subMenu.columnconfigure((1,2), weight=1)
                        
    
    inputTextBox = ctk.CTkTextbox(subMenu, height=100, width=20)
    inputTextBox.grid(row=0, column=0, sticky=ctk.NSEW, padx=5, pady=5, rowspan=10)
    
    emotionLabelList = []
    
    for index, emotion in enumerate(['Joy', 'Sadness','Surprise','Anger','Love','Amazament','Affection','Confusion','Frustration']):
        ctk.CTkLabel(subMenu, text=f'{emotion}:', width=1, font=('',14)).grid(row=index, column=1, sticky=ctk.E)
        emotionLabelList.append(ctk.CTkLabel(subMenu, width=120, text='', font=('',14)))
        emotionLabelList[index].grid(row=index, column=2)
    
    interpretButton = ctk.CTkButton(subMenu,  fg_color='#FFADB6',
                                 font = ('montserrat', 14),
                                 border_width=2,
                                 text_color = '#FFFFFF',
                                 border_color= '#FF6674',
                                 text="Interpret Emojis",
                                 command=lambda: interpretEmoticonsButtonFunc(inputTextBox, emotionLabelList),
                                 hover_color = '#FF6674')
    interpretButton.grid(row=10, column=0, pady=10)
    
    def interpretEmoticonsButtonFunc(inputTextBox, emotionLabelList):
        text = inputTextBox.get(0.0, 'end')
        scores = emoticons.interpretEmoticons(text)
        predominantEmotion = max(scores, key=scores.get)

        iEmotion = 0
        for emotionInScore, score in scores.items():
            print(predominantEmotion, emotionInScore)
            if predominantEmotion == emotionInScore:
                emotionLabelList[iEmotion].configure(text_color='#B6FFAD')
            else:
                emotionLabelList[iEmotion].configure(text_color='#FFADB6')
            emotionLabelList[iEmotion].configure(text=score)
            iEmotion += 1
    subMenu.mainloop()


'''
def textToSpeechSubMenu()
Input:
-
Output:
-
Constraints:
-
'''
def textToSpeechSubMenu():
    subMenu = ctk.CTk()
    subMenu.iconbitmap(os.path.join('GUI/icon.ico'))
    subMenu.title('Text To Speech')
    
    subMenu.geometry(centerWindow(subMenu, 400, 200, subMenu._get_window_scaling()))
    subMenu.resizable(False, False)
    subMenu.focus_set()
    
    subMenu.rowconfigure((0), weight= 1)
    subMenu.rowconfigure((1), weight=4)
    subMenu.rowconfigure((2), weight=2)
    subMenu.columnconfigure((0,1,2), weight=1)

    textLabel = ctk.CTkLabel(subMenu, font = ('montserrat', 14), text = 'Text')
    textBox =ctk.CTkTextbox(subMenu, font= ('montserrat', 14), wrap = 'word', height=200)
    
    emotionLabel = ctk.CTkLabel(subMenu, font = ('montserrat', 14), text = 'Emotion')
    emotionComboBox = ctk.CTkComboBox(subMenu, font = ('montserrat', 14), values=['default', 'joy', 'love', 'anger', 'sadness', 'surprise', 'confusion', 'affection', 'frustration', 'atonishment'])
    
    ttsButton = ctk.CTkButton(subMenu,  fg_color='#FFADB6',
                                 font = ('montserra', 14),
                                 border_width=2,
                                 text_color = '#FFFFFF',
                                 border_color= '#FF6674',
                                 text="Text to Speech",
                                 command=lambda: convertTextToSpeech(textBox.get('1.0',  "end"), emotionComboBox.get()),
                                 hover_color = '#FF6674')
    
    
    textLabel.grid(column=0, row=0, columnspan =1, sticky = ctk.N, pady = 5)
    textBox.grid(column=0, row=1, columnspan=1,rowspan=2, sticky = ctk.S, pady=10)
    
    emotionLabel.grid(column = 2, row = 0, sticky = ctk.N, pady = 5)
    emotionComboBox.grid(column = 2, row = 1, sticky = ctk.N, pady = 10)
    
    ttsButton.grid(column=2, row=2, sticky = ctk.N)
    
    subMenu.mainloop()
    
'''
def textToSpeechSubMenu()
Input:
-
Output:
-
Constraints:
-
'''
def textEditorSubMenu():
    subMenu = ctk.CTk()
    subMenu.iconbitmap(os.path.join('GUI/icon.ico'))
    subMenu.title('Text Editor')
    
    subMenu.focus_set()
    
    subMenu.geometry(centerWindow(subMenu, 800, 600, subMenu._get_window_scaling()))
    subMenu.minsize(width=400, height=200)
    
    subMenu.grid_rowconfigure(0, weight=30)
    subMenu.grid_rowconfigure(1, weight=1)
    subMenu.grid_columnconfigure((0,1,2), weight=1)
    subMenu.grid_columnconfigure(3, weight=10)

    textBox = ctk.CTkTextbox(subMenu, border_spacing=0, font=('montserrat', 14), wrap = 'word')
    textBox.grid(row=0, column=0, sticky='nsew', padx=12, pady=8, columnspan=4)
    
    countCharsLabel = ctk.CTkLabel(subMenu, text='Chars: 0', height=2)
    countCharsLabel.grid(row=1, column=0, pady=0)
    
    countWordsLabel = ctk.CTkLabel(subMenu, text='Words: 0', height=2)
    countWordsLabel.grid(row=1, column=1, pady=0)
    
    countUniqueWordsLabel = ctk.CTkLabel(subMenu, text='Unique Words: 0', height=2)
    countUniqueWordsLabel.grid(row=1, column=2, pady=0)
    
    subMenu.bind('<Key>', lambda e: refreshCounter(textBox, countCharsLabel, countWordsLabel, countUniqueWordsLabel))
    def refreshCounter(pTextBox, pCountChars, pCountWords, pCountUniqueWords):
        content = pTextBox.get(0.0, 'end')
        words, uniqueWords = EditText.wordCounter(content)
        pCountChars.configure(text = f'Chars: {len(content)-1}')
        pCountWords.configure(text = f'Words: {words}')
        pCountUniqueWords.configure(text = f'Unique Words: {uniqueWords}')
    
    # MENUBAR 
    menuBar = tk.Menu(subMenu)
    fileMenu = tk.Menu(menuBar, tearoff=0)
    
    
    
    '''
    Delete the content in pTextBox
    '''
    fileMenu.add_command(label="New File                        Ctrl+N", command= lambda: newFile(textBox))
    def newFile(pTextBox):
        message = CTkMessagebox(title="Text Editor", message="Do you want to save the file?",
                            icon="question", option_1="Cancel", option_2="No", option_3="Yes")
        
        response = message.get()
        
        if response == 'Cancel': return
        
        if response == 'Yes':
            try:
                saveAsDialog(textBox)
            except Exception as e:
                CTkMessagebox(title="Error", message=e, icon="cancel")
                return
        
        pTextBox.delete(0.0, 'end') 
            
        
    '''
    Open a File and set the content to pTextBox
    '''        
    fileMenu.add_command(label="Open File                       Ctrl+S", command= lambda: openFileDialog(textBox))
    def openFileDialog(pTextBox): 
        message = CTkMessagebox(title="Text Editor", message="Do you want to save the file?",
                            icon="question", option_1="Cancel", option_2="No", option_3="Yes")
        
        response = message.get()
        
        if response == 'Cancel': return
        
        if response == 'Yes':
            try:
                saveAsDialog(textBox)
            except Exception as e:
                CTkMessagebox(title="Error", message=e, icon="cancel")
                return
        
        file = tk.filedialog.askopenfilename()
        content, status = EditText.openFile(file)
        
        if status:
            pTextBox.delete(0.0, 'end')
            pTextBox.insert(0.0,content)
        else:
            CTkMessagebox(title="Error", message=content, icon="cancel")
        
        
    '''
    Save a the File in a specific path
    ''' 
    fileMenu.add_command(label="Save File as...                 Ctrl+S", command = lambda: saveAsDialog(textBox) )
    def saveAsDialog(pTextBox):
        file = tk.filedialog.asksaveasfile(filetypes = [('Text File', '*.txt')], defaultextension='.txt')
        file.write(pTextBox.get(0.0, 'end'))
        file.close()
    
    fileMenu.add_separator()
    fileMenu.add_command(label='Print', command = lambda:  CTkMessagebox(title="Info", message='This feature is not avaible D:'))
    fileMenu.add_separator()
    fileMenu.add_command(label="Close", command= lambda: subMenu.destroy())
    
    '''
    Replace the content in pTextBox using editText.findReplace()
    '''
    editMenu = tk.Menu(menuBar, tearoff=0)
    editMenu.add_command(label='Replace                         Ctrl+H', command=lambda: replaceTextDialog(textBox, subMenu))
    def replaceTextDialog(pTextBox, pSubMenu):
        replaceDialog = ctk.CTkToplevel(pSubMenu)
        replaceDialog.geometry(centerWindow(replaceDialog, 300, 120, replaceDialog._get_window_scaling()))    
        replaceDialog.grab_set()
    
        replaceDialog.title('Replace')
        
        findTextEntry = ctk.CTkEntry(replaceDialog, placeholder_text= 'Find What')
        findTextEntry.grid(row=0, column=0, pady=5, padx=5)

        replaceTextEntry = ctk.CTkEntry(replaceDialog, placeholder_text='Replace With')
        replaceTextEntry.grid(row=1, column=0, pady=5, padx=5)
        
        amountTextLabel = ctk.CTkLabel(replaceDialog, text= 'Amount:')
        amountTextLabel.grid(row=0, column=1, pady=5, padx=5, sticky=ctk.NSEW)
        
        amountTextEntry = ctk.CTkEntry(replaceDialog, placeholder_text='All')
        amountTextEntry.grid(row=1, column=1, pady=5, padx=5)
        
        replaceDialog.bind('<Escape>', lambda event: replaceDialog.destroy())
        
        replaceButton = ctk.CTkButton(
            replaceDialog,
            fg_color='#FFADB6',
            font=('montserrat', 14),
            border_width=2,
            text_color='#FFFFFF',
            border_color='#FF6674',
            text="Replace",
            command=lambda: EditText.findReplace(
                pTextBox, 
                findTextEntry.get(), 
                replaceTextEntry.get(), 
                amountTextEntry.get()), 
            hover_color='#FF6674'
        )
        replaceAllButton = ctk.CTkButton(
            replaceDialog,
            fg_color='#FFADB6',
            font=('montserrat', 14),
            border_width=2,
            text_color='#FFFFFF',
            border_color='#FF6674',
            text="Replace All",
            command=lambda: EditText.findReplace(
                pTextBox, 
                findTextEntry.get(), 
                replaceTextEntry.get(), True)
            , 
            hover_color='#FF6674'
        )
        replaceButton.grid(row=3, column=0, padx=5, pady=5)
        replaceAllButton.grid(row=3, column=1, padx=5, pady=5)

        replaceDialog.mainloop().focus_set()
        
    
    menuBar.add_cascade(label="File", menu=fileMenu)
    menuBar.add_cascade(label='Edit', menu=editMenu)
    subMenu.config(menu=menuBar)


    #Binds
    subMenu.bind('<Control-s>', lambda e: saveAsDialog(textBox))
    subMenu.bind('<Control-n>', lambda e: newFile(textBox))
    subMenu.bind('<Control-o>', lambda e: openFileDialog(textBox))
    subMenu.bind('<Control-h>', lambda e:replaceTextDialog(textBox, subMenu))

    subMenu.mainloop()
    
'''
entityRelationShipSubMenu()

'''
def entityRelationShipSubMenu():
    subMenu = ctk.CTk()
    subMenu.iconbitmap(os.path.join('GUI/icon.ico'))
    subMenu.title('Entity-Relationship Analysis')
    
    subMenu.focus_set()
    
    subMenu.geometry(centerWindow(subMenu, 800, 600, subMenu._get_window_scaling()))
    subMenu.minsize(width=700, height=500)
    subMenu.columnconfigure((0,1), weight=1)
    subMenu.rowconfigure(2, weight=4)

    
    textBox = ctk.CTkTextbox(subMenu, width=1500, wrap = 'word')
    textBox.grid(row=0, column=0, sticky = ctk.NS, columnspan = 2, pady=15, padx=5)
   
    
    
    entityFrame = ctk.CTkScrollableFrame(subMenu)
    entityFrame.grid(row=2, column=0, sticky= ctk.NSEW, padx=5, pady=15)
    entityFrame.columnconfigure((0,1,2,3), weight=1)
    entityFrame.rowconfigure(0, weight=1)
     
    relationshipFrame = ctk.CTkScrollableFrame(subMenu)
    relationshipFrame.grid(row=2, column=1, sticky= ctk.NSEW, padx=15, pady=15)
    relationshipFrame.columnconfigure((0,1,2), weight=1)
    relationshipFrame.rowconfigure(0, weight=1)
    
    analysisButton = ctk.CTkButton(subMenu,
                                 fg_color='#FFADB6',
                                 font = ('', 20),
                                 width=120,
                                 height=32,
                                 border_width=2,
                                 text_color = '#FFFFFF',
                                 border_color= '#FF6674',
                                 corner_radius=7,
                                 text="Entity-Relationship Analysis",
                                 command= lambda: analysisButtonFunction(entityFrame, relationshipFrame, textBox),
                                 hover_color = '#FF6674')
    analysisButton.grid(row=1, column=0, columnspan = 2, pady=5, padx=5)


    def analysisButtonFunction(entityFrame, relationshipFrame, textBox):
        
        for widget in entityFrame.winfo_children():
            widget.destroy()
        for widget in relationshipFrame.winfo_children():
            widget.destroy()
            
        text = textBox.get(0.0, 'end')
            
        entsList = namedEntityRecognition(text)
        subjectVerbObject = relationshipRecognition(text)
        
        
        ctk.CTkLabel(entityFrame, text='TEXT', fg_color='#FFADB6', width=50, corner_radius=12).grid(row=0, column=0)
        ctk.CTkLabel(entityFrame, text='START', fg_color='#FFADB6', width=50, corner_radius=12).grid(row=0, column=1)
        ctk.CTkLabel(entityFrame, text='END', fg_color='#FFADB6', width=50, corner_radius=12).grid(row=0, column=2)
        ctk.CTkLabel(entityFrame, text='LABEL', fg_color='#FFADB6', width=50, corner_radius=12).grid(row=0, column=3)   
        for iEnts in range(len(entsList)):
            ctk.CTkLabel(entityFrame, text = entsList[iEnts][0]).grid(row = iEnts+1, column = 0, sticky=ctk.NSEW)
            ctk.CTkLabel(entityFrame, text = entsList[iEnts][1]).grid(row = iEnts+1, column = 1, sticky=ctk.NSEW)
            ctk.CTkLabel(entityFrame, text = entsList[iEnts][2]).grid(row = iEnts+1, column = 2, sticky=ctk.NSEW)
            ctk.CTkLabel(entityFrame, text = entsList[iEnts][3]).grid(row = iEnts+1, column = 3, sticky=ctk.NSEW)
     
        ctk.CTkLabel(relationshipFrame, text='SUBJECT', fg_color='#FFADB6', width=50, corner_radius=12).grid(row=0, column=0)
        ctk.CTkLabel(relationshipFrame, text='VERB', fg_color='#FFADB6', width=50, corner_radius=12).grid(row=0, column=1)
        ctk.CTkLabel(relationshipFrame, text='OBJECT', fg_color='#FFADB6', width=50, corner_radius=12).grid(row=0, column=2)   
        for sentence in range(len(subjectVerbObject)):
            ctk.CTkLabel(relationshipFrame, text = subjectVerbObject[sentence][0]).grid(row = sentence+1, column = 0, sticky=ctk.NSEW)
            ctk.CTkLabel(relationshipFrame, text = subjectVerbObject[sentence][1]).grid(row = sentence+1, column = 1, sticky=ctk.NSEW)
            ctk.CTkLabel(relationshipFrame, text = subjectVerbObject[sentence][2]).grid(row = sentence+1, column = 2, sticky=ctk.NSEW)
            
            
        
        
    subMenu.mainloop()
    
'''
translator
'''
def translatorMenu():
    
    subMenu = ctk.CTk()
    subMenu.iconbitmap(os.path.join('GUI/icon.ico'))
    subMenu.title('Translator')
    
    subMenu.focus_set()
    
    subMenu.geometry(centerWindow(subMenu, 700, 400, subMenu._get_window_scaling()))
    subMenu.resizable(False, False)
    
    subMenu.columnconfigure((0,1,2,3), weight=1)
    subMenu.rowconfigure(0, weight=1)
    subMenu.rowconfigure(1, weight=10)
    
    sourceLanguageOption = ctk.CTkOptionMenu(subMenu, fg_color='#FFADB6', button_color='#FF6674', button_hover_color='#FF6674', text_color='#303030', values=['Detect Language'])
    sourceLanguageOption.grid(row=0, column=0, padx=12, pady=2, sticky= ctk.W)
    
    targetLanguageOption = ctk.CTkOptionMenu(subMenu, fg_color='#FFADB6', button_color='#FF6674', button_hover_color='#FF6674', text_color='#303030', )
    targetLanguageOption.grid(row=0, column=2, padx=12, pady=2, sticky= ctk.W)    
    
    inputTextBox = ctk.CTkTextbox(subMenu)
    inputTextBox.grid(row=1, column=0, columnspan=2, sticky=ctk.NSEW, padx=8, pady=12)
    
    outputTextBox = ctk.CTkTextbox(subMenu, state='disabled'    )
    outputTextBox.grid(row=1, column=2, columnspan=2, sticky=ctk.NSEW, padx=8, pady=12)
    
    languages = getLanguageDict()
    for optionMenu in [sourceLanguageOption, targetLanguageOption]:
            for language in languages:
                optionMenu.configure(values = optionMenu.cget('values') + [language])
                
    targetLanguageOption.set('spanish')
    
    
   
    def refreshTrans(e):
        threadingTranslationFunc = threading.Thread(target=translateFunc, args=(sourceLanguageOption, targetLanguageOption, inputTextBox, outputTextBox))
        threadingTranslationFunc.start()
        
    def translateFunc(sourceLanguageOption, targetLanguageOption, inputTextBox, outputTextBox):
        
        text = inputTextBox.get(0.0, 'end')

        if len(text) < 2: return
    
        if sourceLanguageOption.get() == 'Detect Language':
            codeSourceLanguage = detectLanguage(text)
        else:
            codeSourceLanguage = languages.get(sourceLanguageOption.get())

        codeTargetLanguage = languages.get(targetLanguageOption.get())

        translation = translateText(text, codeSourceLanguage, codeTargetLanguage)
        
        outputTextBox.configure(state='normal')
        outputTextBox.delete(0.0, 'end')
        outputTextBox.insert(0.0, translation)
        outputTextBox.configure(state='disabled')

    inputTextBox.bind('<Key>', refreshTrans)
    subMenu.mainloop()
    
    
    
    
'''
WordCloudSubMenu()
'''

def wordCloudSubMenu():
    subMenu = ctk.CTk()
    subMenu.iconbitmap(os.path.join('GUI/icon.ico'))
    subMenu.title('Word Cloud Generator')
    
    subMenu.focus_set()
    
    subMenu.geometry(centerWindow(subMenu, 450, 450, subMenu._get_window_scaling()))
    subMenu.resizable(False, False)
    
    subMenu.columnconfigure(0, weight=1)
    subMenu.rowconfigure(0, weight=1)

    inputTextBox = ctk.CTkTextbox(subMenu)
    inputTextBox.grid(row = 0, column=0, sticky=ctk.NSEW, padx=10, pady=10)
    
    generateButton = ctk.CTkButton(subMenu,
                                    fg_color='#FFADB6',
                                    font = ('', 20),
                                    width=120,
                                    height=32,
                                    border_width=2,
                                    text_color = '#FFFFFF',
                                    border_color= '#FF6674',
                                    corner_radius=7,
                                    text="Generate",
                                    command= lambda: generateCloudFunc(inputTextBox),
                                    hover_color = '#FF6674')
    generateButton.grid(row=1, column=0, pady=5, padx=5)

    def generateCloudFunc(inputTextBox):
        text = inputTextBox.get(0.0, 'end')
        wordCloud.createWordCloud(text)
        
    subMenu.mainloop()



'''
spellingCheckerMenu()
'''
def spellingCheckerMenu():
    subMenu = ctk.CTk()
    subMenu.iconbitmap(os.path.join('GUI/icon.ico'))
    subMenu.title('Spelling Checker')
    
    subMenu.focus_set()
    
    subMenu.geometry(centerWindow(subMenu, 450, 600, subMenu._get_window_scaling()))
    subMenu.resizable(False, False)
    
    subMenu.columnconfigure((0,1), weight=1)
    subMenu.rowconfigure(0, weight=2)
    subMenu.rowconfigure(1, weight=1)
    subMenu.rowconfigure(2, weight=15)
    
    inputTextBox = ctk.CTkTextbox(subMenu, width=1200)
    inputTextBox.grid(row=0, column=0,columnspan=2, sticky=ctk.NS, padx=5, pady=15)
    
    outputTextBox = ctk.CTkTextbox(subMenu, width=1200)
    outputTextBox.grid(row=2, column=0,columnspan=2, sticky=ctk.NS, padx=5, pady=15)
    
    applyChangesButton = ctk.CTkButton(subMenu,
                                 fg_color='#FFADB6',
                                 font = ('', 20),
                                 width=120,
                                 height=32,
                                 border_width=2,
                                 text_color = '#FFFFFF',
                                 border_color= '#FF6674',
                                 text_color_disabled= '#999999',
                                 corner_radius=7,
                                 state= 'disabled',
                                 text="Apply Changes",
                                 command= lambda: applyChangesButtonFunction(inputTextBox,applyChangesButton),
                                 hover_color = '#FF6674')
    applyChangesButton.grid(row=1, column=1)
    
    '''
    applyChangesButtonFunction
    '''
    def applyChangesButtonFunction(inputTextBox, applyChangesButton):
        textToChange = inputTextBox.get(0.0, 'end')
        inputTextBox.delete(0.0, 'end')
        inputTextBox.insert(0.0, finalCorrection(textToChange))
        
        applyChangesButton.configure(state='disabled')
        
        

    CheckButton = ctk.CTkButton(subMenu,
                                 fg_color='#FFADB6',
                                 font = ('', 20),
                                 width=120,
                                 height=32,
                                 border_width=2,
                                 text_color = '#FFFFFF',
                                 border_color= '#FF6674',
                                 corner_radius=7,
                                 text="Check Spelling",
                                 command= lambda: CheckButtonFunction(inputTextBox, outputTextBox, applyChangesButton),
                                 hover_color = '#FF6674')
    CheckButton.grid(row=1, column=0)
    
    def CheckButtonFunction(inputTextBox, outputTextBox, applyChangesButton):
        corrections = correctText(inputTextBox.get(0.0, 'end'))
        outputTextBox.configure(state='normal')
        outputTextBox.delete(0.0, 'end')
        outputTextBox.insert(0.0, corrections)
        outputTextBox.configure(state='disabled')
        
        applyChangesButton.configure(state='normal')
        
        
        
        
    subMenu.mainloop()
'''
synonymsAntonyms()
'''
def synonymsAntonyms():
    subMenu = ctk.CTk()
    subMenu.iconbitmap(os.path.join('GUI/icon.ico'))
    subMenu.title('Synonym And Antonym')
    
    subMenu.focus_set()
    
    subMenu.geometry(centerWindow(subMenu, 550, 600, subMenu._get_window_scaling()))
    subMenu.resizable(False, False)
    
    subMenu.columnconfigure(0, weight=1)
    subMenu.rowconfigure((0,1,2), weight=1)
    subMenu.rowconfigure(3, weight=50)
    
    ctk.CTkLabel(subMenu, text='Synonyms and Antonyms', font = ('montserrat', 20), corner_radius=12).grid(row=0, column=0, pady=5)
    
    textToAskEntry = ctk.CTkEntry(subMenu, placeholder_text='Word', height=35, width=200)
    textToAskEntry.grid(row=1, column=0, pady=5)
    
    responseTexBox = ctk.CTkTextbox(subMenu, width=1200, font=('montserrat',16), state = 'disabled', wrap = 'word')
    responseTexBox.grid(row=3, column=0, sticky=ctk.NS, padx=20, pady=20),
    
    askButton = ctk.CTkButton(subMenu,
                                 fg_color='#FFADB6',
                                 font = ('', 20),
                                 width=120,
                                 height=32,
                                 border_width=2,
                                 text_color = '#FFFFFF',
                                 border_color= '#FF6674',
                                 corner_radius=7,
                                 text="Search",
                                 command= lambda: searchSynonymsAndAntonyms(textToAskEntry, responseTexBox),
                                 hover_color = '#FF6674')
    '''
    searchSynonymsAndAntonyms()
    '''
    def searchSynonymsAndAntonyms(textToAskEntry, textBox):
        textToAsk = textToAskEntry.get()
        textBox.configure(state='normal')
        textBox.delete(0.0, 'end')
        textBox.insert(0.0, synonymsAndAntonyms(textToAsk))
        textBox.configure(state='disabled')
    askButton.grid(row=2, column=0, pady=5)
    
    subMenu.mainloop()
   
   
   
   
   
   
   
   
    

app = ctk.CTk()
initApp(app)
applyButtons(app)
app.mainloop()
    
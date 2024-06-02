import customtkinter as ctk
import os
from PIL import Image  

app = ctk.CTk()
logo = ctk.CTkImage(light_image=Image.open(os.path.join('GUI/logo.png')), size=(360, 70))

def initApp(app, logo):        
    app.title("Emotional Advanced Text Editor")
    app.geometry("500x600")
    app.iconbitmap(os.path.join('GUI/icon.ico'))
    app.resizable(False, False)
    
    app.columnconfigure((0), weight = 1)
    app.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11), weight = 5)
    
    app.img = ctk.CTkLabel(app, image=logo, text="")
    app.img.grid(row=0, column=0, rowspan=1, padx=20, pady=5)

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
                                 command=print('Req1'),
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
                                 command=print('Req2'),
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
                                 command=print('Req3'),
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
                                 command=print('Req5'),
                                 hover_color = '#FF6674')
    traslatorButton = ctk.CTkButton(master= app,
                                 fg_color='#FFADB6',
                                 font = ('', 20),
                                 width=120,
                                 height=32,
                                 border_width=2,
                                 text_color = '#FFFFFF',
                                 border_color= '#FF6674',
                                 corner_radius=7,
                                 text="Traslator",
                                 command=print('Req6'),
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
                                 command=print('Req8'),
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
    autoCorrectionButton = ctk.CTkButton(master= app,
                                 fg_color='#FFADB6',
                                 font = ('', 20),
                                 width=120,
                                 height=32,
                                 border_width=2,
                                 text_color = '#FFFFFF',
                                 border_color= '#FF6674',
                                 corner_radius=7,
                                 text="Auto-Correction",
                                 command=print('Req10'),
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
                                 command=print('Req10'),
                                 hover_color = '#FF6674')    
    
    
    
    
    
    
    
    interpretEmoticonsButton.grid(row = 1, column = 0)
    textToSpeechButton.grid(row=2, column= 0)
    textEditorButton.grid(row=3, column=0)
    collocationAnalysisButton.grid(row=4, column=0)
    entityRelationshipAnalysisButton.grid(row=5, column=0)
    traslatorButton.grid(row=6, column=0)
    wordCloudButton.grid(row=7, column=0)
    textEncoderButton.grid(row=8, column = 0)
    autoCorrectionButton.grid(row=9, column=0)
    synonymsAndAntonymsButton.grid(row=10, column=0)
initApp(app, logo)
applyButtons(app)
app.mainloop()
    

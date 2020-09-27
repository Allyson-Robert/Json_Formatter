import json
import tkinter as gui
from tkinter import scrolledtext

class Window(gui.Tk):
    def __init__(self, parent, width=960, height=540):
        gui.Tk.__init__(self, parent)
        self.parent = parent
        
        self.title("JSON formatter")
        self.window_width = width
        self.window_height = height 
        self.geometry(f"{self.window_width}x{self.window_height}")
        
        self.draw_window()
        self.bind('<Control-Return>', lambda e: self.on_enter())
        self.bind('<Escape>', lambda e: self.destroy())
        self.mainloop()
    
    def draw_window(self):
        self.TBox_L = scrolledtext.ScrolledText(self)
        self.TBox_L.pack(expand=gui.YES, fill=gui.BOTH, side=gui.LEFT)
        
        self.TBox_R = scrolledtext.ScrolledText(self)
        self.TBox_R.pack(expand=gui.YES, fill=gui.BOTH, side=gui.RIGHT)
    
    def on_enter(self):
        self.TBox_R.delete(1.0, gui.END)
        self.TBox_R.insert(gui.END, self.beautify(self.TBox_L.get(1.0, gui.END)))
        print(self.TBox_L.get(1.0, gui.END))
        print(self.beautify(self.TBox_L.get(1.0, gui.END)))
    
    def beautify(self, json_str):
        return json.dumps(json.loads(json_str), indent=4, sort_keys=True)

if __name__ == "__main__":
    app = Window(None)

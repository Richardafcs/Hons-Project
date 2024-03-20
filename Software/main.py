import tkinter as tk
from gui import MalwareDetectorApp

def main():
    root = tk.Tk()
    app = MalwareDetectorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


'''
import tkinter as tk
from tkinter import filedialog, ttk
from analysis import create_image, analyze_file, load_model
from PIL import ImageTk

class MalwareDetectorApp:
    def __init__(self, master):
        self.master = master
        master.title("Malware Detector")
        master.geometry("900x600")  # Set a fixed window size

        # Model selection
        self.model_label = tk.Label(master, text="Select Model:", font=("Arial", 12))
        self.model_label.pack()

        self.model_options = ['Decision Tree', 'Random Forest', 'SVM', 'K-Nearest Neighbors', 'Gradient Boosting', 'Multilayer Perceptron', 'AdaBoost', 'best_CNN_ES', 'LightGBM']
        self.selected_model = tk.StringVar(master)
        self.selected_model.set(self.model_options[0])

        self.model_menu = tk.OptionMenu(master, self.selected_model, *self.model_options)
        self.model_menu.config(font=("Arial", 12))
        self.model_menu.pack()

        self.load_model_button = tk.Button(master, text="Load Model", command=self.load_model, font=("Arial", 12))
        self.load_model_button.pack()

        # File selection
        self.file_label = tk.Label(master, text="Selected File:", font=("Arial", 12))
        self.file_label.pack()

        self.select_files_button = tk.Button(master, text="Select File", command=self.select_files, font=("Arial", 12))
        self.select_files_button.pack()

        # Analysis result
        self.result_label = tk.Label(master, text="Analysis Result:", font=("Arial", 12))
        self.result_label.pack()

        self.result_text = tk.Text(master, height=4, width=50, font=("Arial", 11))
        self.result_text.pack()

        # Image display
        self.image_label = tk.Label(master)
        self.image_label.pack()

        # Progress bar
        self.progress_bar = ttk.Progressbar(master, orient="horizontal", length=200, mode="determinate")
        self.progress_bar.pack()

        # Status bar
        self.status_bar = tk.Label(master, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W, font=("Arial", 10))
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def load_model(self):
        selected_model_name = self.selected_model.get()
        model = load_model(selected_model_name)
        if model:
            self.model = model
            self.update_status("Model loaded successfully: " + selected_model_name)
        else:
            self.model = None
            self.update_status("Failed to load model")

    def select_files(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.analyze_file(file_path)

    def analyze_file(self, file_path):
        if not hasattr(self, 'model'):
            self.update_status("Please load a model first.")
            return

        # Define progress callback function
        def update_progress(progress):
            self.progress_bar['value'] = progress
            self.progress_bar.update()

        # Reset status and result display
        self.update_status("Analyzing file...")
        self.result_text.delete(1.0, tk.END)

        # Perform analysis with progress callback
        try:
            result, features = analyze_file(file_path, self.model, progress_callback=update_progress)

            # Display analysis result
            self.result_text.insert(tk.END, result)
            self.update_status("Analysis completed")

            # Create image from features (Replace create_image with your actual function)
            image = create_image(features)

            # Convert PIL image to Tkinter PhotoImage
            photo = ImageTk.PhotoImage(image)

            # Display the image
            self.image_label.config(image=photo)
            self.image_label.image = photo

        except Exception as e:
            self.result_text.insert(tk.END, "Error: " + str(e))
            self.update_status("Error during analysis")

    def update_status(self, message):
        self.status_bar.config(text=message)
        
'''

'''
import tkinter as tk
from tkinter import filedialog, ttk
from analysis import create_image, analyze_file, load_model
from PIL import ImageTk

class MalwareDetectorApp:
    def __init__(self, master):
        self.master = master
        master.title("Malware Detector")
        master.geometry("900x600")  # Set a fixed window size

        # Model selection
        self.model_label = tk.Label(master, text="Select Model:", font=("Arial", 12))
        self.model_label.pack()

        self.model_options = ['Decision Tree', 'Random Forest', 'SVM', 'K-Nearest Neighbors', 'Gradient Boosting',
               'Multilayer Perceptron', 'AdaBoost', 'best_CNN_ES', 'LightGBM']  # Add model names here
        self.selected_model = tk.StringVar(master)
        self.selected_model.set(self.model_options[0])

        self.model_menu = ttk.Combobox(master, textvariable=self.selected_model, values=self.model_options)
        self.model_menu.pack()

        self.load_model_button = tk.Button(master, text="Load Model", command=self.load_model, font=("Arial", 12))
        self.load_model_button.pack()

        # File selection
        self.file_label = tk.Label(master, text="Selected File:", font=("Arial", 12))
        self.file_label.pack()

        self.select_files_button = tk.Button(master, text="Choose File", command=self.select_files, font=("Arial", 12))
        self.select_files_button.pack()

        # Analysis result
        self.result_label = tk.Label(master, text="Analysis Result:", font=("Arial", 12))
        self.result_label.pack()

        self.result_text = tk.Text(master, height=4, width=50, font=("Arial", 11))
        self.result_text.pack()

        # Image display
        self.image_label = tk.Label(master)
        self.image_label.pack()

        # Progress bar
        self.progress_bar = ttk.Progressbar(master, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack()

        # Status bar
        self.status_bar = tk.Label(master, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W, font=("Arial", 10))
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def load_model(self):
        selected_model_name = self.selected_model.get()
        try:
            model = load_model(selected_model_name)
            if model:
                self.model = model
                self.update_status("Model loaded successfully: " + selected_model_name)
            else:
                self.model = None
                self.update_status("Failed to load model")
        except Exception as e:
            self.update_status(f"Error loading model: {e}")

    def select_files(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.analyze_file(file_path)

    def analyze_file(self, file_path):
        if not hasattr(self, 'model'):
            self.update_status("Please load a model first.")
            return

        # Define progress callback function
        def update_progress(progress):
            self.progress_bar['value'] = progress
            self.progress_bar.update()

        # Reset status and result display
        self.update_status("Analyzing file...")
        self.result_text.delete(1.0, tk.END)

        # Perform analysis with progress callback
        try:
            result, features = analyze_file(file_path, self.model, progress_callback=update_progress)

            # Display analysis result
            self.result_text.insert(tk.END, result)
            self.update_status("Analysis completed")

            # Create image from features (Replace create_image with your actual function)
            image = create_image(features)

            # Convert PIL image to Tkinter PhotoImage
            photo = ImageTk.PhotoImage(image)

            # Display the image
            self.image_label.config(image=photo)
            self.image_label.image = photo

        except Exception as e:
            self.result_text.insert(tk.END, "Error: " + str(e))
            self.update_status("Error during analysis")

    def update_status(self, message):
        self.status_bar.config(text=message)


'''


import tkinter as tk
from tkinter import ttk, filedialog
from PIL import ImageTk
from analysis import load_model, analyze_file, create_image

class MalwareDetectorApp:
    def __init__(self, master):
        self.master = master
        master.title("Malware Detector")
        master.geometry("900x600")  # Set a fixed window size

        # Title Image
        self.title_image = tk.PhotoImage(file="Designer.png")
        # Resize the image to desired dimensions
        self.title_image = self.title_image.subsample(10, 10) 
        self.title_label = tk.Label(master, image=self.title_image)
        self.title_label.pack()

        # Model selection label
        self.model_selection_label = tk.Label(master, text="Select a Model to Load:", font=("Arial", 12))
        self.model_selection_label.pack()

        # Model selection
        self.model_options = ['LightGBM']
        self.selected_model = tk.StringVar(master)
        self.selected_model.set(self.model_options[0])

        self.model_menu = ttk.Combobox(master, textvariable=self.selected_model, values=self.model_options)
        self.model_menu.pack()

        self.load_model_button = tk.Button(master, text="Load Model", command=self.load_model, font=("Arial", 12))
        self.load_model_button.pack()

        # Model loading status
        self.model_loading_status = tk.Label(master, text="", font=("Arial", 10))
        self.model_loading_status.pack()

        # File selection button and label
        self.select_files_button = tk.Button(master, text="Choose File", command=self.select_files, font=("Arial", 12))
        self.select_files_button.pack()
        self.file_label = tk.Label(master, text="No file selected", font=("Arial", 10))
        self.file_label.pack()

        # Analysis result
        self.result_label = tk.Label(master, text="Analysis Result:", font=("Arial", 12))
        self.result_label.pack()

        self.result_text = tk.Text(master, height=4, width=50, font=("Arial", 11))
        self.result_text.pack()

        # Image display
        self.image_label = tk.Label(master)
        self.image_label.pack()

        # Clear result button
        self.clear_result_button = tk.Button(master, text="Clear Result", command=self.clear_result, font=("Arial", 12))
        self.clear_result_button.pack()

        # Progress bar
        self.progress_bar = ttk.Progressbar(master, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack()

        # Status bar
        self.status_bar = tk.Label(master, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W, font=("Arial", 10))
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def load_model(self):
        selected_model_name = self.selected_model.get()
        self.model_loading_status.config(text=f"Loading {selected_model_name} model...")
        self.master.update()  # Update GUI to show loading status
        try:
            model = load_model(selected_model_name)
            if model:
                self.model = model
                self.update_status("Model loaded successfully: " + selected_model_name)
            else:
                self.model = None
                self.update_status("Failed to load model")
        except Exception as e:
            self.update_status(f"Error loading model: {e}")
        finally:
            self.model_loading_status.config(text="")  # Clear loading status

    def select_files(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_label.config(text=file_path)
            self.analyze_file(file_path)

    def analyze_file(self, file_path):
        if not hasattr(self, 'model'):
            self.update_status("Please load a model first.")
            return

        # Define progress callback function
        def update_progress(progress):
            self.progress_bar['value'] = progress
            self.progress_bar.update()

        # Reset status and result display
        self.update_status("Analyzing file...")
        self.result_text.delete(1.0, tk.END)

        # Perform analysis with progress callback
        try:
            result, features = analyze_file(file_path, self.model, progress_callback=update_progress)

            # Display analysis result
            self.result_text.insert(tk.END, result)
            self.update_status("Analysis completed")

            # Create image from features (Replace create_image with your actual function)
            image = create_image(features)

            # Convert PIL image to Tkinter PhotoImage
            photo = ImageTk.PhotoImage(image)

            # Display the image
            self.image_label.config(image=photo)
            self.image_label.image = photo

        except Exception as e:
            self.result_text.insert(tk.END, "Error: " + str(e))
            self.update_status("Error during analysis")

    def clear_result(self):
        self.result_text.delete(1.0, tk.END)
        self.image_label.config(image=None)

    def update_status(self, message):
        self.status_bar.config(text=message)


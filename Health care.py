import tkinter as tk
from tkinter import messagebox
import pyttsx3
import speech_recognition as sr
import math

# Initialize the speech engine
engine = pyttsx3.init()

class SmartHealthCareApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Health Care System")
        self.root.geometry("800x600")
        self.root.resizable(0,0)
        self.root.configure(bg="#f0f0f0")

        # Title Label
        self.title_label = tk.Label(root, text="Smart Health Care System", font=("Helvetica", 20, "bold"), bg="#4CAF50", fg="white", pady=10)
        self.title_label.pack(fill=tk.X)
        
        # Frames for better alignment
        self.input_frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=10)
        self.input_frame.pack(fill=tk.BOTH, expand=True)

        self.button_frame = tk.Frame(root, bg="#f0f0f0", pady=10)
        self.button_frame.pack()

        self.assistant_frame = tk.Frame(root, bg="#f0f0f0", pady=10)
        self.assistant_frame.pack()

        # Patient Info
        self.create_label_entry(self.input_frame, "Patient Name:", 0)
        self.patient_name_entry = self.create_entry(self.input_frame, 0)

        self.create_label_entry(self.input_frame, "Age:", 1)
        self.age_entry = self.create_entry(self.input_frame, 1)

        self.create_label_entry(self.input_frame, "Gender:", 2)
        self.gender_entry = self.create_entry(self.input_frame, 2)

        self.create_label_entry(self.input_frame, "Symptoms:", 3)
        self.symptoms_entry = self.create_entry(self.input_frame, 3)

        self.create_label_entry(self.input_frame, "Body Temperature (°C):", 4)
        self.temp_entry = self.create_entry(self.input_frame, 4)

        self.create_label_entry(self.input_frame, "Blood Pressure (mmHg):", 5)
        self.bp_entry = self.create_entry(self.input_frame, 5)

        self.create_label_entry(self.input_frame, "Blood Sugar (mg/dL):", 6)
        self.sugar_entry = self.create_entry(self.input_frame, 6)

        self.create_label_entry(self.input_frame, "Location:", 7)
        self.location_entry = self.create_entry(self.input_frame, 7)

        self.create_label_entry(self.input_frame, "Sleeping Time (hours):", 8)
        self.sleep_time_entry = self.create_entry(self.input_frame, 8)

        self.create_label_entry(self.input_frame, "Food Quantity (calories):", 9)
        self.food_qty_entry = self.create_entry(self.input_frame, 9)

        self.create_label_entry(self.input_frame, "Trees Near Home:", 10)
        self.trees_entry = self.create_entry(self.input_frame, 10)

        # Buttons
        self.save_button = tk.Button(self.button_frame, text="Save", command=self.save_patient_info, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), width=10)
        self.save_button.grid(row=0, column=0, padx=10, pady=10)

        self.view_button = tk.Button(self.button_frame, text="View", command=self.view_patient_info, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), width=10)
        self.view_button.grid(row=0, column=1, padx=10, pady=10)

        self.speak_button = tk.Button(self.button_frame, text="Speak", command=self.speak, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), width=10)
        self.speak_button.grid(row=0, column=2, padx=10, pady=10)

        self.calculate_button = tk.Button(self.button_frame, text="Calculate", command=self.calculate, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), width=10)
        self.calculate_button.grid(row=0, column=3, padx=10, pady=10)

        self.assistant_button = tk.Button(self.assistant_frame, text="Assistant", command=self.assistant, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), width=10)
        self.assistant_button.pack(pady=10)

        self.patient_data = []

    def create_label_entry(self, parent, text, row):
        label = tk.Label(parent, text=text, bg="#f0f0f0", font=("Helvetica", 12, "bold"))
        label.grid(row=row, column=0, padx=10, pady=5, sticky=tk.E)
    
    def create_entry(self, parent, row):
        entry = tk.Entry(parent, font=("Helvetica", 12), width=30)
        entry.grid(row=row, column=1, padx=10, pady=5)
        return entry

    def save_patient_info(self):
        info = {
            "Name": self.patient_name_entry.get(),
            "Age": self.age_entry.get(),
            "Gender": self.gender_entry.get(),
            "Symptoms": self.symptoms_entry.get(),
            "Temperature": self.temp_entry.get(),
            "Blood Pressure": self.bp_entry.get(),
            "Blood Sugar": self.sugar_entry.get(),
            "Location": self.location_entry.get(),
            "Sleep Time": self.sleep_time_entry.get(),
            "Food Quantity": self.food_qty_entry.get(),
            "Trees Near Home": self.trees_entry.get()
        }
        
        if all(info.values()):
            self.patient_data.append(info)
            messagebox.showinfo("Success", "Patient information saved successfully!")
            
            for entry in [self.patient_name_entry, self.age_entry, self.gender_entry, self.symptoms_entry,
                          self.temp_entry, self.bp_entry, self.sugar_entry, self.location_entry,
                          self.sleep_time_entry, self.food_qty_entry, self.trees_entry]:
                entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

    def view_patient_info(self):
        if self.patient_data:
            view_window = tk.Toplevel(self.root)
            view_window.title("View Patient Information")
            view_window.geometry("600x400")
            view_window.configure(bg="#f0f0f0")

            scrollbar = tk.Scrollbar(view_window)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            text_area = tk.Text(view_window, yscrollcommand=scrollbar.set, font=("Helvetica", 12), wrap=tk.WORD)
            text_area.pack(expand=True, fill=tk.BOTH)

            for index, patient in enumerate(self.patient_data):
                info = f"Patient {index + 1}\n"
                for key, value in patient.items():
                    info += f"{key}: {value}\n"
                info += "-"*20 + "\n"
                text_area.insert(tk.END, info)

            scrollbar.config(command=text_area.yview)
        else:
            messagebox.showinfo("No Data", "No patient information available.")

    def speak(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                self.query_entry.delete(0, tk.END)
                self.query_entry.insert(0, text)
            except sr.UnknownValueError:
                messagebox.showwarning("Error", "Could not understand the audio")
            except sr.RequestError:
                messagebox.showwarning("Error", "Could not request results; check your network connection")

    def assistant(self):
        assistant_window = tk.Toplevel(self.root)
        assistant_window.title("Assistant")
        assistant_window.geometry("400x250")
        assistant_window.configure(bg="#f0f0f0")
        
        query_label = tk.Label(assistant_window, text="Enter your query:", bg="#f0f0f0", font=("Helvetica", 12, "bold"))
        query_label.pack(padx=10, pady=10)
        
        self.query_entry = tk.Entry(assistant_window, font=("Helvetica", 12), width=50)
        self.query_entry.pack(padx=10, pady=10)
        
        ask_button = tk.Button(assistant_window, text="Ask", command=self.respond, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        ask_button.pack(padx=10, pady=10)
        
        self.response_label = tk.Label(assistant_window, text="", bg="#f0f0f0", font=("Helvetica", 12))
        self.response_label.pack(padx=10, pady=10)
        
    def respond(self):
        query = self.query_entry.get().lower()
        
        if "fever" in query:
            response = "For fever, it's important to stay hydrated and rest. If the fever is high, take fever-reducing medication and consult a doctor."
        elif "headache" in query:
            response = "For headaches, rest in a quiet, dark room. Over-the-counter pain relievers can help. If headaches persist, see a healthcare provider."
        elif "cough" in query:
            response = "For cough, drink warm fluids and use cough drops. If the cough is severe or persistent, consult a doctor."
        else:
            response = "I'm not sure about that. Please consult a healthcare professional"
    
        
        self.response_label.config(text=response)
        engine.say(response)
        engine.runAndWait()

    def calculate(self):
        try:
            # Convert inputs to appropriate types
            temperature = float(self.temp_entry.get())
            blood_pressure = float(self.bp_entry.get())
            blood_sugar = float(self.sugar_entry.get())
            trees_near_home = int(self.trees_entry.get())

            # Calculate perfect sleeping time based on temperature, blood pressure, and blood sugar
            sleeping_time = self.calculate_sleeping_time(temperature, blood_pressure, blood_sugar)
            self.sleep_time_entry.delete(0, tk.END)
            self.sleep_time_entry.insert(0, str(sleeping_time))

            # Calculate perfect food quantity based on trees near home
            food_quantity = self.calculate_food_quantity(trees_near_home)
            self.food_qty_entry.delete(0, tk.END)
            self.food_qty_entry.insert(0, str(food_quantity))

            messagebox.showinfo("Calculation", "Calculation successful!")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values.")

    def calculate_sleeping_time(self, temperature, blood_pressure, blood_sugar):
        # Dummy calculation for illustration
        # You can replace this with your actual algorithm based on medical research
        return round((temperature / 10) + (blood_pressure / 100) - (blood_sugar / 50), 2)

    def calculate_food_quantity(self, trees_near_home):
        # Dummy calculation for illustration
        # You can replace this with your actual algorithm based on nutritional research
        return math.ceil(trees_near_home * 100 / 3)

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartHealthCareApp(root)
    root.mainloop()

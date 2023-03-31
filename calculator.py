import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create two frames for the calculation and result
        self.calc_frame = tk.Frame(master, bg="light blue", padx=10, pady=10)
        self.calc_frame.pack(fill=tk.BOTH, expand=True)

        self.result_frame = tk.Frame(master, bg="white", padx=10, pady=10)
        self.result_frame.pack(fill=tk.BOTH, expand=True)

        # Create entry widget for calculation
        self.calculation = tk.Entry(self.calc_frame, font=("Helvetica", 16))
        self.calculation.pack(fill=tk.BOTH, expand=True)

        # Create labels to display the calculation and result
        self.calculation_label = tk.Label(self.calc_frame, text="Calculation:", font=("Helvetica", 12), fg="black", bg="light blue")
        self.calculation_label.pack(fill=tk.BOTH)

        self.result_label = tk.Label(self.result_frame, text="Result:", font=("Helvetica", 12), fg="black", bg="white")
        self.result_label.pack(fill=tk.BOTH)

        # Create buttons for numbers and operators
        self.button_frame = tk.Frame(master)
        self.button_frame.pack()

        buttons = [
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            "0", ".", "/",
        ]

        # Use a lambda function to pass button text to the button_press method
        for i, symbol in enumerate(buttons):
            button = tk.Button(self.button_frame, text=symbol, font=("Helvetica", 16), bg="white", padx=10, pady=10,
                               command=lambda symbol=symbol: self.button_press(symbol))
            button.grid(row=i // 4, column=i % 4, sticky="nsew")

        # Add equals button
        equals_button = tk.Button(self.button_frame, text="=", font=("Helvetica", 16), bg="white", padx=10, pady=10,
                                  command=self.calculate)
        equals_button.grid(row=4, column=3, sticky="nsew")

        # Add clear button
        clear_button = tk.Button(self.button_frame, text="C", font=("Helvetica", 16), bg="white", padx=10, pady=10,
                                 command=self.clear)
        clear_button.grid(row=4, column=2, sticky="nsew")

    def button_press(self, symbol):
        # Add symbol to the end of the current calculation
        self.calculation.insert(tk.END, symbol)

    def calculate(self):
        try:
            # Evaluate the current calculation
            result = eval(self.calculation.get())

            # Clear the current calculation and display the result
            self.calculation.delete(0, tk.END)
            self.result_label.config(text=f"Result: {result}")
        except (SyntaxError, ZeroDivisionError):
            # Handle errors with the calculation
            self.result_label.config(text="Result: Error")

    def clear(self):
        # Clear the calculation and result labels
        self.calculation.delete(0, tk.END)
        self.result_label.config(text="Result:")


root = tk.Tk()
app = Calculator(root)
root.mainloop()

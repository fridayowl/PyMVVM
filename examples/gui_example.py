import tkinter as tk
from PyMVVM import create_mvvm, ViewModel, View, Command, computed_property, bindable_property

class CounterViewModel(ViewModel):
    def __init__(self, model):
        super().__init__(model)
        self.increment_command = Command(self.increment)
        self.decrement_command = Command(self.decrement)
    
    @computed_property
    def count_text(self):
        return f"Count: {self.model.count}"
    
    def increment(self):
        current_count = self.model.count
        self.model.count = current_count + 1
        # Force notification
        self.notify_observers('count_text')
    
    def decrement(self):
        current_count = self.model.count
        self.model.count = current_count - 1
        # Force notification
        self.notify_observers('count_text')

class CounterView(View):
    def __init__(self, view_model):
        # First store view_model reference
        self.view_model = view_model
        # Then setup UI
        self.setup_ui()
        # Finally initialize base class
        super().__init__(view_model)
    
    def setup_ui(self):
        self.root = tk.Tk()
        self.root.title("Counter Example")
        
        self.frame = tk.Frame(self.root, padx=20, pady=20)
        self.frame.pack(expand=True)
        
        self.label = tk.Label(
            self.frame, 
            text=self.view_model.count_text,
            font=('Helvetica', 16)
        )
        self.label.pack(pady=10)
        
        button_frame = tk.Frame(self.frame)
        button_frame.pack(pady=5)
        
        self.increment_button = tk.Button(
            button_frame,
            text="+",
            command=lambda: self.safe_command(self.view_model.increment_command),
            width=5,
            font=('Helvetica', 12)
        )
        self.increment_button.pack(side=tk.LEFT, padx=5)
        
        self.decrement_button = tk.Button(
            button_frame,
            text="-",
            command=lambda: self.safe_command(self.view_model.decrement_command),
            width=5,
            font=('Helvetica', 12)
        )
        self.decrement_button.pack(side=tk.LEFT, padx=5)
        
        self.root.minsize(200, 150)
        self.center_window()
    
    def safe_command(self, command):
        """Wrapper to ensure command execution triggers updates"""
        command()
        self.update()
    
    def update(self):
        """Update the view when properties change"""
        self.label.config(text=self.view_model.count_text)
    
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def run(self):
        self.root.mainloop()

def main():
    # Create MVVM components using the framework's factory function
    model, vm, view = create_mvvm(
        model_attrs={'count': 0},  # Initial model attributes
        view_model_class=CounterViewModel,
        view_class=CounterView
    )
    view.run()

if __name__ == "__main__":
    main()

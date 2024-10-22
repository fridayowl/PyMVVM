import tkinter as tk
from PyMVVM import create_mvvm, ViewModel, View, Command, computed_property, bindable_property

class CounterModel:
    def __init__(self, count=0):
        self._count = count
        self._observers = {}
    
    @property
    def count(self):
        return self._count
    
    @count.setter
    def count(self, value):
        self._count = value
        self.notify_observers('count')
    
    def add_observer(self, property_name, callback):
        if property_name not in self._observers:
            self._observers[property_name] = []
        self._observers[property_name].append(callback)
    
    def notify_observers(self, property_name):
        if property_name in self._observers:
            for callback in self._observers[property_name]:
                callback()

class CounterViewModel:
    def __init__(self, model):
        self.model = model
        self._observers = {}
        self.increment_command = Command(self.increment)
        self.decrement_command = Command(self.decrement)
        # Bind to model's count property
        self.model.add_observer('count', self._on_count_changed)
    
    def _on_count_changed(self):
        self.notify_observers('count_text')
    
    @property
    def count_text(self):
        return f"Count: {self.model.count}"
    
    def increment(self):
        self.model.count += 1
    
    def decrement(self):
        self.model.count -= 1
    
    def add_observer(self, property_name, callback):
        if property_name not in self._observers:
            self._observers[property_name] = []
        self._observers[property_name].append(callback)
    
    def notify_observers(self, property_name):
        if property_name in self._observers:
            for callback in self._observers[property_name]:
                callback()

class CounterView:
    def __init__(self, view_model):
        self.view_model = view_model
        self.setup_ui()
        self.bind_properties()
    
    def bind_properties(self):
        self.view_model.add_observer('count_text', self.update)
    
    def setup_ui(self):
        self.root = tk.Tk()
        self.root.title("Counter Example")
        
        # Create main frame
        self.frame = tk.Frame(self.root, padx=20, pady=20)
        self.frame.pack(expand=True)
        
        # Create and pack widgets
        self.label = tk.Label(
            self.frame, 
            text=self.view_model.count_text,
            font=('Helvetica', 16)
        )
        self.label.pack(pady=10)
        
        # Button frame for better organization
        button_frame = tk.Frame(self.frame)
        button_frame.pack(pady=5)
        
        self.increment_button = tk.Button(
            button_frame,
            text="+",
            command=self.view_model.increment_command,
            width=5,
            font=('Helvetica', 12)
        )
        self.increment_button.pack(side=tk.LEFT, padx=5)
        
        self.decrement_button = tk.Button(
            button_frame,
            text="-",
            command=self.view_model.decrement_command,
            width=5,
            font=('Helvetica', 12)
        )
        self.decrement_button.pack(side=tk.LEFT, padx=5)
        
        # Set minimum window size
        self.root.minsize(200, 150)
        
        # Center the window
        self.center_window()
    
    def update(self):
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
    # Create the components manually instead of using create_mvvm
    model = CounterModel(count=0)
    vm = CounterViewModel(model)
    view = CounterView(vm)
    view.run()

if __name__ == "__main__":
    main()

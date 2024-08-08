import tkinter as tk
from PyMVVM import create_mvvm, ViewModel, View, Command, computed_property

class CounterViewModel(ViewModel):
    def __init__(self, model):
        super().__init__(model)
        self.increment_command = Command(self.increment)
        self.decrement_command = Command(self.decrement)

    @computed_property
    def count_text(self):
        return f"Count: {self.model.count}"

    def increment(self):
        self.model.count += 1

    def decrement(self):
        self.model.count -= 1

class CounterView(View):
    def __init__(self, view_model):
        super().__init__(view_model)
        self.root = tk.Tk()
        self.root.title("Counter Example")

        self.label = tk.Label(self.root, text=self.view_model.count_text)
        self.label.pack(pady=10)

        self.increment_button = tk.Button(self.root, text="Increment", command=self.view_model.increment_command)
        self.increment_button.pack(pady=5)

        self.decrement_button = tk.Button(self.root, text="Decrement", command=self.view_model.decrement_command)
        self.decrement_button.pack(pady=5)

    def update(self):
        self.label.config(text=self.view_model.count_text)

    def run(self):
        self.root.mainloop()

model, vm, view = create_mvvm(
    {'count': 0},
    view_model_class=CounterViewModel,
    view_class=CounterView
)

view.run()
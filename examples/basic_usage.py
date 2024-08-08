 
from PyMVVM import create_mvvm, ViewModel, View, computed_property

class UserViewModel(ViewModel):
    @computed_property
    def display_name(self):
        return f"{self.model.name} ({self.model.age})"

class UserView(View):
    def update(self):
        print(f"User: {self.view_model.display_name}")

# Create MVVM structure
model, vm, view = create_mvvm(
    {'name': 'John', 'age': 30},
    view_model_class=UserViewModel,
    view_class=UserView
)

# Use the MVVM structure
view.update()  # Output: User: John (30)
model.name = "Jane"
view.update()  # Output: User: Jane (30)
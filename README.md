# PyMVVM
# Simplified MVVM for Python

PyMVVM is a Python package that simplifies the implementation of the Model-View-ViewModel (MVVM) pattern. It provides a set of base classes and utilities to create robust, maintainable, and testable applications.

## Features

- Easy-to-use base classes for Model, ViewModel, and View
- Automatic property binding and change notification
- Support for computed properties
- Command pattern implementation for actions
- Asynchronous command support
- State management in ViewModels
- Dependency injection for data services
- Factory function for quick MVVM setup

## Installation

You can install  PyMVVM using pip:



## Quick Start

Here's a simple example of how to use PyMVVM:

```python
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


## Releasing

This project uses GitHub Actions to automatically publish new releases to PyPI. To create a new release:

1. Update the version number in `setup.py`.
2. Commit your changes and push to GitHub.
3. On GitHub, go to the repository's "Releases" page.
4. Click "Draft a new release".
5. Create a new tag (e.g., v0.1.0), give your release a title, and add release notes.
6. Click "Publish release".

The GitHub Actions workflow will automatically build and publish the new version to PyPI.

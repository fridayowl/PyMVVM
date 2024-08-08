from typing import Callable

def computed_property(func: Callable) -> property:
    """Decorator for computed properties."""
    def getter(self):
        return func(self)
    return property(getter)

def bindable_property(func: Callable) -> property:
    """Decorator for bindable properties that notify observers when changed."""
    prop_name = f"_{func.__name__}"
    
    def getter(self):
        return getattr(self, prop_name)
    
    def setter(self, value):
        setattr(self, prop_name, value)
        self.notify_observers(func.__name__)
    
    return property(getter, setter)

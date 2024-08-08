from typing import Any, Dict, Type, Optional
from .core import Model, ViewModel, View, DataService

def create_mvvm(
    model_attrs: Dict[str, Any], 
    view_model_class: Type[ViewModel] = ViewModel, 
    view_class: Type[View] = View,
    data_service: Optional[DataService] = None
) -> tuple:
    """
    Factory function to create a complete MVVM structure.
    
    Args:
        model_attrs: Attributes for the model.
        view_model_class: Class to use for the view model.
        view_class: Class to use for the view.
        data_service: Optional data service to inject into the view model.
    
    Returns:
        A tuple containing the created model, view model, and view.
    """
    ModelClass = type("DynamicModel", (Model,), {})
    model = ModelClass(**model_attrs)
    view_model = view_model_class(model)
    if data_service:
        view_model.data_service = data_service
    view = view_class(view_model)
    return model, view_model, view

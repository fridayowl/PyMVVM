import asyncio
from PyMVVM import (create_mvvm, ViewModel, View, AsyncCommand, 
                      DataService, computed_property, bindable_property)

class UserDataService(DataService):
    async def fetch_data(self):
        await asyncio.sleep(1)  # Simulate API call
        return {"name": "John", "age": 30}

    async def save_data(self, data):
        await asyncio.sleep(1)  # Simulate API call
        print(f"Saved data: {data}")

class UserViewModel(ViewModel):
    def __init__(self, model):
        super().__init__(model)
        self.load_user_command = AsyncCommand(self.load_user)
        self.save_user_command = AsyncCommand(self.save_user)
        self._is_adult = False

    @bindable_property
    def is_adult(self):
        return self._is_adult

    @computed_property
    def display_name(self):
        return f"{self.model.name} ({self.model.age})"

    async def load_user(self):
        self.state = "loading"
        try:
            data = await self.data_service.fetch_data()
            self.model.name = data["name"]
            self.model.age = data["age"]
            self.is_adult = data["age"] >= 18
            self.state = "idle"
        except Exception as e:
            self.error = str(e)
            self.state = "error"

    async def save_user(self):
        self.state = "saving"
        try:
            await self.data_service.save_data({
                "name": self.model.name,
                "age": self.model.age
            })
            self.state = "idle"
        except Exception as e:
            self.error = str(e)
            self.state = "error"

class UserView(View):
    def update(self):
        print(f"User: {self.view_model.display_name}")
        print(f"Is Adult: {self.view_model.is_adult}")
        print(f"State: {self.view_model.state}")
        if self.view_model.error:
            print(f"Error: {self.view_model.error}")

async def main():
    model, vm, view = create_mvvm(
        {'name': 'Jane', 'age': 25},
        view_model_class=UserViewModel,
        view_class=UserView,
        data_service=UserDataService()
    )

    view.update()
    await vm.load_user_command()
    view.update()
    vm.model.age = 17
    view.update()
    await vm.save_user_command()

asyncio.run(main())
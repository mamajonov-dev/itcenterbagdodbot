from aiogram.dispatcher.filters.state import State, StatesGroup

class RegistrUserState(StatesGroup):
    course = State()
    name = State()
    phone = State()
    phone2 = State()
    confirm = State()
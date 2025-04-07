from aiogram.dispatcher.filters.state import State, StatesGroup

class HacatonStata(StatesGroup):
    name = State()
    age = State()
    phone = State()
    nomer = State()
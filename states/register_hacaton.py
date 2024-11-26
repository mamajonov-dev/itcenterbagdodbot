from aiogram.dispatcher.filters.state import State, StatesGroup

class HacatonStata(StatesGroup):
    name = State()
    age = State()
    nomer = State()
from aiogram.dispatcher.filters.state import State, StatesGroup

class HacatonStata(StatesGroup):
    name = State()

    python_test = State()
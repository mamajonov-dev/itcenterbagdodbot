from aiogram.dispatcher.filters.state import State, StatesGroup

class Commentstate(StatesGroup):
    comment = State()
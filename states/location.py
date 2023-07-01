from aiogram.dispatcher.filters.state import State, StatesGroup


class Loaaction(StatesGroup):
    user_location = State()
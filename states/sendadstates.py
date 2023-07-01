from aiogram.dispatcher.filters.state import State, StatesGroup


class SendadState(StatesGroup):
    ad = State()
    resquest = State()

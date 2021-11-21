import typing

from repository.interfaces import ICardRepository, IMemoryStorage
from domain.entities.card import Card
from domain.value_objects.card import PAN


class MemoryCardRepository(ICardRepository, IMemoryStorage):
    def get_card_by_pan(self, pan: PAN):
        return self._get(pan)

    def get_cards(self):
        return self._get_all()

    def insert_card(self, card: Card):
        if not self._get(card.pan):
            self._put(card.pan, card)
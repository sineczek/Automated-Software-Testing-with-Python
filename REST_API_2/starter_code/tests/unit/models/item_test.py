# from unittest import TestCase # najlepsze rozwiązanie usunąc to, dodać unit_base_test.py i
from tests.unit.unit_base_test import UnitBaseTest # i dodać do class
from models.item import ItemModel
# from models.store import StoreModel #dzięki temu testy przejdą, ale jest to nieużywany import ... lepiej
# from tests.base_test import BaseTest # ale trzeba zmienić dziedziczenie w class i trwa dużo dłużej wszystko (10 razy)


class ItemTest(UnitBaseTest):
    def test_create_item(self):
        item = ItemModel('test',
                         19.99,
                         1)  # na końcu możemy dodać nr sklepu, np. 1 i wówczas przejdzie test, choć sklepu nie mamy to przez użycie do stestów sqlite
        # na innych bazach będzie ERROR
        self.assertEqual(item.name, 'test',
                         "The name of the item after creation does not equal the constructor argument.")
        self.assertEqual(item.price, 19.99,
                         "The price of the item after creation does not equal the constructor argument.")
        self.assertEqual(item.store_id, 1)
        self.assertIsNone(item.store)

    def test_item_json(self):
        item = ItemModel('test', 19.99, 1)
        expected = {
            'name': 'test',
            'price': 19.99
        }

        self.assertEqual(
            item.json(),
            expected,
            "The JSON export of the item is incorrect. Received {}, expected {}.".format(item.json(), expected))

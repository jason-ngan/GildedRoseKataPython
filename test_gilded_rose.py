# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_normal_item(self):
        item_name = "Poison Dagger"
        items = [Item(item_name, 10, 10), Item(item_name, 0, 5), Item(item_name, 5, 0)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(9, items[0].quality)
        self.assertEqual(0, items[1].sell_in)
        self.assertEqual(3, items[1].quality)
        self.assertEqual(4, items[2].sell_in)
        self.assertEqual(0, items[2].quality)

    def test_aged_brie(self):
        item_name = "Aged Brie"
        items = [Item(item_name, 5, 15), Item(item_name, 0, 10), Item(item_name, 4, 50)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(16, items[0].quality)
        self.assertEqual(0, items[1].sell_in)
        self.assertEqual(12, items[1].quality)
        self.assertEqual(3, items[2].sell_in)
        self.assertEqual(50, items[2].quality)

    def test_sulfuras(self):
        item_name = "Sulfuras, Hand of Ragnaros"
        items = [Item(item_name, 5, 80), Item(item_name, 0, 80)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(5, items[0].sell_in)
        self.assertEqual(80, items[0].quality)
        self.assertEqual(0, items[1].sell_in)
        self.assertEqual(80, items[1].quality)
    
    def test_backstage_passes(self):
        item_name = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(item_name, 20, 20), Item(item_name, 9, 10), Item(item_name, 1, 15), Item(item_name, 0, 33)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(19, items[0].sell_in)
        self.assertEqual(21, items[0].quality)
        self.assertEqual(8, items[1].sell_in)
        self.assertEqual(12, items[1].quality)
        self.assertEqual(0, items[2].sell_in)
        self.assertEqual(18, items[2].quality)
        self.assertEqual(0, items[3].sell_in)
        self.assertEqual(0, items[3].quality)

    def test_conjured_item(self):
        item_name = "Conjured Mana Cake"
        items = [Item(item_name, 5, 20), Item(item_name, 0, 30), Item(item_name, 5, 0)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(18, items[0].quality)
        self.assertEqual(0, items[1].sell_in)
        self.assertEqual(26, items[1].quality)
        self.assertEqual(4, items[2].sell_in)
        self.assertEqual(0, items[2].quality)


if __name__ == '__main__':
    unittest.main()

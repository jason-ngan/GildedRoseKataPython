# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        """Updates the quality of every item in the system"""
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            elif item.name == "Aged Brie":
                self.update_aged_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.update_backstage_passes(item)
            elif item.name.startswith("Conjured"):
                self.update_conjured_item(item)
            else:
                self.update_normal_item(item)
        
            self.adjust_quality(item)
            self.adjust_sell_in_date(item)
    
    def check_sell_in_date(self, item):
        """Checks if the sell in date is greater than 0"""
        return item.sell_in > 0
    
    def adjust_quality(self, item):
        """Adjusts the quality of the item so it is within specified bounds"""
        item.quality = max(0, min(50, item.quality))
    
    def adjust_sell_in_date(self, item):
        """Adjusts the sell in date of the item so it is within specified bounds"""
        item.sell_in = max(0, item.sell_in - 1)
    
    def update_normal_item(self, item):
        """Updates the quality of a normal item"""
        if self.check_sell_in_date(item):
            item.quality -= 1
        else:
            item.quality -= 2

    def update_aged_brie(self, item):
        """Updates the quality of an Aged Brie item"""
        if self.check_sell_in_date(item):
            item.quality += 1
        else:
            item.quality += 2

    def update_backstage_passes(self, item):
        """Updates the quality of a Backstage Pass item"""
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in <= 5:
            item.quality += 3
        elif item.sell_in <= 10:
            item.quality += 2
        else:
            item.quality += 1
    
    def update_conjured_item(self, item):
        """Updates the quality of a Conjured item"""
        if self.check_sell_in_date(item):
            item.quality -= 2
        else:
            item.quality -= 4

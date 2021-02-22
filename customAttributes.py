from libs.attributes import AbstractAttributesWidgets
import os
import shutil

import functools

class AttributesManager( AbstractAttributesWidgets ):

    # used to implement the "natural order" of the various attributes definitions
    global_index = 0
    def next_index( self ):
        self.global_index = self.global_index + 1
        return self.global_index

    # just capture the destination
    #def update_destination( self, destination ):
    #    self.destination = destination
    #    return True     

    # same action in all cases from AttributesWidgets
    def get_label_attribute_definitions( self ):
        items = {
            'numbers': 'Does the image contain numbers?',
            'letters': 'Does the image contain Latin letters?',
            'symbols': 'Does the image contain math symbols (including Greek letters and punctuation marks)?',
            'lines'  : 'Does the image contain any lines?',
            'arrows' : 'Does the image contain any arrows?',
            'points' : 'Does the image contain any points?',
            'colors' : 'Does the image contain colors?',
            'fills'  : 'Does the image contain any graytoned, filled or shaded areas?',
            'caption': 'Is the image captioned (with or without a caption text)?'
        }
        result = {}
        for i in items.keys():
            result[i] = {
                "order": self.next_index(),
                "tooltip": items[i],
                "default": "no",
                "type": "checkbox",
                "action": functools.partial(self.update_label_attribute, i)
            }
        return result
        
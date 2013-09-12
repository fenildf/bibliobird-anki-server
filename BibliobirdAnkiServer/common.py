
class CollectionInitializer(object):
    def _setup_model(self, col, did):
        """Create the 'External' model used by Bibliobird.com."""
        mm = col.models

        # NOTE: Supposedly, Anki will check the first field on any model
        # for uniqueness. Since it's really important to us that the 'External ID'
        # is unique, we're giving that one first!

        m = mm.new('External')
        m['did'] = did
        for field_name in ['External ID', 'Front', 'Back']:
            fm = mm.newField(field_name)
            mm.addField(m, fm)

        t = mm.newTemplate('Forward')
        t['qfmt'] = '{{Front}}'
        t['afmt'] = '{{FrontSide}}\n\n<hr id=answer>\n\n{{Back}}'
        mm.addTemplate(m, t)

        t = mm.newTemplate('Reverse')
        t['qfmt'] = '{{Back}}'
        t['afmt'] = '{{FrontSide}}\n\n<hr id=answer>\n\n{{Front}}'
        mm.addTemplate(m, t)

        mm.add(m)
    
    def _setup_deck(self, col):
        """Create the 'bibliobird' deck so we can keep our cards seperate."""
        did = col.decks.id('bibliobird', create=True)
        col.decks.flush()
        return did
    
    def __call__(self, col):
        did = self._setup_deck(col)
        self._setup_model(col, did)


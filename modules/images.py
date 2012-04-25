# coding: utf-8

from gluon import current
# current.session, request, cache
# db.commit(), db.rollback()
# from gluon.dal import Field
# from gluon.html import DIV
# from gluon.sqlhtml import SQLFORM

def THUMBER(image, nx=120, ny=120, name='thumb'):
    if image:
        try:
            request = current.request
            from PIL import Image
            import os
            img = Image.open(request.folder + 'uploads/' + image)
            img.thumbnail((nx, ny), Image.ANTIALIAS)
            root, ext = os.path.splitext(image)
            thumb = '%s_%s%s' % (root, name, ext)
            img.save(request.folder + 'uploads/' + thumb)
            return thumb
        except Exception:
            return image

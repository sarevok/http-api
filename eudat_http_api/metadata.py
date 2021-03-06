# -*- coding: utf-8 -*-

from __future__ import with_statement

from eudat_http_api import app
from eudat_http_api import storage


def stat(identifier, user_metadata=None):
    app.logger.debug('called the metadata service')
    return storage.stat(identifier, user_metadata)


def get_user_metadata(identifier, user_metadata=None):
    return storage.get_user_metadata(identifier, user_metadata)


def set_user_metadata(identifier, user_metadata):
    return storage.set_user_metadata(identifier, user_metadata)

# -*- coding: utf-8 -*-

from .context import skeleton

import pytest

def test_thoughts():
    assert isinstance(skeleton.hmm(), str)


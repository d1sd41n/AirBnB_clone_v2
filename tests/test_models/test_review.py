#!/usr/bin/python3
"""test_review"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import pep8


class test_review(test_basemodel):
    """test_review"""

    def test_Review_pep8(self):
        """ tests pep8 compliance """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/review.py'])
        self.assertEqual(result.total_errors, 0)

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    # def test_place_id(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.place_id), str)

    # def test_user_id(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.user_id), str)

    # def test_text(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.text), str)

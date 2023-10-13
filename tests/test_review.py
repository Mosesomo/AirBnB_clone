import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_place_id_initialization(self):
        review = Review()
        self.assertEqual(review.place_id, "")

    def test_user_id_initialization(self):
        review = Review()
        self.assertEqual(review.user_id, "")

    def test_text_initialization(self):
        review = Review()
        self.assertEqual(review.text, "")


if __name__ == "__main__":
    unittest.main()

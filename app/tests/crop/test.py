from unittest.mock import patch

from django.test import RequestFactory, TestCase

from ...backend.crop.crop import crop_list


class CropListViewMockTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @patch("app.backend.crop.crop.Crop.objects.all")
    def test_crop_list_view_with_mocked_queryset(self, mock_all):
        class MockCrop:
            def __init__(self, name):
                self.name = name
                self.id = 1
                self.planting_date = "2023-04-01"
                self.harvest_date = "2023-09-01"
                self.yield_estimate = "1000kg"

        mock_crop1 = MockCrop("Wheat")
        mock_crop2 = MockCrop("Corn")

        mock_all.return_value = [mock_crop1, mock_crop2]

        request = self.factory.get("/crops/")
        response = crop_list(request)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Wheat", response.content)
        self.assertIn(b"Corn", response.content)

        mock_all.assert_called_once()

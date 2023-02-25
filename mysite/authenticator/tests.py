from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from io import BytesIO
from PIL import Image
from .models import UserFile

class AlgorithmTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_run_algorithm_with_file_upload(self):
        image = Image.new('RGBA', size=(50, 50), color=(155, 0, 0))
        file = BytesIO()
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)

        data = {'file': file}
        response = self.client.post('/run_algorithm/', data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # check that the file was uploaded and associated with the user
        user_files = UserFile.objects.filter(user=self.user)
        self.assertEqual(user_files.count(), 1)
        self.assertEqual(user_files.first().file.name, 'user_uploads/test.png')

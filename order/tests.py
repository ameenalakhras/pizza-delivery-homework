from rest_framework.test import APITestCase
from django.urls import reverse

from authentication.models import User
from order.models import Order


class OrderTestCase(APITestCase):
    url = reverse("order:order_obj", kwargs={'pk': 1})

    def setUp(self):
        self.username = "ameen"
        self.email = "ameen@gmail.com"
        self.password = "strongPassword12$@"
        self.user, _ = User.objects.get_or_create(
            username=self.username,
            email=self.email,
            password=self.password
        )

        self.order, _ = Order.objects.get_or_create(
            user=self.user,
            status=1
        )

    def test_valid_get_request(self):

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

        response_data = response.data
        obj_data = Order.objects.get(id=self.order.id).__dict__
        self.assertEqual(obj_data['id'], response_data['id'])
        self.assertEqual(obj_data['status'], response_data['status'])
        self.assertEqual(obj_data['user_id'], response_data['user'])

    def test_invalid_get_request(self):
        url = reverse("order:order_obj", kwargs={'pk': 13930})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_valid_delete_request(self):
        """test deleting an object"""
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 204)
        order_obj_exists = Order.objects.filter(id=self.order.id).exists()
        self.assertEqual(order_obj_exists, False)

    def test_valid_edit_request(self):
        """test editing an object with patch"""
        data = {
            "status": 2
        }
        response = self.client.patch(self.url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], data['status'])
        order_obj = Order.objects.get(id=self.order.id)
        self.assertEqual(order_obj.status, 2)

    def test_invalid_edit_request(self):
        """test invalid request when the status is delivered"""
        # 4: the id when the status is delivered
        initial_status = 4
        self.order, _ = Order.objects.get_or_create(
            user=self.user,
            status=initial_status
        )

        url = reverse("order:order_obj", kwargs={'pk': self.order.id})
        data = {
            "status": 2
        }

        response = self.client.patch(url, data=data)
        # unprocessable unit
        self.assertEqual(response.status_code, 422)
        order_obj = Order.objects.get(id=self.order.id)
        # the status didn't change
        self.assertEqual(order_obj.status, initial_status)

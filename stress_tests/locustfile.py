from locust import HttpUser, task, between
import random
import os
from faker import Faker

fake = Faker()

class EcommerceUser(HttpUser):
    wait_time = between(2, 5)

    user_id = None
    product_id = None
    order_id = None

    USERS_URL = os.getenv("USER_SERVICE_URL", "http://users:8001")
    PRODUCTS_URL = os.getenv("PRODUCT_SERVICE_URL", "http://products:8002")
    ORDERS_URL = os.getenv("ORDER_SERVICE_URL", "http://orders:8003")

    def on_start(self):
        try:
            name = fake.first_name()
            email = fake.email()
            response = self.client.post(f"{self.USERS_URL}/users", json={"name": name, "email": email})
            if response.status_code in (200, 201):
                self.user_id = response.json().get("id")
            else:
                print(f"Failed to create user: Status {response.status_code}")

            name = fake.word().capitalize()
            price = round(random.uniform(10.0, 100.0), 2)
            quantity = random.randint(1, 100)
            response = self.client.post(
                f"{self.PRODUCTS_URL}/products",
                json={"name": name, "price": price, "quantity": quantity}
            )
            if response.status_code in (200, 201):
                self.product_id = response.json().get("id")
            else:
                print(f"Failed to create product: Status {response.status_code}")

        except Exception as e:
            print(f"Exception during on_start: {e}")

    @task(4)
    def create_order(self):
        if self.user_id and self.product_id:
            try:
                response = self.client.post(
                    f"{self.ORDERS_URL}/orders",
                    json={"user_id": self.user_id, "product_id": self.product_id}
                )
                if response.status_code in (200, 201):
                    self.order_id = response.json().get("id")
                else:
                    print(f"Failed to create order: Status {response.status_code}")
            except Exception as e:
                print(f"Exception during create_order: {e}")

    @task(2)
    def list_orders(self):
        try:
            self.client.get(f"{self.ORDERS_URL}/orders")
        except Exception as e:
            print(f"Exception during list_orders: {e}")

    @task(1)
    def list_users(self):
        try:
            self.client.get(f"{self.USERS_URL}/users")
        except Exception as e:
            print(f"Exception during list_users: {e}")

    @task(1)
    def list_products(self):
        try:
            self.client.get(f"{self.PRODUCTS_URL}/products")
        except Exception as e:
            print(f"Exception during list_products: {e}")

    @task(1)
    def create_user(self):
        try:
            name = fake.first_name()
            email = fake.email()
            response = self.client.post(f"{self.USERS_URL}/users", json={"name": name, "email": email})
            if response.status_code not in (200, 201):
                print(f"Failed to create user: Status {response.status_code}")
        except Exception as e:
            print(f"Exception during create_user: {e}")

    @task(1)
    def create_product(self):
        try:
            name = fake.word().capitalize()
            price = round(random.uniform(10.0, 100.0), 2)
            quantity = random.randint(1, 100)
            response = self.client.post(
                f"{self.PRODUCTS_URL}/products",
                json={"name": name, "price": price, "quantity": quantity}
            )
            if response.status_code not in (200, 201):
                print(f"Failed to create product: Status {response.status_code}")
        except Exception as e:
            print(f"Exception during create_product: {e}")






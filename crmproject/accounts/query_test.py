
from pathlib import Path

print(Path.cwd())

from accounts.models import Customer, Product, Order, Tag

customers = Customer.objects.all()
print(customers.first())

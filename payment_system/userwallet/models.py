# wallet/models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    wallet_balance = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coins = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name}: {self.coins} coins at {self.timestamp}"

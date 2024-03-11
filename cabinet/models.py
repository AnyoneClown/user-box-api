from django.db import models

from user.models import User


class Box(models.Model):
    class DistributionTypeChoices(models.TextChoices):
        RANDOM = "Random"
        UNIFORM = "Uniform"

    name = models.CharField(max_length=50)
    description = models.TextField()
    amount = models.IntegerField()
    attempts = models.IntegerField()
    distribution_type = models.CharField(choices=DistributionTypeChoices.choices, max_length=20)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    current_attempts = models.IntegerField(null=True, blank=True)
    status = models.BooleanField()

    class Meta:
        ordering = ["name"]
        verbose_name = "Box"
        verbose_name_plural = "Boxes"
        app_label = "cabinet"
        db_table = "boxes"

    def __str__(self) -> str:
        return self.name


class UserBox(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userboxes")
    box = models.ForeignKey(Box, on_delete=models.CASCADE, related_name="userboxes")
    status = models.BooleanField()

    class Meta:
        ordering = ["status"]
        verbose_name = "User box"
        verbose_name_plural = "User boxes"
        app_label = "cabinet"
        db_table = "userboxes"

    def __str__(self) -> str:
        return f"User: {self.user.full_name}, box: {self.box.name}, status: {self.status}"


class Coin(models.Model):
    name = models.CharField(max_length=50)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    status = models.BooleanField()

    class Meta:
        ordering = ["name"]
        verbose_name = "Coin"
        verbose_name_plural = "Coins"
        app_label = "cabinet"
        db_table = "coins"

    def __str__(self) -> str:
        return f"Coin: {self.name}, rate: {self.rate}, quantity: {self.quantity}"


class Notification(models.Model):
    text = models.TextField()

    class Meta:
        ordering = ["text"]
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
        app_label = "cabinet"
        db_table = "notifications"

    def __str__(self) -> str:
        return self.text


class UserNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usernotifications")
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE, related_name="usernotifications")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["user"]
        verbose_name = "User notification"
        verbose_name_plural = "User notifications"
        app_label = "cabinet"
        db_table = "usernotification"

    def __str__(self) -> str:
        return f"User: {self.user.full_name} notification: {self.notification.text}, date: {self.date}"


class UserBalance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userbalances")
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name="userbalances")
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ["user"]
        verbose_name = "User balance"
        verbose_name_plural = "User balances"
        app_label = "cabinet"
        db_table = "userbalance"

    def __str__(self) -> str:
        return f"User: {self.user.full_name}, Coin: {self.coin.name}, Balance: {self.balance}"


class Operation(models.Model):
    class StatusChoices(models.TextChoices):
        CREDITED = "Credited"
        DEBITED = "Debited"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="operations")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    operation_number = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    box = models.ForeignKey(Box, on_delete=models.CASCADE, related_name="operations")
    status = models.CharField(choices=StatusChoices.choices, max_length=50)

    class Meta:
        ordering = ["user"]
        verbose_name = "Operation"
        verbose_name_plural = "Operations"
        app_label = "cabinet"
        db_table = "operations"

    def __str__(self) -> str:
        return f"Operation: {self.operation_number}, Timestamp: {self.timestamp}, Box: {self.box.name}"

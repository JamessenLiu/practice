from django.db import models

# Create your models here.
from carts.models import Carts
from users.models import Users


class Orders(models.Model):
    uuid = models.CharField(max_length=200)
    create_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    user_id = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=20)

    def __str__(self):
        return {
            'uuid': self.uuid,
            'create_time': self.create_time,
            'end_time': self.end_time,
            'user_id': self.user_id_id,
            'status': self.status
        }

    class Meta:
        db_table = 'orders'

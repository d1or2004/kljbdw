from django.db import models


class Speciality(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='media/speciality/')
    last_updated = models.DateField(auto_now=True)
    create_data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class Course(models.Model):
    class PriceTypes(models.TextChoices):
        s = "$", "USD"
        sum = "So'm", "UZS"

    title = models.CharField(max_length=30)
    description = models.TextField()
    active_users = models.PositiveIntegerField(default=0)
    price = models.FloatField()
    price_type = models.CharField(max_length=30, choices=PriceTypes.choices, default=PriceTypes.sum)
    image = models.ImageField(upload_to='media/course/')
    reyting = models.FloatField()
    speciality = models.ManyToManyField(Speciality)
    last_updated = models.DateField(auto_now=True)
    create_data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class Position(models.Model):
    name = models.CharField(max_length=20)
    last_updated = models.DateField(auto_now=True)
    create_data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media/teacher/')
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    x_link = models.URLField(null=True, blank=False)
    m_link = models.URLField(null=True, blank=False)
    l_link = models.URLField(null=True, blank=False)
    last_updated = models.DateField(auto_now=True)
    create_data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

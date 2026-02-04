from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    genre = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True, default="0000000000000")

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return f"Review for {self.book.title} by {self.user_name}"

from .models import Author, Book, Review
import random
from datetime import datetime, timedelta

def create_test_data():
    authors = []
    for i in range(10):
        authors.append(Author.objects.create(name=f"Author {i+1}", bio=f"Bio for Author {i+1}"))

    books = []
    for i in range(50):
        author = random.choice(authors)
        books.append(Book.objects.create(
            title=f"Book {i+1}",
            author=author,
            published_date=datetime.now() - timedelta(days=random.randint(1, 1000))
        ))

    for book in books:
        for _ in range(random.randint(1, 5)):
            Review.objects.create(
                book=book,
                content=f"Review for {book.title}",
                rating=random.randint(1, 5)
            )

    print("Test data created successfully.")
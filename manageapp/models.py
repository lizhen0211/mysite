from django.db import models


# Create your models here.

class Person(models.Model):
    people = models.Manager()


class PollManager(models.Manager):
    def with_counts(self):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT p.id, p.question, p.poll_date, COUNT(*)
                FROM manageapp_opinionpoll p, manageapp_response r
                WHERE p.id = r.poll_id
                GROUP BY p.id, p.question, p.poll_date
                ORDER BY p.poll_date DESC""")

            result_list = []
            for row in cursor.fetchall():
                p = self.model(id=row[0], question=row[1], poll_date=row[2])
                p.num_responses = row[3]
                result_list.append(p)
        return result_list


class OpinionPoll(models.Model):
    question = models.CharField(max_length=200)
    poll_date = models.DateField(auto_now=True)
    objects = PollManager()


class Response(models.Model):
    poll = models.ForeignKey(OpinionPoll, on_delete=models.CASCADE)
    person_name = models.CharField(max_length=50)
    response = models.TextField()


class DahlBookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(author='Roald Dahl')


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    objects = models.Manager()
    dahl_objects = DahlBookManager()


class AuthorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role='A')

class EditorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role='B')


class APersonA(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=1, choices=(('A', 'Author'), ('E', 'Editor')), default='A')
    people = models.Manager()
    authors = AuthorManager()
    editors = EditorManager()

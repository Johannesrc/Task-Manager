import uuid
from datetime import datetime


class Task:

    def __init__(self, title, category, description, responsible, priority, estimated_time, due_date, notes) -> None:
        self._task_id = self._assign_id()
        self._title = title
        self._category = category
        self._description = description
        self._responsible = responsible
        self._priority = priority
        self._estimated_time = estimated_time
        self._due_date = due_date
        self._notes = notes
        self._creation_date = datetime.now()
        self._completed = False

    def _assign_id(self):
        return uuid.uuid4()

    def mark_completed(self):
        self._completed = not self._completed

    def __str__(self) -> str:
        status = "Completed" if self._completed else "Pending"
        return f"{self._title} - {self._description} ({status})"

    @property
    def task_id(self):
        return self._task_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def responsible(self):
        return self._responsible

    @responsible.setter
    def responsible(self, value):
        self._responsible = value

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value

    @property
    def estimated_time(self):
        return self._estimated_time

    @estimated_time.setter
    def estimated_time(self, value):
        self._estimated_time = value

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        self._due_date = value

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, value):
        self._notes = value

    @property
    def creation_date(self):
        return self._creation_date

    @property
    def completed(self):
        return self._completed

    @completed.setter
    def completed(self, value):
        self._completed = value

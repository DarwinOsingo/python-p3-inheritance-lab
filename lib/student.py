#!/usr/bin/env python

# lib/student.py

from lib.user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []

    def learn(self, string):
        self.knowledge.append(string)

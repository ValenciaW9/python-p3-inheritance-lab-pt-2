#!/usr/bin/envpython3
import io
import sys

class Student:
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        print("Pick me!")


class ChattyStudent(Student):
    def hello(self):
        super().hello()
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay, well let me just tell you who died...")

    def raise_hand(self):
        for i in range(10):
            super().raise_hand()

class TestChattyStudent:
    def test_says_hello(self):
        '''says a brief greeting, then tries to spoil a TV show.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        chatty_student = ChattyStudent()
        chatty_student.hello()
        sys.stdout = sys.__stdout__
        expected_output = "Hey there! I'm so excited to learn stuff.\n" \
            "How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay, well let me just tell you who died..."
        assert captured_out.getvalue().strip() == expected_output

    def test_raise_hand(self):
        '''respectfully tries to get the teacher's attention ten times.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        chatty_student = ChattyStudent()
        chatty_student.raise_hand()
        sys.stdout = sys.__stdout__
        expected_output = "Pick me!\n" * 10
        assert captured_out.getvalue() == expected_output
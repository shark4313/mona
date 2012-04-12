"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class GenerateMonthlyHistoryTest(TestCase):
    from django.conf import settings
    import subprocess

    path = settings.PROJECT_PATH
    
    def testItRunsAtFirstDayOfMonth(self):
        subprocess.call(['python', path+'/manage.py', 'generate_monthly_history'])
        pass
    
    def testItOperatesOnAllUserProfileRows(self):
        pass
    
    def testItResetsPaidAttributeInUserProfile(self):
        pass
    
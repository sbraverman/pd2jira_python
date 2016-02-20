import json
import unittest
from mock import MagicMock
from pd2jira_python.Ticket import Ticket
import logging


class Ticket_Test(unittest.TestCase):

    def setUp(self):
        self.pd_webhook = self.get_data('pd_webhook.json')
        self.ticket = Ticket(self.pd_webhook, False) 

    def get_data(self, name):
        with open('tests/stubs/{0}'.format(name), 'r') as test_data:
            return json.load(test_data)
    
    def test_incident_number(self):
        self.assertEquals(self.ticket.get_incident_number(self.pd_webhook), 1)

    def test_get_summary(self):
        self.assertEquals(self.ticket.get_summary(self.pd_webhook), "45645")
        
    def test_pager_duty_link(self):
        self.assertEquals(self.ticket.get_pager_duty_link(self.pd_webhook), "https://acme.pagerduty.com/incidents/PIJ90N7")
        
    
if __name__ == '__main__':
    main()

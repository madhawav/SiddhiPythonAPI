import unittest
from multiprocessing import Lock
from time import sleep

import logging

from SiddhiCEP4.DataTypes.LongType import LongType
from SiddhiCEP4.core.SiddhiManager import SiddhiManager
from SiddhiCEP4.core.event.Event import Event
from SiddhiCEP4.core.query.output.callback.QueryCallback import QueryCallback
from SiddhiCEP4.core.util.EventPrinter import PrintEvent


class BasicTests(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.INFO)

    def test_data(self):
        logging.info("Test GetData and SetData Methods")

        event = Event(1, [2, LongType(3)])
        self.assertListEqual(event.getData(),[2,LongType(3)],"GetData not equal to data given in constructor")
        logging.info(type(event.getData(1)))
        self.assertTrue(type(event.getData(1)) == LongType,"Type of Parameter is not LongType")

        event.setData([1, 2])
        self.assertListEqual(event.getData(), [1,2], "GetData not equal to data set by SetData")

    def test_copyFromAndToString(self):
        logging.info("Test CopyFrom and ToString methods")

        event = Event(1, [2, LongType(3)])
        event2 = Event(2)
        event2.copyFrom(event)

        self.assertEqual(str(event),str(event2),"ToString forms of copy is not equal")

    def test_Equals(self):
        logging.info("Test CopyFrom and ToString methods")

        event = Event(1, [2, LongType(3)])
        event2 = Event(1,[2, LongType(3)])

        self.assertEqual(event,event2,"Copy is not equal")

        event2 = Event(1,[2,3])
        self.assertNotEqual(event,event2,"Should not be equal due to Type diference")



if __name__ == '__main__':
    unittest.main()
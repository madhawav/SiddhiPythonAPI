import unittest
import logging
from distutils import log
from time import sleep
from unittest.case import TestCase

from SiddhiCEP4.core.SiddhiManager import SiddhiManager
from SiddhiCEP4.core.debugger.SiddhiDebugger import SiddhiDebugger
from SiddhiCEP4.core.debugger.SiddhiDebuggerCallback import SiddhiDebuggerCallback
from SiddhiCEP4.core.stream.output.StreamCallback import StreamCallback
from Tests.Util.AtomicInt import AtomicInt


class TestDebugger(TestCase):
    def setUp(self):
        self.inEventCount = AtomicInt(0)
        self.debugEventCount = AtomicInt(0)
        logging.basicConfig(level=logging.INFO)

    def getCount(self, event):
        count = 0
        while event != None:
            count += 1
            event = event.getNext()

        return count

    def test_outputstram(self):
        siddhiManager = SiddhiManager()
        cseEventStream = "@config(async = 'true') define stream cseEventStream (symbol string, price float, volume int);"

        query = "@info(name = 'query 1') from cseEventStream select symbol, price, volume insert into OutputStream; "

        executionPlanRuntime = siddhiManager.createExecutionPlanRuntime(cseEventStream + query)

        _self_shaddow = self

        class StreamCallbackImpl(StreamCallback):
            def receive(self, events):
                _self_shaddow.inEventCount.addAndGet(len(events))

        executionPlanRuntime.addCallback("OutputStream", StreamCallbackImpl())

        inputHandler = executionPlanRuntime.getInputHandler("cseEventStream")

        inputHandler.send(["WSO2", 50.0, 60])
        inputHandler.send(["WSO2", 70.0, 40])
        inputHandler.send(["WSO2", 50.0, 60])
        inputHandler.send(["WSO2", 70.0, 40])
        inputHandler.send(["WSO2", 50.0, 60])
        inputHandler.send(["WSO2", 70.0, 40])
        inputHandler.send(["WSO2", 50.0, 60])
        inputHandler.send(["WSO2", 70.0, 40])
        inputHandler.send(["WSO2", 50.0, 60])
        inputHandler.send(["WSO2", 50.0, 60])
        inputHandler.send(["WSO2", 70.0, 40])
        inputHandler.send(["WSO2", 50.0, 60])
        inputHandler.send(["WSO2", 50.0, 60])
        inputHandler.send(["WSO2", 70.0, 40])
        inputHandler.send(["WSO2", 50.0, 60])
        inputHandler.send(["WSO2", 50.0, 60])
        inputHandler.send(["WSO2", 70.0, 40])
        inputHandler.send(["WSO2", 50.0, 60])
        inputHandler.send(["WSO2", 50.0, 60])
        inputHandler.send(["WSO2", 70.0, 40])
        inputHandler.send(["WSO2", 50.0, 60])
        inputHandler.send(["WSO2", 50.0, 60])
        inputHandler.send(["WSO2", 70.0, 40])
        inputHandler.send(["WSO2", 50.0, 60])
        inputHandler.send(["WSO2", 50.0, 60])
        inputHandler.send(["WSO2", 70.0, 40])
        inputHandler.send(["WSO2", 50.0, 60])
        inputHandler.send(["WSO2", 50.0, 60])
        inputHandler.send(["WSO2", 70.0, 40])
        inputHandler.send(["WSO2", 50.0, 60])
        inputHandler.send(["WSO2", 50.0, 60])
        inputHandler.send(["WSO2", 70.0, 40])
        inputHandler.send(["WSO2", 50.0, 60])
        inputHandler.send(["WSO2", 70.0, 40])
        inputHandler.send(["WSO2", 50.0, 60])
        inputHandler.send(["WSO2", 70.0, 40])

        sleep(1)

        _self_shaddow.assertEquals(36, _self_shaddow.inEventCount.get(), "Invalid number of output events")


        executionPlanRuntime.shutdown()
if __name__ == '__main__':
    unittest.main()
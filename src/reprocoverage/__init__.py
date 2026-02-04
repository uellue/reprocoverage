import numpy as np

from libertem.api import Context
from libertem.udf.base import NoOpUDF


def dothething1():
    ctx1 = Context.make_with("inline")
    data = np.zeros((2, 3, 4, 5))
    ds = ctx1.load("memory", data=data)
    ctx1.run_udf(dataset=ds, udf=NoOpUDF())
    
def dothething2():
    ctx2 = Context()
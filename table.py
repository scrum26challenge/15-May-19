import datetime
import time
import numpy as np
import pandas as pd

def timestamp():
    dt1 = datetime.datetime(2019,1,11,3)
    dt2 = datetime.datetime(2019,1,15,6)

    ut1 = time.mktime(dt1.timetuple())
    ut2 = time.mktime(dt2.timetuple())

    times = np.arange(ut1,ut2,1)

    data = {'Time': times}

    df = pd.DataFrame(data)

    return df

def random():
    pass

def normal():
    pass

def hash_algo():
    pass

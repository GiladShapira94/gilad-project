import pandas as pd
import mlrun
from mlrun import MLClientCtx
import time
def data_fetch(context:MLClientCtx):
    time.sleep(40)
    df = pd.DataFrame(data={"col":[1,2,3,4]})
    context.log_dataset(key='df_version_1',df=df,format='csv')

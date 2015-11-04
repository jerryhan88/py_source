import numpy as np
import pandas as pd

def main():
    do_exercise()

def do_exercise():
    # 1
    
    # 2
    aapl_bars = pd.read_csv("./AAPL.csv")
    
    # 3
    date_index = aapl_bars.pop('Date')
    aapl_bars.index = pd.to_datetime(date_index)
    
    #4
    #print(aapl_bars.columns.values)
    for s in aapl_bars.columns.values:
        if s not in ['Open', 'Close', 'Volume']:
            aapl_bars.pop(s)
    df = aapl_bars
    
            
    # print(aapl_bars[:]['1989'])
    #ts1 = pd.Series(np.random.randn(10), index=pd.date_range('1/1/2000', periods=10))
    #print (ts1)
    #ts2 = ts1[[0, 2, 4, 5, 6, 7, 8]]
    #print (ts2)
    #print(ts1 + ts2)
    
    #twoseries_dict = {'A': ts1, 'B': ts2}
    #df = pd.DataFrame(twoseries_dict)
    #print(df)
    #print(df.count())
    #df.dropna()
    #df.fillna(0)
    #print(df.fillna(method='ffill'))
    #df = None
    

    # 3

    # 4
    return df[:]['1989':'2003-04']

if __name__ == "__main__":
    main()
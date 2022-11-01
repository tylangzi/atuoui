import pandas as pd
def handle():
    df=pd.read_csv('data.csv',names=["测试日期","时间段","分支名", "commit", "车辆", "triager", "tag", "xray链接", "模块名",
                                   "所在等级"])
    df.drop_duplicates()
    df = df.groupby(["测试日期","时间段","分支名","所在等级","模块名","车辆","tag"])

    print(df.describe())

if __name__ == '__main__':
    handle()
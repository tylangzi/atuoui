import pandas as pd
def handle():
    df=pd.read_csv('data_1212.csv',names=["triager","分支名","commit","测试日期","模块名","描述信息","tag","所在等级","xray链接","时间段", "车辆"])
    df.drop_duplicates()
    df.to_excel('data_1212.xlsx')
    # df1 = df.groupby(["分支名", "所在等级", "模块名", "车辆", "tag"]).agg({'tag': 'count'}).rename(columns={'tag': '个数'})
    # df = df.groupby(["测试日期","时间段","分支名","所在等级","模块名","车辆","tag","xray链接"])
    # df1.to_excel('data_1121.xlsx')
    # print(df1)
    # print(df1.groupby("所在等级").groups)
    # for group in df1.groupby("所在等级").groups:
    #     print(group)


def ribao():
    df = pd.read_csv('data_1212.csv',
                     names=["triager", "分支名", "commit", "测试日期", "描述信息", "tag", "xray链接", "时间段", "所在等级", "车辆"
                         , "模块名"])
    df.drop_duplicates()
    df1 = df.groupby(["分支名", "所在等级", "模块名", "车辆", "tag"]).agg({'tag': 'count'}).rename(columns={'tag': '个数'})
    df = df.groupby(["测试日期","时间段","分支名","所在等级","模块名","车辆","tag","xray链接"])
    df1.to_excel('data_1212.xlsx')
    print(df1)



if __name__ == '__main__':
    handle()
    # ribao()
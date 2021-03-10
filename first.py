import pandas as pd
import timeit
 
'''
2021. 03. 09 
pandas 이것저것
'''

def testSeries():
    # Series는 index와 values로 구성되어있음. 
    # index 설정을 따로 하지 않고 만들면 0부터 자동 할당되고, values는 입력한 대로 생성됨.
    sr = pd.Series([1,2,3])
    print(sr)
    index = ['one','two','three']
    # values는 명시형변수가 아니네. values를 index 뒤에 넣어도 안된다 \
    # Series 생성자에서 values는 디폴트값이 설정안되어있고, index는 0부터 기본 설정되어 있기 때문에 
    # 디폴트 설정이 안되있는 변수가 먼저 순서대로 와야한다.
    sr = pd.Series( [1,2,3], index=index)
    print(sr)
    print(sr.index)
    print(sr.values)
    print('slicing Series!')
    # index로 슬라이싱도 되고
    print(sr['one':'two'])
    # 숫자로도 슬라이싱됨
    print(sr[0:2])
    start_time = timeit.default_timer() 
    print(sr['three'])
    end_time = timeit.default_timer() 
    print("%f sec" % (end_time - start_time))
# 특정 인덱스에 있는 값을 조회해올때 속도에서 차이가 있을까...? 
    li = [1,2,3]
    start_time = timeit.default_timer() 
    print(li[2])
    end_time = timeit.default_timer() 
    print("%f sec" % (end_time - start_time))
# 값이 작아서 그런가... 속도는 거의 비슷하게 왔다갔다하네.  
    values = []
    for i in range(1000000):
        values.append(i)
    print(len(values),'\n\n')

    start_time = timeit.default_timer() 
    print(values[412348])
    end_time = timeit.default_timer() 
    print("%f sec" % (end_time - start_time))

    sr = pd.Series(values)
    start_time = timeit.default_timer()
    end_time = timeit.default_timer() 
    print("%f sec" % (end_time - start_time))
# 100만개 넣은 obj에서는 시간차이가 매우 많이나네. 거의.. 25배 정도 차이났음.    

def testDataFrame():
# DataFrame은 2차원 배열임. Series가 values, index로 구성되어 있었다면
# DataFrame은 columns이 추가된 2차원 배열 형태를 말함. 
# index가 row num이 될것이고, columns가 col num이 될 것이다.    
    values = [[1,2,3],[4,5,6],[7,8,9]]
    index = ['r1','r2','r3']
    columns = ['c1','c2','c3']
    df = pd.DataFrame(values, index=index, columns=columns)
    print(df) 
# 그런데 index와 columns가 value와 shape이 맞지 않다면??? 당연히 에러나겠지? 
# ㅇㅇ ValueError: Shape of passed values is (3, 3), indices imply (3, 2) 
# 바로 shape 에러남.. 
    print(df.values)
    print(df.index)
    print(df.columns)

# DataFrame은 list나 dictionary가지고도 생성할 수 있음. 
# dicionary의 key가 column index가 되고 row index는 자동 생성됨. 
# row index를 따로 입력해줘도 반영됨
    dic = {'c1': [1,2,3], 'c2':[4,5,6], 'c3':[7,8,9]}
    df = pd.DataFrame(dic, index=['r1','r2','r3'])
    print(df)

if __name__ == "__main__":
    '''
    pandas는 Series, DataFrame, pannel 로 구성되어 있는 클래스임..
    Series는 1차원 배열과 같은 형태이고, DataFrame은 2차원 배열 pannel은 아직 못봄 
    파이썬의 기본 자료형인 list나 dictionary랑 pandas의 Series, DataFrame은 뭐가 다르길래 이렇게 좋다고 그러지?
 ->>> 일단... list와 Series의 가장 큰 차이점은 인덱싱을 할 수 있다는 점이다. 
list와 속성은 같기 때문에 내가 부여한 인덱스를 가지고 슬라이싱도 할 수 있음.
    '''
    #testSeries()

    testDataFrame()

    # 패널은 나중에 다시

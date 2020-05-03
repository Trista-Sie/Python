import multiprocessing as mp
import threading as td
import numpy as np
import concurrent.futures
from queue import Queue
import time


#用random.randint隨機產生亂數整數，並回傳
def random_matrix(m, n, low, high):
    
    return np.random.randint(low, high, size = (m, n))

#呼叫random_matrix隨機產生矩陣
def create_two_matrices(dim_1, dim_2, low, high):   

    A = random_matrix(dim_1, dim_2, low, high)

    B = random_matrix(dim_1, dim_2, low, high)

    print(f'Matrix A = \n {A} \n\nMatrix B = \n {B} \n')

    return (A, B)

def matrix_multiplication(A, B, result):

    #返回計時器的精準時間（系統的執行時間），包含整個系統的睡眠時間
    #由於返回值的基準點是未定義的，所以，只有連續調用的結果之間的差才是有效的。
    
    start = time.perf_counter()

    '''
    #
    # 傳統寫法一：使用迴圈
    #
    # iterating by row of A 
    for i in range(len(A)): 
  
        # iterating by coloum by B  
        for j in range(len(B[0])): 
  
            # iterating by rows of B 
            for k in range(len(B)): 

                result[i][j] += A[i][k] * B[k][j]

    #print(result)   
    '''
    
    #
    # 傳統寫法二：使用Comprehension
    #
    
    result += [[sum(a*b for a,b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]

    #print('\nordinary=\n', result)

    #for A_row in A:
        #for B_col in zip(*B):
            #for i,j in zip(A_row, B_col):
                #print('(A_row, B_col) =', i, j)

    end = time.perf_counter()
    
    return (result, end - start)

#-------------Multiprocessing
def do_processing(A,B,result):

    start = time.perf_counter()

    #取資料集
    #Datazip = [[(a,b) for a,b in zip(A_row, B_col)] for B_col in zip(*B) for A_row in A]

    #print('Datazip=\n', Datazip)


    #使用excutor計算矩陣答案
    with concurrent.futures.ProcessPoolExecutor() as executor:

        #for d in Datazip:
            
            #result = [sum(map(lambda a: a[0]*a[1], d)) for d in Datazip]

        result = [[sum(map(lambda a: a[0]*a[1], zip(A_row, B_col))) for B_col in zip(*B)] for A_row in A]

        result = np.array(result)

    end = time.perf_counter()

    #以計算時間差(end-start)取得multiprocessing的所需時間
    return(result, end - start)


#-------------Multithreading
def do_threading(A,B,result):

    q = Queue()

    start = time.perf_counter()

    #矩陣計算
    def job(A,B, q):

        result = [[sum(map(lambda a: a[0]*a[1], zip(A_row, B_col))) for B_col in zip(*B)] for A_row in A]

        #將陣列轉換成矩陣
        result = np.array(result)

        #回傳矩陣
        q.put(result)

    #使用multithreading建立多執行緒，將參數(A,B,q)傳入函式job
    t1 = td.Thread(target = job, args = (A,B,q))

    t1.start()

    #接收回傳值
    result = q.get()

    #print('result=', result)

    t1.join()

    end = time.perf_counter()

    #以計算時間差(end-start)取得multiprocessing的所需時間
    return(result, end - start)


if __name__ == '__main__':

    dim_1 = dim_2 = int(input('\n請輸入一個 n-by-n 正方矩陣的order n (1<n<8) : ')) 

    #輸入的整數範圍介於-10~30
    low = -10

    high = 30

    #將產生的矩陣指定給變數A,B
    A, B = create_two_matrices(dim_1, dim_2, low, high)

    #創建一個指定形狀以及用0填充的矩陣 zeros(shape, dtype=float, order='C')
    #order為代表行優先或列優先；F代表列優先
    result = np.zeros((dim_1, dim_2), dtype = int)

    print(f'Result = \n{result}')

    result1, elasped_time = matrix_multiplication(A, B, result)

    print('\n======================================================')
    print('\n矩陣相乘的方法一：使用傳統方法\n')
    print(f'Result = \n{result1}\n\n所需時間{elasped_time:.3}秒...')
    print('\n======================================================')

#================

    #Multi-processing
    #將result重置為0
    result = np.zeros((dim_1, dim_2), dtype = int)

    p_result, p_time = do_processing(A,B,result)

    print('\n======================================================')
    print('\n矩陣相乘的方法二：使用多程序方法\n')
    print(f'Result = \n{p_result}\n\n所需時間{p_time:.3}秒...')
    print('\n======================================================')

#================

    #Multi-threading
    #將result重置為0
    result = np.zeros((dim_1, dim_2), dtype = int)

    t_result, t_time = do_threading(A,B,result)

    print('\n======================================================')
    print('\n矩陣相乘的方法三：使用多執行緒方法\n')
    print(f'Result = \n{t_result}\n\n所需時間{t_time:.3}秒...')
    print('\n======================================================')

    input('\nPress enter key to exit...')

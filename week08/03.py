import time

def timer(fun):
    def ex(*args,**kwargs):
        start_time = time.time()
        res = fun(*args,**kwargs)
        endtime = (time.time() - start_time)
        print(f"{fun.__name__} 执行时间是 {endtime}")
        return res        
    return ex

@timer
def ex1(a, b):
    print(a + b)
    time.sleep(1)

def ex2(*args, **kwargs):
    print(args)
    print(kwargs)
    time.sleep(1)

if __name__ == '__main__':
   ex1(1,2)
   ex2(1, 'b', 'c',name = 'lanx')

import os

os.chdir('PZ11')

files = [f for f in os.listdir('.') if os.path.isfile(f)]

os.chdir('..')
os.mkdir('test')
os.mkdir('test/test1')

os.rename('PZ6/wewe.txt', 'test/wewe.txt')
os.rename('PZ6/wewew.txt', 'test/wewew.txt')
os.rename('PZ7/wwwww.txt', 'test/test1/wwwww.txt')
os.rename('test/test1/wwwww.txt', 'test/test1/test.txt')

for file in os.listdir('test'):
    if os.path.isfile(os.path.join('test', file)):
        print(f'{file}: {os.path.getsize(os.path.join("test", file))} bytes')

os.chdir('PZ11')
shortest_file = min(os.listdir('.'), key=len)
print(os.path.basename(shortest_file))

os.chdir('..')
os.chdir('PZ9')
os.startfile('ПЗ9 Отчёт.pdf')

os.chdir('..')
os.remove('test/test1/test.txt')

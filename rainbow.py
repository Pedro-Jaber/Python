from time import sleep
"""
       R G B
1      3 0 0
2      3 1 0
3      3 2 0
4      3 3 0
5      2 3 0
6      1 3 0
7      0 3 0
8      0 3 1
9      0 3 2
10     0 3 3
11     0 2 3
12     0 1 3
13     0 0 3
14     1 0 3
15     2 0 3
16     3 0 3
17     3 0 2
18     3 0 1
1     ~3 0 0~
"""

r = 255  # red
g = 0  # green
b = 0  # blue

passo = 51    # 51

var_range = 5 # 5

timer = 100 / 1000

text = "BOM DIA!"

while True:
    # 255 0 0
    for i in range(0,var_range):
        sleep(timer)
        print(f"\033[38;2;{r};{g};{b}m{text} \033[38;2;255;255;255m")
        g += passo

    # 255 255 0
    for i in range(0,var_range):
        sleep(timer)
        print(f"\033[38;2;{r};{g};{b}m{text} \033[38;2;255;255;255m")
        r -= passo

    # 0 255 0
    for i in range(0,var_range):
        sleep(timer)
        print(f"\033[38;2;{r};{g};{b}m{text} \033[38;2;255;255;255m")
        b += passo

    # 0 255 255
    for i in range(0,var_range):
        sleep(timer)
        print(f"\033[38;2;{r};{g};{b}m{text} \033[38;2;255;255;255m")
        g -= passo

    # 0 0 255
    for i in range(0,var_range):
        sleep(timer)
        print(f"\033[38;2;{r};{g};{b}m{text} \033[38;2;255;255;255m")
        r += passo

    # 255 0 255
    for i in range(0,var_range):
        sleep(timer)
        print(f"\033[38;2;{r};{g};{b}m{text} \033[38;2;255;255;255m")
        b -= passo
    # 255 0 0
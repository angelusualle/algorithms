def draw_line(arr, x1, x2, y):
    screen = build_screen(arr)
    line = screen[y]
    while x1 <= x2:
        line[x1] = 1
        x1 += 1
    for line in screen:
        print(line)

def print_screen(arr):
    for bytearr in arr:
        pixels = []
        for i, byte in enumerate(bytearr):
            while byte != 0:
                pixels.insert(0,(byte & 1))
                byte >>= 1
            while len(pixels) < 8*i:
                pixels.insert(0,0)
        print(pixels)     

def build_screen(arr):
    screen = []
    for bytearr in arr:
        pixels = []
        for i, byte in enumerate(bytearr):
            while byte != 0:
                pixels.insert(0,(byte & 1))
                byte >>= 1
            while len(pixels) < 8*i:
                pixels.insert(0,0)
        screen.insert(0,pixels)  
    return screen

draw_line([bytearray([1,2,3,4]), bytearray([5,6,7,8]), bytearray([9,10,11,12]), bytearray([13,14,15, 16])], 5, 10, 2)
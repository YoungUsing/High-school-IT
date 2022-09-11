import turtle


t = turtle.Turtle()


def get_midpoint(a, b):
    ax, ay = a
    bx, by = b
    return (ax + bx) / 2, (ay + by) / 2


def draw_triangle(a, b, c):
    ax, ay = a
    bx, by = b
    cx, cy = c

    t.penup()
    t.goto(ax, ay)
    t.pendown()
    t.goto(bx, by)
    t.goto(cx, cy)
    t.goto(ax, ay)
    t.penup()


def draw_sierpinski(triangle, depth):
    """
    :param triangle: 指定三角形三个顶点坐标，示例：((ax,ay),(bx,by),(cx,cy))。
    :param depth: 指定层数
    """
    a, b, c = triangle
    draw_triangle(a, b, c)
    if depth == 0:
        return
    else:
        d = get_midpoint(a, b)
        e = get_midpoint(b, c)
        f = get_midpoint(c, a)
        draw_sierpinski([a, d, f], depth-1) #左下三角形
        draw_sierpinski([d, b, e], depth-1) #三角形
        draw_sierpinski([f, e, c], depth-1) #右下三角形


triangle = [[-200, -100], [0, 200], [200, -100]]
n=int(input("输入谢尔斯宾三角形的阶数"))
draw_sierpinski(triangle, n)
turtle.done()

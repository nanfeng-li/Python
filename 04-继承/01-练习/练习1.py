import sys #模块sys用来退出游戏
import pygame #pygame模块，用来制作我们的游戏

def run_game():#定义函数
    #初始化游戏，创建窗口句柄
    pygame.init()  #对背景初始化，让pygame能正常工作
    screen=pygame.display.set_mode((800,600))#窗口大小设置，可自定
    pygame.display.set_caption("外星人入侵")#标题定义

    #开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():   #不断监测事件
            if event.type==pygame.QUIT:
                sys.exit()  #如果检测到退出，则退出游戏
        pygame.display.flip() #flip翻转，加上while循环，即不断刷新屏幕

run_game()


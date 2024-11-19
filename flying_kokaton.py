import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん") # タイトル
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bgf_img = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        w = -1
        h = 0
        key_list = pg.key.get_pressed()    
        if key_list[pg.K_UP]:
            h = -1
        if key_list[pg.K_DOWN]:
            h = 1
        if key_list[pg.K_LEFT]:
            w -= 1
        if key_list[pg.K_RIGHT]:
            w = 1

        kk_rct.move_ip((w, h))

        x = tmr % 3200
        screen.blit(bg_img, [-x, 0]) # screen surfaceに背景画像surfaceを張り付ける
        screen.blit(bgf_img, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(bgf_img, [-x+4800, 0])
        screen.blit(kk_img, kk_rct)
        pg.display.update()
        tmr += 1    
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
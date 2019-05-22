"""Game Development with Pygame
Wizard Tower Main Game code
"""
import socket
import queue
import pygame as pg
from settings import *
from sprites import *
from threading import Thread
#from scoreboard import Scoreboard


class ClientSend:
    def __init__(self, wizard="b", username="Bob", q=queue.Queue()):
        self.w = wizard
        self.n = username
        self.q = q
        host = '174.93.72.251'
        port = 8888
        self.mySocket = socket.socket()
        try:
            self.mySocket.connect((host, port))
            print("Connection Successful at: "+str(host)+":"+str(port))
        except:
            print("Unable to connect to server at: "+str(host)+":"+str(port))

    def send(self, level=0):
        self.x = self.q.get()
        self.y = self.q.get()
        self.l = level
        self.mySocket.send(str([self.n, self.w,  self.x, self.y, self.l]).encode())
        data = self.mySocket.recv(1024).decode()
        print('Received from server: ' + data)


class Game:
    def __init__(self):
        self.q = queue.Queue()
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        #self.scoreboard = Scoreboard()

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()

        """self.walls = pg.sprite.Group()"""
        self.player = Player(self)
        self.player2 = Player2(self)
        self.player3 = Player3(self)
        self.player4 = Player4(self)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.player2)
        self.all_sprites.add(self.player3)
        self.all_sprites.add(self.player4)
        #self.all_sprites.add(self.scoreboard)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        """for wall in WALL_LIST:
            wa = Wall(*wall)
            self.all_sprites.add(wa)
            self.walls.add(wa)"""
        self.run()


    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        # check if player hits a platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0

        if self.player2.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player2, self.platforms, False)
            if hits:
                self.player2.pos.y = hits[0].rect.top
                self.player2.vel.y = 0

        if self.player3.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player3, self.platforms, False)
            if hits:
                self.player3.pos.y = hits[0].rect.top
                self.player3.vel.y = 0

        if self.player4.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player4, self.platforms, False)
            if hits:
                self.player4.pos.y = hits[0].rect.top
                self.player4.vel.y = 0

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    self.player.jump() #put the jump animation here
                if event.key == pg.K_t:
                    self.player2.jump()
                if event.key == pg.K_i:
                    self.player3.jump()
                if event.key == pg.K_UP:
                    self.player4.jump()

    def draw(self):
        # Game Loop - draw
        """self.scoreboard.updateScores(self.player.pos.y, self.player2.pos.y, self.player3.pos.y, self.player4.pos.y)"""
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        """self.display_surface.blit(scoretext, scorebox)"""
        # *after* drawing everything, flip the display
        pg.display.flip()
        self.q.put(self.player.pos.x)
        self.q.put(self.player.vel.y)

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass


def main():
    g = Game()
    g.show_start_screen()
    while g.running:
        g.new()
        g.show_go_screen()

    pg.quit()


def network(wizard="b", username="bob"):
    s = ClientSend(wizard, username)
    while True:
        s.send()


Thread(target=network, args=("Wizard", "Username")).start()

main()

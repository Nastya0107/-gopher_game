import pygame
from add import Player, Bunch_1, Bunch_2, Rock_1, Rock_2, Coin

pygame.init()

width = 1366
height = 768
fps = 30
game_name = "Gopher, go!"
green = "#BDB76B"
img_dir = "media/img/"
snd_dir = "media/snd/"

pygame.mixer.music.load(snd_dir+"main.mp3")
pygame.mixer.music.set_volume(5)
pygame.mixer.music.play(-1)

bg = pygame.image.load(img_dir + "bg.webp")
bg = pygame.transform.scale(bg, (width, height))
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(game_name)

def draw_hp(screen, x, y, hp, hp_width, hp_height):
    very_good = "#32CD32"
    ok = "#FFA500"
    bad = "#FF4500"
    white = "#FFFFFF"
    rect = pygame.Rect(x, y, hp_width, hp_height)
    fill = (hp / 100) * hp_width
    fill_rect = pygame.Rect(x, y, fill, hp_height)

    if hp >= 50:
        pygame.draw.rect(screen, very_good, fill_rect)
    elif hp < 50 and hp > 20:
        pygame.draw.rect(screen, ok, fill_rect)
    elif hp <= 20 :
        pygame.draw.rect(screen, bad, fill_rect)
    pygame.draw.rect(screen, white, rect, 1)

def draw_text(screen, text, size, x, y, color):
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, size)
    text_image = font.render(text, True, color)
    text_rect = text_image.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_image, text_rect)

def get_hit_sprite(hits_dict):
   for hit in hits_dict.values():
       return hit[0]

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = pygame.sprite.Group()
bunches = pygame.sprite.Group()
rocks = pygame.sprite.Group()

bunch_g1 = pygame.sprite.Group()
bunch_g2 = pygame.sprite.Group()
rock_g1 = pygame.sprite.Group()
rock_g2 = pygame.sprite.Group()
coin_g = pygame.sprite.Group()

player_pic = Player()
bunch2 = Bunch_2()
bunch1 = Bunch_1()
rock1 = Rock_1()
rock2 = Rock_2()
coin = Coin()
all_sprites.add([player_pic, bunch1, bunch2, rock1, rock2, coin])
bunches.add([bunch1, bunch2])
bunch_g1.add(bunch1)
bunch_g2.add(bunch2)
rock_g1.add(rock1)
rock_g2.add(rock2)
rocks.add([rock1, rock2])
enemies.add([bunch1, bunch2, rock1, rock2])
player.add(player_pic)
coin_g.add(coin)
def menu():
    screen.blit(bg , (0,0))
    draw_text(screen, game_name, 128, width / 2, height / 4, green)
    draw_text(screen, "Space is a jump", 44,
              width / 2, height / 2, green)
    draw_text(screen, "Press a button to start th game", 36, width / 2, height * 3 / 4, green)
    pygame.display.flip()
    run = True
    while run:
        timer.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                run = False
def won():
    screen.blit(bg , (0,0))
    draw_text(screen, game_name, 128, width / 2, height / 4, green)
    draw_text(screen, "congratulations, You won the game ", 44,
              width / 2, height / 2, green)
    draw_text(screen, "Press a button to finish th game", 44, width / 2, height * 3 / 4, green)
    pygame.mixer.music.load(snd_dir + "won.mp3")
    pygame.mixer.music.set_volume(5)
    pygame.mixer.music.play(-1)
    pygame.display.flip()
    run = True
    while run:
        timer.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                pygame.quit()
game_over = True
count_of_damage = 0
count = 0
timer = pygame.time.Clock()
run = True
while run:
    if game_over:
        game_over = False
        menu()
    timer.tick(fps)
    all_sprites.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    damage = pygame.sprite.groupcollide(enemies,player, False, False)
    cheat = pygame.sprite.groupcollide(rocks, bunches, True, True)
    cheat2 = pygame.sprite.groupcollide(bunch_g1, bunch_g2, True, True)
    cheat3 = pygame.sprite.groupcollide(rock_g1, rock_g2, True, True)
    coins_got = pygame.sprite.groupcollide(player,coin_g, False,True)
    if coins_got:
        count += 1
        coin = Coin()
        coin_g.add(coin)
        all_sprites.add(coin)
        sprite = get_hit_sprite(coins_got)
        sprite.snd_coin.play()
    if damage:
        count_of_damage += 1
        if count_of_damage >= 15:
            player_pic.hp -= 2
            count_of_damage = 0
            sprite = get_hit_sprite(damage)
            sprite.snd_lose.play()
    if player_pic.hp <= 0:
        pygame.quit()
    if len(enemies) <= 2:
        bunch2 = Bunch_2()
        bunch1 = Bunch_1()
        rock1 = Rock_1()
        rock2 = Rock_2()
        all_sprites.add([bunch1, bunch2, rock1, rock2])
        bunches.add([bunch1, bunch2])
        rocks.add([rock1, rock2])
        enemies.add([bunch1, bunch2, rock1, rock2])
        bunch_g1.add(bunch1)
        bunch_g2.add(bunch2)
        rock_g1.add(rock1)
        rock_g2.add(rock2)
    if count == 10:
        won()
    screen.blit(bg,(0, 0) )
    all_sprites.draw(screen)
    draw_hp(screen, 50, 50, player_pic.hp, 200, 20)
    draw_text(screen, "You got: " + str(count) + " coins", 50, 1189, 50, "green")
    pygame.display.update()
pygame.quit()
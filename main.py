import pygame

pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pesawat2an")

MERAH = (250, 50, 50)
PUTIH = (255, 255, 255)
HIJAU = (50, 250, 50)

class Peluru:
  def __init__(self, x, y):
    self.size = 50
    self.x = x
    self.y = y
    self.langkah = 5
  
  def tampilkan(self):
    pygame.draw.rect(screen, MERAH, (self.x, self.y, self.size, self.size))
  
  def gerak(self):
    self.y = self.y - self.langkah

  def keatas(self):
    if self.y < 0:
      return True
  


class Pesawat:
  def __init__(self):
    self.size = 50
    self.x = WIDTH / 2
    self.y = HEIGHT - self.size
    self.tombolKiri = False
    self.tombolKanan = False
    self.langkah = 3
  
  def tampilkan(self):
    gambar = pygame.image.load("player.png")
    gambar = pygame.transform.scale(gambar, (self.size, self.size))
    screen.blit(gambar, (self.x, self.y))
    # pygame.draw.rect(screen, HIJAU, (self.x, self.y, self.size, self.size))

  def gerak(self):
    if self.tombolKanan:
      self.x = self.x + self.langkah
    if self.tombolKiri:
      self.x = self.x - self.langkah




def main():
  run = True
  while run:
    for e in pygame.event.get():
      if e.type == pygame.QUIT:
        run = False
      
      # KEYDOWN
      if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
        run = False
      elif e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
        pesawat.tombolKanan = True
      elif e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
        pesawat.tombolKiri = True
      elif e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
        bullets.append(Peluru(pesawat.x, pesawat.y))

      # KEYUP
      if e.type == pygame.KEYUP:
        pesawat.tombolKanan = False
        pesawat.tombolKiri = False
      
    screen.fill(PUTIH)

    # PELULU
    for bullet in bullets:
      bullet.tampilkan()
      bullet.gerak()
      if bullet.keatas():
        bullets.remove(bullet)

    # PESAWAT
    pesawat.tampilkan()
    pesawat.gerak()

    pygame.display.update()


if __name__ == "__main__":
  pesawat = Pesawat()
  bullets = []
  main()
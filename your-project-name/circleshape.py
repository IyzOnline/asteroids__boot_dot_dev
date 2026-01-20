import pygame

class CircleShape(pygame.sprite.Sprite):
  def __init__(self, x, y, radius):
    if hasattr(self, "containers"):
      super().__init__(self.containers)
    else:
      super().__init__()
  
    self.position = pygame.Vector2(x, y)
    self.velocity = pygame.Vector2(0, 0)
    self.radius = radius
  
  def draw(self, screen):
    pass

  def update(self, dt):
    pass

  def collides_with(self, other):
    total_radius = self.radius + other.radius
    distance_to_other = self.position.distance_to(other.position)
    
    if total_radius > distance_to_other:
      return True
    
    return False
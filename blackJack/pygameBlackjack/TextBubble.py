import pygame
import time

class TextBubble:
    def __init__(self, text, x, y, font):
        self.text = text
        self.x = x
        self.y = y
        self.font = font
        self.start_time = time.time()
        self.visible = True
        self.padding_x = 20
        self.padding_y = 15
       
        self.text_surface = font.render(text, True, (0,0,0))
        self.bubble_rect = pygame.Rect(
            x, y,
            self.text_surface.get_width() + self.padding_x * 2,
            self.text_surface.get_height() + self.padding_y * 2
        )
        

    def draw(self, screen):
        duration = 2
        # Hide bubble if duration is over
        elapsed = time.time() - self.start_time
        fade_time = 0.5  
        if elapsed > duration: #if time is up, start fade
            alpha = max(0, 255 - int((elapsed - duration) / fade_time * 255))
            if alpha <= 0:
                self.visible = False
                return
        else:
            alpha = 255
        #draw fading
        bubble_surface = pygame.Surface(self.bubble_rect.size, pygame.SRCALPHA)
        bubble_surface.set_alpha(alpha)
        pygame.draw.rect(bubble_surface, (255,255,255), bubble_surface.get_rect(), border_radius=15)
        screen.blit(bubble_surface, (self.x, self.y))


        # Draw if visible
        if self.visible:
            # Draw bubble background and border
            pygame.draw.rect(screen, (255,255,255), self.bubble_rect, border_radius=15)
            pygame.draw.rect(screen, (0, 0, 0), self.bubble_rect, 2, border_radius=15)

            # Draw text
            screen.blit(self.text_surface,
                        (self.x + self.padding_x, self.y + self.padding_y))

            # Draw the tail
            tail_points = [
                (self.x + self.bubble_rect.width // 2 - 10, self.y),             
                (self.x + self.bubble_rect.width // 2 + 10, self.y),             
                (self.x + self.bubble_rect.width // 2, self.y - 15)
            ]
            pygame.draw.polygon(screen, (255,255,255), tail_points)
            pygame.draw.polygon(screen, (0, 0, 0), tail_points, 2)


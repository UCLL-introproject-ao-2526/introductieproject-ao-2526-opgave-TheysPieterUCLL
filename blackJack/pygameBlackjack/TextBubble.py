import pygame
import time

class TextBubble:
    def __init__(self, text, x, y, font, duration=3,
                 text_color=(0, 0, 0), bubble_color=(255, 255, 255)):
        self.text = text
        self.x = x
        self.y = y
        self.font = font
        self.text_color = text_color
        self.bubble_color = bubble_color
        self.duration = duration
        self.start_time = time.time()
        self.visible = True

        # Pre-render the text once for performance
        self.text_surface = font.render(text, True, text_color)
        padding_x, padding_y = 20, 15
        self.bubble_rect = pygame.Rect(
            x, y,
            self.text_surface.get_width() + padding_x * 2,
            self.text_surface.get_height() + padding_y * 2
        )
        self.padding_x = padding_x
        self.padding_y = padding_y

    def draw(self, screen):
        # Hide bubble if duration is over
        elapsed = time.time() - self.start_time
        fade_time = 0.5  # seconds
        if elapsed > self.duration:
            alpha = max(0, 255 - int((elapsed - self.duration) / fade_time * 255))
            if alpha <= 0:
                self.visible = False
                return
        else:
            alpha = 255

        bubble_surface = pygame.Surface(self.bubble_rect.size, pygame.SRCALPHA)
        bubble_surface.set_alpha(alpha)
        pygame.draw.rect(bubble_surface, self.bubble_color, bubble_surface.get_rect(), border_radius=15)
        screen.blit(bubble_surface, (self.x, self.y))


        # Draw only if visible
        if self.visible:
            # Draw bubble background and border
            pygame.draw.rect(screen, self.bubble_color, self.bubble_rect, border_radius=15)
            pygame.draw.rect(screen, (0, 0, 0), self.bubble_rect, 2, border_radius=15)

            # Draw the text
            screen.blit(self.text_surface,
                        (self.x + self.padding_x, self.y + self.padding_y))

            # Draw the tail
            tail_points = [
                (self.x + self.bubble_rect.width // 2 - 10, self.y),             # left base of tail (top edge)
                (self.x + self.bubble_rect.width // 2 + 10, self.y),             # right base of tail
                (self.x + self.bubble_rect.width // 2, self.y - 15)
            ]
            pygame.draw.polygon(screen, self.bubble_color, tail_points)
            pygame.draw.polygon(screen, (0, 0, 0), tail_points, 2)

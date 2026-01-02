import pygame

class Chip:
    def __init__(self, start_pos):
        self.x, self.y = start_pos
        self.tx, self.ty = start_pos
        self.lost = False
        self.speed = 500
        self.width, self.height = 120, 70
        self.center = (self.width // 2, self.height // 2)

        self.surface = pygame.Surface((self.width + 10, self.height + 10), pygame.SRCALPHA)
        self.isMoving = False
        self.draw_chip()

    def draw_chip(self):
        self.surface.fill((0, 0, 0, 0))

        chip_radius_x = self.width // 2
        chip_radius_y = self.height // 2
        chip_center = (chip_radius_x, chip_radius_y)

        if not self.isMoving:   #only shadow if not movin
            shadow_offset = (6, 6)
            pygame.draw.ellipse(
            self.surface,
            (20, 20, 20, 180),  # dark gray, semi-transparent
            (chip_center[0] - chip_radius_x + shadow_offset[0],
            chip_center[1] - chip_radius_y / 2 + shadow_offset[1],
            chip_radius_x * 2, chip_radius_y * 1.4)
            )

        # Chip body
        pygame.draw.ellipse(
            self.surface,
            (200, 0, 0),
            (0, 0, self.width, self.height)
        )

        # Inner ring
        pygame.draw.ellipse(
            self.surface,
            (255, 255, 255),
            (10, 10, self.width - 20, self.height - 20),
            3
        )

        # Decorative edge markings
        for angle in range(0, 360, 45):
            v = pygame.math.Vector2(1, 0).rotate(angle)
            x = chip_center[0] + int(chip_radius_x * 0.75 * v.x)
            y = chip_center[1] + int(chip_radius_y * 0.75 * v.y)

            pygame.draw.ellipse(
                self.surface,
                (255, 255, 255),
                (x - 4, y - 3, 8, 6)
            )
            # --- Denomination text ---
        font_chip = pygame.font.Font(None, 36)
        text_chip = font_chip.render("25", True, (255, 255, 255))
        text_rect = text_chip.get_rect(center=chip_center)
        self.surface.blit(text_chip, text_rect)

    def move_to(self,end_pos):
        self.tx, self.ty = end_pos
        self.isMoving = True

    def update(self, dt):
        dt = dt
        
        pos = pygame.math.Vector2(self.x, self.y)
        target = pygame.math.Vector2(self.tx, self.ty)

        direction = target - pos
        distance = direction.length()

        if distance > 0:
            direction.normalize_ip() #vect in place with length 1
            move = self.speed * dt #pixel per frame

            if move >= distance: #no overshoot
                pos = target
                self.isMoving = False
            else:
                pos += direction * move
                self.isMoving = True
            self.x, self.y = pos #round(pos.x), round(pos.y) for "whole" pixels but gives problems when losing chips? 
            self.draw_chip()


    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))
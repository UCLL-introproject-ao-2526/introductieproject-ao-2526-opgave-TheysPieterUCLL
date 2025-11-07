# black jack in python wth pygame!
import copy
import random
import pygame
from TextBubble import TextBubble

pygame.init()
# game variables
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['H', 'D', 'S', 'C']
deck = [rank + suit for suit in suits for rank in cards]
decks = 4
WIDTH = 900
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Pygame Blackjack!')
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 44)
smaller_font = pygame.font.Font('freesansbold.ttf', 36)
active = False
# win, loss, draw/push
records = [0, 0, 0]
player_score = 0
dealer_score = 0
initial_deal = False
my_hand = []
dealer_hand = []
outcome = 0
reveal_dealer = False
hand_active = False
outcome = 0
add_score = False
results = ['', 'SEEMS LIKE YOU BUSTED o_O', 'YOU WIN :)', 'BETTER LUCK NEXT TIME :(  AGAIN?', 'THAT IS A TIE ...']
txtExtra = ['','','YOU ARE NOT CHEATING, RIGHT? :/ ', 'PAYING RENT IS OVERRATED, AM I RIGHT ;} ' ,'5']
CARD_BASE_SIZE = (32, 48)
CARD_DISPLAY_SIZE = (160, 275)
CARD_SPACING = 100

bubble_texts = ["O, HELLO THERE!", "FEELING LUCKY TODAY?"]
bubbles = []
current_bubble_index = 0

bubbles.append(TextBubble(bubble_texts[0], 100, 100, smaller_font, duration=2))




# deal cards by selecting randomly from deck, and make function for one card at a time
def deal_cards(current_hand, current_deck):
    card = random.randint(0, len(current_deck))
    current_hand.append(current_deck[card - 1])
    current_deck.pop(card - 1)
    return current_hand, current_deck


# draw scores for player and dealer on screen
def draw_scores(player, dealer):
    screen.blit(font.render(f'Score[{player}]', True, 'white'), (650, 400))
    if reveal_dealer:
        screen.blit(font.render(f'Score[{dealer}]', True, 'white'), (650, 100))


def draw_cards(player, dealer, reveal):
    """Draws the player's and dealer's cards using the pixel-art instruction system."""
    # --- Draw player cards ---
    for i, card in enumerate(player):
        x = 55 + (CARD_SPACING * i)
        y = 390 + (15 * i)

        # Get the pixel-art instructions for this card
        instructions = get_card_pixel_instructions(card)

        # Create a temporary surface for one card
        card_surface = pygame.Surface(CARD_BASE_SIZE, pygame.SRCALPHA)
        render_card(card_surface, get_card_pixel_instructions(card))

        # Scale up for visibility
        scaled = pygame.transform.scale(card_surface, CARD_DISPLAY_SIZE)
        screen.blit(scaled, (x, y))

    # --- Draw dealer cards ---
    for i, card in enumerate(dealer):
        x = 55 + (CARD_SPACING * i)
        y = 60 + (15 * i)

        if i == 0 and not reveal:
            # hidden card: draw the back
            card_surface = pygame.Surface((16, 15), pygame.SRCALPHA)
            render_card_back(card_surface, get_card_back_instructions())
            scaled = pygame.transform.scale(card_surface, CARD_DISPLAY_SIZE)
            screen.blit(scaled, (x, y))
            
        else:
            # visible card: render actual face
            instructions = get_card_pixel_instructions(card)
            card_surface = pygame.Surface(CARD_BASE_SIZE, pygame.SRCALPHA)
            render_card(card_surface, instructions)
            scaled = pygame.transform.scale(card_surface, CARD_DISPLAY_SIZE)
            screen.blit(scaled, (x, y))


# pass in player or dealer hand and get best score possible
def calculate_score(hand):
  
    hand_score = 0
    aces_count = sum('A' in card for card in hand)

    # Add up base score
    for card in hand:
        rank = card[:-1]  # everything except the last character (the suit)
        
        if rank in ['2','3','4','5','6','7','8','9','10']:
            hand_score += int(rank)
        elif rank in ['J','Q','K']:
            hand_score += 10
        elif rank == 'A':
            hand_score += 11  # Aces start as 11

    # Adjust Aces from 11 to 1 as needed
    while hand_score > 21 and aces_count > 0:
        hand_score -= 10
        aces_count -= 1

    return hand_score



# draw game conditions and buttons
def draw_game(act, record, result):
    global current_bubble_index, bubbles, bubble_texts
    button_list = []
    # initially on startup (not active) only option is to deal new hand
    if not act:
        
        current_bubble = bubbles[current_bubble_index]

        if current_bubble.visible:
            current_bubble.draw(screen)
        else:
            # When one finishes, spawn the next one (if any)
            if current_bubble_index + 1 < len(bubble_texts):
                current_bubble_index += 1
                bubbles.append(TextBubble(
                    bubble_texts[current_bubble_index], 
                    100, 100 + current_bubble_index * 40, 
                smaller_font, duration=2
                ))
            else:
                deal = pygame.draw.rect(screen, 'white', [280, 500, 300, 100], 0, 5)
                pygame.draw.rect(screen, 'green', [280, 500, 300, 100], 3, 5)
                deal_text = font.render('YES I DO!', True, 'black')
                screen.blit(deal_text, (325, 530))
                button_list.append(deal)
    # once game started, shot hit and stand buttons and win/loss records
    else:
        hit = pygame.draw.rect(screen, 'white', [50, 720, 300, 100], 0, 5)
        pygame.draw.rect(screen, 'green', [50, 720, 300, 100], 3, 5)
        hit_text = font.render('HIT ME', True, 'black')
        screen.blit(hit_text, (125, 750))
        button_list.append(hit)
        stand = pygame.draw.rect(screen, 'white', [550, 720, 300, 100], 0, 5)
        pygame.draw.rect(screen, 'green', [550, 720, 300, 100], 3, 5)
        stand_text = font.render('STAND', True, 'black')
        screen.blit(stand_text, (630, 755))
        button_list.append(stand)
        score_text = smaller_font.render(f'Wins: {record[0]}   Losses: {record[1]}   Draws: {record[2]}', True, 'white')
        screen.blit(score_text, (15, 840))
    # if there is an outcome for the hand that was played, display a restart button and tell user what happened
    if result != 0:
        # store bubbles in a list
        bubbles = []

    # first bubble (special extra if player is far ahead)
        if records[0] - records[1] >=4 or records[1] - records[0] >= 4:
            bubbles.append(TextBubble(txtExtra[result], 30, 120, smaller_font, duration=2))

    # second bubble (normal result)
        else:
            bubbles.append(TextBubble(results[result], 100, 160, smaller_font, duration=2))

    # draw visible bubble(s)
        for bubble in bubbles:
            if bubble.visible:
                bubble.draw(screen)
        # screen.blit(font.render(results[result], True, 'white'), (15, 25))
        deal = pygame.draw.rect(screen, 'white', [300, 370, 300, 100], 0, 5)
        pygame.draw.rect(screen, 'green', [300, 370, 300, 100], 3, 5)
        pygame.draw.rect(screen, 'black', [303, 373, 294, 94], 3, 5)
        deal_text = font.render('NEW HAND', True, 'black')
        screen.blit(deal_text, (325, 400))
        button_list.append(deal)
    return button_list


# check endgame conditions function
def check_endgame(hand_act, deal_score, play_score, result, totals, add):
    # check end game scenarios is player has stood, busted or blackjacked
    # result 1- player bust, 2-win, 3-loss, 4-push
    if not hand_act and deal_score >= 17:
        if play_score > 21:
            result = 1
        elif deal_score < play_score <= 21 or deal_score > 21:
            result = 2
        elif play_score < deal_score <= 21:
            result = 3
        else:
            result = 4
        if add:
            if result == 1 or result == 3:
                totals[1] += 1
            elif result == 2:
                totals[0] += 1
            else:
                totals[2] += 1
            add = False
    return result, totals, add

def get_card_pixel_instructions(card):
 
    # Validate input
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    suits = ['H','D','S','C']
    if len(card) < 2 or card[:-1] not in ranks or card[-1].upper() not in suits:
        raise ValueError(f"Invalid card code: {card}")

    rank = card[:-1]
    suit = card[-1].upper()

    # Colors (RGB)
    WHITE = (245, 245, 245)
    BLACK = (0, 0, 0)
    RED = (220, 0, 0)
    GREEN = (0, 100, 0)

    color = RED if suit in ['H', 'D'] else BLACK

    # Card dimensions (small pixel card)
    CARD_W, CARD_H = 32, 48
    cx, cy = CARD_W // 2, CARD_H // 2

    instructions = []

    # Background and border
    instructions.append(("rect", GREEN, (0, 0, CARD_W, CARD_H)))         # table background
    instructions.append(("rect", WHITE, (2, 2, CARD_W - 4, CARD_H - 4))) # white card
    instructions.append(("rect", BLACK, (0, 0, CARD_W, CARD_H, 2)))      # border (width 2)

    # Suit symbols (pixel-art style)
    if suit == "H":
        instructions.append(("polygon", color, [(cx-3, cy), (cx, cy+5), (cx+3, cy)]))
        instructions.append(("circle", color, (cx-2, cy-2, 2)))
        instructions.append(("circle", color, (cx+2, cy-2, 2)))
    elif suit == "D":
        instructions.append(("polygon", color, [(cx, cy-4), (cx+4, cy), (cx, cy+4), (cx-4, cy)]))
    elif suit == "S":
        instructions.append(("polygon", color, [(cx, cy-5), (cx-4, cy+2), (cx+4, cy+2)]))
        instructions.append(("rect", color, (cx-1, cy+2, 2, 4)))
    elif suit == "C":
        instructions.append(("circle", color, (cx-2, cy-2, 2)))
        instructions.append(("circle", color, (cx+2, cy-2, 2)))
        instructions.append(("circle", color, (cx, cy+1, 2)))
        instructions.append(("rect", color, (cx-1, cy+3, 2, 4)))

    # Ranks in corners
    instructions.append(("text", color, (3, 2, rank)))
    instructions.append(("text_rotated", color, (CARD_W - 12, CARD_H - 12, rank, 180)))

    return instructions

def render_card(screen, instructions):
    for shape, color, params in instructions:
        if shape == "rect":
            if len(params) == 5:
                pygame.draw.rect(screen, color, params[:4], params[4])
            else:
                pygame.draw.rect(screen, color, params)
        elif shape == "circle":
            x, y, r = params
            pygame.draw.circle(screen, color, (x, y), r)
        elif shape == "polygon":
            pygame.draw.polygon(screen, color, params)
        elif shape == "text":
            x, y, text = params
            font = pygame.font.SysFont("Courier", 10, bold=True)
            surf = font.render(text, True, color)
            screen.blit(surf, (x, y))
        elif shape == "text_rotated":
            x, y, text, angle = params
            font = pygame.font.SysFont("Courier", 10, bold=True)
            surf = font.render(text, True, color)
            screen.blit(pygame.transform.rotate(surf, angle), (x, y))


def get_card_back_instructions():
    """Returns pixel-art drawing instructions for the back of a playing card."""
    pattern = [
        "WWWWWWWWWWWWWWWW",
        "WRRRRRRRRRRRRRRW",
        "WRWRWRWRWRWRWRRW",
        "WRRRRRRRRRRRRRRW",
        "WRWRWRWRWRWRWRRW",
        "WRRRRRRRRRRRRRRW",
        "WRWRWRWRWRWRWRRW",
        "WRRRRRRRRRRRRRRW",
        "WRWRWRWRWRWRWRRW",
        "WRRRRRRRRRRRRRRW",
        "WRWRWRWRWRWRWRRW",
        "WRRRRRRRRRRRRRRW",
        "WRWRWRWRWRWRWRRW",
        "WRRRRRRRRRRRRRRW",
        "WWWWWWWWWWWWWWWW"
    ]

    color_map = {
        "W": (255, 255, 255),  # white
        "R": (180, 0, 0)       # dark red
    }

    instructions = []
    for y, row in enumerate(pattern):
        for x, char in enumerate(row):
            if char in color_map:
                instructions.append((x, y, color_map[char]))

    return instructions

def render_card_back(surface, instructions, pixel_size=1):
    for x, y, color in instructions:
        pygame.draw.rect(surface, color, (x * pixel_size, y * pixel_size, pixel_size, pixel_size))

def draw_chip(centerx, centery):
    chip_center = (centerx, centery)
    chip_radius_x = 60    # horizontal radius
    chip_radius_y = 35    # vertical radius (flatter look)

    # --- Shadow (for depth) ---
    shadow_offset = (6, 6)
    pygame.draw.ellipse(
        screen,
        (20, 20, 20, 180),  # dark gray, semi-transparent
        (chip_center[0] - chip_radius_x + shadow_offset[0],
         chip_center[1] - chip_radius_y / 2 + shadow_offset[1],
         chip_radius_x * 2, chip_radius_y * 1.4)
    )

    # --- Outer red ellipse ---
    pygame.draw.ellipse(screen, (200, 0, 0),
        (chip_center[0] - chip_radius_x,
         chip_center[1] - chip_radius_y,
         chip_radius_x * 2, chip_radius_y * 2))

    # --- Inner white ring ---
    pygame.draw.ellipse(screen, (255, 255, 255),
        (chip_center[0] - chip_radius_x + 6,
         chip_center[1] - chip_radius_y + 6,
         (chip_radius_x - 6) * 2, (chip_radius_y - 6) * 2), 3)

    # --- Inner solid red center ---
    pygame.draw.ellipse(screen, (180, 0, 0),
        (chip_center[0] - chip_radius_x + 15,
         chip_center[1] - chip_radius_y + 15,
         (chip_radius_x - 15) * 2, (chip_radius_y - 15) * 2))

    # --- White accent stripes ---
    for angle in range(0, 360, 45):
        v = pygame.math.Vector2(1, 0).rotate(angle)
        x = chip_center[0] + int(chip_radius_x * 0.8 * v.x)
        y = chip_center[1] + int(chip_radius_y * 0.8 * v.y)
        pygame.draw.ellipse(screen, (255, 255, 255),
            (x - 4, y - 3, 8, 6))

    # --- Denomination text ---
    font_chip = pygame.font.Font(None, 36)
    text_chip = font_chip.render("25", True, (255, 255, 255))
    text_rect = text_chip.get_rect(center=chip_center)
    screen.blit(text_chip, text_rect)


# main game loop
run = True
while run:
    
    # run game at our framerate and fill screen with bg color
    timer.tick(fps)
# --- Draw Blackjack Table ---

# Draw wood border first (behind everything)
    pygame.draw.rect(screen, (90, 45, 0), [0, 0, 900, 900], border_radius=40)  # wood frame

# Draw inner felt (slightly smaller, inset inside wood)
    pygame.draw.rect(screen, (0, 80, 0), [20, 20, 860, 860], border_radius=40)

# Add soft lighting / gradient effects on top
    pygame.draw.circle(screen, (0, 120, 0), (450, 450), 400)
    pygame.draw.circle(screen, (0, 150, 0), (450, 450), 300)

    


    draw_chip(700,300)
    chipsStack = records[0] - records[1]
    if chipsStack>0:
        for i in range(chipsStack):
            if i%2==0:
                draw_chip(700+5,650-i*5)
            else:
                draw_chip(700-5,650-i*5)

 
 

    # initial deal to player and dealer
    if initial_deal:
        for i in range(2):
            my_hand, game_deck = deal_cards(my_hand, game_deck)
            dealer_hand, game_deck = deal_cards(dealer_hand, game_deck)
        initial_deal = False
    # once game is activated, and dealt, calculate scores and display cards
    if active:
        player_score = calculate_score(my_hand)
        draw_cards(my_hand, dealer_hand, reveal_dealer)
        if reveal_dealer:
            dealer_score = calculate_score(dealer_hand)
            if dealer_score < 17:
                dealer_hand, game_deck = deal_cards(dealer_hand, game_deck)
        draw_scores(player_score, dealer_score)
    buttons = draw_game(active, records, outcome)

    # event handling, if quit pressed, then exit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            if not active:
                if buttons[0].collidepoint(event.pos):
                    active = True
                    initial_deal = True
                    game_deck = copy.deepcopy(decks * deck)
                    my_hand = []
                    dealer_hand = []
                    outcome = 0
                    hand_active = True
                    reveal_dealer = False
                    outcome = 0
                    add_score = True
            else:
                # if player can hit, allow them to draw a card
                if buttons[0].collidepoint(event.pos) and player_score < 21 and hand_active:
                    my_hand, game_deck = deal_cards(my_hand, game_deck)
                # allow player to end turn (stand)
                elif buttons[1].collidepoint(event.pos) and not reveal_dealer:
                    reveal_dealer = True
                    hand_active = False
                elif len(buttons) == 3:
                    if buttons[2].collidepoint(event.pos):
                        active = True
                        initial_deal = True
                        game_deck = copy.deepcopy(decks * deck)
                        my_hand = []
                        dealer_hand = []
                        outcome = 0
                        hand_active = True
                        reveal_dealer = False
                        outcome = 0
                        add_score = True
                        dealer_score = 0
                        player_score = 0


    # if player busts, automatically end turn - treat like a stand
    if hand_active and player_score >= 21:
        hand_active = False
        reveal_dealer = True

    outcome, records, add_score = check_endgame(hand_active, dealer_score, player_score, outcome, records, add_score)

    pygame.display.flip()
pygame.quit()

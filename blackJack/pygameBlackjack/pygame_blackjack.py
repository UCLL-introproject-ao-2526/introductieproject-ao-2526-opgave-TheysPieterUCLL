import copy
import random
import pygame
from TextBubble import TextBubble
from Chip import Chip

pygame.init()
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
# w,L,D
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
txtExtra = ['YOU ARE NOT CHEATING, RIGHT? :/ ', 'PAYING RENT IS OVERRATED, AM I RIGHT ;} ' ]
CARD_BASE_SIZE = (32, 48)
CARD_DISPLAY_SIZE = (160, 275)
CARD_SPACING = 100

bubble_texts = ["O, HELLO THERE!", "FEELING LUCKY TODAY?"]
bubbles = []
current_bubble_index = 0

bubbles.append(TextBubble(bubble_texts[0], 100, 100, smaller_font))
clock = pygame.time.Clock()
dt=clock.tick(60) / 1000
chip1 = Chip(start_pos=(400, -75) )
chip2 = Chip(start_pos=(700, 300)) 

chips = []

# deal cards randomly from deck to hand
def deal_cards(current_hand, current_deck):
    card = random.randint(0, len(current_deck))
    current_hand.append(current_deck[card - 1])
    current_deck.pop(card - 1)
    return current_hand, current_deck


# draw scores
def draw_scores(player, dealer):
    screen.blit(font.render(f'Score[{player}]', True, 'white'), (650, 400))
    if reveal_dealer:
        screen.blit(font.render(f'Score[{dealer}]', True, 'white'), (650, 100))


def draw_cards(player, dealer, reveal):
    # --- Draw player cards with pixel art---
    for i, card in enumerate(player):
        x = 55 + (CARD_SPACING * i)
        y = 390 + (15 * i)

        card_surface = pygame.Surface(CARD_BASE_SIZE, pygame.SRCALPHA)
        render_card(card_surface, get_card_pixel_instructions(card))

        # Scale up 
        scaled = pygame.transform.scale(card_surface, CARD_DISPLAY_SIZE)
        screen.blit(scaled, (x, y))

    # --- Draw dealer cards with pixel art ---
    for i, card in enumerate(dealer):
        x = 55 + (CARD_SPACING * i)
        y = 60 + (15 * i)

        if i == 0 and not reveal:
            # hidden card: draw back
            card_surface = pygame.Surface((16, 15), pygame.SRCALPHA)
            get_card_back_instructions(card_surface)
            scaled = pygame.transform.scale(card_surface, CARD_DISPLAY_SIZE)
            screen.blit(scaled, (x, y))
            
        else:
            # visible card: render face
            card_surface = pygame.Surface(CARD_BASE_SIZE, pygame.SRCALPHA)
            render_card(card_surface, get_card_pixel_instructions(card))
            scaled = pygame.transform.scale(card_surface, CARD_DISPLAY_SIZE)
            screen.blit(scaled, (x, y))


# pass in hand and get best score
def calculate_score(hand):
  
    hand_score = 0
    aces_count = sum('A' in card for card in hand)

    # Add up base score
    for card in hand:
        rank = card[:-1]  # only rank
        
        if rank in ['2','3','4','5','6','7','8','9','10']:
            hand_score += int(rank)
        elif rank in ['J','Q','K']:
            hand_score += 10
        elif rank == 'A':
            hand_score += 11  

    # Adjust Aces from 11 to 1 if needed
    while hand_score > 21 and aces_count > 0:
        hand_score -= 10
        aces_count -= 1

    return hand_score



# draw game conditions and buttons
def draw_game(act, record, result):
    global current_bubble_index, bubbles, bubble_texts

    button_list = []
    # initially on startup 
    if not act:
        #textbubble one after another
        current_bubble = bubbles[current_bubble_index]

        if current_bubble.visible:
            current_bubble.draw(screen)
        elif current_bubble_index + 1 < len(bubble_texts):
                current_bubble_index += 1
                bubbles.append(TextBubble(
                    bubble_texts[current_bubble_index], 
                    100, 100 + current_bubble_index * 40, 
                smaller_font
                ))
            #after intro, show start button
        else:
            deal = pygame.draw.rect(screen, 'white', [280, 500, 300, 100], 0, 5)
            pygame.draw.rect(screen, 'green', [280, 500, 300, 100], 3, 5)
            deal_text = font.render('YES I DO!', True, 'black')
            screen.blit(deal_text, (325, 530))
            button_list.append(deal)
    # once game started, show hit and stand buttons and records
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
    # if there is an outcome, display a restart button and text bubble
    if result != 0:
        # reset bubbels so only game active bubbels appear
        bubbles = []

    # first bubble (special extra if player is far ahead/behind)
        if records[0] - records[1] >=4:
            bubbles.append(TextBubble(txtExtra[0], 30, 120, smaller_font))
        elif records[1] - records[0] >=4:
            bubbles.append(TextBubble(txtExtra[1], 30, 120, smaller_font))

    # second bubble (normal result)
        else:
            bubbles.append(TextBubble(results[result], 100, 160, smaller_font))

    # draw visible bubble

        if bubbles[0].visible:
            bubbles[0].draw(screen)
        deal = pygame.draw.rect(screen, 'white', [300, 370, 300, 100], 0, 5)
        pygame.draw.rect(screen, 'green', [300, 370, 300, 100], 3, 5)
        pygame.draw.rect(screen, 'black', [303, 373, 294, 94], 3, 5)
        deal_text = font.render('NEW HAND', True, 'black')
        screen.blit(deal_text, (325, 400))
        button_list.append(deal)
    return button_list


# check endgame 
def check_endgame(hand_act, deal_score, play_score, result, totals, add):
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
                if chips:
                    chips[-1].lost = True
                    chips[-1].move_to((200,-30)) #player lost a chip
                
            elif result == 2:
                totals[0] += 1
                if totals[0]>totals[1]:
                    chips.append(Chip((700,0))) #player won a chip
            else:
                totals[2] += 1
            add = False
    return result, totals, add

def get_card_pixel_instructions(card):

    rank = card[:-1]
    suit = card[-1].upper()

    WHITE = (245, 245, 245)
    BLACK = (0, 0, 0)
    RED = (220, 0, 0)

    color = RED if suit in ['H', 'D'] else BLACK
   
    CARD_W, CARD_H = 32, 48
    cx, cy = CARD_W // 2, CARD_H // 2

    instructions = []

    # Background and border
    instructions.append(("rect", WHITE, (2, 2, CARD_W - 4, CARD_H - 4))) # white card
    instructions.append(("rect", BLACK, (0, 0, CARD_W, CARD_H, 2)))      # border (width 2)

    # Suit symbols
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
                pygame.draw.rect(screen, color, params[:4], params[4]) #for border around cards
            else:
                pygame.draw.rect(screen, color, params) #normal rectangel
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


def get_card_back_instructions(surface):
    """ pixel-art back of playing card."""
    surf = surface

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

 
    for y, row in enumerate(pattern):
        for x, char in enumerate(row):
            if char == 'W':
                pygame.draw.rect(surf, (255,255,255), (x , y , 1,1))
            else:
                pygame.draw.rect(surf, (180,0,0), (x , y , 1,1))



# main loop
run = True
while run:

    
    timer.tick(fps)
# --- Draw Table ---

# Draw wood border 
    pygame.draw.rect(screen, (90, 45, 0), [0, 0, 900, 900], border_radius=40)  

# Draw inner felt 
    pygame.draw.rect(screen, (0, 80, 0), [20, 20, 860, 860], border_radius=40)

# Add lighting / gradient
    pygame.draw.circle(screen, (0, 120, 0), (450, 450), 400)
    pygame.draw.circle(screen, (0, 150, 0), (450, 450), 300)

#draw chipstack when winning
    for i, chip in enumerate(chips):
        if not chip.lost:
            x = 705 if i%2 == 0 else 695
            y = 640 - i*5
            chip.move_to((x,y))
        chip.update(dt)
        chip.draw(screen)

#remove lost chip after it has moved offscreen
    if chips and chips[-1].lost and not chips[-1].isMoving:
        chips.pop()
    


    chip1.draw(screen)
    chip1.move_to((400,300))
 

    # initial deal to player and dealer
    if initial_deal:
        
        for i in range(2):
            my_hand, game_deck = deal_cards(my_hand, game_deck)
            dealer_hand, game_deck = deal_cards(dealer_hand, game_deck)
        initial_deal = False

    # game active 
    if active:
        chip2.draw(screen) #top right chip
        chip1.update(dt)     #moving chip
        
        player_score = calculate_score(my_hand)
        draw_cards(my_hand, dealer_hand, reveal_dealer)
        if reveal_dealer:
            dealer_score = calculate_score(dealer_hand)
            if dealer_score < 17:
                dealer_hand, game_deck = deal_cards(dealer_hand, game_deck)
        draw_scores(player_score, dealer_score)
    buttons = draw_game(active, records, outcome)

    # event handling
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
                # if hand under 21, player can hit
                if buttons[0].collidepoint(event.pos) and player_score < 21 and hand_active:
                    my_hand, game_deck = deal_cards(my_hand, game_deck)
                # end turn, stand
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


    # if player busts turn is ended
    if hand_active and player_score >= 21:
        hand_active = False
        reveal_dealer = True

    outcome, records, add_score = check_endgame(hand_active, dealer_score, player_score, outcome, records, add_score)

    pygame.display.flip()
pygame.quit()




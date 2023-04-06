import random

lst_color = ('\x03', '\x04', '\x05', '\x06')
lst_values = ('As', 'Roi', 'Dame', 'Valet', 2, 3, 4, 5, 6, 7, 8, 9, 10)
lst_cards = []

lst_cards_dealer = []
lst_cards_player = []

value_dealer = 0
value_player = 0

cash = 200
to_bet = 0
quit_game = False
flag = False
i = -1

def init_cards() :
    global lst_cards
    global lst_color
    global lst_values
    lst_cards = []
    for i in range(13) :
        for j in range(4) :
            lst_cards.append(f"{lst_values[i]}{lst_color[j]}")
    random.shuffle(lst_cards)

def draw(list) :
    global i
    i += 1
    return list[i]

def get_value_cards(lst_cards, if_as) :
    # print(lst_cards)
    as_player = 0
    as_dealer = 0
    sum = 0
    for i in lst_cards :
        if i[:-1].isdigit() :
            sum += int(i[:-1])
        elif i[:-1] == "As" :
            sum += 11
            if if_as == 0:
                as_player += 1
            else :
                as_dealer += 1
        else :
            sum += 10
        # print(sum)
    if if_as == 0:
        while sum > 21 and as_player > 0 :
            # print(sum)
            sum += -10 
            as_player += -1
    else :
        while sum > 21 and as_dealer > 0 :
            # print(sum)
            sum += -10 
            as_dealer += -1
    # print(f"sum = {sum}")
    return sum

# def pretty_display(lst_cards):
#     temp_str = ''
#     for i in lst_cards :
#         temp_str += i + ' '
#     return temp_str[:-1]

def display_cards(who, lst_cards, value):
    x = f"{who} | {' '.join(lst_cards)} | {value}"
    return x

def player_win():
    global to_bet
    global cash
    print('Vous avez gagner')
    cash += to_bet
    to_bet = 0

def dealer_win():
    global to_bet
    global cash
    print('Vous avez perdu')
    cash += -to_bet
    to_bet = 0

def egality():
    global to_bet
    global cash
    print('Vous avez fait égalité')
    to_bet = 0

print("Aucune réponse équivaut a dire 'non' pour dire oui il suffit de rentrer nimporte quoi d'autre que du vide")
quit_game = input('voulez vous jouer ? : ')
while quit_game != '':

    value_dealer = 0
    value_player = 0
    lst_cards_dealer = []
    lst_cards_player = []
    
    print("-----(Mise)-----")
    print(f"vôtre solde est de {cash}")
    while to_bet > cash or to_bet <= 0:
        try:
            to_bet = int(input('combien voulez vous miser ? : '))
            break
        except ValueError:
            print("une valeur numérique s'il vous plait")
    print("----------------")
    
    init_cards()
    
    print("-----(Croupier)-----")
    lst_cards_dealer.append(draw(lst_cards))
    value_dealer = get_value_cards(lst_cards_dealer, 1)
    print(display_cards("Croupier", lst_cards_dealer, value_dealer))
    print("--------------------")
    
    print("-----(Joueur)-----")
    lst_cards_player.append(draw(lst_cards))
    value_player = get_value_cards(lst_cards_player, 0)
    print(display_cards("Joueur", lst_cards_player, value_player))
    print("------------------")
    
    player_continue = input("voulez vous continuer ?: ")
    while player_continue != "" :
        
        print("-----(Joueur)-----")
        lst_cards_player.append(draw(lst_cards))
        value_player = get_value_cards(lst_cards_player, 0)
        print(display_cards("Joueur", lst_cards_player, value_player))
        print("------------------")
        
        if value_player > 21 :
            dealer_win()
            break
        else :
            player_continue = input("voulez vous continuer ?: ")
    
    if value_player <= 21 :
        while value_dealer < 22 :
            print("-----(Croupier)-----")
            lst_cards_dealer.append(draw(lst_cards))
            value_dealer = get_value_cards(lst_cards_dealer, 1)
            print(display_cards("Croupier", lst_cards_dealer, value_dealer))
            print("--------------------")
            
            if value_dealer > 21 :
                player_win()
                break
            elif value_dealer == value_player :
                egality()
                break
            elif value_dealer > value_player:
                dealer_win()
                break
    
    print(f"vôtre solde est de {cash}")
    if cash > 0 :
        print("///////////////////////////////////////////////")
        quit_game = input('voulez vous continuer de jouer ? : ')
    else :
        print("vôtre solde ne vous permet plus de jouer")
        quit_game = ''

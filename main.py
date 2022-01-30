import dealer

d = dealer.Dealer()
d.greet()
while True:
    d.init_players()
    if not d.run_players(): break
    cls()

startingPoints = [int(line.strip().split(': ')[1]) for line in open("inputday21")]; players = len(startingPoints)
deterministicDie = lambda x:(((D:=lambda x,s:(x-1)%s+1)(x*3,100)+D(x*3-1,100)+D(x*3-2,100),1),)
quantumDie = lambda x: zip(range(3,10),[1,3,6,7,6,3,1])
def nextMove(player, dice, maxScore, pos, move, score, multiplier, moveCounts, winning, highscores):
  for roll, count in dice((players*move) - (players-player-1)):
    p = (pos + roll - 1) % 10 + 1
    s = score + p
    moveCounts.setdefault(move, 0)
    winning.setdefault(move, 0)
    moveCounts[move] += count * multiplier
    highscores[move] = max(highscores.get(move, 0), score)
    if s >= maxScore:
      winning[move] += count * multiplier
    else:
      nextMove(player, dice, maxScore, p, move + 1, s, count * multiplier, moveCounts, winning, highscores)
  return (winning, moveCounts, highscores)
play = lambda player, dice, maxScore, start: nextMove(player, dice, maxScore, start, 1, 0, 1, {}, {}, {})
practice = [play(player, deterministicDie, 1000, start) for player,start in enumerate(startingPoints)]
practiceTurns = [*map(max,map(lambda x:x[0],practice))]; loser = lambda scores: scores.index(max(scores))
winning, universes = zip(*[play(player, quantumDie, 21, start)[:2] for player,start in enumerate(startingPoints)])
notwinning = [{i:universes[p][i] - winning[p][i] for i in universes[p]} for p in range(players)]; prevPlayer = lambda x: (x-1)%players
prevTurn = lambda turns, player, turn: turns[player][turn] if player else (turns[prevPlayer(player)][turn-1] if turn > 1 else 1)
totalWinning = [[winning[p][i] * prevTurn(notwinning, p, i) for i in winning[p]] for p in range(players)]
print(practice[loser(practiceTurns)][2][min(practiceTurns)]*(min(practiceTurns)*2-1)*3, max(map(sum,totalWinning)))

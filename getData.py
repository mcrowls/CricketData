from bs4 import BeautifulSoup
import numpy as np
import requests


class Ball():
    def __init__(self, ballNo, ballDesc, ballExp):
        self.ballNo = ballNo
        self.ballDesc = ballDesc
        self.ballExp = ballExp
        return

    def sortBall(self, dict):

        def runsScored(self, dict):
            splitString = self.ballDesc.split(' to ')
            self.bowler = splitString[0]
            self.batsman = splitString[1].split(',')[0]
            self.runsScored = 0
            if '(no ball)' in splitString[1]:
                self.runsScored += 1
            else:
                self.runsScored += dict[splitString[1].split(' ')[1]]
            del self.ballDesc
            return

        def overAndBall(self):
            ballNum = self.ballNo.split('.')
            self.over = int(ballNum[0])
            self.ball = int(ballNum[1])
            del self.ballNo
            return
        
        runsScored(self, dict)
        overAndBall(self)
        return


def group(n, p, d, dict={'no': 0, '1': 1, '2': 2, '3': 3, 'FOUR': 4, 'SIX': 6, 'OUT': -1}):
    deliveries = []
    for i in range(len(n)):
        delivery = Ball(n[i], p[i], d[i])
        print(delivery)
        delivery.sortBall(dict)
        deliveries.append(delivery)
    return np.asarray(deliveries)
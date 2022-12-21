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
            self.runsScored = dict[splitString[1].split(' ')[1]]
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


def scrape(src, dict={'no': 0, '1': 1, '2': 2, '3': 3, 'FOUR': 4, 'SIX': 6, 'OUT': -1}):
    req = requests.get(src).text
    soup = BeautifulSoup(req, 'html.parser')
    balls = soup.find_all('div', class_="ds-text-tight-m ds-font-regular ds-flex ds-px-3 ds-py-2 lg:ds-px-4 lg:ds-py-[10px] ds-items-start ds-select-none lg:ds-select-auto")
    deliveries = []
    for ball in balls:
        desc = ball.find('div', class_="ds-leading-none ds-mb-0.5").text
        num = ball.find('span', class_="ds-text-tight-s ds-font-regular ds-mb-1 lg:ds-mb-0 lg:ds-mr-3 ds-block ds-text-center").text
        expl = ball.find('p', class_="ci-html-content").text
        delivery = Ball(num, desc, expl)
        delivery.sortBall(dict)
        deliveries.append(delivery)
    return np.asarray(deliveries)
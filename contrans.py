import numpy as np
import pandas as pd
import os


class contrans:
        def __init__(self):
                self.mypassword = os.getenv('mypassword')

        def get_votes(self):
                url = 'https://voteview.com/static/data/out/votes/HS118_votes.csv'
                votes = pd.read_csv(url)
                return votes
        
        def get_ideology(self):
                url = 'https://voteview.com/static/data/out/members/H118_members.csv'
                members = pd.read_csv(url)
                return members
import random
import tkinter as tk
from tkinter import messagebox
import pickle
import numpy as np


# 載入 Q 表
def load_q_table():
    with open("q_table.pkl", "rb") as f:
        return pickle.load(f)

Q_table = load_q_table()

# 參數設定
MAX_SCORE = 21
MAX_X1 = MAX_SCORE - 1
MAX_AI_SCORE = 31
ACTIONS = [0, 1]  # 0: 停牌, 1: 抽牌

def calculate_score(cards):
    score = 0
    aces = 0
    for card, suit in cards:  # 每張卡牌包含數字和花色
        if card == 1:
            aces += 1
            score += 11  # 初步計算A為11
        elif card > 10:
            score += 10  # J, Q, K 都當作 10 點
        else:
            score += card
    while score > 21 and aces:
        score -= 10  # 如果超過21，將A當作1點
        aces -= 1
    return score

def draw_card(player, cards):
    suit = random.choice(list(cards.keys()))
    card = random.choice(cards[suit])
    cards[suit].remove(card)
    player.append((card, suit))  # 把卡牌的數字和花色作為一個元組加入
    return player, cards

def init_game():
    cards = {
        'spades': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'hearts': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'diamonds': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'clubs': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    player_1 = []
    house = []
    return cards, player_1, house

def choose_action(player_score, player_hidden, house_score):
    X1 = max(0, player_score - player_hidden)
    house_score = min(house_score, MAX_AI_SCORE)

    # AI 若已達 21 點或超過玩家，強制停牌
    if house_score >= 21 or house_score > player_score:
        action = 0  # 停牌
    else:
        action = np.argmax(Q_table[X1][house_score])  # 根據 Q 表選擇動作

    return action

def house_action(house, player_1, cards, player_hidden):
    while True:
        player_score = calculate_score(player_1)
        house_score = calculate_score(house)
        action = choose_action(player_score, player_hidden, house_score)
        if action == 0:
            break
        else:
            house, cards = draw_card(house, cards)
            if calculate_score(house) > 21:
                break
    return house, cards  # 返回更新後的結果


class BlackJackGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("21點遊戲")
        self.geometry("600x500")
        self.cards, self.player_1, self.house = init_game()
        self.player_hidden = None

        # 使用字典來代表卡牌花色的 Unicode 字符
        self.suits = {
            'spades': '♠',  # 黑桃
            'hearts': '♥',  # 紅心
            'diamonds': '♦',  # 方塊
            'clubs': '♣'  # 梅花
        }

        # 設定背景顏色
        self.config(bg="#2e3b4e")

        # 玩家和莊家得分顯示
        self.player_score_label = tk.Label(self, text="玩家得分: 0", font=("Arial", 14), fg="white", bg="#2e3b4e")
        # self.player_score_label.pack(pady=10)
        self.player_score_label.pack_configure(pady=(100, 15)) 
        self.house_score_label = tk.Label(self, text="莊家得分: 0", font=("Arial", 14), fg="white", bg="#2e3b4e")
        self.house_score_label.pack(pady=10)

        # 玩家和莊家卡牌框架
        self.cards_frame = tk.Frame(self, bg="#2e3b4e")
        self.cards_frame.pack(pady=20)

        # 按鈕區域
        self.button_frame = tk.Frame(self, bg="#2e3b4e")
        self.button_frame.pack(side='bottom',pady=60)

        self.hit_button = tk.Button(self.button_frame, text="開始遊戲(Start)", command=self.start_game, font=("Arial", 12), bg="#4CAF50", fg="white", relief="raised")
        self.hit_button.grid(row=0, column=0, padx=10)

        self.hit_button = tk.Button(self.button_frame, text="抽卡 (Hit)", command=self.hit, font=("Arial", 12), bg="#4CAF50", fg="white", relief="raised")
        self.hit_button.grid(row=0, column=1, padx=10)

        self.stand_button = tk.Button(self.button_frame, text="停牌 (Stand)", command=self.stand, font=("Arial", 12), bg="#f44336", fg="white", relief="raised")
        self.stand_button.grid(row=0, column=2, padx=10)

        self.stand_button = tk.Button(self.button_frame, text="結束 (End)", command=self.close_game, font=("Arial", 12), bg="#f44336", fg="white", relief="raised")
        self.stand_button.grid(row=0, column=3, padx=10)

    def update_ui(self):
        player_score = calculate_score(self.player_1)
        house_score = calculate_score(self.house)
        self.player_score_label.config(text=f"玩家得分: {player_score}")
        self.house_score_label.config(text=f"莊家得分: {house_score}")

        # 更新玩家手牌顯示
        for widget in self.cards_frame.winfo_children():
            widget.destroy()  # 清除舊的卡牌顯示
        player_card_frame = tk.Frame(self.cards_frame, bg="#2e3b4e")
        player_card_frame.pack(pady=10)
        for card, suit in self.player_1:
            card_text = f"{self.suits[suit]} {card}"  # 顯示花色和數字
            tk.Label(player_card_frame, text=card_text, font=("Arial", 14), fg="white", bg="#2e3b4e").pack(side="left", padx=10)

        # 更新莊家手牌顯示
        house_card_frame = tk.Frame(self.cards_frame, bg="#2e3b4e")
        house_card_frame.pack(pady=10)
        for card, suit in self.house:
            card_text = f"{self.suits[suit]} {card}"  # 顯示花色和數字
            tk.Label(house_card_frame, text=card_text, font=("Arial", 14), fg="white", bg="#2e3b4e").pack(side="left", padx=10)


    def hit(self):
        self.player_1, self.cards = draw_card(self.player_1, self.cards)
        self.update_ui()
        if calculate_score(self.player_1) > 21:
            self.end_game("玩家爆掉！")
        elif len(self.player_1)>=5:
            self.end_game("五張牌合計小於21，玩家獲勝！")

    def stand(self):
        self.house, self.cards = house_action(self.house, self.player_1, self.cards, self.player_hidden)
        self.update_ui()  # 這裡會更新 UI
        player_score = calculate_score(self.player_1)
        house_score = calculate_score(self.house)
        if player_score > 21:
            self.end_game("玩家爆掉！")
        elif house_score > 21:
            self.end_game("莊家爆掉！")
        elif player_score > house_score:
            self.end_game("玩家獲勝！")
        elif player_score < house_score:
            self.end_game("莊家獲勝！")
        else:
            self.end_game("平局！")


    def end_game(self, result):
        messagebox.showinfo("遊戲結束", result)
    
    def close_game(self):
        self.quit()

    def start_game(self):
        self.cards, self.player_1, self.house = init_game()
        for _ in range(2):
            self.player_1, self.cards = draw_card(self.player_1, self.cards)
            self.house, self.cards = draw_card(self.house, self.cards)
        self.player_hidden = self.player_1[0][0]  # 取出卡牌數字
        self.update_ui()
        if calculate_score(self.player_1)==21:
            self.end_game('Black Jack!玩家獲勝！')
        if calculate_score(self.house)==21:
            self.end_game('Black Jack!莊家獲勝！')


if __name__ == "__main__":
    app = BlackJackGUI()
    app.mainloop()

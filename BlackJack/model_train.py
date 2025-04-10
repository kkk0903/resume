import numpy as np
import pickle
import matplotlib.pyplot as plt

# 參數設定
MAX_SCORE = 21 #玩家最大可能分數
MAX_AI_SCORE = 31  # AI 最大可能分數 (21 + 10)
MAX_X1 = MAX_SCORE - 1  # X1 = player_score - player_score_hidden，AI可見的玩家手牌上限
ACTIONS = [0, 1]  # 0: 停牌, 1: 抽牌
ALPHA = 0.001  # 學習率η
GAMMA = 0.9  # 折扣因子γ
EPSILON = 0.1  # 探索機率
EPISODES_PER_RUN = 500000  # 每次執行的訓練回合數

# 加載 Q 表（如果已經存在）
def load_q_table():
    try:
        with open("q_table.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return np.zeros((MAX_X1 + 1, MAX_AI_SCORE + 1, len(ACTIONS)))

# 加載訓練進度（回合數和 rewards）
def load_training_progress():
    try:
        with open("training_progress.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return 0, []  # 默認從第0回合開始，並且沒有任何訓練數據

# 儲存 Q 表
def save_q_table():
    with open("q_table.pkl", "wb") as f:
        pickle.dump(Q, f)
    print("Q-table saved.")

# 儲存訓練進度
def save_training_progress(episode, rewards):
    with open("training_progress.pkl", "wb") as f:
        pickle.dump((episode, rewards), f)
    print("Training progress saved.")

def get_reward(player_score, ai_score):
    if ai_score > MAX_SCORE:
        return -2  # 爆掉，失敗
    if ai_score > player_score:
        return 1   # AI 贏了
    elif ai_score < player_score:
        # if ai_score == 21:
        #     return 0.5
        # if ai_score == 20:
        #     return 0.35
        # if ai_score == 19:
        #     return 0.25
        return -1  # AI 輸了
    return 0  # 平手




        # X1 = player_score(random生成) - player_score_hidden(random生成)
        # state:(X1,ai_score) action:[0,1], reward由player_score與ai_score比較，試誤累積Q函數
        # 





def train_qlearning(start_episode=0):
    total_rewards = []  # 用來儲存每回合的回報
    for episode in range(start_episode, start_episode + EPISODES_PER_RUN):
        total_reward = 0  # 每回合的總回報
        player_score = np.random.randint(1, MAX_SCORE + 1)
        player_score_hidden = np.random.randint(1, 11)
        ai_score = np.random.randint(1, MAX_SCORE + 1)
        X1 = player_score - player_score_hidden

        done = False
        while not done:
            # EPSILON = max(0.1, 1 - (episode / (start_episode + EPISODES_PER_RUN)))  # 每回合減少

            if np.random.rand() < EPSILON:
                action = np.random.choice(ACTIONS)  # 探索
            else:
                action = np.argmax(Q[X1][ai_score])  # 利用

            if action == 1:  # 抽牌
                card = np.random.randint(1, 11)
                ai_score += card
            reward = get_reward(player_score, ai_score)
            total_reward += reward  # 累加每回合的回報
            next_X1 = X1
            next_ai_score = min(ai_score, MAX_AI_SCORE)
            
            # 更新 Q 表
            Q[X1][ai_score][action] += ALPHA * (reward + GAMMA * np.max(Q[next_X1][next_ai_score]) - Q[X1][ai_score][action])
            
            if ai_score >= MAX_SCORE or action == 0:
                done = True
        
        if episode % 1000 == 0:
            print(f"Episode {episode}/{start_episode + EPISODES_PER_RUN} finished")
        total_rewards.append(total_reward)  # 保存每回合的總回報

    return total_rewards  # 返回 total_rewards

def smooth_rewards(rewards, window=100):
    return np.convolve(rewards, np.ones(window)/window, mode='valid')

def plot_rewards(rewards):
    plt.plot(rewards)
    plt.title("Training Progress (Total Rewards)")
    plt.xlabel("Episodes")
    plt.ylabel("Total Rewards")
    plt.show()

if __name__ == "__main__":
    Q = load_q_table()  # 加載現有的 Q 表
    start_episode, rewards = load_training_progress()  # 加載訓練進度（從哪一回合開始，及已保存的rewards）
    
    # 從上次訓練的地方繼續
    rewards = train_qlearning(start_episode=start_episode)
    
    # 儲存 Q 表和訓練進度
    save_q_table()  
    save_training_progress(start_episode + EPISODES_PER_RUN, rewards)  # 更新訓練進度

    # 繪製學習曲線
    smoothed_rewards = smooth_rewards(rewards)
    plot_rewards(smoothed_rewards)

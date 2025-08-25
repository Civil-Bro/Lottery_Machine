# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 11:12:28 2025

@author: Ikun
"""

import pandas as pd
import random
import tkinter as tk
from tkinter import ttk
class LotteryMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("抽奖机")
        self.root.geometry("400x400")
        
        # 加载数据
        self.load_data()
        
        # 创建界面
        self.create_widgets()
        
    def load_data(self):
        # 读取CSV文件
        self.counttable = pd.read_csv('counttable.csv')
        # 删除Ciallo学长
        self.counttable = self.counttable[self.counttable['username'] != 'Ciallo学长']

        
    def create_widgets(self):
        # 主框架
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 标题
        title_label = ttk.Label(main_frame, text="抽奖机", font=("Arial", 16))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # 抽奖按钮
        self.lottery_button = ttk.Button(main_frame, text="开始抽奖", command=self.start_lottery)
        self.lottery_button.grid(row=1, column=0, columnspan=2, pady=10)
        
        # 结果显示
        self.result_label = ttk.Label(main_frame, text="点击按钮开始抽奖", font=("Arial", 14))
        self.result_label.grid(row=2, column=0, columnspan=2, pady=20)
        
        # 中奖历史
        history_label = ttk.Label(main_frame, text="中奖历史:", font=("Arial", 12))
        history_label.grid(row=3, column=0, sticky=tk.W, pady=5)
        
        # 历史列表
        self.history_listbox = tk.Listbox(main_frame, width=50, height=10)
        self.history_listbox.grid(row=4, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))
        
        # 配置网格权重
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # 初始化中奖历史
        self.winner_history = []
        
    def start_lottery(self):
        # 根据权重随机选择中奖者
        weights = self.counttable['count'].tolist()
        winner = random.choices(
            self.counttable['username'].tolist(),
            weights=weights,
            k=1
        )[0]
        
        # 显示中奖结果
        self.result_label.config(text=f"恭喜 {winner} 中奖!")
        
        # 添加到历史记录
        self.winner_history.append(winner)
        self.history_listbox.insert(tk.END, winner)
        
        # 滚动到最新记录
        self.history_listbox.see(tk.END)

# 创建主窗口并运行程序
if __name__ == "__main__":
    root = tk.Tk()
    app = LotteryMachine(root)
    root.mainloop()
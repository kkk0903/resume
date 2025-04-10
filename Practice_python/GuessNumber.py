{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2276f405-72de-4389-81ba-0929960a591d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['6', '2', '1', '8']\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "請輸入四位不重複的數字開始遊戲，結束遊戲請輸入\"end\" sad\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wrong input\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "請輸入四位不重複的數字開始遊戲，結束遊戲請輸入\"end\" gsgf\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wrong input\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "請輸入四位不重複的數字開始遊戲，結束遊戲請輸入\"end\" qaz\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Wrong input\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "請輸入四位不重複的數字開始遊戲，結束遊戲請輸入\"end\" 6218\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4 A 0 B\n",
      "Correct!\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "x=[str(i) for i in range(0,10)]\n",
    "answer=random.sample(x,4)\n",
    "print(answer)\n",
    "while True:\n",
    "    n=input('請輸入四位不重複的數字開始遊戲，結束遊戲請輸入\"end\"')\n",
    "    if n.lower()=='end':\n",
    "        print('Game over')\n",
    "        break\n",
    "    if (len(n)!=len(set(n))) or len(n)!=4 or n.isdigit()!=True:\n",
    "        print('Wrong input')\n",
    "        continue\n",
    "\n",
    "    A=0\n",
    "    B=0\n",
    "    for i in range(4):\n",
    "        for j in range(4):\n",
    "            if n[i]==answer[j]:\n",
    "                if n[i]==answer[i]:\n",
    "                    A+=1\n",
    "                else:\n",
    "                    B+=1\n",
    "    print(A,\"A\",B,'B')\n",
    "    if A==4:\n",
    "        print('Correct!')\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "5623e76f-f977-4e71-812e-9cc944df1c70",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "歡迎來到 4 位數字猜測遊戲！輸入 'end' 可結束遊戲。\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "請輸入四位不重複的數字:  111\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "輸入錯誤，請輸入四位不重複的數字。\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "請輸入四位不重複的數字:  1234\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0A0B\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "請輸入四位不重複的數字:  5678\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1A2B\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "請輸入四位不重複的數字:  90\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "輸入錯誤，請輸入四位不重複的數字。\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "請輸入四位不重複的數字:  1290\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1A0B\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "請輸入四位不重複的數字:  1294\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1A0B\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "請輸入四位不重複的數字:  1234\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0A0B\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "請輸入四位不重複的數字:  1294\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1A0B\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "請輸入四位不重複的數字:  5123\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0A1B\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "請輸入四位不重複的數字:  1623\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1A0B\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "請輸入四位不重複的數字:  5978\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0A3B\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "請輸入四位不重複的數字:  5698\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2A1B\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "請輸入四位不重複的數字:  7695\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4A0B\n",
      "恭喜！你猜對了！\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "def generate_answer():\n",
    "    return \"\".join(map(str, random.sample(range(10), 4)))\n",
    "\n",
    "def calculate_AB(guess, answer):\n",
    "    A = sum(1 for i in range(4) if guess[i] == answer[i])\n",
    "    B = sum(1 for digit in guess if digit in answer) - A\n",
    "    return A, B\n",
    "\n",
    "def main():\n",
    "    answer = generate_answer()\n",
    "    print(\"歡迎來到 4 位數字猜測遊戲！輸入 'end' 可結束遊戲。\")\n",
    "    \n",
    "    while True:\n",
    "        guess = input(\"請輸入四位不重複的數字: \")\n",
    "        \n",
    "        if guess.lower() == \"end\":\n",
    "            print(f\"遊戲結束，答案是 {answer}\")\n",
    "            break\n",
    "        \n",
    "        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:\n",
    "            print(\"輸入錯誤，請輸入四位不重複的數字。\")\n",
    "            continue\n",
    "        \n",
    "        A, B = calculate_AB(guess, answer)\n",
    "        print(f\"{A}A{B}B\")\n",
    "        \n",
    "        if A == 4:\n",
    "            print(\"恭喜！你猜對了！\")\n",
    "            break\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a178d554-f049-4048-9232-36a2bd3fe15e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['2', '1', '9', '3']\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "請輸入四位不重複的數字開始遊戲，結束遊戲請輸入\"end\" 2193\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4 A 0 B\n",
      "Correct!\n"
     ]
    }
   ],
   "source": [
    "def guessNumber():\n",
    "    import random\n",
    "    x=[str(i) for i in range(0,10)]\n",
    "    answer=random.sample(x,4)\n",
    "    print(answer)\n",
    "    while True:\n",
    "        n=input('請輸入四位不重複的數字開始遊戲，結束遊戲請輸入\"end\"')\n",
    "        if n.lower()=='end':\n",
    "            print('Game over')\n",
    "            break\n",
    "        if (len(n)!=len(set(n))) or len(n)!=4 or n.isdigit()!=True:\n",
    "            print('Wrong input')\n",
    "            continue\n",
    "    \n",
    "        A=0\n",
    "        B=0\n",
    "        for i in range(4):\n",
    "            for j in range(4):\n",
    "                if n[i]==answer[j]:\n",
    "                    if n[i]==answer[i]:\n",
    "                        A+=1\n",
    "                    else:\n",
    "                        B+=1\n",
    "        print(A,\"A\",B,'B')\n",
    "        if A==4:\n",
    "            print('Correct!')\n",
    "            break\n",
    "guessNumber()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c6694604-dbd3-40ba-89bf-e8578184bf8a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

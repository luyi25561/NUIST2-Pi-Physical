#Author:Lu Yi and Tan Zihao
import RPi.GPIO as GPIO
import time

# 初始化GPIO
GPIO.setmode(GPIO.BCM)  # 使用BCM引脚编号规则
GREEN_PIN = 17  # 绿灯接GPIO17
RED_PIN = 18    # 红灯接GPIO18
# 设置引脚为输出模式，初始低电平（灯灭）
GPIO.setup(GREEN_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RED_PIN, GPIO.OUT, initial=GPIO.LOW)

def quiz_led():
    print("Welcome to the Python Basic Quiz!")
    print("Answer the following questions (input the option letter, e.g. a):")
    # 问题、选项、正确答案
    questions = [
        "1. Which of the following is NOT a python data type?\na) int\nb) float\nc) rational\nd) string\ne) bool",
        "2. Which of the following is NOT a built-in operation in Python?\na) +\nb) %\nc) abs()\nd) sqrt()",
        "3. In a mixed-type expression involving ints and floats, Python will convert:\na) floats to ints\nb) ints to strings\nc) floats and ints to strings\nd) ints to floats",
        "4. The best structure for implementing a multi-way decision in Python is:\na) if\nb) if-else\nc) if-elif-else\nd) ury",
        "5) What statement can be executed in the body of a loop to cause it to terminate?\na) if\nb) exit\nc) continue\nd) break"
    ]
    answers = ["c", "d", "d", "c", "d"]
    score = 0

    # 循环答题
    for i in range(len(questions)):
        # 每次答题前确保灯灭
        GPIO.output(GREEN_PIN, GPIO.LOW)
        GPIO.output(RED_PIN, GPIO.LOW)
        user_ans = input(f"\n{questions[i]}\nYour answer: ").strip().lower()
        # 判断答案并控制LED
        if user_ans == answers[i]:
            print("Correct!")
            GPIO.output(GREEN_PIN, GPIO.HIGH)  # 绿灯亮
            score += 1
        else:
            print("Incorrect!")
            GPIO.output(RED_PIN, GPIO.HIGH)    # 红灯亮
        time.sleep(1.5)  # 灯亮1.5秒，方便观察

    # 小测结束，灯灭，输出分数
    GPIO.output(GREEN_PIN, GPIO.LOW)
    GPIO.output(RED_PIN, GPIO.LOW)
    print(f"\nQuiz completed! You got {score}/{len(questions)} questions correct.")
    # 清理GPIO设置，释放引脚
    GPIO.cleanup()

# 运行带LED的小测函数
if __name__ == "__main__":
    quiz_led()
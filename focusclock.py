import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print(f"Remaining: {seconds // 60} min {seconds % 60} sec")
        time.sleep(1)
        seconds -= 1
    print("Time's up! Focus on your work now.")

focus_timer(25) # 设置专注时间为25分钟

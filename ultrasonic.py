import pigpio
import time

# GPIOピン番号
PIN_A = 17
PIN_B = 18

# pigpioに接続
pi = pigpio.pi()

# 出力として設定
pi.set_mode(PIN_A, pigpio.OUTPUT)
pi.set_mode(PIN_B, pigpio.OUTPUT)

# 最初は両方LOW
pi.write(PIN_A, 0)
pi.write(PIN_B, 0)

FREQUENCY = 41000  # Hz
PERIOD_US = 1000000 // FREQUENCY  # マイクロ秒単位の周期
QUARTER_PERIOD_US = PERIOD_US // 4  # 周期の1/4

try:
    print(f"周波数: {FREQUENCY}Hz, 周期: {PERIOD_US}マイクロ秒")
    print(f"各状態の時間: {QUARTER_PERIOD_US}マイクロ秒")
    
    while True:
        # 状態1: PIN_A HIGH, PIN_B LOW
        pi.write(PIN_A, 1)
        pi.write(PIN_B, 0)
        time.sleep(QUARTER_PERIOD_US / 1000000)
        
        # 状態2: 両方LOW（デッドタイム）
        pi.write(PIN_A, 0)
        pi.write(PIN_B, 0)
        time.sleep(QUARTER_PERIOD_US / 1000000)

        # while if time の　調整　Add 2025.03.27
        time.sleep(QUARTER_PERIOD_US / 1000000)


        
        # 状態3: PIN_A LOW, PIN_B HIGH
        pi.write(PIN_A, 0)
        pi.write(PIN_B, 1)
        time.sleep(QUARTER_PERIOD_US / 1000000)
        
        # 状態4: 両方LOW（デッドタイム）
        pi.write(PIN_A, 0)
        pi.write(PIN_B, 0)
        time.sleep(QUARTER_PERIOD_US / 1000000)
        
except KeyboardInterrupt:
    print("プログラム終了")
finally:
    pi.write(PIN_A, 0)
    pi.write(PIN_B, 0)
    pi.stop()
  

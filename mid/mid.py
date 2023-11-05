# 1. 請使用函數print出自己的姓名, 學號, 與今天日期, 並且遵照下列格式
"""
Display personal info.

score:
    Name(str): 10%
    Id(int): 10%
    Date(str): use function 10%, if not 5%
"""


# 2. 請生成一個合乎規則的信用卡資訊, 其中最少必須包括卡號, 有效日期, 安全碼
#    並且將其中資訊全部放於一個字典之中
"""
Create, verify, and display credit card info.

score:
    credit_card_info(dict): 2%
        Valid card number(int): 20%
        Exp. date(str): 3%
        CVV code(int): 3%
        other detail info: 2%
"""

# 3. 龍與地下城文字小遊戲
# step 1: 創造角色, 並且隨機生成能力值
#       1.1 輸入角色名稱, 種族, 職業
#       1.2 根據角色種族, 職業生成能力值
#
# step 2: 冒險: 打贏兩次戰鬥算獲勝, 反之則失敗, 或是連走三格也算獲勝
#       2.1 每次行動都必須擲骰子, 6: 安全通過, 5~2: 遇到一隻怪物, 1: 遇到兩隻
#       2.2 戰鬥採猜拳方式, 一樣擲骰子, 6~5: 勝利; 4~3: 平手; 2~1: 失敗

# 必須驗證輸入的內容
# 骰子只有六面
# 數值會影響骰子的結果
"""
Dungeons & Dragons game.

score:
    Character(dict): 
        Id(str): (姓名不得超過20個字)
        Race(str): ('人類', '矮人', '精靈') 5%
        Class(str): ('戰士', '遊俠', '法師') 5%
        Ability scores(dict): 
            (力量(STR)(int), 敏捷(DEX)(int), 智慧(INT)(int)): 10%

            基本: {STR, DEX, INT}
            人類: {50, 50, 50}
            矮人: {70, 50, 30}
            精靈: {30, 70, 50}

            戰士: {1.3, 1, 0.9}
            遊俠: {0.9, 1.3, 1}
            法師: {0.9, 1, 1.3}

            E.g.
            role = {
                    "id": "role1",
                    "race": "人類",
                    "class": "戰士",
                    "ability": {"STR": 65, "DEX": 50, "INT": 45},
            }

    Adventure(function): 15%
        數值影響: 5%
            如果力量(STR)越高越容易在戰鬥中骰到5或6, 反之則容易骰到1或2
            如果敏捷(DEX)越高越容易骰到通過, 反之則不容易

"""


def midexam_info():
    print("第一題: 30%")
    print("第二題: 30%")
    print("第三題: 40%")
    print("加油!")
    print("繳交期限: 11/12 23:59")


if __name__ == "__main__":
    midexam_info()

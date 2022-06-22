"""
P1.1 图像处理子系统
"""
import json


def analyze_img(img):
    """

    :param img: 就是要识别的图片
    :return:
    """
    pass  # TODO 调用安全帽识别系统

    # 之后返回x个hat，y个person，以及把握
    hat = []  # TODO
    person = []  # TODO
    hat_num = len(hat)
    person_num = len(person)

    # 形成警示语句
    notice = f"有{person_num}人疑似未佩戴安全帽！\n请根据图像前往核实并记录！"

    return notice


def punish(person_id: str):
    # 读取文件
    with open("assets/punishment.json", "r") as jsn:
        dic = json.load(jsn)

        if __name__ == '__main__':
            print(dic)

    if person_id in dic:
        dic[person_id] += 1
    else:
        dic[person_id] = 1

    # 写入文件
    with open("assets/punishment.json", "w") as jsn:
        json.dump(dic, jsn, indent=4)


if __name__ == '__main__':
    punish("091901429")

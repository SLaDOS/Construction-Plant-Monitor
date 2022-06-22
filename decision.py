"""
P1.3 决策系统
"""
import json
import params


def over_threshold(value_: int):
    """
    判断是否超过阈值，若是超过就要发起询问，跳出界面给项目负责人决策（我们假设这个负责人不在工地，是坐办公室的）

    :param value_: 这个是传入的，待判断的数值
    :return: True or False
    """
    if value_ >= params.THRESHOLD:
        request_for_decision()
        return True
    return False


def request_for_decision(converser):
    """
    用来发起询问项目负责人，详细数据让他去自行查看

    :return: none
    """
    converser.ui.label_13.setText('危险！风险系数高！\n                    请作出决策：')


def make_announcement(lenth):
    """
    BOSS点了确定以后，就要按照他输入的参数形成停工的通知

    :param lenth:
    :return:
    """

    # 写入文件
    with open("assets/suspend.json", "w") as jsn:
        dic = {"停工时长(天)": lenth, }
        json.dump(dic, jsn, indent=4)


def values_for_boss():
    """
    返回各种参数，给项目负责人看

    :return: 用来计算风险指数的所有参数
    """
    # TODO

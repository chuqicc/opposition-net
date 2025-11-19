'''
Author: Dani Mac chuqicc@gmail.com
Date: 2025-03-06 10:31:09
LastEditors: DANI WIN chenc98@univie.ac.at
LastEditTime: 2025-06-12 15:49:01
FilePath: /nba data/project/00_Draw_fullcourt_NBA.py
Description: using sportypy to draw a full court NBA
'''
# import nba court
import matplotlib.pyplot as plt
from sportypy.surfaces.basketball import NBACourt # type: ignore
colors_dict = {
    'plot_background': '#d2ab6f00',       # 绘图背景 - 透明
    "offensive_half_court": "#e8e0d7",     # 进攻半场 - 米白色/浅米色
    "defensive_half_court": "#e8e0d7",     # 防守半场 - 米白色/浅米色
    "court_apron": "#d2ab6f00",              # 场地围裙/边缘 - 透明

    "center_circle_outline": "#13294b",   # 中圈轮廓 - 深蓝色
    "center_circle_fill": "#e8e0d7",
    "center_circle_fill": "#e8e0d7",         # 中圈填充 - 透明
    "sideline": "#13294b",                 # 边线 - 深蓝色
    "endline": "#13294b",                  # 底线 - 深蓝色
    "division_line": "#13294b",            # 分界线/中场线 - 深蓝色

    "painted_area": ["#e8e0d7", "#ffffff00"],  # 禁区区域 - 米白色和完全透明
    "lane_boundary": ["#ffffff", "#ffffff00"],  # 禁区边界 - 白色和完全透明

    "two_point_range": ["#e8e0d7", "#ffffff66"],  # 两分区域 - 米白色和半透明白色
    "three_point_line": ["#13294b", "#ffffff"],  # 三分线 - 深蓝色和白色

    "free_throw_circle_outline": "#ffffff", # 罚球圈轮廓 - 白色
    "free_throw_circle_dash": "#ffffff",   # 添加这个设置罚球圈虚线部分
    "free_throw_circle_fill": "#e8e0d7",   # 罚球圈填充 - 米白色/浅米色

    "lane_space_mark": "#ffffff",           # 禁区间距标记 - 白色
    'inbounding_line': '#000000',           # 出界线 - 黑色
    "substitution_line": "#ffffff",         # 替补席线 - 白色

    'baseline_lower_defensive_box': '#d2ab6f00',  # 底线下的防守区 - 透明
    'lane_lower_defensive_box': '#d2ab6f00',  # 禁区下的防守区 - 透明

    'team_bench_line': '#13294b',           # 球队替补席线 - 深蓝色
    "restricted_arc": "#e8e0d7",            # 限制弧线 - 米白色/浅米色
    "backboard": "#13294b",                 # 篮板 - 深蓝色
    'basket_ring': '#f55b33',               # 篮筐 - 橙色
    'net': '#ffffff',                      # 篮网 - 白色
}

color_updates = colors_dict  # Use the colors_dict for color updates

court = NBACourt(color_updates=color_updates)

# print(court._features)  # 查看绘制的元素
court.court_params['lane_lower_defensive_box_marks_visibility'] = False

# 直接修改内圈填充对象的plot_kwargs
# 修改所有中心圈对象
for idx, feature in enumerate(court._features):
    # 修改内圈填充为米白色
    if 'CenterCircleFill' in str(type(feature)):
        if feature.feature_radius == 2.1667:  # 这是内圈
            print(f"修改内圈填充对象: {idx}")
            feature.color = "#e8e0d7"
            feature.plot_kwargs['facecolor'] = "#e8e0d7"
    # 修改内圈轮廓为米白色
    elif 'CenterCircleOutline' in str(type(feature)):
        if feature.feature_radius == 2.1667:  # 这是内圈轮廓
            print(f"修改内圈轮廓对象: {idx}")
            feature.color = "#e8e0d7"  # 改为米白色
            feature.plot_kwargs['facecolor'] = "#e8e0d7"  # 改为米白色
        else:
            # 保持外圈轮廓为深蓝色
            feature.color = "#13294b"
            feature.plot_kwargs['facecolor'] = "#13294b"

'''
for idx, feature in enumerate(court._features):
    if 'CenterCircle' in str(type(feature)):
        print(f"对象 {idx}: {feature}")
        # 尝试打印对象的所有属性
        for attr in dir(feature):
            if not attr.startswith('_') and not callable(getattr(feature, attr)):
                print(f"  {attr}: {getattr(feature, attr)}")
'''

court.draw()
# output_path = r'E:\workspace_chuqi\phd_nba\fullcourtnba.png'
# plt.savefig(output_path, dpi=300)
plt.show()

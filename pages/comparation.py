import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# 创建DataFrame存储数据
data = {
    ('ETH-ADE'): [0.81, 0.36, 0.39, 0.39],
    ('ETH-FDE'): [1.52, 0.65, 0.83, 0.66],
    ('HOTEL-ADE'): [0.72, 0.17, 0.12, 0.13],
    ('HOTEL-FDE'): [1.61, 0.36, 0.21, 0.22],
    ('UNIV-ADE'): [0.60, 0.31, 0.20, 0.22],
    ('UNIV-FDE'): [1.26, 0.62, 0.44, 0.45],
    ('ZARA1-ADE'): [0.34, 0.26, 0.15, 0.17],
    ('ZARA1-FDE'): [0.69, 0.55, 0.33, 0.30], 
    ('ZARA2-ADE'): [0.42, 0.22, 0.11, 0.13], 
    ('ZARA2-FDE'): [0.84, 0.46, 0.25, 0.27]
}
index = ['Social GAN', 'STAR', 'Trajectron++', 'MID']
df = pd.DataFrame(data, index=index)

# 设置页面标题和背景颜色
st.set_page_config(page_title="表格展示", page_icon=":chart:", layout="wide")
st.markdown(
    "<h1 style='text-align: center; color: #ff6347;'>MID与其他方法对比</h1>",
    unsafe_allow_html=True
)

# 展示具有自定义样式的表格
st.write("<style>table {margin: auto;text-align: center;}</style>", unsafe_allow_html=True)
st.write(df)

st.write("**Social-GAN**: Agrim Gupta, Justin Johnson, Li Fei-Fei, Silvio Savarese,\
and Alexandre Alahi. Social gan: Socially acceptable trajectories with generative adversarial networks. In **CVPR**, pages\
2255–2264, 2018.")
st.write("**STAR**: Cunjun Yu, Xiao Ma, Jiawei Ren, Haiyu Zhao, and Shuai Yi.\
Spatio-temporal graph transformer networks for pedestrian\
trajectory prediction. In **ECCV**, August 2020.")
st.write("**Trajectron++**: Tim Salzmann, Boris Ivanovic, Punarjay Chakravarty, and\
Marco Pavone. Trajectron++: Dynamically-feasible trajectory forecasting with heterogeneous data. In **ECCV**, 2020.")
# st.write("**MID**: ")

df = pd.DataFrame(data)
st.write("")
st.write("")
st.write("")

# 使用st.columns创建两列布局
col1, col2 = st.columns(2)

# 在第一列显示内容
with col1:
    # 提取对应算法的数据
    social_gan_data = [data[('ETH-ADE')][0], data[('HOTEL-ADE')][0], data[('UNIV-ADE')][0], data[('ZARA1-ADE')][0], data[('ZARA2-ADE')][0]]
    star_data = [data[('ETH-ADE')][1], data[('HOTEL-ADE')][1], data[('UNIV-ADE')][1], data[('ZARA1-ADE')][1], data[('ZARA2-ADE')][1]]
    trajectron_data = [data[('ETH-ADE')][2], data[('HOTEL-ADE')][2], data[('UNIV-ADE')][2], data[('ZARA1-ADE')][2], data[('ZARA2-ADE')][2]]
    mid_data = [data[('ETH-ADE')][3], data[('HOTEL-ADE')][3], data[('UNIV-ADE')][3], data[('ZARA2-ADE')][3], data[('ZARA2-ADE')][3]]
    index = ['ETH', 'HOTEL', 'UNIV', 'ZARA1', 'ZARA2']
    fig, ax = plt.subplots()
    ax.plot(index, social_gan_data, label='Social GAN')
    ax.plot(index, star_data, label='STAR')
    ax.plot(index, trajectron_data, label='Trajectron++')
    ax.plot(index, mid_data, label='MID')

    plt.xlabel('Scenarios')
    plt.ylabel('Values')
    plt.title('Performance of Different Models(ADE)')
    plt.legend()
    st.pyplot(fig)
    # st.write("")

# 在第二列显示内容
with col2:
   # 筛选出ADE结尾的列数据
    social_gan_data = [data[('ETH-ADE')][0], data[('HOTEL-ADE')][0], data[('UNIV-ADE')][0], data[('ZARA1-ADE')][0], data[('ZARA2-ADE')][0]]
    star_data = [data[('ETH-ADE')][1], data[('HOTEL-ADE')][1], data[('UNIV-ADE')][1], data[('ZARA1-ADE')][1], data[('ZARA2-ADE')][1]]
    trajectron_data = [data[('ETH-ADE')][2], data[('HOTEL-ADE')][2], data[('UNIV-ADE')][2], data[('ZARA1-ADE')][2], data[('ZARA2-ADE')][2]]
    mid_data = [data[('ETH-ADE')][3], data[('HOTEL-ADE')][3], data[('UNIV-ADE')][3], data[('ZARA2-ADE')][3], data[('ZARA2-ADE')][3]]
    index = ['ETH', 'HOTEL', 'UNIV', 'ZARA1', 'ZARA2']
    fig, ax = plt.subplots()
    ax.plot(index, social_gan_data, label='Social GAN')
    ax.plot(index, star_data, label='STAR')
    ax.plot(index, trajectron_data, label='Trajectron++')
    ax.plot(index, mid_data, label='MID')

    plt.xlabel('Scenarios')
    plt.ylabel('FDE')
    plt.title('Performance of Different Models(FDE)')
    plt.legend()
    st.pyplot(fig)
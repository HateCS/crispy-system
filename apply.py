import streamlit as st
import os



#########
#SIDEBAR
########
st.sidebar.header('从以下场景选择查看 :crystal_ball:')
nav = st.sidebar.radio('',['Home', '操场', '足球场', '校园内道路'])
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')

#CONTACT
########
expander = st.sidebar.expander('Contact')
expander.write("I'd love your feedback :smiley: Want to collaborate? Develop a project? Find me at \
                2020211314@bupt.cn")


#HOME
if nav == 'Home':
    # st.title("MID应用效果展示")
    st.markdown("<h4 style='text-align: center; color:grey;'>MID应用效果展示 &#129302;</h4>", unsafe_allow_html=True)
    st.header('', divider='rainbow')
    # st.header('_Streamlit_ is :blue[cool] :sunglasses:')

    st.write("选定了三个场景，分别为操场、足球场、校园内道路，以下是3个场景的简介")

    # st.divider()
    st.subheader("操场", divider='grey')
    st.write("本场景从北京邮电大学操场看台拍摄，时长约为半分钟")
    st.write("评估结果ADE(平均位移距离): 0.39    FDE(最终位移距离): 0.60")
    st.divider()

    st.subheader("足球场", divider='gray')
    st.write("本场景从北京邮电大学操场看台拍摄，时长约为半分钟")
    st.write("评估结果ADE(平均位移距离): 0.64    FDE(最终位移距离): 1.07")
    st.divider()

    st.subheader("校园内道路", divider='grey')
    st.write("本场景从北京邮电大学一宿舍楼阳台拍摄，时长约为一个小时二十分钟")
    st.write("评估结果ADE(平均位移距离): 0.21  FDE(最终位移距离): 0.41")
    st.divider()



if nav == '足球场':    
    st.markdown("<h4 style='text-align: center; color:grey;'>足球场 &#129302;</h4>", unsafe_allow_html=True)
    st.subheader("MID应用于足球运动",divider="rainbow")
    # st.header('This is a header with a divider', divider='rainbow')
    # st.header('_Streamlit_ is :blue[cool] :sunglasses:')

    st.caption("本视频拍摄于北京邮电大学操场，视频中主要为五人在进行足球运动，本轨迹预测模型在这五人的轨迹上进行工作。数据全部为手工标注")
    col1, col2 = st.columns(2)
    with col1:
        video_file = open('soccer1.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
    with col2:
        st.image("soccer.png")

    # 对照样例
    st.subheader("下面是一个视频与预测图的对照样例",divider="rainbow")
    video_file = open('soccer1.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)
    # 使用st.columns创建两列布局
    col1, col2 = st.columns(2)
    with col1:
        st.caption("图例如下")
        st.image("legend.png")

    with col2:
        st.caption("轨迹图如下")
        st.image("./vis/soccer1/pred_69.png",use_column_width=True)
    st.divider()

    st.subheader("其余的轨迹图如下所示",divider="rainbow")
    folder_path = r'.\vis\soccer1'  # 替换为您的文件夹路径
    # 列出文件夹中的所有文件
    file_list = os.listdir(folder_path)
    # 展示每张图片
    for file_name in file_list:
        if file_name.endswith('.png') or file_name.endswith('.jpg'):
            image_path = os.path.join(folder_path, file_name)
            st.image(image_path, caption=file_name, use_column_width=True)
    st.balloons()

if nav == '校园内道路':
    st.markdown("<h4 style='text-align: center; color:grey;'>校园内道路 &#129302;</h4>", unsafe_allow_html=True)
    st.write("本场景下的数据区别于之前的手工标注，借助了本机部署的YOLO模型")
    st.write("原视频较大，加载花费时间太长，这里只截取一段")
    # 如果打开会直接卡死 QAQ
    # st.video("C0039.mp4")
    # st.caption("图例说明")
    # st.image("legend.png")
    st.image("sushe.png")

    st.subheader("部分轨迹图如下所示",divider="rainbow")
    folder_path = r'.\vis\univ'  # 替换为您的文件夹路径
    # 列出文件夹中的所有文件
    file_list = os.listdir(folder_path)
    # 展示每张图片
    for file_name in file_list:
        if file_name.endswith('.png') or file_name.endswith('.jpg'):
            image_path = os.path.join(folder_path, file_name)
            st.image(image_path, caption=file_name, use_column_width=True)

    col1,col2 = st.columns(2)

    st.balloons()
       
if nav == '操场':
    st.markdown("<h4 style='text-align: center; color:grey;'>操场 &#129302;</h4>", unsafe_allow_html=True)
    st.subheader("本视频拍摄于北京邮电大学操场，本轨迹预测模型模型选取了视频中两位绕操场跑步的同学和一个漫步的小朋友。数据全部为手工标注",divider="rainbow")

    video_file = open('walk1.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)

    st.divider()

    st.subheader("下面是一个视频与预测图的对照样例",divider="rainbow")
    video_file = open('walk1_cutter.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)
    # 使用st.columns创建两列布局
    col1, col2 = st.columns(2)
    with col1:
        st.caption("图例如下")
        st.image("legend.png")

    with col2:
        st.caption("轨迹图如下")
        st.image("./vis/walk1/pred_19.png",use_column_width=True)
    st.divider()
    st.subheader("其余的轨迹图如下所示",divider="rainbow")
    folder_path = r'.\vis\walk1'  # 替换为您的文件夹路径
    # 列出文件夹中的所有文件
    file_list = os.listdir(folder_path)
    # 展示每张图片
    for file_name in file_list:
        if file_name.endswith('.png') or file_name.endswith('.jkcpg'):
            image_path = os.path.join(folder_path, file_name)
            st.image(image_path, use_column_width=True)
    st.balloons()


import cv2
import os
import sys

image_base_path = "D:\\python3.7\\images\\";

def get_images(video_path):
    #如果是循环，则取消该行注释，将下一行注释掉
    #frame_times = -1
    frame_times = 15000
    fileName = video_path.split("\\")[-1:][0].split('.')[0]
    image_out_path = image_base_path + fileName
    if not os.path.exists(image_out_path):
        os.makedirs(image_out_path) 

    cap = cv2.VideoCapture(video_path)
    #帧率(frames per second)
    video_fps = cap.get(cv2.CAP_PROP_FPS)
    #总帧数(frames)
    total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    #总时长
    total_times = int(total_frames / video_fps)
    print("+---- 当前视频帧率为:" + str(video_fps) + "\n" + "+---- 总计帧数为:" + str(total_frames) + "\n" + "+---- 视频时长为:" + str(total_times))
    
    user_select = input("是否继续执行(y)或者(n)")
    if (user_select == "y"):
        print("继续执行")
    elif (user_select == "n"):
        sys.exit()

    #从此处开始是循环提取所有帧
    while cap.isOpened():
        frame_times = frame_times + 1
        success, frame = cap.read()
        if not success:
            break;

        cv2.imencode('.jpg', frame)[1].tofile(image_out_path + "\\" + str(frame_times) + ".jpg")
        print("已完成帧数" + str(frame_times), end='\r')
    
    print("+---- 提取完成，共生成" + str(frame_times) + "个图片")
    '''
    #从此处开始是提取特定帧
    while cap.isOpened():
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_times)
        success, frame = cap.read()
        #停止帧写入，如果再写就是空白
        if not success:
            break
        cv2.imencode('.jpg', frame)[1].tofile(image_out_path + "\\" + str(frame_times) + ".jpg")
        break
    '''

if __name__ == '__main__':
    get_images('D:\\python3.7\\11.mp4')
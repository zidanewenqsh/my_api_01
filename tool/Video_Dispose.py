import torch.nn as nn
import cv2 as cv
import os
import glob

class Video_Img():
    def __init__(self,video_path,video_name,save_path):
        super(Video_Img, self).__init__()
        self.save_path=save_path
        self.video_name=video_name
        self.cap=cv.VideoCapture(os.path.join(video_path,video_name))

    def Go(self):
        num=0
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)
        while self.cap.isOpened():
            num+=1
            judge,img=self.cap.read()
            if judge:
                #if num%(25//self.fps)==0:
                    # img=img.transpose(1,0,2)
                    cv.imwrite(os.path.join(self.save_path, "{0}-{1}.jpg".format(self.video_name,num)), img)
                    cv.waitKey(1)
            else:
                break
        self.cap.release()
        cv.destroyAllWindows()

class Img_Video:
    def __init__(self,img_path,fps):
        self.img_path=img_path
        self.fps=fps
        fourcc=cv.VideoWriter_fourcc(*"MJPG")
        self.VideoWriter=cv.VideoWriter("video_YoloV3_2.avi",fourcc,fps,(416,416))

    def Go(self):
        # imgs=glob.glob(self.img_path+"\*.jpg")
        num=0
        for i,img_name in enumerate(os.listdir(self.img_path)):
            #int(25//self.fps)
            #print(os.path.join(self.img_path,"{0}.jpg".format(str(num))))
            # newname = "pic_%03d.jpg" % i
            newname = "%d_0.jpg" % i
            print(newname)
            img_read=cv.imread(os.path.join(self.img_path,newname))
            # img_read=cv.resize(img_read,(416,416))
            # cv.imshow("img",img_read)
            # cv.waitKey(1)
            self.VideoWriter.write(img_read)
        self.VideoWriter.release()
        cv.destroyAllWindows()


if __name__ == '__main__':
    # video_path=r"F:\Test_File\Center_Classify\video_recognetion"
    save_path=r"D:\PycharmProjects\myproject_201909\company\video\savepath"
    # for video_name in os.listdir(video_path):
    #     video_img = Video_Img(video_path, video_name=video_name,save_path=save_path)
    #     video_img.Go()

    img_path=r"D:\PycharmProjects\myproject_201909\company\video\imgpath3"
    img_video=Img_Video(img_path,fps=4)
    img_video.Go()
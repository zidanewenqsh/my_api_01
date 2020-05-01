import torch
import torch.nn as nn

kernels = 5
strides = 2
paddings = 1
outpaddings = 1


# sizes = [1, 4, 8, 16, 32, 96]
def conv_same(size=416):
    # for i, size in enumerate(sizes):
    # flag = False
    # if i < len(sizes) - 1:
    #     print(i)
    #     a = torch.randn(1, 1, size, size)
    sizelist = []
    while size > 3:
        for k in range(1, kernels + 1):

            for s in range(1, min(strides, k) + 1):

                for p in range(min(3, size)):
                    if k <= 2 * p:
                        continue
                    try:
                        if k < size:

                            # print(1)
                            a = torch.randn(1, 1, size, size)
                            fc = nn.Conv2d(1, 1, kernel_size=k, stride=s, padding=p)
                            b = fc(a)
                            # print("size", size, b.size())
                            # print("asize:%d to %d, kernel_size=%d, stride=%d, padding=%d" % (
                            #     size, b.size(2), k, s, p))
                            if k==3 and s==2 and p==1:
                                print("size:%d to %d, kernel_size=%d, stride=%d, padding=%d" % (
                                        size, b.size(2), k, s, p))
                                if b.size(2) not in sizelist:
                                    sizelist.append(b.size(2))
                            # if b.size(2) % 2 == 0:
                            #     if b.size(2) == size // 2:
                            #         # print("size:%d to %d, kernel_size=%d, stride=%d, padding=%d" % (
                            #         #     size, b.size(2), k, s, p))
                            #         if b.size(2) not in sizelist:
                            #             sizelist.append(b.size(2))
                            #         flag = True
                            # elif b.size(2) % 2 ==1:
                            #
                            #     if b.size(2) == size // 2:
                            #         # print("size:%d to %d, kernel_size=%d, stride=%d, padding=%d" % (
                            #         #     size, b.size(2), k, s, p))
                            #         if b.size(2) not in sizelist:
                            #             sizelist.append(b.size(2))
                            #         flag = True
                            #
                            #     # break
                        else:
                            # print("size:%d to %d, kernel_size=%d, stride=%d, padding=%d" % (
                            #     size, b.size(2), k, s, p))
                            break

                    except(BaseException) as e:
                        print("wrongsize: %d, kernel_size=%d,stride=%d,padding=%d" % (size, k, s, p))
                        print("e", e)
        size = b.size(2)

    print(sizelist)

    return


def conv_size(sizes=[96, 32, 16, 8, 4, 1]):
    # sizes = [96, 32, 16, 8, 4, 1]
    for i, size in enumerate(sizes):
        flag = False
        if i < len(sizes) - 1:
            print(i)
            a = torch.randn(1, 1, size, size)

            for k in range(1, kernels + 1):

                for s in range(1, min(strides, k) + 1):

                    for p in range(min(3, size)):
                        try:
                            fc = nn.Conv2d(1, 1, kernel_size=k, stride=s, padding=p)
                            b = fc(a)
                            if b.size(2) == sizes[i + 1]:
                                print("size:%d to %d, kernel_size=%d, stride=%d, padding=%d" % (
                                    size, b.size(2), k, s, p))
                                flag = True
                                break
                        except(BaseException) as e:
                            print("wrongsize: %d, kernel_size=%d,stride=%d,padding=%d" % (size, k, s, p))
                            print("e", e)

    return


def convtrans_size(sizes=[1, 4, 8, 16, 32, 96]):
    # sizes = [1, 4, 8, 16, 32, 96]
    # sizes = [1, 4, 8,16]
    for i, size in enumerate(sizes):
        flag = False
        if i < len(sizes) - 1:
            print(i)
            a = torch.randn(1, 1, size, size)

            for k in range(1, kernels + 1):
                # print("*************", k)

                for s in range(1, min(strides, k) + 1):
                    # print("*************",s,min(strides, k))

                    for p in range(min(3, size)):

                        for op in range(s):
                            try:
                                fc = nn.ConvTranspose2d(1, 1, kernel_size=k, stride=s, padding=p, output_padding=op)
                                b = fc(a)

                                if b.size(2) == sizes[i + 1]:
                                    print("size:%d to %d, kernel_size=%d, stride=%d, padding=%d, output_padding=%d" % (
                                        size, b.size(2), k, s, p, op))
                                    flag = True

                            except(BaseException) as e:
                                print("wrongsize: %d, kernel_size=%d,stride=%d,padding=%d,output_padding=%d" % (
                                    size, k, s, p, op))
                                print("e", e)
                                # continue

    return


'''
size: 4, kernel_size=1,stride=1,padding=2,output_padding=0
kernel_size=1,stride=1,padding=0,output_padding=0 1 1
size: 1, kernel_size=1,stride=1,padding=1,output_padding=0'''


# a1 = torch.randn(1,1,4,4)
# a2 = torch.randn(1,1,1,1)
# fc1 = nn.ConvTranspose2d(1,1,1,1,2,0)
# fc2 = nn.ConvTranspose2d(1,1,1,1,1,0)
# b1 = fc1(a1)
# b2 =fc2(a2)
# print(b1.size())
# print(b2.size())
def gansize(size=[28, 14, 7, 4, 1]):
    conv_size(size)
    size.reverse()
    convtrans_size(size)


if __name__ == '__main__':
    print(1)
    # a = [96,32,16,8,4,1]
    a = [28, 14, 7, 4, 1]
    # gansize(a)
    # conv_same(466)
    gansize([466, 233, 117, 59, 30])
    # a = [28, 14, 7, 4, 1]
    # conv_size(a)
    # print("**************")
    # convtrans_size(reversed(a))

    # print(a.reverse())
    # print(reversed(a))
    # b = reversed(a)
    # print(list(b))
    # print(a)

    # sizes = [8, 16, 32, 96]
    # for i, size in enumerate(sizes):
    #
    #     if i < len(sizes) - 1:
    #         print(i)
    #         a = torch.randn(1, 1, size, size)
    #         # try:
    #         for k in range(1, max(kernels, size) + 1):
    #
    #             for s in range(1, min(strides, k) + 1):
    #
    #                 for p in range(min(3, size)):
    #                     for op in range(min(s, p) + 1):
    #
    #                         fc = nn.ConvTranspose2d(1, 1, kernel_size=k, stride=s, padding=p, output_padding=op)
    #                         b = fc(a)
    #                         print(i, b.size(), sizes[i], sizes[i + 1])
    #                         if b.size(2) == sizes[i + 1]:
    #                             print("size:%d,kernel_size=%d,stride=%d,padding=%d,output_padding=%d" % (
    #                             size, k, s, p, op), b.size(2))

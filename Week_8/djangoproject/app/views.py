from django.shortcuts import render
import os

# Create your views here.
# 跳转至当前应用的首页index.html
def index(request):
    return render(request, 'index.html')

# 实现单文件上传业务处理
def fileupload(request):
    if request.POST:
        # 接收客户端请求数据
        obj = request.FILES.get('uploadFile', None)
        # 处理请求数据
        # 获取上传文件的名称
        uploadFileName = obj.name
        print('\n上传文件基本信息：')
        print('-' * 40)
        print('文件名称：{0}'.format(uploadFileName))
        # 检测并创建服务器端接收客户端上传文件的文件夹
        uploadDirPath = os.path.join(os.getcwd(), 'app/static/file')
        # 检测文件夹是否存在
        if not os.path.exists(uploadDirPath):
            # 创建一个新的文件夹
            os.mkdir(uploadDirPath)
            print('服务器端上传文件构建成功.')
        else:
            print('服务器端上传文件夹已经存在.')
        # 获取客户端上传文件在服务器端的绝对路径
        uploadFileFullPath = uploadDirPath + os.sep + uploadFileName
        print('上传文件绝对路径：{0}'.format(uploadFileFullPath))
        try:
            # 写入文件数据
            with open(uploadFileFullPath, 'wb+') as fp:
                # 将上传文件对象分割成多个数据块并循环写入
                for chunk in obj.chunks():
                    fp.write(chunk)
                print('上传文件写入完毕.')
            # 响应客户端
            return render(request, 'fileupload.html', {'success_msg':'[OK] 文件上传成功.'})
        except:
            # 响应客户端
            return render(request, 'fileupload.html', {'error_msg':'[Error] 文件上传失败.'})
    else:
        return render(request, 'fileupload.html')

# 多文件上传业务实现
def multiupload(request):
    if request.POST:
        # 接收客户端请求数据
        objs = request.FILES.getlist('uploadFile', None)
        # 处理请求数据
        # 创建标志位，用来记录每个文件上传操作是否成功
        flag = True
        # 使用for循环遍历上传文件集合
        for obj in objs:
            # 获取上传文件的名称
            uploadFileName = obj.name
            print('\n上传文件基本信息：')
            print('-' * 40)
            print('文件名称：{0}'.format(uploadFileName))
            # 检测并创建服务器端接收客户端上传文件的文件夹
            uploadDirPath = os.path.join(os.getcwd(), 'app/static/file')
            # 检测文件夹是否存在
            if not os.path.exists(uploadDirPath):
                # 创建一个新的文件夹
                os.mkdir(uploadDirPath)
                print('服务器端上传文件构建成功.')
            else:
                print('服务器端上传文件夹已经存在.')
            # 获取客户端上传文件在服务器端的绝对路径
            uploadFileFullPath = uploadDirPath + os.sep + uploadFileName
            print('上传文件绝对路径：{0}'.format(uploadFileFullPath))
            try:
                # 写入文件数据
                with open(uploadFileFullPath, 'wb+') as fp:
                    # 将上传文件对象分割成多个数据块并循环写入
                    for chunk in obj.chunks():
                        fp.write(chunk)
                    print('上传文件写入完毕.')                
            except:
                # 标志位设置为False
                flag = False
                break # 退出循环
        # 响应客户端
        if flag:
            return render(request, 'multiupload.html', {'success_msg':'[OK] 批量文件上传成功.'})
        else:
            return render(request, 'multiupload.html', {'error_msg':'[Error] 批量文件上传失败'})
    else:
        # 响应客户端
        return render(request, 'multiupload.html')
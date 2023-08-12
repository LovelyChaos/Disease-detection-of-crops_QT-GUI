#import CropModels
from Program.CropModels import *
import numpy as np

'''
预测data在model上的结果
输出两个GPU上的数组 所有的label值和所有的预测值
'''
def predict(image_dir, model_dir):
    import torchvision.transforms as transforms
    import torch
    from torch.autograd import Variable
    # import CropModels
    import cv2
    import torch.nn.functional as F
    NB_CLASS = 59
    all_labels = []
    all_outputs = []
    model_class = partial(DenseNetFinetune, net_cls=M.densenet121)
    print('[+] loading model... ', end='', flush=True)
    model = model_class(NB_CLASS)
    #model.cuda()
    print('done')
    #model = get_model(model_class)
    #model.load_state_dict(torch.load(r'../model/2018-11-04_acc_best.pth')['state_dict'])
    model.load_state_dict(torch.load(model_dir, map_location='cpu')['state_dict'])
    model.eval()
    img = cv2.imdecode(np.fromfile(image_dir,dtype=np.uint8),-1)
    img =  cv2.resize(img, (224,224), interpolation = cv2.INTER_CUBIC)
    transf = transforms.ToTensor()
    img_tensor = transf(img)
    inputs =img_tensor
    inputs = inputs.unsqueeze(0)
    inputs = Variable(inputs)
    outputs = model(inputs)
    test_prob = F.softmax((outputs), dim=1)
    final_label = int(test_prob.argmax())
    print('final_label!!!!!最后的预测种类', final_label)
    return final_label

if __name__ == '__main__':

    image_dir = 'D:/Dachuang/APP/image/apple.jpg'
    model_dir = '../2018-11-04_acc_best.pth'
    predict(image_dir, model_dir)
    print('finish')
from functools import partial
from torch import nn
import torchvision.models as M
densenet121 = M.densenet121
class DenseNetFinetune(nn.Module):
    finetune = True

    def __init__(self, num_classes, net_cls=M.densenet121):
        super().__init__()
        self.net = net_cls(pretrained=True)
        self.net.classifier = nn.Linear(self.net.classifier.in_features, num_classes)

    def fresh_params(self):
        return self.net.classifier.parameters()

    def forward(self, x):
        return self.net(x)

densenet121_finetune = partial(DenseNetFinetune, net_cls=M.densenet121)


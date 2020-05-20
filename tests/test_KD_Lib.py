# -*- coding: utf-8 -*-
"""Tests for `KD_Lib` package."""

import torch
from KD_Lib.TAKD.main import main_TAKD
from KD_Lib.original.mnist import mnist
from KD_Lib.models.resnet import ResNet18, ResNet34, ResNet50, ResNet101, ResNet152


def test_mnist():
    mnist(epochs=0)


def test_resnet():
    params = [4,4,8,8,16]
    ResNet18(params)
    ResNet34(params)
    ResNet50(params)
    ResNet101(params)
    ResNet152(params)


def test_TAKD():
    config = {
        'teacher': {
            'name': 'resnet101',
            'params': [32, 32, 64, 64, 128],
            'optimizer': 'adam',
            'train_epoch': 0
        },
        'assistants': [
            {
                'name': 'resnet50',
                'params': [32, 32, 64, 64, 128],
                'optimizer': 'adam',
                'train_epoch': 0
            },
            {
                'name': 'resnet34',
                'params': [32, 32, 64, 64, 128],
                'optimizer': 'adam',
                'train_epoch': 0
            },
        ],
        'student': {
            'name': 'resnet18',
            'params': [16, 32, 32, 16, 8],
            'optimizer': 'adam',
            'train_epoch': 0
        },
        'dataset': {
            'name': 'mnist',
            'location': './data/mnist',
            'batch_size': 128,
            'num_classes': 10,
            'num_channels': 1
        },
        'loss_function': 'cross_entropy',
        'assistant_train_order': [[-1], [-1, 0]]
    }
    main_TAKD(config)


def test_attention_model():
    params = [4, 4, 8, 8, 16]
    sample_input = torch.ones(size=(1, 3, 32, 32), requires_grad=False)
    model = ResNet152(params, att=True)
    sample_output = model(sample_input)
    print(sample_output)

# -*- coding: utf-8 -*-
"""Generator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OY0JumgWTuTAfQnl4FxWyzl9UtYJAccM
"""

import tensorflow as tf

def scale_down(filters, size, shape , apply_norm = True):
  initializer = tf.random_normal_initializer(0., 0.02)
  result = tf.keras.Sequential()
  result.add(tf.keras.layers.Conv2D(filters , size , strides = 2 , padding = 'same' , batch_input_shape = shape , use_bias = False))
  if apply_norm:
    result.add(tf.keras.layers.BatchNormalization())
  result.add(tf.keras.layers.LeakyReLU())
  return result



def scale_up(filters , size , shape , apply_dropout = False):
    initializer = tf.random_normal_initializer(0., 0.02)
    result = tf.keras.Sequential()
    result.add(tf.keras.layers.Conv2DTranspose(filters, size, strides=2, batch_input_shape=shape,
                                    padding='same',use_bias=False))

    result.add(tf.keras.layers.BatchNormalization())

    if apply_dropout:
        result.add(tf.keras.layers.Dropout(0.5))

    result.add(tf.keras.layers.ReLU())

    return result

def buildGenerator():
  inputs = tf.keras.layers.Input(shape = (256,256,3))

  down_stack = [
        scale_down(64, 4, (None, 256, 256, 3), apply_norm=False), 
        scale_down(128, 4, (None, 128, 128, 64)), 
        scale_down(256, 4, (None, 64, 64, 128)), 
        scale_down(512, 4, (None, 32, 32, 256)), 
        scale_down(512, 4, (None, 16, 16, 512)), 
        scale_down(512, 4, (None, 8, 8, 512)), 
        scale_down(512, 4, (None, 4, 4, 512)),  
        scale_down(512, 4, (None, 2, 2, 512)),    
  ]

  up_stack = [
        scale_up(512, 4, (None, 1, 1, 512), apply_dropout=True), 
        scale_up(512, 4, (None, 2, 2, 1024), apply_dropout=True), 
        scale_up(512, 4, (None, 4, 4, 1024), apply_dropout=True), 
        scale_up(512, 4, (None, 8, 8, 1024)), 
        scale_up(256, 4, (None, 16, 16, 1024)), 
        scale_up(128, 4, (None, 32, 32, 512)), 
        scale_up(64, 4, (None, 64, 64, 256))
  ]
  initializer = tf.random_normal_initializer(0., 0.02)
  last = tf.keras.layers.Conv2DTranspose(3, 4,strides=2,padding='same', kernel_initializer=initializer)

  x = inputs
  skips = []

  for down in down_stack:
    x = down(x)
    skips.append(x)

  skips = reversed(skips[:-1])

  for up , skip in zip(up_stack,skips):
    x = up(x)
    x = tf.keras.layers.Concatenate()([x , skip])
  
  x = last(x)
  x = tf.keras.activations.tanh(x)
  return tf.keras.Model(inputs = inputs , outputs = x)

# Link refrensi: https://www.tensorflow.org/guide/gpu

from __future__ import absolute_import, division, print_function, unicode_literals

tf.debugging.set_log_device_placement(True)

print("Tensorflow Version:", tf.__version__)

gpus = tf.config.experimental.list_logical_devices('GPU')
if gpus:
  # Replicate your computation on multiple GPUs
  c = []
  for gpu in gpus:
    with tf.device(gpu.name):
      a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
      b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
      c.append(tf.matmul(a, b))

  with tf.device('/CPU:0'):
    matmul_sum = tf.add_n(c)

  print(matmul_sum)
  print(" ")
  print("Created By Wayan Dadang Syahreza Ganteng")
  print("Testing GPU CUDA cuDNN pada Tensorflow GPU versi",tf.__version__)
  print("Happy Machine Learning and Keep Learning")
  print(" ")

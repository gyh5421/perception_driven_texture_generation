# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Read and preprocess image data.

 Image processing occurs on a single image at a time. Image are read and
 preprocessed in parallel across multiple threads. The resulting images
 are concatenated together to form a single batch for training or evaluation.

 -- Provide processed image data for a network:
 inputs: Construct batches of evaluation examples of images.
 distorted_inputs: Construct batches of training examples of images.
 batch_inputs: Construct batches of training or evaluation examples of images.

 -- Data processing:
 parse_example_proto: Parses an Example proto containing a training example
   of an image.

 -- Image decoding:
 decode_jpeg: Decode a JPEG encoded string into a 3-D float32 Tensor.

 -- Image preprocessing:
 image_preprocessing: Decode and preprocess one image for evaluation or training
 distort_image: Distort one image for training a network.
 eval_image: Prepare one image for evaluation.
 distort_color: Distort the color in one image for training.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

    
if __name__ == '__main__':
    filename_queue = tf.train.string_input_producer(['recorderdata/train-00000-of-00400','recorderdata/train-00001-of-00400','recorderdata/train-00002-of-00400','recorderdata/train-00003-of-00400','recorderdata/train-00004-of-00400'], shuffle=False, capacity=1)
    reader=tf.TFRecordReader()
    _, example_serialized = reader.read(filename_queue)
    feature_map = {
      'image/encoded': tf.FixedLenFeature([], dtype=tf.string,
                                          default_value=''),
      'image/class/label': tf.VarLenFeature(dtype=tf.float32,
                                              ),
                                              }
    features = tf.parse_single_example(example_serialized, feature_map)
    label = tf.reshape(features['image/class/label'].values, [3, 4])
    loss1 = tf.reduce_sum(tf.pow(label,2),1)
    loss2 = 0.5*tf.reduce_sum(loss1)
    sess=tf.Session()
    noize=tf.random_uniform([1,5],-1,1,tf.float32)
    with sess.as_default():
        tf.train.start_queue_runners()
        for _ in xrange(5):
            a, b, c = sess.run([label, loss1, loss2])
            print(a)
            print(b)
            print(c)


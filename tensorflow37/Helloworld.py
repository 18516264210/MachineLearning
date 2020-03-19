
import tensorflow as tf

print(tf.version)


hello = tf.constant("hw tf")

sess = tf.Session()

print(sess.run(hello))

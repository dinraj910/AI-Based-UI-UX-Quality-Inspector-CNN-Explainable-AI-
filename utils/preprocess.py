import tensorflow as tf

IMAGE_SIZE = 256

def preprocess_image(path):
    img = tf.io.read_file(path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.resize(img, (IMAGE_SIZE, IMAGE_SIZE))
    img = tf.cast(img, tf.float32) / 255.0
    return tf.expand_dims(img, axis=0)

import streamlit as st
import tensorflow as tf
import numpy as np


def model_prediction(prediction_image):
    model = tf.keras.models.load_model("trained_model.h5")
    image = tf.keras.preprocessing.image.load_img(prediction_image, target_size=(64, 64))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])
    predictions = model.predict(input_arr)
    return np.argmax(predictions)


st.header("Предсказать что на изображении")
test_image = st.file_uploader("Выберите изображение:")
if test_image is not None:
    st.image(test_image, width=4, use_column_width=True)
    if st.button("Предсказать"):
        with st.spinner("Подождите"):
            result_index = model_prediction(test_image)
            with open("labels_ru.txt", encoding='utf-8') as f:
                content = f.readlines()
            label = []
        for i in content:
            label.append(i[:-1])
        st.success("На изображении {}".format(label[result_index]))

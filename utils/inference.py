def run_inference(model, img_tensor):
    score, flags = model.predict(img_tensor)
    return score[0][0] * 100, flags[0]

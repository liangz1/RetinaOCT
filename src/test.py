import numpy as np
# from preprocess import preprocess
# from multiprocessing import Pool

# Plug in custom models here
from Inception import InceptionDR

# Plug in data loader
from data_utils import get_test_data_batches


def test_old(best_model_path=
             '/home/yunhan/KaggleDiatetic/src/inception_v3_binary_class/inception_v3_50_50_13_best_f1.h5'):
    """

    :param best_model_path: str: path to best model weight file
    :return: probability of having DR
    """
    print("building model")
    best_model = InceptionDR("eval")
    print("loading model")
    best_model.load_best_model(best_model_path)
    print("loading test data")
    y_pred = []
    for pix in get_test_data_batches():
        y = best_model.model.predict(pix)
        y_pred.append(y)
    pred_data = np.vstack(y_pred)
    np.save('Y_51000_pred.npy', pred_data)
    return


def test(best_model_path='/home/yunhan/KaggleDiatetic/src/inception_v3_50_50_5class_0.h5'):
    """

    :param image_path: str: path to image to be evaluated
    :param best_model: str: path to best model weight file
    :return: probability of having DR
    """
    print("building model")
    best_model = InceptionDR("eval")
    print("loading model")
    best_model.load_best_model(best_model_path)
    print("loading test data")
    pix = get_test_data_batches()
    # with Pool(16) as p:
    #     pix_prep = p.map(preprocess, pix)

    n = pix.shape[0]
    batch_size = 32
    num_batch = n // batch_size
    y_pred = []
    for i in range(num_batch):
        print("testing batch %d" % (i+1))
        batch = np.stack(pix[i*batch_size:(i+1)*batch_size])
        batch = batch / 255

        y = best_model.model.predict(batch)
        y_pred.append(y)
    pred_data = np.vstack(y_pred)
    np.save('Y_3000_pred.npy', pred_data)
    return


if __name__ == '__main__':
    test_old()


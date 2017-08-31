from functools import partial

def imshow(cv2, name, input, fig_size=None, cmap="gray"):
    """
    params:
        name - The "title" that would show on OpenCv window.
        input - the input data
        **the two params are the existing parameters in opencv.imshow**
        fig_size - receives a tuple for the image size to be printed in the notebook
        cmap - a matplotlib-compliant color map code to use in our image
    """
    ## by default, we'll infer the image rendering size by the input shape
    ## assuming a density of 80 dpi
    if fig_size is None:
        dpi = 80
        im_data = input
        try:
            height, width, depth = im_data.shape
        except:
            height, width = im_data.shape
        fig_size = width / float(dpi), height / float(dpi)

    try:
        input = cv2.cvtColor(input,cv2.COLOR_BGR2RGB)
    except :
        input = input

    import matplotlib.pyplot as plt
    get_ipython().magic(u'matplotlib inline')
    
    fig, ax = plt.subplots(figsize=fig_size)
    print("Showing Image: {}".format(name))
    ax.imshow(input, interpolation='none', aspect="auto", cmap=cmap)
    plt.show()

def override_imshow(cv2):
    ## from now on, cv2.imshow will call our function instead.
    cv2.imshow = partial(imshow, cv2)


# SoC2021-(Un)Clear
The project is based on Image Super Resolution , namely the Enhanced Super Resolution Generative Adverserial Networks(ESRGAN) [paper](https://arxiv.org/abs/1609.04802). The project started the first week of April and included the following topics :
## Image handling using OpenCV:
* We covered the basics of image handling such as image resizing , rescaling , inter-conversion of images from different color systems, smoothening of images by eroding  and dilating and different types of blurring .

* This was followed by covering of certain important functions such as the Gaussian pyramids ,the Canny edge detections ,  the SIFT algorithm for image feature detection , Contours and Convex hulls.

* This was followed by assignment one which included image importing , starting live video camera using OpenCV , changing color systems , making use of different techniques of image changing such blurs and smoothening and making a pencil sketch of our image and live video.

## Basics of Machine learning:
* We started with the basic Machine Learning course offered by Google , and learnt about the various terminologies involved such as Training, test and validation dataset, Feature crosses , logistic regression , the Neural Networks and Embeddings.

* This was followed by udacity's Tensorflow course wher we learnt about CNNs and transfer learning.
* The next assignment was based on this section's implementation , making a handwritten-number recognition model. The dataset can be found [here](https://www.kaggle.com/c/digit-recognizer/overview) . This assignment helped us in implementing all what we had learnt until then.

## Basics of Generative Adverserial Networks:
* We learnt about GANs,short for Generative Adverserial Networks , are Machine Learning models which generate an data close to reality based on certain given data. It includes two models , one is the generator , which generates fake data from a real data and other is the discriminator which distinguishes output made by the generator(fake data) from the real data.

* Apart from basics, we also covered the losses involved in GANs and the various problems faced while using GANs.

* The section concluded with an assignment based on anime-sketch coloring GAN. This included making of a basic GAN which colours an anime-sketch based on a given input data. It was a lengthy assignment but gave interesting results , a copy of result images produced has been added in the same folder.

## SRGAN and ESRGAN:
* This section included the core of the project , namely the Super Resolution of Images using GANs. It includes the perceptual losses and the changed discriminator.

* The project concluded with the implementation of the same. This included choosing a low quality image and resolving it to a high quality using the implementation given in the paper.

* This project used everything that we had learnt on the way: Use of OpenCV for changing image properties , use of Tensorflow for making the models , Transfer Learning for the VGG loss included in the ESRGAN research paper and the main component , the Generative Adverserial Network.

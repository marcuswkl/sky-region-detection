# sky-region-detection

The aim of this project is to develop a computer vision algorithm that can be used to automatically identify pixels that belong to the sky region. Identifying the sky region in outdoor images can be the very first step in many real-world applications, such as weather forecast, solar exposure detection and ground robot navigation.

The SkyFinder datasets consist of daytime and nighttime images taken from different cameras at different locations. Each dataset also comes with a mask (also known as ground truth or “correct answer”) that indicates the sky region (white colour region) for evaluation purpose.

You are required to develop a computer vision algorithm to identify pixels belonging to the sky region by using Python and OpenCV, and evaluate its performance by applying it to the images taken from a few selected SkyFinder datasets. You can either design your algorithm based on an existing algorithm that you have studied and try to improve from there, or combine the ideas from different algorithms into one.

1. Download the images from camera **1093**, **4795**, **8438** and **10870** [here](https://cs.valdosta.edu/~rpmihail/skyfinder/images/index.html).
2. Develop a computer vision algorithm that can be used to identify sky pixels.
3. Evaluate the algorithm by using images from camera **4232**, **9483**, **8438** and **10917**.
4. Improve the computer vision algorithm to achieve better performance.

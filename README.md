# Final Project

## Explanation

Basically I only did simple things;

- Resize the image for feeding the input (standarize the input)
- Blur with a Gaussian Filter to reduce the non-independance of the images
- Edge Detection with the Canny Algorithm
- And multimple non-parametric algorithms for this simple problem

I found that the Stochastic Gradient Descent model was the best for solving the problem, with an awesome 100% accuracy in the test set, I repeated the training and test multiple time (10) to see if this score was mantain (It wasn't, it was reduce to 99.78%, which is still awesome).

I think that:

- The Edge Detection with Canny was a good decision.
- Stochastic Gradient Descent was the best algorithm probably because of it's smoothness.

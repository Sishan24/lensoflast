# Deep Learning Syllabus Mapping

The project application belongs to Unit V: Image Processing. Units I–IV are demonstrated through the main model and controlled academic experiments. Not every syllabus item needs to be forced into the final inference pipeline.

| Syllabus topic | ExpiryLens implementation / evidence |
|---|---|
| McCulloch-Pitts neuron | Small threshold-neuron demonstration in a notebook; explain limitations |
| MLP | Baseline semantic date-field classifier |
| Representation power of MLPs | Compare a shallow and deeper MLP on a defined classification task |
| Sigmoid neurons | Activation-function experiment on a binary classification baseline |
| Feed-forward networks | MLP baseline |
| Backpropagation | Training explanation and gradient-based model training |
| Gradient Descent | Optimiser comparison using a fixed model/data split |
| Momentum-based GD | Compare convergence with plain SGD |
| Nesterov accelerated GD | Compare with SGD and Momentum |
| Stochastic GD | Train recognition/classification models with mini-batches |
| PCA | Exploratory dimensionality-reduction experiment on extracted features |
| SVD | Matrix factorisation/low-rank approximation demonstration |
| Parameters vs hyperparameters | Document trainable weights vs learning rate, batch size, sequence length, etc. |
| Autoencoders | Denoising autoencoder for degraded label crops |
| PCA and autoencoders | Compare low-dimensional representations in an experiment |
| Regularisation in autoencoders | Weight penalties and latent bottleneck experiments |
| Denoising autoencoders | Corrupt clean label crops and train reconstruction |
| Sparse autoencoders | Optional sparsity-penalty experiment |
| Bias-variance tradeoff | Compare model capacity and train/validation performance |
| L1/L2 regularisation | Controlled generalisation experiment |
| Early stopping | Stop based on validation metric |
| Data augmentation | Rotation, perspective, brightness, blur and noise, within realistic limits |
| Encoder-decoder | Optional sequence recognition decoder experiment |
| Attention mechanism | Compare attention-based decoding or attention over sequence features |
| Attention over images | Optional visual attention experiment; include only if feasible |
| Batch normalisation | CNN training experiment |
| CNN architecture | Main visual feature extractor |
| Convolution/pooling | Feature-map and pooling demonstrations |
| CNN applications | Product-label image processing |
| AlexNet / ZFNet / VGGNet / GoogLeNet / ResNet | Architecture literature/controlled transfer-learning comparison where feasible; do not implement all from scratch |
| RNN | Simple recurrent baseline for character sequences |
| BPTT | Explain and demonstrate sequence-model training |
| Vanishing/exploding gradients | Compare vanilla RNN and gated recurrent model behaviour |
| Truncated BPTT | Discuss or demonstrate sequence chunking if the implementation uses it |
| GRU | Compare GRU and LSTM on the same recognition/classification task |
| LSTM | Main sequence modelling candidate |

## Minimum credible evidence

1. MLP baseline and training curves.
2. CNN-only or CNN + CTC recognition baseline.
3. CNN + BiLSTM recognition model.
4. One attention or decoder comparison.
5. Denoising autoencoder experiment.
6. Optimiser comparison: SGD, Momentum, Nesterov.
7. RNN vs LSTM/GRU gradient/sequence experiment.
8. PCA and SVD notebook experiments.
9. Final test-set evaluation and failure analysis.

Keep a results table with model version, dataset split, random seed, optimiser, learning rate, batch size, metric and date of run.

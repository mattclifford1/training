# setup (with conda)
make new conda env:

```
$ conda create -n myenv python=3.9
$ conda activate myenv
```

install requirements:

```
$ pip install -r requirements.txt
```

run local notebook server:

```
$ jupyter-notebook
```

# training spam classifier
to train spam classifier for text classification, run the notebook inside `train_spam_clf`

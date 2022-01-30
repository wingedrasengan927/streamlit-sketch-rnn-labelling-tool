# Sketch Labeling Tool
## Streamlit Custom Component built in Vue JS

![Demo](https://github.com/wingedrasengan927/streamlit-sketch-rnn-labelling-tool/blob/vue3/streamlit_sketch_rnn_labeling_tool/data/streamlit-app-2022-01-30-15-01-77.mp4)

This is a sketch tool similar to *Quick, Draw!*, but specifically designed to label data to be used by sequential models like Sketch-RNN

The Tool tracks the following attributes:<br>
| attributes | Description                                |
|------------|--------------------------------------------|
| x          | offset along X-axis                        |
| y          | Offset along Y-axis                        |
| p1         | 1 if the pen is touching the Canvas else 0 |
| p2         | 1 if the pen lifts from the Canvas else 0  |
| p3         | 1 when the drawing is finished else 0      |

## Setup

- Ensure you have [Python 3.6+](https://www.python.org/downloads/), [Node.js](https://nodejs.org), and [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) installed.
- Create a new Python virtual environment for the template:

### Venv
```
$ python3 -m venv venv  # create venv
$ . venv/bin/activate   # activate venv
$ pip install streamlit # install streamlit
```

### Conda

```
$ conda create -n streamlit-sketch-rnn-labeling-tool python=3.6 anaconda
$ conda activate streamlit-sketch-rnn-labeling-tool
$ pip install streamlit # install streamlit
```

- Clone the repository, Initialize and run the component template frontend:

```
$ git clone https://github.com/wingedrasengan927/streamlit-sketch-rnn-labelling-tool.git
$ cd streamlit-sketch-rnn-labelling-tool
$ cd streamlit_sketch_rnn_labeling_tool/frontend
$ npm install    # Install npm dependencies
$ npm run serve  # Start the Webpack dev server
```

- From a separate terminal, assuming you've activated the newly created virtual environment, run the template's Streamlit app from the `streamlit-sketch-rnn-labeling-tool` directory:

```
$ streamlit run app.py
```

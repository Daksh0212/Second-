from fastai.vision.all import *
import gradio as gr
learn = load_learner('model.pkl')
categories = learn.dls.vocab

def classify_images(img):
  pred,idx,probs = learn.predict(img)
  return dict(zip(categories, map(float, probs)))

image = gr.Image(height=192, width=192, type='pil')
label = gr.Label()
examples = ['examples/grizzly.jpeg', 'examples/black.jpeg', 'examples/teddy.jpeg']

intf = gr.Interface(fn=classify_images, inputs=image, outputs=label, examples=examples)
intf.launch(inline=False)